# Taxonomy 3.0 migration / 分类迁移

The collection uses **18 financial tasks, 111 subcategories and 15 independent method labels**, with four disjoint physical collections: `main/core`, `main/application`, `findings/core` and `findings/application`. Main/Findings and Core/Application are independent axes. The migration preserves all **1,631 admitted long papers** and **1,543 PDFs**, including the original **88 papers without local PDFs**.

现采用 **18 个金融方向、111 个子分类和 15 个独立技术方法标签**。四个集合分别存储目录、分类、索引、总结和 PDF；Main 与 Findings 不混合，Core 与 Application 不混合。原有 1,631 篇长文与 1,543 份 PDF 全部保留，88 篇原本暂无本地 PDF 的论文继续保留官方链接。

| Collection | Papers |
|---|---:|
| [Main / Core](../../main/core/README.md) | 300 |
| [Main / Application](../../main/application/README.md) | 1,144 |
| [Findings / Core](../../findings/core/README.md) | 112 |
| [Findings / Application](../../findings/application/README.md) | 75 |

- [Schema / 分类定义](schema.json) defines task boundaries and all proposed subcategories. Empty subcategories are retained as navigation definitions; they are not claims of existing coverage.
- [Decisions / 逐篇决定](decisions.jsonl) records each paper's primary task, primary subcategory, related labels, methods, financial scope, evidence and review status.
- [Migration / 迁移对应表](migration.json) maps every old paper/PDF identity to its new partition and classification. PDF SHA-256 values are preserved.
- [Validation / 校验](validation.json) checks identity preservation, disjoint partitions, unchanged non-taxonomy metadata and agreement with explicit decisions.
- [Frozen v2 inputs / 冻结旧输入](baseline.json.gz) and [manifest / 清单](baseline_manifest.json) retain original catalogs, assignments, schema and summary evidence. Draft proposals and draft decisions are historical intermediate artifacts, not active classification inputs.

The migration reuses retained inclusion and task evidence for unchanged assignments and records new contribution reviews separately. `inherited_evidence_mapping` does **not** claim a new full-text reading. `method_review_status` records inherited method labels explicitly. Ten general-method or multi-domain papers move from Core to Application after abstract review; the decisions retain reasons. Financial benchmarks can be Core when their main domain is finance, or Application when finance is one substantive slice of a multi-domain resource.

未改变的归类继承原有金融收录与任务证据，新增贡献复核单独记录；`inherited_evidence_mapping` 不表示重新通读全文。技术标签的继承状态另行记录。10 篇通用方法或跨领域资源经摘要核对后由 Core 调整为 Application，并保留理由。金融基准并不自动属于 Core：金融为核心研究领域时属于 Core，金融仅为跨领域资源的一部分时属于 Application。

Five retained admissions have insufficient evidence for a specific primary subcategory. Their primary task is provisional, their subcategory is empty, and `needs_review` is visible in exports and paper notes. They remain in the collection without an invented detailed label:

以下 5 篇旧收录记录的主要子分类证据不足，主方向暂定，子分类留空，并明确标记 `needs_review`；没有为了填满分类而推断细分任务：

- `kdd-2017-30051c903823`
- `icml-2018-2132`
- `icml-2023-23887`
- `2025.emnlp-main.736`
- `2026.emnlp-main.2547`

## Maintenance / 维护

Definitions live in `scripts/taxonomy_v3.py` and `scripts/finance_subtopics_v3.py`; explicit decisions live here. `apply_taxonomy_v3.py` applies reviewed labels to current partition catalogs without changing admissions. `build_summaries_v3.py` rebuilds task-specific bilingual summaries and evidence ledgers; `build_collection.py` rebuilds exports and navigation. `verify_tracks.py` checks current artifacts and original admissions. Historical v2 classifiers/import migrations are retained for provenance and refuse to overwrite the v3 collection.

分类定义、逐篇决定和生成结果分别维护。修改决定后先应用，再重建总结及索引；验证器同时检查当前四个集合与历史收录证据。旧版导入脚本属于历史工具，不应用于覆盖现有目录。
