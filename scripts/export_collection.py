#!/usr/bin/env python3
"""Rebuild finance topic views, workbook, notes, and bibliography locally.

The CSV and structured JSONL are the curated inputs. This command never changes
the inclusion decisions or reclassifies existing papers.
"""
import csv
import os
import json
import re
from collections import Counter
from pathlib import Path

import openpyxl
from openpyxl.styles import Font, PatternFill

from build_indexes import escape, link, table, write_page

REPO = Path(__file__).resolve().parents[1]
TRACK = os.environ.get('AI4FINANCE_TRACK', 'main')
assert TRACK in {'main', 'findings'}
ROOT = REPO / TRACK


def write_csv(path, rows, columns):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', encoding='utf-8-sig', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=columns, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(rows)


def sheet(book, name, rows, columns):
    page = book.create_sheet(name)
    page.append(columns)
    for row in rows:
        page.append([row.get(key, '') for key in columns])
    page.freeze_panes = 'A2'
    page.auto_filter.ref = page.dimensions
    for cell in page[1]:
        cell.font = Font(color='FFFFFF', bold=True)
        cell.fill = PatternFill('solid', fgColor='264653')
    for i, key in enumerate(columns, 1):
        page.column_dimensions[openpyxl.utils.get_column_letter(i)].width = (
            65 if key in {'title', 'finance_topics', 'finance_subtopics', 'finance_methods',
                          'finance_primary_topic', 'topic', 'definition'} else 24)
    for row in page.iter_rows(min_row=2):
        for i, cell in enumerate(row):
            if isinstance(cell.value, str):
                cell.data_type = 's'
                if columns[i] in {'paper_url', 'pdf_url', 'local_path'} and cell.value:
                    cell.hyperlink = cell.value
                    cell.font = Font(color='0563C1', underline='single')


def main():
    with (ROOT / 'finance_catalog.csv').open(encoding='utf-8-sig', newline='') as stream:
        reader = csv.DictReader(stream)
        columns = reader.fieldnames
        rows = list(reader)
    records = [json.loads(line) for line in (ROOT / 'finance_catalog.jsonl').read_text().splitlines()]
    schema = json.loads((ROOT / 'checks/finance_taxonomy/schema.json').read_text())
    assignments = json.loads((ROOT / 'checks/finance_taxonomy/assignments.json').read_text())
    assert {r['id'] for r in rows} == {r['id'] for r in records} == set(assignments)
    excel_columns = [c for c in columns if c not in {'abstract', 'metadata_sources', 'oral_evidence', 'award_evidence'}]
    book = openpyxl.Workbook()
    book.remove(book.active)
    sheet(book, 'Confirmed Finance', rows, excel_columns)
    topics = []
    for topic in schema['topics']:
        subset = [row for row in rows if topic['id'] in assignments[row['id']]['topic_ids']]
        core = sum(row['finance_scope'] == 'core' for row in subset)
        topics.append({'topic_id': topic['id'], 'topic': topic['label'], 'papers': len(subset),
                       'core': core, 'application': len(subset)-core,
                       'primary': sum(assignments[row['id']]['primary_topic_id'] == topic['id'] for row in rows),
                       'definition': topic['description']})
        write_csv(ROOT / f"indexes/finance_topics/{topic['id']}.csv", subset, columns)
        sheet(book, topic['sheet'], subset, excel_columns)
        page = ROOT / f"indexes/finance_topics/{topic['id']}.md"
        subtopics = [s for s in schema['subtopics'] if s['parent_id'] == topic['id']]
        sub_counts = ['| Subtopic | Papers |', '|---|---:|']
        for sub in subtopics:
            count = sum(sub['id'] in assignments[row['id']]['subtopic_ids'] for row in subset)
            sub_counts.append(f"| {escape(sub['label'])} | {count} |")
        lines = [f"# {topic['label']}", '', topic['description'], '',
                 f'{len(subset):,} {TRACK.title()} long papers. Topic memberships can overlap.', '',
                 '[All topics](../ai_for_finance.md) · [Classification definitions](../finance_taxonomy.md) · '
                 f"[CSV]({topic['id']}.csv) · [Excel](../../finance_catalog.xlsx)", '',
                 '\n'.join(sub_counts), '',
                 '| Year | Venue | Paper | Scope | Primary topic | Subtopics | Methods | Resources |',
                 '|---|---|---|---|---|---|---|---|']
        for row in sorted(subset, key=lambda r: (-int(r['year']), r['venue'], r['title'].casefold())):
            note = link(f"indexes/finance_notes/{row['id']}.md", page)
            resource = f"[PDF]({link(row['local_path'], page)})" if row['local_path'] else f"[Online]({row['paper_url']})"
            lines.append(f"| {row['year']} | {row['venue']} | [{escape(row['title'])}]({note}) | "
                         f"{row['finance_scope']} | {escape(row['finance_primary_topic'])} | "
                         f"{escape(row['finance_subtopics'])} | {escape(row['finance_methods'])} | {resource} |")
        page.write_text('\n'.join(lines) + '\n')
    sheet(book, 'Topics', topics, list(topics[0]))
    for category, field, title in [('subtopics', 'subtopic_ids', 'Subtopics'), ('methods', 'method_ids', 'Methods')]:
        stats = [{'id': item['id'], 'label': item['label'],
                  'papers': sum(item['id'] in a[field] for a in assignments.values())} for item in schema[category]]
        sheet(book, title, stats, list(stats[0]))
    coverage = []
    for venue in sorted({row['venue'] for row in rows}):
        for year in sorted({row['year'] for row in rows if row['venue'] == venue}):
            subset = [row for row in rows if row['venue'] == venue and row['year'] == year]
            coverage.append({'venue': venue, 'year': year, 'papers': len(subset),
                             'core': sum(r['finance_scope'] == 'core' for r in subset),
                             'application': sum(r['finance_scope'] == 'application' for r in subset),
                             'local_pdfs': sum(r['download_status'] == 'downloaded' for r in subset)})
    sheet(book, 'By Venue and Year', coverage, list(coverage[0]))
    missing = [row for row in rows if row['download_status'] != 'downloaded']
    sheet(book, 'Missing PDFs', missing, excel_columns)
    book.save(ROOT / 'finance_catalog.xlsx')
    write_csv(ROOT / 'checks/missing_pdfs.csv', missing,
              ['id', 'title', 'venue', 'year', 'track', 'finance_scope', 'paper_url', 'pdf_url', 'download_status'])

    toc = ['# AI for Finance', '', f'{len(rows):,} {TRACK.title()} long papers, organized into 23 overlapping finance topics.', '',
           '[Home](../README.md) · [Excel](../finance_catalog.xlsx) · [CSV](../finance_catalog.csv) · '
           '[BibTeX](../finance_references.bib) · [Classification definitions](finance_taxonomy.md) · '
           '[Selection evidence](../checks/README.md)', '',
           '| Topic | Papers | Core | Application | Primary | Data |', '|---|---:|---:|---:|---:|---|']
    for topic in topics:
        ident = topic['topic_id']
        toc.append(f"| [{escape(topic['topic'])}](finance_topics/{ident}.md) | {topic['papers']} | "
                   f"{topic['core']} | {topic['application']} | {topic['primary']} | [CSV](finance_topics/{ident}.csv) |")
    toc.extend(['', 'Each paper has one primary finance topic. Technical methods are separate labels.', ''])
    (ROOT / 'indexes/ai_for_finance.md').write_text('\n'.join(toc))
    write_page('indexes/financial_time_series.md', 'Financial time series',
               [r for r in rows if 'time_series' in assignments[r['id']]['topic_ids']])

    bib = []
    for record in records:
        key = re.sub('[^A-Za-z0-9_-]', '_', record['id'])
        title = record['title'].replace('&', r'\&').replace('%', r'\%').replace('#', r'\#')
        entry = f'@inproceedings{{{key},\n  title = {{{{{title}}}}},\n'
        entry += '  author = {' + ' and '.join(record['authors']) + '},\n'
        entry += '  booktitle = {' + record.get('booktitle', record['venue'] + ' main conference') + '},\n'
        entry += f"  year = {{{record['year']}}},\n  url = {{{record['paper_url']}}}"
        if record.get('doi'):
            entry += f",\n  doi = {{{record['doi']}}}"
        bib.append(entry + '\n}\n')
    (ROOT / 'finance_references.bib').write_text('\n'.join(bib))
    print(f'Rebuilt topic pages, CSVs, workbook, and bibliography for {len(rows):,} papers.')


if __name__ == '__main__':
    main()
