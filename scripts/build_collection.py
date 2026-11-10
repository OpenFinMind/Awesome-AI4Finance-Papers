#!/usr/bin/env python3
"""Rebuild both tracks and bilingual entry points without changing admissions."""
import csv
import json
import os
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
VENUES=('ICML','ICLR','ACL','EMNLP','NeurIPS','AAAI')


def read(track):
    with (ROOT/track/'finance_catalog.csv').open(encoding='utf-8-sig',newline='') as stream:
        return list(csv.DictReader(stream))


def main():
    rows={track:read(track) for track in ('main','findings')}
    schema=json.loads((ROOT/'main/checks/finance_taxonomy/schema.json').read_text())
    for track in rows:
        env={**os.environ,'AI4FINANCE_TRACK':track}
        for script in ('export_collection.py','build_indexes.py'):
            subprocess.run([sys.executable,str(ROOT/'scripts'/script)],env=env,check=True)
        for lang in ('en','zh'):
            title='Main' if track=='main' else 'Findings'
            data=rows[track];counts=Counter(r['finance_scope'] for r in data)
            pdfs=sum(r['download_status']=='downloaded' for r in data)
            links=('[English](README.md) | [中文](README.zh-CN.md) | [Repository home](../README.md)' if lang=='en' else
                   '[English](README.md) | [中文](README.zh-CN.md) | [仓库首页](../README.zh-CN.md)')
            intro=(f'{len(data):,} long papers: {counts["core"]:,} finance core and {counts["application"]:,} financial applications; {pdfs:,} local PDFs.' if lang=='en' else
                   f'共 {len(data):,} 篇长文：金融核心研究 {counts["core"]:,} 篇、金融应用 {counts["application"]:,} 篇；本地 PDF {pdfs:,} 份。')
            lines=[f'# AI for Finance — {title}', '', links, '', intro, '',
                   ('This directory contains only '+title+' long papers. Local paths in its CSV/JSONL/Excel are relative to this directory.' if lang=='en' else
                    '本目录仅存储 '+title+' 长文。CSV、JSONL 与 Excel 中的本地路径均相对于本目录。'), '',
                   ('## Browse' if lang=='en' else '## 浏览'), '',
                   '- [All papers / 全部论文](indexes/all_papers.md)',
                   '- [Finance tasks / 金融任务](indexes/ai_for_finance.md) · [Subtopics / 子方向](indexes/subtopics.md) · [Methods / 技术方法](indexes/methods.md)',
                   '- [Core / 金融核心研究](indexes/core.md) · [Applications / 金融应用](indexes/applications.md)',
                   '- [Excel](finance_catalog.xlsx) · [CSV](finance_catalog.csv) · [JSONL](finance_catalog.jsonl) · [BibTeX](finance_references.bib)',
                   '- [Taxonomy / 分类说明](indexes/finance_taxonomy.md) · [Selection evidence / 筛选依据](checks/README.md)', '',
                   '| Venue / 会议 | Long papers / 长文 |', '|---|---:|']
            for venue in VENUES:
                subset=[r for r in data if r['venue']==venue]
                if subset:lines.append(f'| [{venue}](indexes/venues/{venue.lower()}.md) | {len(subset)} |')
            lines+=['', ' · '.join(f'[{year}](indexes/years/{year}.md)' for year in sorted({r['year'] for r in data},reverse=True)), '',
                    ('Papers without verified long-paper eligibility are kept out of this catalog. See the [screening audit](../checks/track_screening/README.md) for coverage and pending cases.' if lang=='en' else
                     '无法核验长文属性的论文不进入正式清单；筛查覆盖和待核验记录见[筛查审计](../checks/track_screening/README.md)。'), '']
            lines[4:4]=['**Long papers only. Short papers are excluded. / 仅收录长文，不收录短文。**', '']
            (ROOT/track/('README.md' if lang=='en' else 'README.zh-CN.md')).write_text('\n'.join(lines))
    venue_table=['| Venue / 会议 | Main | Findings |','|---|---:|---:|']
    for venue in VENUES:
        cells=[]
        for track in rows:
            count=sum(r['venue']==venue for r in rows[track])
            cells.append(f'[{count}]({track}/indexes/venues/{venue.lower()}.md)' if count else ('—' if track=='findings' and venue not in ('ACL','EMNLP') else '0'))
        venue_table.append(f'| {venue} | '+ ' | '.join(cells)+' |')
    topic_table=['| Finance task / 金融任务 | Main | Findings |','|---|---:|---:|']
    for topic in schema['topics']:
        cells=[f"[{sum(topic['id'] in r['finance_topic_ids'].split('; ') for r in rows[track])}]({track}/indexes/finance_topics/{topic['id']}.md)" for track in rows]
        topic_table.append(f"| {topic['label']} | "+' | '.join(cells)+' |')
    for lang in ('en','zh'):
        zh=lang=='zh'
        lines=['# Awesome AI4Finance Papers', '', '[English](README.md) | [中文](README.zh-CN.md)', '',
               ('按金融任务、子方向和技术方法整理的 AI for Finance 长文论文库，由 [OpenFinMind](https://github.com/OpenFinMind) 维护。' if zh else
                'AI for Finance long papers organized by financial task, subtopic, and technical method. Maintained by [OpenFinMind](https://github.com/OpenFinMind).'), '',
               '## '+('收录范围' if zh else 'Scope'), '',
               ('收录 **2017–2026** 年 **ICML、ICLR、ACL、EMNLP、NeurIPS、AAAI Main** 及 **ACL、EMNLP Findings** 中与金融相关的长文，涵盖金融核心研究与金融应用。Main 与 Findings 分开存储，并按金融任务、子方向和技术方法整理。' if zh else
                'Covers finance-related long papers from **ICML, ICLR, ACL, EMNLP, NeurIPS, and AAAI Main**, and **ACL / EMNLP Findings**, within **2017–2026**, including finance core research and financial applications. Main and Findings are stored separately and organized by financial task, subtopic, and technical method.'), '',
               '## '+('独立目录' if zh else 'Separate collections'), '',
               '| '+('类别 | 长文 | 论文与分类 | 数据导出 |' if zh else 'Track | Long papers | Papers and classifications | Exports |'),
               '|---|---:|---|---|']
        for track in rows:
            n=len(rows[track]);title=track.title()
            lines.append(f'| [{title}]({track}/README'+('.zh-CN.md' if zh else '.md')+f') | {n:,} | [Tasks]({track}/indexes/ai_for_finance.md) · [Subtopics]({track}/indexes/subtopics.md) · [Methods]({track}/indexes/methods.md) | [Excel]({track}/finance_catalog.xlsx) · [CSV]({track}/finance_catalog.csv) · [JSONL]({track}/finance_catalog.jsonl) · [BibTeX]({track}/finance_references.bib) |')
        lines+=['', ('Main 与 Findings 各有独立目录、索引、逐篇笔记、CSV、JSONL、Excel、BibTeX 和 PDF。导出文件中的 `local_path` 相对于所属类别目录；根目录不提供混合两类的论文清单。' if zh else
                    'Main and Findings each have their own indexes, paper notes, CSV, JSONL, Excel, BibTeX, and PDFs. Exported `local_path` values are relative to the corresponding track directory.'), '',
                '## '+('按会议浏览' if zh else 'By venue'), '', '\n'.join(venue_table), '',
                '## '+('按金融任务浏览' if zh else 'By financial task'), '',
                ('金融任务允许多标签，计数存在重叠；每篇另有唯一主方向。子方向描述具体任务，技术方法独立标注 LLM、强化学习、图学习、扩散、因果等，避免把技术名称当成金融任务。' if zh else
                 'Financial tasks allow multiple labels, so counts overlap; every paper also has one primary task. Subtopics describe more specific problems. Technical methods such as LLMs, reinforcement learning, graph learning, diffusion, and causal methods are recorded separately.'), '',
                '\n'.join(topic_table), '', '## '+('分类说明' if zh else 'Classification'), '',
                ('- **金融核心研究（core）**：研究问题直接面向金融。\n- **金融应用（application）**：通用方法含有实质性的金融数据、实验、业务场景、建模或领域综述；不等同于金融专用方法。' if zh else
                 '- **Core:** the research problem directly concerns finance.\n- **Application:** a general method has substantive financial data, experiments, business cases, modeling, or a domain review; it need not be a finance-specific method.'), '',
                ('筛选与核验说明见[筛查审计](checks/track_screening/README.md)。' if zh else
                 'Selection and verification details are available in the [screening audit](checks/track_screening/README.md).'), '',
                '## '+('资源' if zh else 'Resources'), '',
                ('PDF 位于 `<main|findings>/pdfs/<venue>/<year>/`；官方版本与作者 arXiv 版本分别标注，并记录 SHA-256。未下载的已收录论文保留在线链接。论文版权归作者与出版方。维护方式见 [CONTRIBUTING.md](CONTRIBUTING.md)。' if zh else
                 'PDFs live under `<main|findings>/pdfs/<venue>/<year>/`. Publisher and author arXiv versions are distinguished and hashed with SHA-256. Admitted papers without local PDFs retain online links. Paper copyrights remain with the authors and publishers. See [CONTRIBUTING.md](CONTRIBUTING.md) for maintenance.'), '']
        lines[4:4]=['[GitHub](https://github.com/OpenFinMind/Awesome-AI4Finance-Papers) · [Hugging Face](https://huggingface.co/datasets/OpenFinMind/Awesome-AI4Finance-Papers)', '',
                    '**仅收录长文，不收录短文。**' if zh else '**Long papers only. Short papers are excluded.**', '']
        (ROOT/('README.zh-CN.md' if zh else 'README.md')).write_text('\n'.join(lines))


if __name__=='__main__':main()
