#!/usr/bin/env python3
"""Audit AAAI provenance and preservation of pre-existing collection records."""
import csv
import gzip
import hashlib
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'checks/aaai_expansion'


def fingerprint(record):
    return hashlib.sha256(json.dumps(record, ensure_ascii=False, sort_keys=True).encode()).hexdigest()


def main():
    with (ROOT / 'finance_catalog.csv').open(encoding='utf-8-sig', newline='') as stream:
        rows = {r['id']: r for r in csv.DictReader(stream)}
    records = {r['id']: r for r in map(json.loads, (ROOT / 'finance_catalog.jsonl').read_text().splitlines())}
    assignments = json.loads((ROOT / 'checks/finance_taxonomy/assignments.json').read_text())
    baseline = json.loads((DEST / 'baseline_record_hashes.json').read_text())
    for pid, expected in baseline['papers'].items():
        assert fingerprint(rows[pid]) == expected['csv_record'], (pid, 'Original CSV changed')
        assert fingerprint(records[pid]) == expected['jsonl_record'], (pid, 'Original JSONL changed')
        assert fingerprint(assignments[pid]) == expected['assignment'], (pid, 'Original classification changed')

    publisher = {}
    sources = json.loads((DEST / 'source_manifest.json').read_text())
    for source in sources:
        raw = gzip.decompress((ROOT / source['file']).read_bytes())
        assert hashlib.sha256(raw).hexdigest() == source['sha256_uncompressed']
        for paper in json.loads(raw)['message']['items']:
            publisher[paper['DOI'].lower()] = paper
    decisions = json.loads((DEST / 'review_decisions.json').read_text())
    pdfs = {p['id']: p for p in json.loads((DEST / 'pdf_results.json').read_text())}
    aaai_ids = {pid for pid, row in rows.items() if row['venue'] == 'AAAI'}
    assert aaai_ids == set(decisions) == set(pdfs)
    rules = json.loads((DEST / 'track_rules.json').read_text())
    legacy = json.loads((DEST / 'legacy_sections.json').read_text())
    evidence_counts = Counter()
    for pid in aaai_ids:
        row, record, decision = rows[pid], records[pid], decisions[pid]
        original = publisher[record['doi'].lower()]
        assert int(original['volume']) + 1986 == int(row['year'])
        assert record['volume'] == original['volume'] and record['issue'] == original['issue']
        assert row['track'] == record['track'] == 'main'
        year = int(row['year'])
        if year >= 2020:
            assert 1 <= int(record['issue']) <= rules[str(year)]['last_main_issue'], pid
        else:
            assert legacy[pid]['track'] == 'main' and legacy[pid]['section'], pid
        assert row['finance_scope'] == decision['scope'], pid
        assert row['finance_evidence_excerpt'] == decision['evidence_excerpt'], pid
        assert row['download_status'] == 'downloaded' and pdfs[pid]['identity']['identity_verified'], pid
        assert pdfs[pid]['sha256'] == row['sha256'], pid
        if decision['evidence_type'].startswith('fulltext_'):
            assert row['finance_scope'] == 'application', pid
            assert decision['evidence_pdf_sha256'] == row['sha256'], pid
            assert decision['evidence_pdf_version'] == row['pdf_version'], pid
        if row['pdf_version'] == 'arxiv_author_version':
            assert pdfs[pid]['requested_url'].startswith('https://arxiv.org/pdf/'), pid
        evidence_counts[decision['evidence_type']] += 1
        note = (ROOT / f'indexes/finance_notes/{pid}.md').read_text()
        assert f"AAAI {row['year']} · main · {row['finance_scope']}" in note
    # Concrete boundary cases: technical proceedings also contain ineligible tracks.
    for excluded in ['aaai-2018-11411', 'aaai-2020-5623', 'aaai-2023-26973',
                     'aaai-2024-30126', 'aaai-2025-34970', 'aaai-2026-41099']:
        assert excluded not in rows, excluded
    assert all(row['track'] == 'main' for row in rows.values())
    report = {
        'validated_at_utc': datetime.now(timezone.utc).isoformat(),
        'original_records_preserved': len(baseline['papers']),
        'original_csv_jsonl_and_classifications_unchanged': True,
        'publisher_metadata_records': len(publisher), 'source_cache_hashes_match': True,
        'aaai_papers': len(aaai_ids),
        'aaai_years': dict(sorted(Counter(rows[pid]['year'] for pid in aaai_ids).items())),
        'aaai_scope': dict(Counter(rows[pid]['finance_scope'] for pid in aaai_ids)),
        'aaai_evidence_types': dict(evidence_counts),
        'aaai_pdf_versions': dict(Counter(rows[pid]['pdf_version'] for pid in aaai_ids)),
        'aaai_pdfs_identity_verified': len(aaai_ids),
        'main_track_memberships_checked': True, 'special_track_examples_excluded': True,
        'all_records_main_only': True, 'collection_papers': len(rows),
    }
    (DEST / 'validation.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
