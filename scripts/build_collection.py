#!/usr/bin/env python3
"""Rebuild four separate collections and bilingual native Markdown entry points."""
import csv,json,os,subprocess,sys
from collections import Counter
from pathlib import Path
from collection_io import ROOT,TRACKS,SCOPES,partitions
from taxonomy_v3 import schema
VENUES=('ICML','ICLR','ACL','EMNLP','NeurIPS','AAAI','KDD')
GH='https://github.com/OpenFinMind/Awesome-AI4Finance-Papers'
HF='https://huggingface.co/datasets/OpenFinMind/Awesome-AI4Finance-Papers'

def exports(prefix):return ' · '.join(f'[{label}]({prefix}{filename})' for label,filename in [('CSV','finance_catalog.csv'),('JSONL','finance_catalog.jsonl'),('Excel','finance_catalog.xlsx'),('BibTeX','finance_references.bib')])
def navigation(prefix):return f'[Tasks / 金融任务]({prefix}indexes/ai_for_finance.md) · [Subcategories / 子分类]({prefix}indexes/subtopics.md) · [Methods / 技术方法]({prefix}indexes/methods.md)'
def definitions(folder,s):
    lines=['# Classification / 分类说明','','Taxonomy 3.0 / 分类版本 3.0。Main/Findings and Core/Application are independent partitions. / 发表轨道与金融范围独立分区。','',
    '- **Core / 金融核心研究**: the main research problem or contribution concerns finance. / 主要研究问题或贡献直接面向金融。',
    '- **Application / 金融应用**: finance is a substantive application of a general method. / 通用方法含有实质性的金融应用。',
    '- One primary task and one primary subcategory; related tasks, subcategories and methods may overlap. / 一个主方向和一个主要子分类；关联方向、子分类与方法允许多标签。',
    '- Insufficiently supported subcategories remain pending, visible in the catalog and paper note. / 证据不足的子分类保留待核对状态，在清单与逐篇笔记中显示。','',
    '**Boundaries / 分类边界**','',
    'Predictive signal discovery → factor mining; economic pricing relationships → pricing. Sequence structure/reconstruction → time series; explicit prices/returns/volatility/fundamentals → valuation prediction. Portfolio weights → portfolio; trading/execution/hedging actions → financial decision. Loss/default/uncertainty → financial risk; fraud/attacks/privacy/compliance → financial safety. Insurance pricing/claims/reserves/longevity → actuarial science; insurance sales/service → financial services. / 预测信号发现归因子挖掘，经济定价关系归定价；序列结构与重建归时间序列，明确的价格、收益、波动率与基本面预测归估值预测；组合权重归投资组合，交易执行对冲行动归金融决策；损失与违约归金融风险，欺诈攻击隐私合规归金融安全；保险精算任务与保险销售服务分开。','',
    'A dataset, benchmark or capability audit as the main contribution → financial evaluation. Reusable financial-domain pretraining/post-training/adaptation → financial models. Merely reporting experiments or using an LLM is insufficient. / 数据集、基准或能力诊断为主要贡献时归金融评测；可复用金融领域模型的训练适配归金融模型；仅做实验或调用 LLM 不自动归入这两类。','',
    '[Task index / 任务目录](ai_for_finance.md) · [Per-paper evidence / 逐篇依据](../checks/finance_taxonomy/assignments.json) · [Schema / 分类定义](../checks/finance_taxonomy/schema.json)','']
    for topic in s['topics']:
        lines += [f"## [{topic['label']}](finance_topics/{topic['id']}.md)",'',topic['description'],'']
        lines += [f"- [{x['label']}](subtopics/{x['id']}.md)" for x in s['subtopics'] if x['parent_id']==topic['id']]+['']
    lines+=['## Methods / 技术方法','']+[f"- [{m['label']}](methods/{m['id']}.md)" for m in s['methods']]+['']
    (folder/'indexes/finance_taxonomy.md').write_text('\n'.join(lines))
def main():
    s=schema();data={}
    for track,scope,folder in partitions():
        with (folder/'finance_catalog.csv').open(encoding='utf-8-sig',newline='') as f:data[track,scope]=list(csv.DictReader(f))
        env={**os.environ,'AI4FINANCE_TRACK':track,'AI4FINANCE_SCOPE':scope}
        for script in ('export_collection.py','build_indexes.py'):subprocess.run([sys.executable,str(ROOT/'scripts'/script)],env=env,check=True)
        definitions(folder,s)
        for zh in (False,True):
            name='README.zh-CN.md' if zh else 'README.md';rows=data[track,scope]
            lines=[f'# AI for Finance — {track.title()} / {scope.title()}','', '[English](README.md) | [中文](README.zh-CN.md) | [Home / 首页](../../'+name+')','',
            f"{len(rows):,} long papers / 篇长文 · {sum(r['download_status']=='downloaded' for r in rows):,} PDFs。",'',
            ('本集合独立存储 '+track.title()+' / '+scope+' 长文；本地路径相对于本目录。' if zh else f'This collection stores {track.title()} / {scope} long papers independently. Local paths are relative to this directory.'),'',
            navigation(''),'','[All papers / 全部论文](indexes/all_papers.md) · [Classification / 分类说明](indexes/finance_taxonomy.md)','',exports(''),'',
            ('每个任务页上半部分提供本集合独立的中英文总结及代表论文。' if zh else 'Each task page starts with a bilingual summary and representative papers from this collection.'),'',
            '| Venue / 会议 | Long papers / 长文 |','|---|---:|']
            for venue in VENUES:
                n=sum(r['venue']==venue for r in rows)
                if n:lines.append(f'| [{"KDD Research Track" if venue=="KDD" else venue}](indexes/venues/{venue.lower()}.md) | {n} |')
            lines+=['',f'[GitHub]({GH}) · [Hugging Face]({HF})',''];(folder/name).write_text('\n'.join(lines))
    for zh in (False,True):
        name='README.zh-CN.md' if zh else 'README.md'
        for track in TRACKS:
            lines=[f'# AI for Finance — {track.title()}','', '[English](README.md) | [中文](README.zh-CN.md) | [Home / 首页](../'+name+')','',
            ('Core 与 Application 分开存储、浏览、导出和总结。' if zh else 'Core and Application have separate storage, browsing, exports and summaries.'),'',
            '| Collection / 集合 | Long papers / 长文 | Browse / 浏览 | Exports / 导出 |','|---|---:|---|---|']
            for scope in SCOPES:lines.append(f'| [{scope.title()}]({scope}/{name}) | {len(data[track,scope])} | {navigation(scope+"/")} | {exports(scope+"/")} |')
            (ROOT/track/name).write_text('\n'.join(lines)+'\n')
        lines=['# Awesome AI4Finance Papers','','[English](README.md) | [中文](README.zh-CN.md)','',
        ('按金融任务、子分类和技术方法整理的 AI for Finance 长文论文库，由 [OpenFinMind](https://github.com/OpenFinMind) 维护。' if zh else 'AI for Finance long papers organized by financial task, subcategory and technical method. Maintained by [OpenFinMind](https://github.com/OpenFinMind).'),'',
        '## '+('收录范围' if zh else 'Scope'),'',
        ('收录 **2017–2026** 年 **ICML、ICLR、ACL、EMNLP、NeurIPS、AAAI Main**、**KDD Research Track** 及 **ACL、EMNLP Findings** 中与金融相关的长文，涵盖金融核心研究与金融应用；不收录短文。' if zh else 'Covers finance-related **long papers** from **ICML, ICLR, ACL, EMNLP, NeurIPS and AAAI Main**, **KDD Research Track**, and **ACL / EMNLP Findings**, within **2017–2026**. Includes financial core research and financial applications. Short papers are excluded.'),'',
        '## '+('独立目录' if zh else 'Separate collections'),'',
        '| Track / 轨道 | Scope / 范围 | Long papers / 长文 | PDFs | Browse / 浏览 | Exports / 导出 |','|---|---|---:|---:|---|---|']
        for track,scope,_ in partitions():
            prefix=f'{track}/{scope}/';rows=data[track,scope]
            lines.append(f'| {track.title()} | [{scope.title()}]({prefix}{name}) | {len(rows):,} | {sum(r["download_status"]=="downloaded" for r in rows):,} | {navigation(prefix)} | {exports(prefix)} |')
        lines+=['',('四个集合各自提供分类索引、逐篇笔记、任务总结、数据导出和 PDF；每篇 PDF 只保留一份。任务页上半部分提供该集合独立的中英文研究总结。' if zh else 'Each collection has its own indexes, paper notes, task summaries, exports and PDFs. Each PDF is stored once. Task pages start with bilingual summaries for their collection.'),'',
        '## '+('按金融方向浏览' if zh else 'By financial task'),'',
        ('每篇有一个主方向；关联方向允许重叠，表中计数为任务关联篇数。技术方法单独标注。' if zh else 'Each paper has one primary task. Related tasks may overlap; counts below are task memberships. Technical methods are separate labels.'),'',
        '| Task / 方向 | Main Core | Main Application | Findings Core | Findings Application |','|---|---:|---:|---:|---:|']
        for task in s['topics']:
            cells=[]
            for track,scope,_ in partitions():
                n=sum(task['id'] in r['finance_topic_ids'].split('; ') for r in data[track,scope]);cells.append(f"[{n}]({track}/{scope}/indexes/finance_topics/{task['id']}.md)")
            lines.append(f"| {task['label']} | "+' | '.join(cells)+' |')
        lines+=['','## '+('分类说明' if zh else 'Classification'),'','- **Core / 金融核心研究**: the main research problem or contribution concerns finance. / 主要研究问题或贡献直接面向金融。','- **Application / 金融应用**: finance is a substantive application of a general method. / 金融是通用方法的实质性应用。','',
        ('完整子分类及边界见各集合的 **Classification / 分类说明**；证据不足的细分归类保留待核对状态。金融风险与金融安全独立分类。' if zh else 'Complete subcategories and boundaries are defined in each collection’s classification guide. Insufficiently supported refinements remain pending. Financial Risk and Financial Safety are separate tasks.'),'',
        '## '+('按会议浏览' if zh else 'By venue'),'','| Venue / 会议 | Main | Findings |','|---|---:|---:|']
        for venue in VENUES:
            cells=[]
            for track in TRACKS:
                cells.append(' · '.join(f'[{scope}: {sum(r["venue"]==venue for r in data[track,scope])}]({track}/{scope}/indexes/venues/{venue.lower()}.md)' for scope in SCOPES) if track=='main' or venue in ('ACL','EMNLP') else '—')
            lines.append(f'| {"KDD Research Track" if venue=="KDD" else venue} | '+ ' | '.join(cells)+' |')
        lines+=['', '## '+('资源' if zh else 'Resources'),'','PDF: `<main|findings>/<core|application>/pdfs/<venue>/<year>/`. Missing PDFs retain official online links. / 暂无本地 PDF 的已收录论文保留官方链接。','',
        '[Contributing / 维护说明](CONTRIBUTING.md) · [Screening evidence / 收录依据](checks/track_screening/README.md) · [Classification migration / 分类迁移记录](checks/taxonomy_v3/README.md)','',f'[GitHub]({GH}) · [Hugging Face]({HF})','']
        (ROOT/name).write_text('\n'.join(lines))
if __name__=='__main__':main()
