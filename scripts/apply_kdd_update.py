#!/usr/bin/env python3
"""Apply explicit reviewed KDD decisions without changing existing paper records."""
import csv
import hashlib
import json
import re
import shutil
from pathlib import Path

from collect_kdd import AUDIT, ROOT, POLICIES, key, save
from finance_taxonomy_rules import classify


def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True).encode()).hexdigest()


def main():
    folder = ROOT / 'main'
    with (folder / 'finance_catalog.csv').open(encoding='utf-8-sig', newline='') as stream:
        reader = csv.DictReader(stream)
        columns = reader.fieldnames
        rows = {p['id']: p for p in reader}
    records = {p['id']: p for p in map(json.loads, (folder / 'finance_catalog.jsonl').read_text().splitlines())}
    assignments_path = folder / 'checks/finance_taxonomy/assignments.json'
    assignments = json.loads(assignments_path.read_text())
    overrides_path = folder / 'checks/finance_taxonomy/manual_overrides.json'
    overrides = json.loads(overrides_path.read_text())
    baseline = json.loads((AUDIT / 'baseline_record_hashes.json').read_text())['main']
    for pid, hashes in baseline.items():
        assert digest(rows[pid]) == hashes['csv']
        assert digest(records[pid]) == hashes['jsonl']
        assert digest(assignments[pid]) == hashes['assignment']
    source = {p['id']: p for p in json.loads((AUDIT / 'records.json').read_text())}
    decisions = json.loads((AUDIT / 'review_decisions.json').read_text())
    pdfs = {p['id']: p for p in json.loads((AUDIT / 'fulltext_results.json').read_text())}
    schema = json.loads((folder / 'checks/finance_taxonomy/schema.json').read_text())
    labels = {kind: {p['id']: p['label'] for p in schema[kind]} for kind in ['topics', 'subtopics', 'methods']}
    existing_titles = {key(p['title']): pid for pid, p in records.items() if pid not in decisions}
    existing_dois = {p.get('doi', '').lower(): pid for pid, p in records.items() if p.get('doi') and pid not in decisions}
    admitted = []
    for pid, decision in decisions.items():
        paper = source[pid]
        assert paper['publication_track'] == 'Research Track' and paper['track'] == 'main'
        assert key(paper['title']) not in existing_titles, (pid, 'Duplicate existing title')
        assert not paper['doi'] or paper['doi'] not in existing_dois, (pid, 'Duplicate DOI')
        override = {k: decision[k] for k in ['primary_topic_id', 'topic_ids', 'reason', 'evidence_excerpt']}
        assignment = classify(paper, decision, override)
        overrides[pid] = override
        assignments[pid] = assignment
        finance = {**decision, 'relevance_zh': ('研究问题直接面向金融。' if decision['scope'] == 'core' else
                   '通用方法包含已复核的金融数据、实验或业务场景。'),
                   'primary_topic': labels['topics'][assignment['primary_topic_id']],
                   **{field: assignment[field] for field in ['topic_ids', 'subtopic_ids', 'method_ids']},
                   'topics': [labels['topics'][i] for i in assignment['topic_ids']],
                   'subtopics': [labels['subtopics'][i] for i in assignment['subtopic_ids']],
                   'methods': [labels['methods'][i] for i in assignment['method_ids']],
                   'taxonomy_version': schema['version']}
        result = pdfs[pid]
        download = {'status': 'not_downloaded', 'local_path': ''}
        if result['status'] == 'inspected':
            original = Path('/tmp/ai4finance_kdd_review') / result['cache_filename']
            assert hashlib.sha256(original.read_bytes()).hexdigest() == result['sha256']
            filename = pid + '__' + re.sub(r'[^A-Za-z0-9_-]+', '_', paper['title']).strip('_')[:100] + '.pdf'
            relative = Path('pdfs/KDD') / str(paper['year']) / filename
            target = folder / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(original, target)
            download.update(status='downloaded', local_path=relative.as_posix(),
                            **{field: result[field] for field in ['pages', 'bytes', 'sha256', 'pdf_version', 'source_url']})
        policy = POLICIES[paper['year']]
        length = {'paper_length': 'long', 'evidence_type': 'regular_full_paper_track',
                  'source_url': paper['track_evidence_url'], 'official_track': 'Research Track',
                  'official_section': paper.get('official_section', 'Research Track Papers'),
                  'format_policy_url': policy,
                  'reason': 'Regular KDD Research full-paper track; no short, ADS, Datasets/Benchmarks, workshop, demo or invited entries.'}
        record = {k: paper[k] for k in ['id', 'title', 'authors', 'year', 'venue', 'abstract', 'paper_url', 'doi']}
        record.update(track='main', publication_track='Research Track',
                      pdf_url=download.get('source_url') or ('https://dl.acm.org/doi/pdf/' + paper['doi'] if paper['doi'] else ''),
                      abstract_source=paper['abstract_source'],
                      booktitle=f'Proceedings of the ACM SIGKDD Conference on Knowledge Discovery and Data Mining (Research Track)',
                      metadata_sources=list(dict.fromkeys(filter(None, [paper['track_evidence_url'], paper['abstract_source'],
                          'https://api.crossref.org/works/' + paper['doi'] if paper['doi'] else '']))),
                      awards=[], award_evidence=[], oral=False, oral_evidence=[], presentation_original=[],
                      code_urls=sorted(set(re.findall(r'https?://(?:github\.com|gitlab\.com)/[^\s<>\\)]+', paper['abstract']))),
                      finance=finance, download=download, paper_length='long', paper_length_evidence=length,
                      research={'primary_topic_id': 'finance' if finance['scope'] == 'core' else None,
                                'topic_ids': ['finance'], 'subtopic_ids': [], 'review_status': 'finance_only_classification'})
        records[pid] = record
        row = {k: '' for k in columns}
        row.update(id=pid, title=paper['title'], authors='; '.join(paper['authors']), venue='KDD', year=str(paper['year']),
                   track='main', research_primary_topic='AI for Finance / 金融人工智能' if finance['scope'] == 'core' else '',
                   research_topics='AI for Finance / 金融人工智能', research_topic_ids='finance',
                   research_review_status='finance_only_classification', is_best_or_outstanding='False',
                   is_oral='False', oral_candidate_unverified='False', finance_scope=finance['scope'],
                   finance_primary_topic=finance['primary_topic'], finance_topics='; '.join(finance['topics']),
                   finance_subtopics='; '.join(finance['subtopics']), finance_methods='; '.join(finance['methods']),
                   finance_topic_ids='; '.join(finance['topic_ids']), finance_relevance_zh=finance['relevance_zh'],
                   finance_evidence_type=finance['evidence_type'], finance_evidence_excerpt=finance['evidence_excerpt'],
                   paper_url=paper['paper_url'], pdf_url=record['pdf_url'], download_status=download['status'],
                   code_urls='; '.join(record['code_urls']), metadata_sources='; '.join(record['metadata_sources']),
                   abstract=paper['abstract'], paper_length='long', paper_length_evidence_type=length['evidence_type'],
                   paper_length_evidence_url=length['source_url'])
        if download['status'] == 'downloaded':
            row.update({k: str(download[k]) for k in ['local_path', 'pdf_version', 'pages', 'bytes', 'sha256']})
        rows[pid] = row
        page = folder / 'indexes/finance_notes' / (pid + '.md')
        note = [f'# {paper["title"]}', '', f'KDD {paper["year"]} · Research Track · Main · {finance["scope"]} · long', '',
                f'- Official paper: {paper["paper_url"]}', f'- Research Track: {paper["track_evidence_url"]}',
                f'- Primary task: {finance["primary_topic"]}', f'- Tasks: {"; ".join(finance["topics"])}',
                f'- Subtopics: {"; ".join(finance["subtopics"])}', f'- Methods: {"; ".join(finance["methods"])}',
                f'- Financial evidence source: {decision["evidence_url"]}',
                f'- Long-paper evidence: regular Research full-paper track ([format policy]({policy})).', '',
                '## Financial evidence', '', decision['evidence_excerpt'], '', '## Abstract', '', paper['abstract'], '']
        if download['status'] == 'downloaded':
            from urllib.parse import quote
            note += [f'[PDF]({quote("../../" + download["local_path"], safe="/._-")})', '',
                     f'Version: `{download["pdf_version"]}` · SHA-256: `{download["sha256"]}`', '']
        page.write_text('\n'.join(note))
        admitted.append({'id': pid, 'year': paper['year'], 'doi': paper['doi'],
                         'source_url': paper['track_evidence_url'], 'paper_length_evidence': length})
    ordered = sorted(rows.values(), key=lambda r: (int(r['year']), r['venue'], r['title'].casefold()))
    with (folder / 'finance_catalog.csv').open('w', encoding='utf-8-sig', newline='') as stream:
        writer = csv.DictWriter(stream, columns)
        writer.writeheader()
        writer.writerows(ordered)
    (folder / 'finance_catalog.jsonl').write_text(''.join(json.dumps(records[r['id']], ensure_ascii=False) + '\n' for r in ordered))
    save(assignments_path, assignments)
    save(overrides_path, overrides)
    save(AUDIT / 'admitted_records.json', admitted)
    updates = json.loads((folder / 'checks/collection_updates.json').read_text())
    updates = [u for u in updates if u['venue'] != 'KDD'] + [{
        'date': '2026-11-20', 'venue': 'KDD', 'track': 'main', 'publication_track': 'Research Track',
        'years': [2017, 2026], 'added_papers': len(decisions), 'audit': 'checks/track_screening/kdd/README.md'}]
    save(folder / 'checks/collection_updates.json', updates)
    print('Applied', len(decisions), 'reviewed KDD papers;', len(rows), 'Main long papers.')


if __name__ == '__main__':
    main()
