#!/usr/bin/env python3
"""Verify migration against immutable v2 inputs and explicit v3 decisions."""
import csv,json,gzip,io,hashlib
from collections import Counter
from collection_io import ROOT,TRACKS,SCOPES,catalog,records,assignments,legacy
from taxonomy_v3 import schema

def digest(v):return hashlib.sha256(json.dumps(v,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
def main():
    audit=ROOT/'checks/taxonomy_v3';manifest=json.loads((audit/'migration.json').read_text());entries={r['id']:r for r in manifest['papers']}
    decisions={r['id']:r for r in map(json.loads,(audit/'decisions.jsonl').read_text().splitlines())}
    assert len(entries)==len(manifest['papers'])==len(decisions)==1631
    origin=json.loads((audit/'baseline_origin.json').read_text());frozen=json.loads((audit/'baseline_manifest.json').read_text())
    assert hashlib.sha256((audit/'baseline.json.gz').read_bytes()).hexdigest()==origin['baseline_sha256']==frozen['baseline_sha256']
    assert origin['original_git_blobs_verified']==58 and origin['all_snapshot_files_match_source_commit']
    s=schema();parents={r['id']:r['parent_id'] for r in s['subtopics']}
    assert len(s['topics'])==18 and len(s['subtopics'])==111 and len(s['methods'])==15
    assert len(parents)==111
    seen=set();scopes={};pdfs=0;scopechanges=[];pending=[]
    mutable_finance={'scope','primary_topic','primary_topic_id','primary_subtopic_id','topic_ids','topics','subtopic_ids','subtopics','method_ids','methods','taxonomy_version','review_status','classification_reason','classification_evidence_excerpt'}
    mutable_csv={'finance_scope','finance_primary_topic','finance_topics','finance_subtopics','finance_methods','finance_topic_ids','finance_primary_topic_id','finance_primary_subtopic_id','finance_primary_subtopic','finance_review_status','local_path'}
    for track in TRACKS:
        new=records(track);rows=catalog(track);a=assignments(track);old=legacy(track,'jsonl');oldrows=legacy(track,'csv')
        assert set(new)==set(rows)==set(a)==set(old)==set(oldrows)
        assert not seen.intersection(new);seen.update(new)
        for pid,p in new.items():
            d=decisions[pid];before=old[pid];entry=entries[pid];scope=d['scope']
            assert p['finance']['scope']==rows[pid]['finance_scope']==scope
            assert d['track']==track and entry['track']==track
            assert entry['original_record_sha256']==digest(before) and entry['record_sha256']==digest({**p,'download':{**p.get('download',{}),'local_path':p['download']['local_path'].split('/',1)[1]}} if p.get('download',{}).get('local_path') else p)
            # Every non-taxonomy record field and inclusion/length proof is immutable.
            normalized=json.loads(json.dumps(p));original=json.loads(json.dumps(before))
            normalized.pop('finance');original.pop('finance')
            if normalized.get('download',{}).get('local_path'):normalized['download']['local_path']=normalized['download']['local_path'].split('/',1)[1]
            assert normalized==original,(pid,'Non-taxonomy record changed')
            for key,value in before['finance'].items():
                if key not in mutable_finance:assert p['finance'][key]==value,(pid,key)
            for key,value in oldrows[pid].items():
                if key not in mutable_csv:assert rows[pid][key]==value,(pid,key)
            expected=scope+'/'+oldrows[pid]['local_path'] if oldrows[pid]['local_path'] else ''
            assert rows[pid]['local_path']==expected
            assert d['primary_topic_id']==a[pid]['primary_topic_id']
            for field in ('topic_ids','subtopic_ids','method_ids','primary_subtopic_id'):assert d[field]==a[pid][field]==p['finance'][field],(pid,field)
            assert d['primary_topic_id'] in d['topic_ids']
            if d['primary_subtopic_id']:
                assert parents[d['primary_subtopic_id']]==d['primary_topic_id'] and d['primary_subtopic_id'] in d['subtopic_ids']
            else:assert d['status']=='needs_review';pending.append(pid)
            assert all(parents[sub] in d['topic_ids'] for sub in d['subtopic_ids'])
            if scope!=before['finance']['scope']:
                assert d['scope_review_status']=='official_abstract_review' and d.get('scope_reason');scopechanges.append(pid)
            if rows[pid]['local_path']:
                path=ROOT/track/rows[pid]['local_path'];assert path.is_file() and path.stat().st_size==int(rows[pid]['bytes']);assert entry['pdf_path']==str(path.relative_to(ROOT));assert entry['sha256']==rows[pid]['sha256'];pdfs+=1
        scopes[track]=dict(Counter(p['finance']['scope'] for p in new.values()))
        for forbidden in ('finance_catalog.csv','finance_catalog.jsonl','finance_catalog.xlsx','finance_references.bib','pdfs','indexes','summaries'):
            assert not (ROOT/track/forbidden).exists(),(track,'Legacy mixed-scope artifact',forbidden)
    assert seen==set(decisions)==set(entries)
    assert pdfs==1543
    report=dict(papers=len(seen),pdfs=pdfs,topics=18,subtopics=111,methods=15,scope=scopes,scope_changes=len(scopechanges),scope_changed_ids=scopechanges,pending_subcategory_ids=pending,all_original_papers_accounted_for=True,all_non_taxonomy_fields_preserved=True,admission_and_length_proofs_preserved=True,explicit_decisions_match_all_catalogs=True,four_partitions_disjoint=True,classification_status_counts=dict(Counter(d['status'] for d in decisions.values())))
    (audit/'validation.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
