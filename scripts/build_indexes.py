#!/usr/bin/env python3
"""Rebuild browsing indexes from the finance CSV using only the standard library."""
import csv
import json
import os
from collections import Counter
from pathlib import Path
from urllib.parse import quote

REPO = Path(__file__).resolve().parents[1]
TRACK = os.environ.get('AI4FINANCE_TRACK', 'main')
assert TRACK in {'main', 'findings'}
ROOT = REPO / TRACK
VENUES = ('ACL', 'EMNLP') if TRACK == 'findings' else ('AAAI', 'ACL', 'EMNLP', 'ICLR', 'ICML', 'NeurIPS')


def read_rows():
    with (ROOT / 'finance_catalog.csv').open(encoding='utf-8-sig', newline='') as stream:
        return list(csv.DictReader(stream))


def escape(value):
    return str(value).replace('|', '\\|').replace('\n', ' ')


def link(path, page):
    return quote(os.path.relpath(ROOT / path, page.parent), safe='/._-')


def table(rows, page):
    lines = ['| Year | Venue | Paper | Scope | Resources |',
             '|---|---|---|---|---|']
    for row in sorted(rows, key=lambda r: (-int(r['year']), r['venue'], r['title'].casefold())):
        note = link(f"indexes/finance_notes/{row['id']}.md", page)
        resources = [f"[Paper]({row['paper_url']})"]
        if row['local_path']:
            resources.append(f"[PDF]({link(row['local_path'], page)})")
        elif row['pdf_url']:
            resources.append(f"[Online PDF]({row['pdf_url']})")
        lines.append(f"| {row['year']} | {row['venue']} | [{escape(row['title'])}]({note}) | "
                     f"{row['finance_scope']} | {' · '.join(resources)} |")
    return '\n'.join(lines)


def write_page(path, title, rows):
    page = ROOT / path
    page.parent.mkdir(parents=True, exist_ok=True)
    page.write_text(f"# {title}\n\n{len(rows):,} {TRACK.title()} long papers.\n\n"
                    f"[Home]({link('README.md', page)}) · "
                    f"[Topics]({link('indexes/ai_for_finance.md', page)}) · "
                    f"[CSV]({link('finance_catalog.csv', page)})\n\n"
                    + table(rows, page) + '\n', encoding='utf-8')


def main():
    rows = read_rows()
    assert rows and all(row['track'] == TRACK for row in rows)
    schema = json.loads((ROOT / 'checks/finance_taxonomy/schema.json').read_text())
    snapshot = json.loads((ROOT / 'checks/source_snapshot.json').read_text())
    counts = Counter(row['finance_scope'] for row in rows)
    downloaded = sum(row['download_status'] == 'downloaded' for row in rows)
    for venue in VENUES:
        write_page(f'indexes/venues/{venue.lower()}.md', venue,
                   [row for row in rows if row['venue'] == venue])
    years = sorted({row['year'] for row in rows}, reverse=True)
    for year in years:
        write_page(f'indexes/years/{year}.md', year,
                   [row for row in rows if row['year'] == year])
    write_page('indexes/all_papers.md', 'All papers', rows)
    write_page('indexes/core.md', 'Finance core', [r for r in rows if r['finance_scope'] == 'core'])
    write_page('indexes/applications.md', 'Finance applications',
               [r for r in rows if r['finance_scope'] == 'application'])

    # Catalogs and PDFs stay within their own publication track.
    assignment = json.loads((ROOT / 'checks/finance_taxonomy/assignments.json').read_text())
    for category, field in [('subtopics', 'subtopic_ids'), ('methods', 'method_ids')]:
        lines = [f"# {category.title()}", '', '[Home](../README.md) · [Finance tasks](ai_for_finance.md)', '',
                 '| Category | Papers |', '|---|---:|']
        for item in schema[category]:
            subset = [row for row in rows if item['id'] in assignment[row['id']][field]]
            write_page(f"indexes/{category}/{item['id']}.md", item['label'], subset)
            lines.append(f"| [{escape(item['label'])}]({category}/{item['id']}.md) | {len(subset)} |")
        (ROOT / f'indexes/{category}.md').write_text('\n'.join(lines)+'\n')
    print(f'Built {TRACK} browsing indexes for {len(rows):,} long papers.')


if __name__ == '__main__':
    main()
