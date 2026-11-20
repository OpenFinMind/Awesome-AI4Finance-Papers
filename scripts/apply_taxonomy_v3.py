#!/usr/bin/env python3
"""Apply explicit v3 decisions to the four partitions, preserving admissions."""
import csv,json,hashlib,shutil,re
from pathlib import Path
from collection_io import ROOT,TRACKS,SCOPES
from taxonomy_v3 import schema

def save(p,v):
    p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def write_clean(path,text):path.write_text('\n'.join(line.rstrip() for line in text.splitlines()).rstrip()+'\n')
def digest(v):return hashlib.sha256(json.dumps(v,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
def main():
    decisions={r['id']:r for r in map(json.loads,(ROOT/'checks/taxonomy_v3/decisions.jsonl').read_text().splitlines())}
    manifest=json.loads((ROOT/'checks/taxonomy_v3/migration.json').read_text());entries={r['id']:r for r in manifest['papers']}
    s=schema();labels={k:{r['id']:r['label'] for r in s[k]} for k in ('topics','subtopics','methods')}
    for track in TRACKS:
        groups={scope:[] for scope in SCOPES}
        for scope in SCOPES:
            folder=ROOT/track/ scope
            with (folder/'finance_catalog.csv').open(encoding='utf-8-sig',newline='') as f:
                reader=csv.DictReader(f);columns=reader.fieldnames;rows={r['id']:r for r in reader}
            assignments=json.loads((folder/'checks/finance_taxonomy/assignments.json').read_text())
            for r in map(json.loads,(folder/'finance_catalog.jsonl').read_text().splitlines()):
                pid=r['id'];d=decisions[pid];row=rows[pid];a=assignments[pid];target=ROOT/track/d['scope']
                if scope!=d['scope']:
                    for relative in ([row['local_path']] if row['local_path'] else [])+[f'indexes/finance_notes/{pid}.md']:
                        dest=target/relative;dest.parent.mkdir(parents=True,exist_ok=True);assert not dest.exists();(folder/relative).rename(dest)
                f=r['finance'];f.update(scope=d['scope'],primary_topic_id=d['primary_topic_id'],primary_topic=labels['topics'][d['primary_topic_id']],primary_subtopic_id=d['primary_subtopic_id'],review_status=d['status'],classification_reason=d['reason'])
                for key,cat in [('topic_ids','topics'),('subtopic_ids','subtopics'),('method_ids','methods')]:
                    f[key]=d[key];f[cat]=[labels[cat][x] for x in d[key]];a[key]=d[key]
                a.update(primary_topic_id=d['primary_topic_id'],primary_subtopic_id=d['primary_subtopic_id'],review_status=d['status'],reason=d['reason'],scope_review_status=d['scope_review_status'])
                a['topic_evidence']=[dict(topic_id=x,subtopic_id=d['primary_subtopic_id'] if x==d['primary_topic_id'] else None,source=d.get('review_source','retained_financial_evidence'),excerpt=d.get('review_excerpt') or d['evidence_excerpt'] or r.get('abstract','') or r['title'],matched=d['reason']) for x in d['topic_ids']]
                row.update(finance_scope=d['scope'],finance_primary_topic=f['primary_topic'],finance_topics='; '.join(f['topics']),finance_subtopics='; '.join(f['subtopics']),finance_methods='; '.join(f['methods']),finance_topic_ids='; '.join(f['topic_ids']),finance_primary_topic_id=d['primary_topic_id'],finance_primary_subtopic_id=d['primary_subtopic_id'] or '',finance_primary_subtopic=labels['subtopics'].get(d['primary_subtopic_id'],''),finance_review_status=d['status'])
                # Re-render classification in the source note; admission prose stays.
                note=target/f'indexes/finance_notes/{pid}.md';text=note.read_text().split('\n## Classification / 分类')[0].rstrip()

                for label,value in [('Primary topic',row['finance_primary_topic']),('Topics',row['finance_topics']),('Subtopics',row['finance_subtopics']),('Methods',row['finance_methods'])]:
                    text=re.sub(r'^- '+label+r':.*$',lambda m:'- '+label+': '+value,text,flags=re.M)
                text=re.sub(r'^(.*? · '+track+r' · )(?:core|application)$',lambda m:m.group(1)+d['scope'],text,flags=re.M)
                write_clean(note,text+'\n\n## Classification / 分类\n\n'+f"- Primary task / 主方向: {f['primary_topic']}\n- Primary subcategory / 主要子分类: {row['finance_primary_subtopic'] or 'Pending review / 待核对'}\n- Related tasks / 关联方向: {row['finance_topics']}\n- Subcategories / 子分类: {row['finance_subtopics']}\n- Methods / 技术方法: {row['finance_methods'] or 'Not labeled / 暂未标注'}\n- Review status / 核对状态: `{d['status']}`\n- [Definitions / 分类定义](../finance_taxonomy.md) · [Evidence / 分类依据](../../checks/finance_taxonomy/assignments.json)\n")
                entry=entries[pid];entry.update(scope=d['scope'],primary_topic_id=d['primary_topic_id'],primary_subtopic_id=d['primary_subtopic_id'],review_status=d['status'],reason=d['reason'],record_sha256=digest(r),pdf_path=f"{track}/{d['scope']}/{row['local_path']}" if row['local_path'] else '')
                groups[d['scope']].append((r,row,a))
        for scope,items in groups.items():
            folder=ROOT/track/scope;items.sort(key=lambda x:(x[0]['year'],x[0]['venue'],x[0]['title'].casefold()))
            with (folder/'finance_catalog.csv').open('w',encoding='utf-8-sig',newline='') as f:
                w=csv.DictWriter(f,columns);w.writeheader();w.writerows([x[1] for x in items])
            (folder/'finance_catalog.jsonl').write_text(''.join(json.dumps(x[0],ensure_ascii=False)+'\n' for x in items))
            a={x[0]['id']:x[2] for x in items};save(folder/'checks/finance_taxonomy/assignments.json',a);save(folder/'checks/finance_taxonomy/schema.json',s);save(folder/'checks/finance_taxonomy/manual_overrides.json',{pid:x for pid,x in a.items() if x['review_status'] not in ('inherited_evidence_mapping','needs_review')})
    save(ROOT/'checks/taxonomy_v3/migration.json',manifest)
if __name__=='__main__':main()
