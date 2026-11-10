#!/usr/bin/env python3
"""Verify both track exports, physical separation, long-paper proof and provenance."""
import csv
import gzip
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote,urlsplit
from paper_length_policy import excluded_publication_reason

ROOT=Path(__file__).resolve().parents[1]
AUDIT=ROOT/'checks/track_screening'


def rows(path):
    with path.open(encoding='utf-8-sig',newline='') as stream:return list(csv.DictReader(stream))


def main():
    for track in ('main','findings'):
        subprocess.run([sys.executable,str(ROOT/'scripts/verify_collection.py')],
                       env={**os.environ,'AI4FINANCE_TRACK':track},check=True)
    catalogs={t:{p['id']:p for p in rows(ROOT/t/'finance_catalog.csv')} for t in ('main','findings')}
    assert not (set(catalogs['main']) & set(catalogs['findings']))
    assert not ({p['paper_url'] for p in catalogs['main'].values()} & {p['paper_url'] for p in catalogs['findings'].values()})
    assert set(p['venue'] for p in catalogs['main'].values())=={'ICML','ICLR','ACL','EMNLP','NeurIPS','AAAI'}
    assert set(p['venue'] for p in catalogs['findings'].values())<={'ACL','EMNLP'}
    for forbidden in ('finance_catalog.csv','finance_catalog.jsonl','pdfs','indexes'):
        assert not (ROOT/forbidden).exists(),('Mixed root artifact',forbidden)
    original={p['id']:p for p in csv.DictReader(io.StringIO(gzip.decompress((AUDIT/'finance_catalog.csv.baseline.gz').read_bytes()).decode('utf-8-sig')))}
    original_records={p['id']:p for p in map(json.loads,gzip.decompress((AUDIT/'finance_catalog.jsonl.baseline.gz').read_bytes()).decode().splitlines())}
    main_records={p['id']:p for p in map(json.loads,(ROOT/'main/finance_catalog.jsonl').read_text().splitlines())}
    length={p['id']:p for p in json.loads((AUDIT/'main_length_review.json').read_text())}
    assert set(catalogs['main'])=={k for k,v in length.items() if v['paper_length']=='long'
                                  and not excluded_publication_reason(original_records[k])}
    for pid,row in catalogs['main'].items():
        assert {k:row[k] for k in original[pid]}==original[pid],(pid,'Original financial catalog fields changed')
        assert {k:v for k,v in main_records[pid].items() if k not in ('paper_length','paper_length_evidence')}==original_records[pid],pid
    findings_records={p['id']:p for p in map(json.loads,(ROOT/'findings/finance_catalog.jsonl').read_text().splitlines())}
    decisions=json.loads((AUDIT/'findings_review_decisions.json').read_text())
    pdfs={p['id']:p for p in json.loads((AUDIT/'findings_fulltext_results.json').read_text())}
    candidate_records=json.loads((AUDIT/'findings_records.json').read_text())
    assert set(pdfs)=={p['id'] for p in candidate_records if p['fulltext_candidate']}
    assert all(p['status']=='inspected' for p in pdfs.values())
    assert set(catalogs['findings'])=={k for k in decisions if pdfs[k]['content_exceeds_short_limit']}
    for track,records in [('main',main_records),('findings',findings_records)]:
        for pid,p in records.items():
            e=p['paper_length_evidence']
            assert e['paper_length']=='long'
            if e['evidence_type']=='publisher_content_boundary_inspection':
                proof=e['inspection'];assert proof['inspected_content_page']>=6
                assert proof['sixth_content_page_words']>=160
                assert proof['first_backmatter_page']>=proof['inspected_content_page']
                assert e['pdf_sha256']==p['download']['sha256']
                if proof['inspected_content_page']>9:
                    visual=json.loads((AUDIT/'long_only_recheck.json').read_text())['visual_checks'][pid]
                    assert visual['pdf_sha256']==p['download']['sha256']
                    assert visual['inspected_pdf_page']==6 and visual['main_body_confirmed']
            if track=='findings':
                assert pdfs[pid]['title_token_overlap']>=0.8
                assert p['finance']['scope']==decisions[pid]['scope']
    official_ids=set()
    for source in json.loads((AUDIT/'findings_sources.json').read_text()):
        path=ROOT/source['file']
        data=gzip.decompress(path.read_bytes())
        assert hashlib.sha256(data).hexdigest()==source['uncompressed_sha256']
        tree=ET.fromstring(data);year=tree.get('id').split('.')[0]
        for volume in tree.findall('volume'):
            if volume.get('id') in ('acl','emnlp'):
                official_ids.update(f"{year}.findings-{volume.get('id')}.{p.get('id')}" for p in volume.findall('paper'))
    inventory=list(csv.DictReader(io.StringIO(gzip.decompress((AUDIT/'screening_inventory.csv.gz').read_bytes()).decode('utf-8-sig'))))
    assert official_ids=={p['id'] for p in inventory if p['track']=='findings'}
    assert {p['id'] for p in inventory if p['disposition']=='admitted_long_finance'}==set(main_records)|set(findings_records)
    main_source=json.loads((AUDIT/'main_sources.json').read_text())
    assert hashlib.sha256(gzip.decompress((ROOT/main_source['file']).read_bytes())).hexdigest()==main_source['uncompressed_sha256']
    links=0
    for path in ROOT.rglob('*.md'):
        if '.git' in path.parts:continue
        for target in re.findall(r'\]\(([^)]+)\)',path.read_text()):
            url=urlsplit(target.strip('<>'))
            if url.scheme or url.netloc or not url.path:continue
            resolved=(path.parent/unquote(url.path)).resolve()
            assert resolved.is_relative_to(ROOT) and (resolved.exists() or resolved==AUDIT/'validation.json'),(str(path.relative_to(ROOT)),target)
            links+=1
    report=dict(main_long_papers=len(main_records),findings_long_papers=len(findings_records),
                all_track_ids_disjoint=True,all_root_and_track_links_resolve=True,
                local_markdown_links_checked=links,main_original_financial_fields_preserved=True,
                official_findings_inventory_complete=True,findings_source_records=len(official_ids),
                screening_inventory_records=len(inventory),long_paper_evidence_validated=True)
    report['explicit_short_paper_records']=0
    recheck=json.loads((AUDIT/'long_only_recheck.json').read_text())
    assert recheck['admitted_main']==len(main_records) and recheck['admitted_findings']==len(findings_records)
    (AUDIT/'validation.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
