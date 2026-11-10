#!/usr/bin/env python3
"""Write one screening disposition per source record, without presentation filters."""
import csv
import gzip
import io
import json
from collections import Counter
from pathlib import Path

from screen_tracks import FIN, save
from paper_length_policy import excluded_publication_reason

ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'checks/track_screening'


def csv_rows(path):
    with path.open(encoding='utf-8-sig',newline='') as stream:
        return list(csv.DictReader(stream))


def main():
    main_ids={p['id'] for p in csv_rows(ROOT/'main/finance_catalog.csv')}
    findings_ids={p['id'] for p in csv_rows(ROOT/'findings/finance_catalog.csv')}
    old={p['id']:p for p in csv_rows(ROOT/'main/checks/initial_screening/all_candidate_dispositions.csv')}
    length={p['id']:p for p in json.loads((DEST/'main_length_review.json').read_text())}
    rows=[]
    for p in json.loads(gzip.decompress((ROOT/'main/sources/initial_main_universe.json.gz').read_bytes())):
        pid=p['id']
        outside=excluded_publication_reason(p)
        status=('admitted_long_finance' if pid in main_ids else
                'short_paper_excluded' if pid in length and length[pid]['paper_length']=='short' else
                'finance_length_unverified' if pid in length else
                old[pid]['status'] if pid in old else 'metadata_screen_no_confirmed_finance')
        if outside:status='outside_main_track'
        rows.append(dict(id=pid,venue=p['venue'],year=p['year'],track='other_or_unverified' if outside else 'main',
                         abstract_available=bool(p['abstract']),metadata_finance_signal=bool(FIN.search(p['title']+' '+p['abstract'])),
                         disposition=status,reason=outside or old.get(pid,{}).get('reason','See initial full-universe screening evidence; not a proof of financial irrelevance.')))
    publisher={}
    rules=json.loads((ROOT/'main/checks/aaai_expansion/track_rules.json').read_text())
    legacy=set(json.loads((ROOT/'main/checks/aaai_expansion/legacy_main_ids.json').read_text()))
    aaai={p['id']:p for p in csv_rows(ROOT/'main/checks/aaai_expansion/candidate_dispositions.csv')}
    for path in sorted((ROOT/'main/sources/aaai').glob('crossref_*.json.gz')):
        for item in json.loads(gzip.decompress(path.read_bytes()))['message']['items']:
            volume=str(item.get('volume',''));url=item.get('resource',{}).get('primary',{}).get('URL','')
            ident=url.rstrip('/').split('/')[-1]
            if not volume.isdigit() or not 31<=int(volume)<=40 or not ident.isdigit():continue
            year=int(volume)+1986;pid=f'aaai-{year}-{ident}';issue=str(item.get('issue',''))
            main_track=pid in legacy if year<2020 else issue.isdigit() and 1<=int(issue)<=rules[str(year)]['last_main_issue']
            status='admitted_long_finance' if pid in main_ids else aaai.get(pid,{}).get('disposition',aaai.get(pid,{}).get('status','metadata_screen_no_confirmed_finance'))
            if not main_track:status='outside_verified_main_track'
            publisher[pid]=dict(id=pid,venue='AAAI',year=year,track='main' if main_track else 'other_or_unverified',
                abstract_available=bool(item.get('abstract')),metadata_finance_signal=bool(FIN.search(str(item.get('title',''))+' '+str(item.get('abstract','')))),
                disposition=status,reason=aaai.get(pid,{}).get('reason','Publisher main-track membership and metadata screened; see the AAAI audit.'))
    rows+=list(publisher.values())
    # Full-text review decisions are independent of the original Main list.
    decisions=json.loads((DEST/'findings_review_decisions.json').read_text())
    pdfs={p['id']:p for p in json.loads((DEST/'findings_fulltext_results.json').read_text())}
    findings=json.loads((DEST/'findings_records.json').read_text())
    for p in findings:
        pid=p['id']
        if pid in findings_ids:status='admitted_long_finance';reason='Reviewed financial evidence and verified long-paper content extent.'
        elif pid in decisions:status='finance_length_unverified';reason='Financial relevance confirmed; long-paper eligibility is not verified.'
        elif pid in pdfs:status='fulltext_screen_not_confirmed';reason='Reviewed candidate text; no substantive financial task/data/case admitted. Background, lexical, funding, affiliation and reference-only hits do not suffice.'
        else:status='metadata_screen_no_candidate';reason='No candidate under the documented metadata query; unreviewed full text may still contain financial applications.'
        rows.append(dict(id=pid,venue=p['venue'],year=p['year'],track='findings',abstract_available=bool(p['abstract']),
                         metadata_finance_signal=bool(p['metadata_hits']),disposition=status,reason=reason))
    assert len({p['id'] for p in rows})==len(rows)
    data=io.StringIO(newline='');writer=csv.DictWriter(data,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
    (DEST/'screening_inventory.csv.gz').write_bytes(gzip.compress(data.getvalue().encode('utf-8-sig'),mtime=0))
    save(DEST/'screening_summary.json',dict(source_records=len(rows),
        initial_main_universe_records=len(rows)-len(publisher)-len(findings),aaai_publisher_records=len(publisher),
        aaai_verified_main_records=sum(p['track']=='main' for p in publisher.values()),
        findings_records=len(findings),findings_fulltexts_inspected=len(pdfs),
        independent_of_award_or_presentation=True,findings_finance_confirmed=len(decisions),
        findings_long_finance_admitted=len(findings_ids),main_long_finance_admitted=len(main_ids),
        dispositions=dict(Counter(p['disposition'] for p in rows)),
        venue_track_source_counts=dict(Counter(p['venue']+'/'+p['track'] for p in rows)),
        caveat='Corpus-wide metadata screening with targeted full-text review. A negative query or unavailable/unreviewed full text is not proof of financial irrelevance.'))
    print(f'Wrote {len(rows):,} screening dispositions.')


if __name__=='__main__':main()
