# Awesome AI4Finance Papers

[English](README.md) | [中文](README.zh-CN.md)

[GitHub](https://github.com/OpenFinMind/Awesome-AI4Finance-Papers) · [Hugging Face](https://huggingface.co/datasets/OpenFinMind/Awesome-AI4Finance-Papers)

**Long papers only. Short papers are excluded.**

AI for Finance long papers organized by financial task, subtopic, and technical method. Maintained by [OpenFinMind](https://github.com/OpenFinMind).

## Scope

Covers finance-related long papers from **ICML, ICLR, ACL, EMNLP, NeurIPS, and AAAI Main**, and **ACL / EMNLP Findings**, within **2017–2026**, including finance core research and financial applications. Main and Findings are stored separately and organized by financial task, subtopic, and technical method.

## Separate collections

| Track | Long papers | Papers and classifications | Exports |
|---|---:|---|---|
| [Main](main/README.md) | 1,310 | [Tasks](main/indexes/ai_for_finance.md) · [Subtopics](main/indexes/subtopics.md) · [Methods](main/indexes/methods.md) | [Excel](main/finance_catalog.xlsx) · [CSV](main/finance_catalog.csv) · [JSONL](main/finance_catalog.jsonl) · [BibTeX](main/finance_references.bib) |
| [Findings](findings/README.md) | 187 | [Tasks](findings/indexes/ai_for_finance.md) · [Subtopics](findings/indexes/subtopics.md) · [Methods](findings/indexes/methods.md) | [Excel](findings/finance_catalog.xlsx) · [CSV](findings/finance_catalog.csv) · [JSONL](findings/finance_catalog.jsonl) · [BibTeX](findings/finance_references.bib) |

Main and Findings each have their own indexes, paper notes, CSV, JSONL, Excel, BibTeX, and PDFs. Exported `local_path` values are relative to the corresponding track directory.

## By venue

| Venue / 会议 | Main | Findings |
|---|---:|---:|
| ICML | [273](main/indexes/venues/icml.md) | — |
| ICLR | [194](main/indexes/venues/iclr.md) | — |
| ACL | [169](main/indexes/venues/acl.md) | [83](findings/indexes/venues/acl.md) |
| EMNLP | [216](main/indexes/venues/emnlp.md) | [104](findings/indexes/venues/emnlp.md) |
| NeurIPS | [298](main/indexes/venues/neurips.md) | — |
| AAAI | [160](main/indexes/venues/aaai.md) | — |

## By financial task

Financial tasks allow multiple labels, so counts overlap; every paper also has one primary task. Subtopics describe more specific problems. Technical methods such as LLMs, reinforcement learning, graph learning, diffusion, and causal methods are recorded separately.

| Finance task / 金融任务 | Main | Findings |
|---|---:|---:|
| Alpha Mining / 量化因子挖掘 | [8](main/indexes/finance_topics/alpha_mining.md) | [6](findings/indexes/finance_topics/alpha_mining.md) |
| Time Series / 时间序列 | [348](main/indexes/finance_topics/time_series.md) | [3](findings/indexes/finance_topics/time_series.md) |
| Asset Pricing / 资产定价 | [10](main/indexes/finance_topics/asset_pricing.md) | [0](findings/indexes/finance_topics/asset_pricing.md) |
| Derivatives & Hedging / 衍生品定价与对冲 | [14](main/indexes/finance_topics/derivatives.md) | [0](findings/indexes/finance_topics/derivatives.md) |
| Portfolio & Investment / 投资组合与投资管理 | [91](main/indexes/finance_topics/portfolio.md) | [5](findings/indexes/finance_topics/portfolio.md) |
| Trading & Microstructure / 交易与市场微观结构 | [79](main/indexes/finance_topics/trading.md) | [12](findings/indexes/finance_topics/trading.md) |
| Market Prediction / 股价、收益与波动率预测 | [94](main/indexes/finance_topics/market_prediction.md) | [10](findings/indexes/finance_topics/market_prediction.md) |
| Credit & Financial Risk / 信贷与金融风险 | [257](main/indexes/finance_topics/credit_risk.md) | [3](findings/indexes/finance_topics/credit_risk.md) |
| Insurance & Actuarial / 保险与精算 | [21](main/indexes/finance_topics/insurance.md) | [6](findings/indexes/finance_topics/insurance.md) |
| Fraud & AML / 欺诈检测与反洗钱 | [62](main/indexes/finance_topics/fraud_aml.md) | [7](findings/indexes/finance_topics/fraud_aml.md) |
| Financial NLP / 金融文本、情感与事件 | [88](main/indexes/finance_topics/financial_nlp.md) | [21](findings/indexes/finance_topics/financial_nlp.md) |
| Financial QA & Reasoning / 金融问答与数值推理 | [86](main/indexes/finance_topics/financial_qa.md) | [30](findings/indexes/finance_topics/financial_qa.md) |
| Financial IR & RAG / 金融检索与RAG | [108](main/indexes/finance_topics/financial_ir.md) | [14](findings/indexes/finance_topics/financial_ir.md) |
| Document AI / 票据、财报与图表理解 | [57](main/indexes/finance_topics/document_ai.md) | [12](findings/indexes/finance_topics/document_ai.md) |
| Financial Agents / 金融Agent与决策 | [54](main/indexes/finance_topics/financial_agents.md) | [22](findings/indexes/finance_topics/financial_agents.md) |
| Macro & Economic Forecasting / 宏观经济与预测 | [26](main/indexes/finance_topics/macro_economics.md) | [6](findings/indexes/finance_topics/macro_economics.md) |
| Corporate Finance & Accounting / 公司金融与会计 | [44](main/indexes/finance_topics/corporate_finance.md) | [16](findings/indexes/finance_topics/corporate_finance.md) |
| ESG & Sustainable Finance / ESG与可持续金融 | [17](main/indexes/finance_topics/esg.md) | [4](findings/indexes/finance_topics/esg.md) |
| Banking & Customer Service / 银行业务与客户服务 | [49](main/indexes/finance_topics/banking.md) | [12](findings/indexes/finance_topics/banking.md) |
| Blockchain & Digital Assets / 区块链与数字资产 | [40](main/indexes/finance_topics/blockchain.md) | [3](findings/indexes/finance_topics/blockchain.md) |
| Financial Safety & Compliance / 金融安全与合规 | [84](main/indexes/finance_topics/financial_safety.md) | [16](findings/indexes/finance_topics/financial_safety.md) |
| Financial Models & Benchmarks / 金融模型与评测资源 | [92](main/indexes/finance_topics/financial_models.md) | [21](findings/indexes/finance_topics/financial_models.md) |
| Other Financial Applications / 其他金融应用 | [7](main/indexes/finance_topics/other_finance.md) | [0](findings/indexes/finance_topics/other_finance.md) |

## Classification

- **Core:** the research problem directly concerns finance.
- **Application:** a general method has substantive financial data, experiments, business cases, modeling, or a domain review; it need not be a finance-specific method.

Selection and verification details are available in the [screening audit](checks/track_screening/README.md).

## Resources

PDFs live under `<main|findings>/pdfs/<venue>/<year>/`. Publisher and author arXiv versions are distinguished and hashed with SHA-256. Admitted papers without local PDFs retain online links. Paper copyrights remain with the authors and publishers. See [CONTRIBUTING.md](CONTRIBUTING.md) for maintenance.
