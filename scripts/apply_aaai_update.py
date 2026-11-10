#!/usr/bin/env python3
"""Apply reviewed AAAI admissions while preserving existing records verbatim."""
import csv
import hashlib
import json
import re
from pathlib import Path

from finance_taxonomy_rules import classify

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'checks/aaai_expansion'


def hash_record(record):
    return hashlib.sha256(json.dumps(record, ensure_ascii=False, sort_keys=True).encode()).hexdigest()


def sanitize(value):
    """Remove PDF extraction control characters that cannot be stored in Excel."""
    if isinstance(value, str):
        return re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', '', value)
    if isinstance(value, list):
        return [sanitize(item) for item in value]
    if isinstance(value, dict):
        return {key: sanitize(item) for key, item in value.items()}
    return value


def main():
    if not (ROOT / 'finance_catalog.csv').exists():
        raise SystemExit('Historical import tool: use scripts/build_collection.py for the separated long-paper collection.')
    with (ROOT / 'finance_catalog.csv').open(encoding='utf-8-sig', newline='') as stream:
        reader = csv.DictReader(stream)
        columns = reader.fieldnames
        rows = {row['id']: row for row in reader}
    records = {r['id']: r for r in map(json.loads, (ROOT / 'finance_catalog.jsonl').read_text().splitlines())}
    assignments_path = ROOT / 'checks/finance_taxonomy/assignments.json'
    assignments = json.loads(assignments_path.read_text())
    overrides_path = ROOT / 'checks/finance_taxonomy/manual_overrides.json'
    overrides = json.loads(overrides_path.read_text())
    baseline = DEST / 'baseline_record_hashes.json'
    if not baseline.exists():
        baseline.write_text(json.dumps({
            'source_commit': 'e7abe45cccd7eaeee41692249e34f180d5fa3236',
            'papers': {pid: {'csv_record': hash_record(row), 'jsonl_record': hash_record(records[pid]),
                             'assignment': hash_record(assignments[pid])} for pid, row in rows.items()},
        }, indent=2) + '\n')
    schema = json.loads((ROOT / 'checks/finance_taxonomy/schema.json').read_text())
    definitions = {kind: {item['id']: item['label'] for item in schema[kind]}
                   for kind in ('topics', 'subtopics', 'methods')}
    candidates = {p['id']: p for p in json.loads((DEST / 'candidates.json').read_text())}
    decisions = sanitize(json.loads((DEST / 'review_decisions.json').read_text()))
    (DEST / 'review_decisions.json').write_text(json.dumps(decisions, ensure_ascii=False, indent=2) + '\n')
    pdfs = {p['id']: p for p in json.loads((DEST / 'pdf_results.json').read_text())}
    for pid, decision in decisions.items():
        paper = candidates[pid]
        download = pdfs.get(pid, {'id': pid, 'status': 'not_downloaded', 'local_path': ''})
        assignment = classify(paper, decision, decision.get('taxonomy_override'))
        if decision.get('taxonomy_override'):
            overrides[pid] = decision['taxonomy_override']
        assignments[pid] = assignment
        finance = {
            **decision, 'relevance_zh': ('以金融任务或金融数据为核心研究对象。' if decision['scope'] == 'core'
                                      else '通用方法包含已核验的金融数据、实验或场景建模。'),
            'primary_topic': definitions['topics'][assignment['primary_topic_id']],
            'topic_ids': assignment['topic_ids'],
            'topics': [definitions['topics'][i] for i in assignment['topic_ids']],
            'subtopic_ids': assignment['subtopic_ids'],
            'subtopics': [definitions['subtopics'][i] for i in assignment['subtopic_ids']],
            'method_ids': assignment['method_ids'],
            'methods': [definitions['methods'][i] for i in assignment['method_ids']],
            'taxonomy_version': schema['version'],
        }
        code_urls = sorted(set(re.findall(r'https?://(?:github\.com|gitlab\.com)/[^\s<>\\)]+', paper['abstract'])))
        record = {key: paper[key] for key in ['id', 'title', 'authors', 'venue', 'year', 'abstract',
                   'paper_url', 'pdf_url', 'doi', 'volume', 'issue', 'proceedings_pages']}
        record.update(track='main', abstract_source=paper['metadata_sources'][0],
                      booktitle='Proceedings of the AAAI Conference on Artificial Intelligence',
                      metadata_sources=paper['metadata_sources'] + [decision['main_track_evidence']],
                      awards=[], award_evidence=[], oral=False, oral_evidence=[],
                      presentation_original=[], code_urls=code_urls,
                      finance=finance, download=download,
                      research={'primary_topic_id': 'finance' if finance['scope'] == 'core' else None,
                                'topic_ids': ['finance'], 'subtopic_ids': [],
                                'review_status': 'finance_only_classification'})
        records[pid] = record
        row = {key: '' for key in columns}
        row.update(id=pid, title=paper['title'], authors='; '.join(paper['authors']), venue='AAAI',
                   year=str(paper['year']), track='main',
                   research_primary_topic='AI for Finance / 金融人工智能' if finance['scope'] == 'core' else '',
                   research_topics='AI for Finance / 金融人工智能', research_topic_ids='finance',
                   research_review_status='finance_only_classification', is_best_or_outstanding='False',
                   is_oral='False', oral_candidate_unverified='False', finance_scope=finance['scope'],
                   finance_primary_topic=finance['primary_topic'], finance_topics='; '.join(finance['topics']),
                   finance_subtopics='; '.join(finance['subtopics']), finance_methods='; '.join(finance['methods']),
                   finance_topic_ids='; '.join(finance['topic_ids']), finance_relevance_zh=finance['relevance_zh'],
                   finance_evidence_type=finance['evidence_type'], finance_evidence_excerpt=finance['evidence_excerpt'],
                   paper_url=paper['paper_url'], pdf_url=paper['pdf_url'], download_status=download['status'],
                   code_urls='; '.join(code_urls), metadata_sources='; '.join(record['metadata_sources']),
                   abstract=paper['abstract'])
        if download['status'] == 'downloaded':
            row.update({key: str(download[key]) for key in ['local_path', 'pdf_version', 'pages', 'bytes', 'sha256']})
        rows[pid] = row
        note = [f"# {paper['title']}", '', f"AAAI {paper['year']} · main · {finance['scope']}", '',
                f"- Official paper: {paper['paper_url']}", f"- DOI: https://doi.org/{paper['doi']}",
                f"- Metadata source: {paper['metadata_sources'][0]}",
                f"- Main-track evidence: {decision['main_track_evidence']} (volume {paper['volume']}, issue {paper['issue']})",
                f"- Financial evidence: `{finance['evidence_type']}`",
                f"- Primary topic: {finance['primary_topic']}",
                f"- Topics: {'; '.join(finance['topics'])}",
                f"- Subtopics: {'; '.join(finance['subtopics'])}",
                f"- Methods: {'; '.join(finance['methods'])}",
                '- [Classification definitions](../finance_taxonomy.md) · '
                '[Classification evidence](../../checks/finance_taxonomy/assignments.json)']
        if row['local_path']:
            note.append(f"- Local PDF: [open](../../{row['local_path']}); version: `{row['pdf_version']}`")
        else:
            note.append(f"- Online PDF: {paper['pdf_url']}")
        if code_urls:
            note.append('- Code links from the abstract: ' + '; '.join(code_urls))
        note.extend(['', '## Financial relevance evidence', '', finance['evidence_excerpt'], '',
                     '## Abstract', '', paper['abstract'], ''])
        (ROOT / f'indexes/finance_notes/{pid}.md').write_text(
            '\n'.join(line.rstrip() for line in note).rstrip() + '\n')
    ordered = sorted(rows.values(), key=lambda r: (r['venue'], int(r['year']), r['title'].casefold()))
    with (ROOT / 'finance_catalog.csv').open('w', encoding='utf-8-sig', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=columns)
        writer.writeheader()
        writer.writerows(ordered)
    (ROOT / 'finance_catalog.jsonl').write_text(''.join(json.dumps(records[row['id']], ensure_ascii=False) + '\n'
                                                       for row in ordered))
    assignments_path.write_text(json.dumps(assignments, ensure_ascii=False, indent=2) + '\n')
    overrides_path.write_text(json.dumps(overrides, ensure_ascii=False, indent=2) + '\n')
    updates = [{'date': '2026-11-10', 'venue': 'AAAI', 'track': 'main', 'years': [2017, 2026],
                'added_papers': len(decisions), 'audit': 'checks/aaai_expansion/README.md'}]
    (ROOT / 'checks/collection_updates.json').write_text(json.dumps(updates, indent=2) + '\n')
    print(f'Applied {len(decisions)} AAAI records. Collection total: {len(rows)}.')


if __name__ == '__main__':
    main()
