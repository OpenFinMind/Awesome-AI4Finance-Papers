#!/usr/bin/env python3
"""Build physically separate long-paper catalogs from preserved review inputs."""
import csv
import gzip
import json
import re
import shutil
from pathlib import Path

from finance_taxonomy_rules import classify
from screen_tracks import save
from paper_length_policy import short_paper_reason, excluded_publication_reason

ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT/'checks/track_screening'
CACHE = Path('/tmp/ai4finance_findings_review')
POLICY = 'https://github.com/acl-org/acl-style-files/blob/master/formatting.md#paper-length'


def clean(value):
    if isinstance(value,str):
        return re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]','',value)
    if isinstance(value,list):
        return [clean(x) for x in value]
    if isinstance(value,dict):
        return {k:clean(v) for k,v in value.items()}
    return value


def write_catalog(folder, rows, records, assignments, columns):
    rows=sorted(rows,key=lambda r:(r['venue'],int(r['year']),r['title'].casefold()))
    with (folder/'finance_catalog.csv').open('w',encoding='utf-8-sig',newline='') as stream:
        writer=csv.DictWriter(stream,fieldnames=columns)
        writer.writeheader();writer.writerows(rows)
    (folder/'finance_catalog.jsonl').write_text(''.join(json.dumps(records[r['id']],ensure_ascii=False)+'\n' for r in rows))
    save(folder/'checks/finance_taxonomy/assignments.json',assignments)


def main():
    import io
    reader=csv.DictReader(io.StringIO(gzip.decompress((AUDIT/'finance_catalog.csv.baseline.gz').read_bytes()).decode('utf-8-sig')))
    original_rows=list(reader)
    columns=list(reader.fieldnames)+['paper_length','paper_length_evidence_type','paper_length_evidence_url']
    original_records={p['id']:p for p in map(json.loads,gzip.decompress((AUDIT/'finance_catalog.jsonl.baseline.gz').read_bytes()).decode().splitlines())}
    main_folder=ROOT/'main'
    length={r['id']:r for r in json.loads((AUDIT/'main_length_review.json').read_text())}
    reviewed_path=AUDIT/'length_overrides.json'
    if reviewed_path.exists():
        for pid,review in json.loads(reviewed_path.read_text()).items():
            if review['track']=='main':
                assert original_records[pid]['download']['sha256']==review['pdf_sha256']
                length[pid].update(review)
        save(AUDIT/'main_length_review.json',list(length.values()))
    old_assign=json.loads((main_folder/'checks/finance_taxonomy/assignments.json').read_text())
    rows=[];records={};assignments={};removed=[]
    for row in original_rows:
        pid=row['id'];evidence=length[pid]
        outside=excluded_publication_reason(original_records[pid])
        if outside:
            removed.append(dict(id=pid,title=row['title'],reason='outside_main_track',publication_evidence=outside,
                                length_evidence=evidence))
            continue
        assert not (evidence['paper_length']=='long' and short_paper_reason(original_records[pid])), (pid,'Contradictory short-paper evidence')
        if evidence['paper_length']!='long':
            removed.append(dict(id=pid,title=row['title'],reason=evidence['paper_length'],length_evidence=evidence))
            continue
        row.update(paper_length='long',paper_length_evidence_type=evidence['evidence_type'],
                   paper_length_evidence_url=evidence.get('source_url',row['paper_url']))
        records[pid]={**original_records[pid], 'paper_length':'long','paper_length_evidence':evidence}
        rows.append(row);assignments[pid]=old_assign[pid]
    write_catalog(main_folder,rows,records,assignments,columns)
    save(AUDIT/'main_scope_migration.json',dict(source_commit='685f2131547bddf32a41f6900e713a76dd7b0a3d',
        original_records=len(original_rows),retained=len(rows),removed_or_pending=removed,
        financial_decisions_and_classifications_preserved=True,
        content_length_rule='Substantive content beyond page five, before explicit back matter; never total PDF pages.',
        content_length_policy=POLICY))
    old_overrides=json.loads((main_folder/'checks/finance_taxonomy/manual_overrides.json').read_text())
    save(main_folder/'checks/finance_taxonomy/manual_overrides.json',{k:v for k,v in old_overrides.items() if k in assignments})
    folder=ROOT/'findings'
    (folder/'indexes/finance_notes').mkdir(parents=True,exist_ok=True)
    for name in ['checks/finance_taxonomy/schema.json','indexes/finance_taxonomy.md']:
        (folder/name).parent.mkdir(parents=True,exist_ok=True);shutil.copy2(main_folder/name,folder/name)
    schema=json.loads((folder/'checks/finance_taxonomy/schema.json').read_text())
    definitions={kind:{item['id']:item['label'] for item in schema[kind]} for kind in ('topics','subtopics','methods')}
    candidates={p['id']:p for p in json.loads((AUDIT/'findings_records.json').read_text())}
    results={p['id']:p for p in json.loads((AUDIT/'findings_fulltext_results.json').read_text())}
    decisions=json.loads((AUDIT/'findings_review_decisions.json').read_text())
    # A malicious-link attack is a cybersecurity task; its name alone is not financial evidence.
    decisions.pop('2026.findings-acl.686',None)
    save(AUDIT/'findings_review_decisions.json',decisions)
    labels={};rows=[];records={};assignments={};overrides={};pending=[]
    override_path=AUDIT/'findings_taxonomy_overrides.json'
    if override_path.exists():overrides=json.loads(override_path.read_text())
    for pid,decision in decisions.items():
        paper=candidates[pid];pdf=results[pid]
        assert not short_paper_reason(paper), (pid,'Short papers cannot enter Findings')
        assert pdf['title_token_overlap']>=0.8,(pid,'PDF title not verified')
        if not pdf['content_exceeds_short_limit']:
            pending.append(dict(id=pid,title=paper['title'],reason='long_paper_type_unverified',
                                inspection=pdf['length_inspection'],paper_url=paper['paper_url']))
            continue
        assignment=clean(classify(paper,decision,overrides.get(pid)))
        finance=clean({**decision,'primary_topic':definitions['topics'][assignment['primary_topic_id']],
                 'relevance_zh':'以金融任务为核心研究对象。' if decision['scope']=='core' else '通用方法包含已复核的金融数据、实验或场景。',
                 'taxonomy_version':schema['version'],**{field:assignment[field] for field in ('topic_ids','subtopic_ids','method_ids')}})
        for kind,field in [('topics','topic_ids'),('subtopics','subtopic_ids'),('methods','method_ids')]:
            finance[kind]=[definitions[kind][i] for i in assignment[field]]
        relative=f"pdfs/{paper['venue']}/{paper['year']}/{pid}.pdf"
        target=folder/relative;target.parent.mkdir(parents=True,exist_ok=True)
        if not target.exists():shutil.copy2(CACHE/(pid+'.pdf'),target)
        download=dict(id=pid,status='downloaded',local_path=relative,pdf_version='publisher',
                      bytes=pdf['bytes'],sha256=pdf['sha256'],pages=pdf['pages'],
                      requested_url=paper['pdf_url'],final_url=paper['pdf_url'],
                      identity_verification='Official paper-specific Anthology PDF; title tokens verified on first page.',
                      title_token_overlap=pdf['title_token_overlap'])
        evidence=dict(paper_length='long',evidence_type='publisher_content_boundary_inspection',
                      source_url=paper['pdf_url'],pdf_sha256=pdf['sha256'],
                      inspection=pdf['length_inspection'],policy_url=POLICY)
        code_urls=sorted(set(re.findall(r'https?://(?:github\.com|gitlab\.com)/[^\s<>\\)]+',paper['abstract'])))
        record={k:v for k,v in paper.items() if k not in ('metadata_hits','fulltext_candidate')}
        record.update(finance=finance,download=download,paper_length='long',paper_length_evidence=evidence,
                      code_urls=code_urls,research=dict(primary_topic_id='finance' if finance['scope']=='core' else None,
                                                       topic_ids=['finance'],subtopic_ids=[],review_status='finance_only_classification'))
        records[pid]=clean(record);assignments[pid]=assignment
        row={key:'' for key in columns}
        row.update(id=pid,title=paper['title'],authors='; '.join(paper['authors']),venue=paper['venue'],
                   year=str(paper['year']),track='findings',research_primary_topic='AI for Finance / 金融人工智能' if finance['scope']=='core' else '',
                   research_topics='AI for Finance / 金融人工智能',research_topic_ids='finance',research_review_status='finance_only_classification',
                   is_best_or_outstanding='False',is_oral='False',oral_candidate_unverified='False',
                   finance_scope=finance['scope'],finance_primary_topic=finance['primary_topic'],
                   finance_topics='; '.join(finance['topics']),finance_subtopics='; '.join(finance['subtopics']),
                   finance_methods='; '.join(finance['methods']),finance_topic_ids='; '.join(finance['topic_ids']),
                   finance_relevance_zh=finance['relevance_zh'],finance_evidence_type=finance['evidence_type'],
                   finance_evidence_excerpt=finance['evidence_excerpt'],paper_url=paper['paper_url'],pdf_url=paper['pdf_url'],
                   code_urls='; '.join(code_urls),metadata_sources='; '.join(paper['metadata_sources']),abstract=paper['abstract'],
                   download_status='downloaded',**{k:str(download[k]) for k in ('local_path','pdf_version','pages','bytes','sha256')},
                   paper_length='long',paper_length_evidence_type=evidence['evidence_type'],paper_length_evidence_url=paper['pdf_url'])
        rows.append(clean(row))
        note=[f"# {paper['title']}",'',f"{paper['venue']} {paper['year']} · Findings · long · {finance['scope']}",'',
              f"- Paper: {paper['paper_url']}",f"- [Publisher PDF](../../{relative})",f"- Primary finance task: {finance['primary_topic']}",
              f"- Finance tasks: {'; '.join(finance['topics'])}",f"- Subtopics: {'; '.join(finance['subtopics'])}",
              f"- Methods: {'; '.join(finance['methods']) or 'Not established from retained evidence'}",
              '- [Classification evidence](../../checks/finance_taxonomy/assignments.json) · [Long-paper evidence](../../finance_catalog.jsonl)',
              '', '## Financial relevance / 金融相关性', '', finance['evidence_excerpt'], '', '## Abstract / 摘要', '',
              paper['abstract'] or 'Official metadata has no abstract; see the retained publisher-PDF evidence.','']
        (folder/'indexes/finance_notes'/f'{pid}.md').write_text('\n'.join(line.rstrip() for line in clean(note)).rstrip()+'\n')
    write_catalog(folder,rows,records,assignments,columns)
    save(folder/'checks/finance_taxonomy/manual_overrides.json',{k:v for k,v in overrides.items() if k in assignments})
    save(folder/'checks/pending_length_verification.json',pending)
    save(folder/'checks/source_snapshot.json',dict(literature_snapshot_date='2026-11-10',source='official ACL Anthology XML and PDFs',years=[2020,2026]))
    print(f'Main: {len(original_rows)-len(removed)}; Findings: {len(rows)}; financial Findings with unverified length: {len(pending)}')


if __name__=='__main__':main()
