# AAAI main-track addition

Historical AAAI addition audit. The current Main long-paper catalog and current validation are described in the [track screening audit](../../../checks/track_screening/README.md).

Collection date: **2026-11-10**. Coverage window: **2017–2026**.

This update adds **160 AAAI main-technical-track papers**: **77 core** and **83 application** papers. All 160 have an identity-checked local PDF: **105 publisher versions** and **55 author arXiv versions**. The initial 1,178 records and their financial classifications are preserved. Findings remain excluded.

## Sources and track boundaries

- AAAI's publisher-deposited [Crossref journal metadata](https://api.crossref.org/journals/2374-3468/works) supplies titles, authors, abstracts, DOIs, volumes, issues, and publisher resource links. The [source manifest](source_manifest.json) records request URLs, retrieval times, and uncompressed hashes; compressed responses are retained under `sources/aaai/` at the repository root.
- Official AAAI proceedings directories establish the distinction between main technical issues and other programs. Examples: [2020](https://aaai.org/proceeding/aaai-34-2020/), [2021](https://aaai.org/proceeding/aaai-35-2021/), [2023](https://aaai.org/proceeding/aaai-37-2023/), [2025](https://aaai.org/proceeding/aaai-39-2025/), and [2026](https://aaai.org/proceeding/aaai-40-2026/).
- [Track rules](track_rules.json) record the main-issue ranges. For example, AAAI 2024 issue 19 is the [special track on Safe, Robust and Responsible AI](https://ojs.aaai.org/index.php/AAAI/issue/view/594), so issues 19–21 are excluded. AAAI 2026 issues 44–48 are outside the main technical tracks.
- Legacy mixed-volume editions need a section lookup in addition to the DOI. [Legacy section records](legacy_sections.json) retain the matched section labels and official proceedings references. The secondary `ai-conferences/AAAI<year>` catalogs were used to corroborate legacy section membership and discover possible author versions; they are not the authority for financial relevance or a substitute for the publisher bibliographic record.

IAAI, EAAI, special tracks, senior-member presentations, student abstracts, demos, and journal reprints are excluded. A financial title in the AAAI proceedings does not automatically establish main-track eligibility.

## Screening and admission

The metadata collection contains **22,308 unique publisher records**, including non-main programs. Rule-based screening produced **2,321 candidates**; a keyword match alone is not an admission.

1. Title/abstract review confirmed 105 papers with a directly stated financial problem or application.
2. An additional 508 main-track candidates were queued for full-text inspection. Available PDFs passed title-and-author identity checks before their text was used. Matches in references, generic examples, or unrelated meanings were rejected as evidence. Examples include algorithm “portfolios”, mathematical or hardware uses of “M4”, and elliptic PDEs.
3. Full-text review added 55 application papers with actual financial datasets, experiments, or a concrete financial case model. These include exchange-rate forecasting, credit scoring and recourse, financial fraud, blockchain data, and banking cash withdrawals.

The [admission decisions](review_decisions.json) retain scope, evidence type, source excerpt, source URL, track information, and reviewed taxonomy overrides. [Full-text decisions](fulltext_review_decisions.json) retain the reviewed positive and negative matches. [Candidate dispositions](candidate_dispositions.csv) distinguish admitted records from other tracks, unresolved full texts, and candidates without established financial evidence. Unavailable or unverified full text is not treated as proof that a paper is nonfinancial.

Financial `core` and `application` labels follow the existing definitions. General methods are not promoted to core simply because they use a financial benchmark. Each record has one primary finance topic; additional finance topics and methods are independent labels. PDF extraction control characters are removed from exported evidence text.

## Benchmark-specific checks

- M4 contains financial series, but M4-Hourly alone does not establish financial relevance. [Official M4 category provenance](m4_financial_domain_provenance.json) records the Finance frequency distribution. M4-based admissions identify the non-hourly subsets actually used.
- DeepBooTS uses M4-Hourly, which is not its admission basis. Its financial application is the separately documented NN5 ATM cash-withdrawal benchmark.
- Synthetic financial case models are marked separately from real financial datasets. For example, the causal-recourse paper retains a credit-card approval case model and is an application paper.

## PDFs and validation

[PDF results](pdf_results.json) and individual `pdf_records/` files record acquisition attempts, final URLs, file versions, SHA-256, page counts, and title/author identity results. Public author versions remain explicitly marked `arxiv_author_version`; they are not asserted to be identical to the published conference version.

[Initial-record hashes](baseline_record_hashes.json) support preservation checks. [AAAI validation](validation.json) checks source cache hashes, bibliographic identity, track boundaries, admission evidence, PDF versions, and unchanged original records. [Collection validation](../validation.json) additionally checks all catalog exports, topic memberships, local links, and PDF hashes.

Rebuild and validate:

```bash
pip install -r scripts/requirements.txt
python scripts/export_collection.py
python scripts/build_indexes.py
python scripts/verify_collection.py
python scripts/verify_aaai_update.py
```

The initial source snapshot remains historical provenance. This addition has its own [update record](../collection_updates.json). The collection does not claim exhaustive coverage of experiments hidden in unavailable full texts.
