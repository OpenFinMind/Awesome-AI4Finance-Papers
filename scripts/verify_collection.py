#!/usr/bin/env python3
"""Validate the published collection without accessing the original library."""
import csv
import os
import hashlib
import json
import re
import zipfile
import gzip
from paper_length_policy import short_paper_reason, excluded_publication_reason, acl2019_program_types, title_key
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree as ET

REPO = Path(__file__).resolve().parents[1]
TRACK = os.environ.get('AI4FINANCE_TRACK', 'main')
assert TRACK in {'main', 'findings'}
ROOT = REPO / TRACK


def read_csv(path):
    with path.open(encoding='utf-8-sig', newline='') as stream:
        return list(csv.DictReader(stream))


def digest(path):
    result = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            result.update(block)
    return result.hexdigest()


def workbook_sheets(path):
    ns = {'s': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
    rel_ns = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id'
    with zipfile.ZipFile(path) as archive:
        assert archive.testzip() is None, 'Corrupt Excel archive'
        strings = []
        if 'xl/sharedStrings.xml' in archive.namelist():
            strings = [''.join(node.itertext()) for node in
                       ET.fromstring(archive.read('xl/sharedStrings.xml'))]
        relationships = {node.attrib['Id']: node.attrib['Target'] for node in
                         ET.fromstring(archive.read('xl/_rels/workbook.xml.rels'))}
        sheets = ET.fromstring(archive.read('xl/workbook.xml')).find('s:sheets', ns)
        result = {}
        for sheet in sheets:
            target = relationships[sheet.attrib[rel_ns]]
            target = target.lstrip('/') if target.startswith('/') else 'xl/' + target
            data = ET.fromstring(archive.read(target)).find('s:sheetData', ns)
            rows = []
            for row in data:
                values = {}
                for cell in row:
                    column = re.match(r'[A-Z]+', cell.attrib['r']).group()
                    if cell.attrib.get('t') == 'inlineStr':
                        inline = cell.find('s:is', ns)
                        value = ''.join(inline.itertext()) if inline is not None else ''
                    else:
                        value = cell.findtext('s:v', default='', namespaces=ns)
                        if cell.attrib.get('t') == 's':
                            value = strings[int(value)]
                    values[column] = value
                rows.append(values)
            result[sheet.attrib['name']] = rows
        return result


def sheet_records(rows):
    header = rows[0]
    return [{name: row.get(column, '') for column, name in header.items()} for row in rows[1:]]


def main():
    rows = read_csv(ROOT / 'finance_catalog.csv')
    ids = {row['id'] for row in rows}
    assert len(ids) == len(rows), 'Duplicate paper IDs'
    assert all(row['track'] == TRACK for row in rows), 'Mixed publication tracks in catalog'
    assert all(row['venue'] in {'AAAI', 'ACL', 'EMNLP', 'ICLR', 'ICML', 'NeurIPS'} for row in rows)
    assert all(2017 <= int(row['year']) <= 2026 for row in rows)
    assert all(row['paper_length'] == 'long' for row in rows), 'Non-long paper admitted'
    assert all(row['finance_scope'] in {'core', 'application'} for row in rows)
    assert all(urlsplit(row['paper_url']).scheme in {'http', 'https'}
               and urlsplit(row['paper_url']).netloc for row in rows)
    assert len({row['paper_url'] for row in rows}) == len(rows), 'Duplicate official paper URL'
    notes = {path.stem for path in (ROOT / 'indexes/finance_notes').glob('*.md')}
    assert notes == ids, 'Paper note IDs do not match catalog'

    records = [json.loads(line) for line in (ROOT / 'finance_catalog.jsonl').read_text().splitlines()]
    assert len(records) == len(rows) and {r['id'] for r in records} == ids
    structured = {r['id']: r for r in records}
    official_2019 = acl2019_program_types(gzip.decompress(
        (REPO/'checks/track_screening/length_sources/acl-2019-program-github.gz').read_bytes()).decode())
    schema = json.loads((ROOT / 'checks/finance_taxonomy/schema.json').read_text())
    assignments = json.loads((ROOT / 'checks/finance_taxonomy/assignments.json').read_text())
    assert set(assignments) == ids
    definitions = {key: {item['id']: item for item in schema[key]}
                   for key in ('topics', 'subtopics', 'methods')}
    pdf_paths = set()
    total_bytes = 0
    for row in rows:
        pid = row['id']
        record = structured[pid]
        assert short_paper_reason(record) is None, (pid, short_paper_reason(record))
        assert excluded_publication_reason(record) is None, (pid, excluded_publication_reason(record))
        if record['venue']=='ACL' and int(record['year'])==2019:
            assert official_2019.get(title_key(record['title']))=='long', (pid,'Not in official Main Long Papers program')
        assert record['track'] == row['track'] == TRACK, pid
        for field in ('title', 'venue', 'year', 'paper_url'):
            assert str(record[field]) == row[field], (pid, field)
        assert record['paper_length'] == 'long' and record['paper_length_evidence'], pid
        finance = record['finance']
        assert finance['scope'] == row['finance_scope'], pid
        assignment = assignments[pid]
        # Some imported title/abstract reviews have no separate inclusion excerpt.
        # Their retained classification evidence must still identify the source text.
        assert row['finance_evidence_excerpt'].strip() or (
            row['finance_evidence_type'] == 'title_abstract_review'
            and any(e.get('source') in {'title', 'abstract'} and e.get('excerpt', '').strip()
                    for e in assignment['topic_evidence'])
        ), (pid, 'Missing inclusion evidence')
        assert assignment['primary_topic_id'] in assignment['topic_ids'], pid
        for field, category in [('topic_ids', 'topics'), ('subtopic_ids', 'subtopics'),
                                ('method_ids', 'methods')]:
            assert len(assignment[field]) == len(set(assignment[field])), (pid, field)
            assert set(assignment[field]) <= set(definitions[category]), (pid, field)
            assert finance[field] == assignment[field], (pid, field)
        assert all(definitions['subtopics'][sid]['parent_id'] in assignment['topic_ids']
                   for sid in assignment['subtopic_ids']), pid
        for column, field, category in [('finance_topics', 'topic_ids', 'topics'),
                                         ('finance_subtopics', 'subtopic_ids', 'subtopics'),
                                         ('finance_methods', 'method_ids', 'methods')]:
            assert row[column] == '; '.join(definitions[category][i]['label']
                                            for i in assignment[field]), (pid, column)
        assert row['finance_primary_topic'] == definitions['topics'][assignment['primary_topic_id']]['label']
        assert row['finance_topic_ids'].split('; ') == assignment['topic_ids'], pid
        if row['download_status'] == 'downloaded':
            relative = row['local_path']
            path = (ROOT / relative).resolve()
            assert path.is_relative_to(ROOT / 'pdfs') and path.is_file(), relative
            assert relative not in pdf_paths, 'Duplicate PDF path'
            pdf_paths.add(relative)
            assert path.stat().st_size == int(row['bytes']), relative
            with path.open('rb') as stream:
                assert stream.read(5) == b'%PDF-', relative
            assert digest(path) == row['sha256'], relative
            assert record['download']['local_path'] == relative, pid
            total_bytes += path.stat().st_size
        else:
            assert not row['local_path'], pid
    actual_pdfs = {str(path.relative_to(ROOT)) for path in (ROOT / 'pdfs').rglob('*.pdf')}
    assert actual_pdfs == pdf_paths, 'Unexpected or missing PDF files'

    sheets = workbook_sheets(ROOT / 'finance_catalog.xlsx')
    all_sheet = sheet_records(sheets['Confirmed Finance'])
    assert {row['id'] for row in all_sheet} == ids and len(all_sheet) == len(rows)
    excel_rows = {row['id']: row for row in all_sheet}
    for row in rows:
        for column in ('title', 'venue', 'year', 'track', 'finance_scope', 'finance_primary_topic',
                       'finance_topics', 'finance_subtopics', 'finance_methods', 'local_path', 'sha256'):
            assert excel_rows[row['id']][column] == row[column], (row['id'], column, 'Excel')
    for topic in schema['topics']:
        subset = read_csv(ROOT / f"indexes/finance_topics/{topic['id']}.csv")
        expected = {row['id'] for row in rows if topic['id'] in assignments[row['id']]['topic_ids']}
        assert {row['id'] for row in subset} == expected and len(subset) == len(expected)
        sheet = sheet_records(sheets[topic['sheet']])
        assert {row['id'] for row in sheet} == expected and len(sheet) == len(expected)
    bibkeys = re.findall(r'^@\w+\{([^,]+),', (ROOT / 'finance_references.bib').read_text(), re.M)
    assert len(bibkeys) == len(rows) and len(set(bibkeys)) == len(rows), 'BibTeX count/duplicates'
    assert set(bibkeys) == {re.sub('[^A-Za-z0-9_-]', '_', pid) for pid in ids}, 'BibTeX identities differ'
    missing_rows = read_csv(ROOT / 'checks/missing_pdfs.csv')
    expected_missing = {row['id'] for row in rows if row['download_status'] != 'downloaded'}
    assert {row['id'] for row in missing_rows} == expected_missing

    links_checked = 0
    for path in ROOT.rglob('*.md'):
        if '.git' in path.parts:
            continue
        for target in re.findall(r'\]\(([^)]+)\)', path.read_text()):
            target = target.strip('<>')
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            resolved = (path.parent / unquote(parsed.path)).resolve()
            # A successful run creates this report after checking all links.
            report_target = ROOT / 'checks/validation.json'
            assert resolved.is_relative_to(REPO) and (resolved.exists() or resolved == report_target), (str(path), target)
            links_checked += 1

    report = {
        'validated_at_utc': datetime.now(timezone.utc).isoformat(),
        'papers': len(rows), 'tracks': dict(Counter(row['track'] for row in rows)),
        'scope': dict(Counter(row['finance_scope'] for row in rows)),
        'venues': dict(Counter(row['venue'] for row in rows)),
        'years': dict(sorted(Counter(row['year'] for row in rows).items())),
        'topics': len(schema['topics']), 'paper_notes': len(notes),
        'pdfs': len(pdf_paths), 'pdf_bytes': total_bytes,
        'missing_pdfs': len(missing_rows), 'local_markdown_links_checked': links_checked,
        'title_abstract_reviews_without_separate_inclusion_excerpt': [
            row['id'] for row in rows if not row['finance_evidence_excerpt'].strip()],
        'csv_jsonl_excel_classifications_consistent': True,
        'topic_memberships_consistent': True, 'bibtex_identities_consistent': True,
        'all_local_links_resolve': True, 'all_pdf_hashes_match': True,
        'separate_track_validated': TRACK,
        'explicit_short_paper_records': 0,
    }
    (ROOT / 'checks/validation.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
