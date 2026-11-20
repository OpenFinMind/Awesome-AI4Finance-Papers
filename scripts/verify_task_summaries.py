#!/usr/bin/env python3
"""Verify summary provenance, track membership and reproducible page insertion."""
import hashlib
import json
import re
from pathlib import Path

from task_summaries import START, END, render_summary
from collection_io import partitions

ROOT = Path(__file__).resolve().parents[1]


def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True).encode()).hexdigest()


def main():
    total = dict(summary_pages=0, populated_summaries=0, empty_task_notices=0,
                 unique_representative_papers=0, representative_paper_appearances=0)
    report = {}
    for track,scope,folder in partitions():
        records = {p['id']: p for p in map(json.loads, (folder / 'finance_catalog.jsonl').read_text().splitlines())}
        assignments = json.loads((folder / 'checks/finance_taxonomy/assignments.json').read_text())
        schema = json.loads((folder / 'checks/finance_taxonomy/schema.json').read_text())
        evidence = json.loads((folder / 'checks/task_summaries/evidence.json').read_text())
        tasks = {t['id'] for t in schema['topics']}
        assert evidence['track'] == track and evidence['scope']==scope and set(evidence['topics']) == tasks
        assert {p.stem for p in (folder / 'summaries').glob('*.md')} == tasks
        for name, sha in evidence['preserved_input_sha256'].items():
            assert hashlib.sha256((folder / name).read_bytes()).hexdigest() == sha, (track, name, 'Input changed')
        referenced = set()
        nonempty = appearances = 0
        unique_prose = set()
        for task in sorted(tasks):
            proof = evidence['topics'][task]
            members = {pid for pid in records if task in assignments[pid]['topic_ids']}
            assert proof['task_memberships'] == len(members)
            assert proof['core'] == sum(records[pid]['finance']['scope'] == 'core' for pid in members)
            assert proof['application'] == len(members) - proof['core']
            source = folder / 'summaries' / (task + '.md')
            text = source.read_text()
            assert hashlib.sha256(text.encode()).hexdigest() == proof['source_sha256'], (track, task, 'Unreviewed source edit')
            assert '### 中文' in text and '### English' in text
            ids = proof['representative_ids']
            assert len(ids) == len(set(ids)) and set(ids) <= members
            links = set(re.findall(r'finance_notes/([^/\s)]+)\.md', text))
            assert links == set(ids), (track, task, 'Reference mismatch')
            if members:
                nonempty += 1
                assert ids and '### Representative papers / 代表论文' in text
                assert '研究机会（编辑判断）' in text and 'Research opportunities (editorial)' in text
                prose = text.split('### 中文', 1)[1].split('### Representative papers', 1)[0]
                assert prose not in unique_prose, (track, task, 'Repeated summary')
                unique_prose.add(prose)
                for row in proof['contribution_and_boundary_notes']:
                    assert row['id'] in ids
                    assert all(row[field] in text for field in ('contribution_zh', 'contribution_en', 'boundary_zh', 'boundary_en'))
            else:
                assert not ids and '暂无收录论文' in text and 'has no admitted papers' in text
            page = folder / 'indexes/finance_topics' / (task + '.md')
            rendered = page.read_text()
            assert rendered.count(START) == rendered.count(END) == 1
            block = rendered[rendered.index(START):rendered.index(END) + len(END)]
            assert block == render_summary(folder, task, page), (track, task, 'Generated prose differs')
            assert rendered.index(START) < rendered.index(END) < rendered.index('## Subtopic statistics') < rendered.index('## Full paper list')
            list_ids = re.findall(r'finance_notes/([^/\s)]+)\.md', rendered.split('## Full paper list', 1)[1])
            assert set(list_ids) == members and len(list_ids) == len(members), (track, task, 'Full list changed')
            appearances += len(ids)
            referenced.update(ids)
        assert referenced == set(evidence['papers'])
        for pid, proof in evidence['papers'].items():
            paper = records[pid]
            assert proof['catalog_record_sha256'] == digest(paper), (track, pid, 'Stale evidence')
            assert proof['abstract'] == paper['abstract'] and proof['official_url'] == paper['paper_url']
            if proof['fulltext_available']:
                assert proof['pdf_sha256'] == paper['download']['sha256']
                assert (folder / proof['pdf_path']).is_file() and proof['fulltext_characters'] > 1000
        result = dict(track=track, scope=scope, summary_pages=len(tasks), populated_summaries=nonempty,
                      empty_task_notices=len(tasks)-nonempty, unique_representative_papers=len(referenced),
                      representative_paper_appearances=appearances,
                      current_task_membership_verified=True, bilingual_sources_verified=True,
                      source_and_rendered_summary_identical=True, complete_paper_lists_preserved=True,
                      catalog_and_classification_inputs_preserved=True,
                      evidence_bound_to_catalog_and_pdf_hashes=True)
        (folder / 'checks/task_summaries/validation.json').write_text(json.dumps(result, indent=2)+'\n')
        report[track+'/'+scope] = result
        for key in total:
            total[key] += result[key]
    report['total'] = total
    (ROOT / 'checks/task_summaries_validation.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
