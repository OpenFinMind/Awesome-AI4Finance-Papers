# Contributing / 维护说明

Maintain four independent collections: `main/core/`, `main/application/`, `findings/core/` and `findings/application/`. Each has its own catalogs, notes, classifications, indexes, summaries, exports and PDFs. `local_path` is relative to its collection directory. Store one copy of each PDF; use related task labels for cross-references.

分别维护 Main/Core、Main/Application、Findings/Core、Findings/Application 四个集合。清单、分类、索引、笔记、总结、导出和 PDF 分开存储，本地路径相对于各自集合。每篇 PDF 只存一份，交叉方向通过标签引用。

## Admission / 收录

- Cover the seven conferences and years specified in the homepage. KDD is limited to Research Track; Findings applies only to ACL and EMNLP.
- Verify publication track and long-paper eligibility independently. Keep official volume/program evidence or auditable regular-full-paper/content-boundary evidence. Total PDF page count alone is insufficient. Exclude short papers and unresolved publication types.
- Core means the main research problem or contribution directly concerns finance. Application means a general method has substantive financial data, experiments, modeling or use cases. Scope is independent of task and method labels.
- Keep one primary financial task and one evidenced primary subcategory. Related tasks, subcategories and technical methods may overlap. If evidence cannot support a specific refinement, leave it empty and mark `needs_review` explicitly.
- Financial Risk concerns losses, default and uncertainty; Financial Safety concerns fraud, attacks, privacy and compliance. Datasets/benchmarks as the main contribution belong to Financial Evaluation; reusable finance-domain training/adaptation belongs to Financial Models. Merely using an LLM or reporting experiments does not establish either contribution.
- Name PDF versions correctly; retain byte counts, SHA-256 values and official links.

仅收录已核验的指定轨道长文，不以获奖、口头报告或总页数替代收录依据。逐篇保留金融关联、分类与长文证据。通用方法的金融应用不自动升格为 Core；技术名称不能替代金融任务。主要子分类证据不足时明确标记待核对。

## Classification and rebuilding / 分类与重建

The 18 task definitions are in `scripts/taxonomy_v3.py`; the 111 subcategories are in `scripts/finance_subtopics_v3.py`. Explicit per-paper decisions are stored in [the v3 audit](checks/taxonomy_v3/README.md). Preserve the frozen baseline and historical admission decisions; record new classification reasoning rather than modifying historical evidence.

18 个一级方向、111 个子分类及技术方法分别定义。修改当前分类应更新逐篇决定和支持证据；旧版基线与历史收录依据保持不变。

```bash
python -m pip install -r scripts/requirements.txt
# After reviewing and changing explicit classification decisions:
python scripts/apply_taxonomy_v3.py
python scripts/build_summaries_v3.py
python scripts/build_collection.py
python scripts/verify_tracks.py
git diff --check
```

`apply_taxonomy_v3.py` updates existing papers and moves a paper/PDF only if its reviewed scope changes; it does not admit new papers. The four partition catalogs and assignments are the inputs to the normal index/export build. `build_summaries_v3.py` rebuilds the initial migration summaries from task-specific prose and retained paper evidence; review its representative selection before publication. For later editorial edits, change the summary sources and refresh their evidence-ledger source hashes instead of overwriting them with a migration rebuild.

应用脚本只修改现有论文分类，不新增收录；正常索引构建以四个集合的 CSV、JSONL 与分类记录为输入。总结迁移生成器使用独立任务评析及已有论文证据，发布前需核对代表论文选择。后续人工编辑总结时，直接维护正文与证据哈希，避免重新运行迁移生成器覆盖编辑内容。

## Task summaries / 任务总结

Bilingual sources live in `<main|findings>/<core|application>/summaries/<task>.md`. They appear above the corresponding task statistics and full paper list. A representative must belong to that exact track, scope and task. Evidence ledgers are stored in each collection's `checks/task_summaries/` and bind sources to catalog records and available PDF passages. Extracting a PDF is not a claim to have read every word. Evaluation guidance, comparison boundaries and research opportunities are editorial synthesis.

中英文任务总结、代表论文和统计都限定在对应集合。总结来源位于各集合的 `summaries/`，证据台账位于 `checks/task_summaries/`。数据与指标不兼容时不合并数值排名。PDF 抽取不等于逐字通读，评测建议、适用边界与研究机会标明为编辑评析。

## Verification and historical sources / 验证与历史来源

`verify_tracks.py` checks all four catalogs, Excel/BibTeX identities, PDF hashes, link resolution, source/rendered summaries, official Main/Findings and long-paper evidence, KDD Research inventories and the taxonomy migration. The v3 validator compares every paper with frozen inputs, permits only explicitly reviewed taxonomy/scope changes and preserves all non-taxonomy metadata and inclusion evidence.

[Track screening](checks/track_screening/README.md), [KDD audit](checks/track_screening/kdd/README.md) and earlier AAAI reports retain historical source evidence. Original import/classification scripts are historical tools; their v2 classifier refuses to overwrite the v3 collection. Historical reports describe their original publication state, not current scope counts.

验证同时覆盖当前结果与历史证据。旧版导入、分类和迁移脚本仅作为历史工具保留；不可直接覆盖现有四个集合。历史报告中的数量属于当次发布状态。

PDF copyrights remain with the authors and publishers. / PDF 版权归作者与出版方。
