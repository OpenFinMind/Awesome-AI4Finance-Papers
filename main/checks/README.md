# Evidence and selection criteria

This Main directory contains confirmed financial long papers from the main tracks of AAAI, ACL, EMNLP, ICLR, ICML, and NeurIPS, plus KDD Research Track, covering 2017–2026. Findings is stored separately in the sibling findings directory. Short papers and records without verified long-paper eligibility are outside this directory’s admitted catalog. Awards and oral presentation status are supplementary labels, not admission requirements.

## Financial relevance

- `core`: financial markets, investment, trading, credit, insurance, financial safety, financial documents, corporate disclosure, ESG, or another directly financial research problem.
- `application`: a general method with specific financial data, a financial experiment or business case, substantive financial modeling, or a review of financial tasks.

Background mentions, funding costs, financial affiliations, references to financial papers, and ambiguous uses of words such as “credit”, “portfolio”, or “alpha” are insufficient on their own. Generic time-series methods are included only when the retained evidence establishes financial relevance.

Each catalog record and [paper note](../core/indexes/ai_for_finance.md) preserves the available financial evidence type and excerpt. A rule-assisted screening result is not equivalent to a complete manual reading of every paper.

Three core title/abstract-review records have no separate inclusion excerpt in the imported catalog. Their retained title/abstract classification evidence is available in the assignments and corresponding notes; the validation report lists their IDs. The imported metadata exports preserve these original values.

## Classification records

- [Schema](../core/checks/finance_taxonomy/schema.json): topic, subtopic, and method definitions.
- [Assignments](../core/checks/finance_taxonomy/assignments.json): paper-level classifications and matching evidence.
- [Manual overrides](../core/checks/finance_taxonomy/manual_overrides.json): reviewed classification corrections.
- [Readable taxonomy](../core/indexes/finance_taxonomy.md): category boundaries and usage.

Each paper has exactly one primary finance topic and can have multiple topic, subtopic, and method labels. Changing a topic does not upgrade an application paper to a core paper.

## Validation and provenance

- [Initial source snapshot](source_snapshot.json): literature snapshot date, source revision, and hashes of imported metadata exports.
- [Collection validation](validation.json): latest local file, classification, export, link, and PDF integrity checks.
- [PDFs unavailable locally](missing_pdfs.csv): confirmed included papers without a local PDF; this is not a list of unconfirmed finance candidates.

The initial source library screened five main-conference universes independently of award or oral status. The [AAAI addition audit](aaai_expansion/README.md) records its separate publisher-metadata screening, track rules, and title/abstract and full-text decisions. The [update history](collection_updates.json) distinguishes later additions from the initial snapshot. Coverage is limited by metadata and full-text availability; it does not claim zero omissions.

The [KDD Research Track audit](../../checks/track_screening/kdd/README.md) records the separate 2017–2026 official inventory, full-paper policies, reviewed financial evidence and source hashes. The historical KDD addition preserved the earlier admissions and classifications; subsequent v3 classification changes are recorded separately.

## Long-paper scope revision

The source snapshot and AAAI addition audit describe historical imports. The current long-only catalog is governed by the [track screening audit](../../checks/track_screening/README.md). The [scope migration manifest](../../checks/track_screening/main_scope_migration.json) explains every record removed or deferred. Admission and long-paper evidence are preserved; current task and scope changes are recorded in the v3 migration.

## Current four-collection classification / 当前四集合分类

Current Main catalogs are stored separately in [Core](../core/README.md) and [Application](../application/README.md). Classification and summary links above point to Core; the corresponding Application definitions and evidence are available through its entry page. See [the v3 migration](../../checks/taxonomy_v3/README.md) for all 18 tasks, 111 subcategories, per-paper decisions, pending refinements and old-to-new paths. Historical source reports retain the state of their original import.

当前 Main 的 Core 与 Application 分别存储。上方分类链接指向 Core；Application 的定义与逐篇依据见其独立入口。分类迁移记录覆盖全部论文对应关系与待核对状态，历史来源报告保留当次导入状态。
