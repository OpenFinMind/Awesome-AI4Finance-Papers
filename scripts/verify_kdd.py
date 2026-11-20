#!/usr/bin/env python3
"""Verify KDD Research membership, reviewed financial evidence and preservation."""
import csv
import gzip
import hashlib
import io
import json
from collections import Counter

from collect_kdd import AUDIT, ROOT, SOURCES, URLS, POLICIES, parse, save
from apply_kdd_update import digest
from collection_io import catalog,records as track_records,assignments as track_assignments,legacy


def load(name):
    return json.loads((AUDIT / name).read_text())


def csv_records(path):
    with path.open(encoding='utf-8-sig', newline='') as stream:
        return {p['id']: p for p in csv.DictReader(stream)}


def main():
    manifest = load('source_manifest.json')
    assert {p['file'] for p in manifest} == {p.relative_to(ROOT).as_posix() for p in SOURCES.glob('*.gz')}
    for source in manifest:
        raw = (ROOT / source['file']).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == source['compressed_sha256']
        assert hashlib.sha256(gzip.decompress(raw)).hexdigest() == source['uncompressed_sha256']
    sources = {p['id']: p for p in load('records.json')}
    official = {}
    counts = {}
    for year in URLS:
        path = SOURCES / f'official_{year}.html.gz'
        meta = json.loads(path.with_suffix('.gz.meta.json').read_text())
        assert meta['url'].rstrip('/') == URLS[year].rstrip('/')
        papers = parse(year, gzip.decompress(path.read_bytes()))
        counts[year] = len(papers)
        official.update({p['id']: p for p in papers})
        policy = SOURCES / f'research_policy_{year}.html.gz'
        pm = json.loads(policy.with_suffix('.gz.meta.json').read_text())
        assert pm['url'].rstrip('/') == POLICIES[year].rstrip('/'), (year, pm['url'])
        assert len(gzip.decompress(policy.read_bytes())) > 1000
    assert set(official) == set(sources)
    for pid, paper in sources.items():
        assert paper['title'] == official[pid]['title']
        assert paper['year'] == official[pid]['year']
        assert paper['publication_track'] == 'Research Track' and paper['track'] == 'main'
    baseline = load('baseline_record_hashes.json')
    catalogs, records, assignments = {}, {}, {}
    for track in ('main', 'findings'):
        catalogs[track] = catalog(track)
        records[track] = track_records(track)
        assignments[track] = track_assignments(track)
        historical={kind:legacy(track,kind) for kind in ('csv','jsonl','assignment')}
        for pid, hashes in baseline[track].items():
            assert digest(historical['csv'][pid]) == hashes['csv'], (pid, 'CSV changed')
            assert digest(historical['jsonl'][pid]) == hashes['jsonl'], (pid, 'JSONL changed')
            assert digest(historical['assignment'][pid]) == hashes['assignment'], (pid, 'assignment changed')
    decisions = load('review_decisions.json')
    admitted = {p['id']: p for p in load('admitted_records.json')}
    inspections = {p['id']: p for p in load('fulltext_results.json')}
    candidates = {p['id']: p for p in load('candidate_queue.json')}
    kdd = {pid: p for pid, p in records['main'].items() if p['venue'] == 'KDD'}
    assert set(kdd) == set(decisions) == set(admitted)
    assert set(records['main']) == set(baseline['main']) | set(kdd)
    assert set(records['findings']) == set(baseline['findings'])
    assert not any(p['venue'] == 'KDD' for p in records['findings'].values())
    assert set(inspections) == set(candidates) == {p['id'] for p in sources.values() if p['fulltext_candidate']}
    legacy_main_assignments=legacy("main","assignment")
    pdf_count = 0
    for pid, paper in kdd.items():
        decision, source = decisions[pid], sources[pid]
        proof = paper['paper_length_evidence']
        assert proof == admitted[pid]['paper_length_evidence']
        assert proof['evidence_type'] == 'regular_full_paper_track' and proof['paper_length'] == 'long'
        assert proof['official_track'] == paper['publication_track'] == 'Research Track'
        assert proof['source_url'] == URLS[paper['year']] == source['track_evidence_url']
        assert proof['format_policy_url'] == POLICIES[paper['year']]
        assert paper['paper_length'] == 'long' and paper['track'] == 'main'
        assert decision['evidence_excerpt'] and decision['evidence_url'] and decision['reason']
        assert paper['finance']['scope'] == decision['scope']
        assert legacy_main_assignments[pid]['primary_topic_id'] == decision['primary_topic_id']
        assert set(legacy_main_assignments[pid]['topic_ids']) == set(decision['topic_ids'])
        if 'benchmark_evidence' in decision:
            benchmark = decision['benchmark_evidence']
            assert (ROOT / benchmark['cached_document']).exists()
            assert benchmark['paper_results_excerpt'] and benchmark['benchmark_definition']
        download = paper['download']
        if download['status'] == 'downloaded':
            pdf_count += 1
            inspected = inspections[pid]
            assert inspected['status'] == 'inspected' and inspected['title_token_overlap'] >= .65
            data = (ROOT / 'main' / download['local_path']).read_bytes()
            assert data.startswith(b'%PDF-')
            assert hashlib.sha256(data).hexdigest() == download['sha256'] == inspected['sha256']
            assert len(data) == download['bytes'] == inspected['bytes']
    inventory = list(csv.DictReader(io.StringIO(gzip.decompress((AUDIT.parent / 'screening_inventory.csv.gz').read_bytes()).decode('utf-8-sig'))))
    kdd_inventory = {p['id']: p for p in inventory if p['venue'] == 'KDD'}
    assert set(kdd_inventory) == set(official)
    assert {pid for pid, p in kdd_inventory.items() if p['disposition'] == 'admitted_long_finance'} == set(kdd)
    assert all(p['track'] == 'main' for p in kdd_inventory.values())
    report = dict(official_research_records=len(official), official_counts_by_year=counts,
                  source_hashes_verified=len(manifest), official_research_sources_reparsed=True,
                  regular_full_paper_policies_verified=len(POLICIES), admitted=len(kdd),
                  admitted_pdfs=pdf_count, financial_scopes=dict(Counter(p['scope'] for p in decisions.values())),
                  original_main_records_preserved=len(baseline['main']),
                  original_findings_records_preserved=len(baseline['findings']),
                  findings_admissions_preserved=True, complete_kdd_inventory=True,
                  historical_kdd_decisions_verified=True,v3_classification_migration_verified_separately=True, downloaded_pdf_hashes_and_identity_verified=True)
    save(AUDIT / 'validation.json', report)
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
