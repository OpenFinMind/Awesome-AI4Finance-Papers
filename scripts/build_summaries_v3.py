#!/usr/bin/env python3
"""Build partition-specific bilingual summaries from task prose and paper evidence."""
import hashlib,json,re
from collections import Counter
from collection_io import ROOT,partitions,legacy
from taxonomy_v3 import baseline,schema
from summary_content_v3 import CONTENT

def digest(v):return hashlib.sha256(json.dumps(v,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
def cell(v):return str(v).replace('|','\\|').replace('\n',' ')
def main():
    frozen=baseline();s=schema()
    for track,scope,folder in partitions():
        records={p['id']:p for p in map(json.loads,(folder/'finance_catalog.jsonl').read_text().splitlines())}
        assignments=json.loads((folder/'checks/finance_taxonomy/assignments.json').read_text())
        oldledger=json.loads(frozen[track+'/checks/task_summaries/evidence.json']);oldnotes={}
        for topic in oldledger['topics'].values():
            for n in topic['contribution_and_boundary_notes']:oldnotes.setdefault(n['id'],n)
        evidence=dict(date='2026-11-20',track=track,scope=scope,basis='Task-specific editorial synthesis with representative abstracts and retained financial evidence. Earlier targeted PDF passages are retained where available; no complete new full-text audit is claimed.',boundaries='Evaluation guidance and opportunities are editorial synthesis.',topics={},papers={},preserved_input_sha256={})
        for filename in ('finance_catalog.csv','finance_catalog.jsonl','checks/finance_taxonomy/schema.json','checks/finance_taxonomy/assignments.json'):
            evidence['preserved_input_sha256'][filename]=hashlib.sha256((folder/filename).read_bytes()).hexdigest()
        for task in s['topics']:
            tid=task['id'];members=[p for pid,p in records.items() if tid in assignments[pid]['topic_ids']]
            eligible=sorted(members,key=lambda p:(p['id'] in oldnotes,assignments[p['id']]['primary_topic_id']==tid,p['year']),reverse=True)
            selected=eligible[:4];ids=[p['id'] for p in selected]
            lines=['## Research summary / 研究总结','',f"**{task['label']} · {track.title()} / {scope.title()}**",'',f'2026-11-20 · {len(members)} task memberships / 篇任务关联论文。','']
            notes=[]
            if not members:
                lines+=['### 中文','','当前集合中，该任务暂无收录论文。','','### English','','The current collection has no admitted papers for this task.','']
            else:
                counts=Counter(m for p in members for m in assignments[p['id']]['method_ids']);methodlabels={m['id']:m['label'] for m in s['methods']}
                methods='; '.join(f'{methodlabels[mid]} ({n})' for mid,n in counts.most_common(5)) or 'Not labeled / 暂未标注'
                subcounts=Counter(sub for p in members for sub in assignments[p['id']]['subtopic_ids'] if any(x['id']==sub and x['parent_id']==tid for x in s['subtopics']))
                sublabels={x['id']:x['label'] for x in s['subtopics']};subs='; '.join(f'{sublabels[sub]} ({n})' for sub,n in subcounts.most_common(5)) or 'Pending review / 待核对'
                focuszh,focusen,gapzh,gapen=CONTENT[tid]
                refs=' · '.join(f"[{i}](../indexes/finance_notes/{p['id']}.md)" for i,p in enumerate(selected,1))
                lines+=['### 中文','', '**研究问题与子方向。** '+focuszh,'', '**当前收录与方法。** '+f'本页仅总结 {track.title()} / {scope} 中的论文。当前较常见的子分类：{subs}。已标注的方法：{methods}。这些是多标签篇数，不能直接相加，也不表示性能排名。','', '**数据与评测。** '+task['evaluation_zh']+' 代表论文的摘要、金融关联证据及原文链接见 '+refs+'；不同数据与指标不合并为统一数值结论。','', '**研究机会（编辑判断）。** '+gapzh,'', '### English','', '**Problem and subdirections.** '+focusen,'', '**Current coverage and methods.** '+f'This page covers only {track.title()} / {scope}. Frequent subcategories: {subs}. Recorded methods: {methods}. Counts overlap and are not performance rankings.','', '**Data and evaluation.** '+task['evaluation_en']+' Representative abstracts, financial evidence and original sources are linked at '+refs+'. Results from incompatible data or metrics are not pooled.','', '**Research opportunities (editorial).** '+gapen,'', '### Representative papers / 代表论文','', '| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |','|---|---|---|']
                for i,p in enumerate(selected,1):
                    pid=p['id'];note=oldnotes.get(pid)
                    if note is None:
                        note=dict(id=pid,contribution_zh='研究主题：'+p['title'],contribution_en='Research topic: '+p['title'],boundary_zh='按原文的任务、数据和实验设置解释结果。',boundary_en='Interpret results within the original task, data and experimental setting.')
                    notes.append(note)
                    lines.append(f"| [{i}. {cell(p['title'])}](../indexes/finance_notes/{pid}.md) · {p['venue']} {p['year']} | {cell(note['contribution_zh'])}<br>{cell(note['contribution_en'])} | {cell(note['boundary_zh'])}<br>{cell(note['boundary_en'])} |")
                    proof=json.loads(json.dumps(oldledger['papers'].get(pid,{})))
                    proof.update(catalog_record_sha256=digest(p),abstract=p.get('abstract',''),official_url=p['paper_url'],financial_evidence=p['finance'].get('evidence_excerpt',''))
                    if not proof.get('fulltext_available'):
                        proof.update(fulltext_available=False,fulltext_characters=0,pdf_path=p.get('download',{}).get('local_path',''),pdf_sha256=p.get('download',{}).get('sha256',''))
                    evidence['papers'][pid]=proof
            text='\n'.join(lines).rstrip()+'\n';dest=folder/'summaries'/f'{tid}.md';dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(text)
            evidence['topics'][tid]=dict(task_memberships=len(members),core=len(members) if scope=='core' else 0,application=len(members) if scope=='application' else 0,representative_ids=ids,contribution_and_boundary_notes=notes,source_sha256=hashlib.sha256(text.encode()).hexdigest())
        dest=folder/'checks/task_summaries';dest.mkdir(parents=True,exist_ok=True);(dest/'evidence.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+'\n')
        (dest/'README.md').write_text('# Summary evidence / 总结依据\n\n[Evidence ledger / 来源记录](evidence.json) binds representative papers to this track, scope, task, catalog record and available PDF evidence. Contributions retained from earlier reading notes are distinguished from topic descriptions. Evaluation guidance and opportunities are editorial synthesis; extracting a PDF does not imply a complete reading.\n\n[Summary sources / 总结正文](../../summaries/) are rendered above each task list. Main/Findings and Core/Application are summarized separately. Empty tasks explicitly say 暂无收录论文.\n')
        print('Summaries',track,scope,len(evidence['topics']),len(evidence['papers']))
if __name__=='__main__':main()
