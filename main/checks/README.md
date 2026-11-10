# Evidence and selection criteria

This Main directory contains confirmed financial long papers from the main tracks of AAAI, ACL, EMNLP, ICLR, ICML, and NeurIPS, covering 2017–2026. Findings is stored separately in the sibling findings directory. Short papers and records without verified long-paper eligibility are outside this directory’s admitted catalog. Awards and oral presentation status are supplementary labels, not admission requirements.

## Financial relevance

- `core`: financial markets, investment, trading, credit, insurance, financial safety, financial documents, corporate disclosure, ESG, or another directly financial research problem.
- `application`: a general method with specific financial data, a financial experiment or business case, substantive financial modeling, or a review of financial tasks.

Background mentions, funding costs, financial affiliations, references to financial papers, and ambiguous uses of words such as “credit”, “portfolio”, or “alpha” are insufficient on their own. Generic time-series methods are included only when the retained evidence establishes financial relevance.

Each catalog record and [paper note](../indexes/ai_for_finance.md) preserves the available financial evidence type and excerpt. A rule-assisted screening result is not equivalent to a complete manual reading of every paper.

Three core title/abstract-review records have no separate inclusion excerpt in the imported catalog. Their retained title/abstract classification evidence is available in the assignments and corresponding notes; the validation report lists their IDs. The imported metadata exports preserve these original values.

## Classification records

- [Schema](finance_taxonomy/schema.json): topic, subtopic, and method definitions.
- [Assignments](finance_taxonomy/assignments.json): paper-level classifications and matching evidence.
- [Manual overrides](finance_taxonomy/manual_overrides.json): reviewed classification corrections.
- [Readable taxonomy](../indexes/finance_taxonomy.md): category boundaries and usage.

Each paper has exactly one primary finance topic and can have multiple topic, subtopic, and method labels. Changing a topic does not upgrade an application paper to a core paper.

## Validation and provenance

- [Initial source snapshot](source_snapshot.json): literature snapshot date, source revision, and hashes of imported metadata exports.
- [Collection validation](validation.json): latest local file, classification, export, link, and PDF integrity checks.
- [PDFs unavailable locally](missing_pdfs.csv): confirmed included papers without a local PDF; this is not a list of unconfirmed finance candidates.

The initial source library screened five main-conference universes independently of award or oral status. The [AAAI addition audit](aaai_expansion/README.md) records its separate publisher-metadata screening, track rules, and title/abstract and full-text decisions. The [update history](collection_updates.json) distinguishes later additions from the initial snapshot. Coverage is limited by metadata and full-text availability; it does not claim zero omissions.

## Long-paper scope revision

The source snapshot and AAAI addition audit describe historical imports. The current long-only catalog is governed by the [track screening audit](../../checks/track_screening/README.md). The [scope migration manifest](../../checks/track_screening/main_scope_migration.json) explains every record removed or deferred. Existing financial decisions and topic assignments for retained Main papers are preserved.
