# Awesome AI4Finance Papers

[English](README.md) | [中文](README.zh-CN.md)

[GitHub](https://github.com/OpenFinMind/Awesome-AI4Finance-Papers) · [Hugging Face](https://huggingface.co/datasets/OpenFinMind/Awesome-AI4Finance-Papers)

**仅收录长文，不收录短文。**

按金融任务、子方向和技术方法整理的 AI for Finance 长文论文库，由 [OpenFinMind](https://github.com/OpenFinMind) 维护。

## 收录范围

收录 **2017–2026** 年 **ICML、ICLR、ACL、EMNLP、NeurIPS、AAAI Main** 及 **ACL、EMNLP Findings** 中与金融相关的长文，涵盖金融核心研究与金融应用。Main 与 Findings 分开存储，并按金融任务、子方向和技术方法整理。

## 独立目录

| 类别 | 长文 | 论文与分类 | 数据导出 |
|---|---:|---|---|
| [Main](main/README.zh-CN.md) | 1,310 | [Tasks](main/indexes/ai_for_finance.md) · [Subtopics](main/indexes/subtopics.md) · [Methods](main/indexes/methods.md) | [Excel](main/finance_catalog.xlsx) · [CSV](main/finance_catalog.csv) · [JSONL](main/finance_catalog.jsonl) · [BibTeX](main/finance_references.bib) |
| [Findings](findings/README.zh-CN.md) | 187 | [Tasks](findings/indexes/ai_for_finance.md) · [Subtopics](findings/indexes/subtopics.md) · [Methods](findings/indexes/methods.md) | [Excel](findings/finance_catalog.xlsx) · [CSV](findings/finance_catalog.csv) · [JSONL](findings/finance_catalog.jsonl) · [BibTeX](findings/finance_references.bib) |

Main 与 Findings 各有独立目录、索引、逐篇笔记、CSV、JSONL、Excel、BibTeX 和 PDF。导出文件中的 `local_path` 相对于所属类别目录；根目录不提供混合两类的论文清单。

## 按会议浏览

| Venue / 会议 | Main | Findings |
|---|---:|---:|
| ICML | [273](main/indexes/venues/icml.md) | — |
| ICLR | [194](main/indexes/venues/iclr.md) | — |
| ACL | [169](main/indexes/venues/acl.md) | [83](findings/indexes/venues/acl.md) |
| EMNLP | [216](main/indexes/venues/emnlp.md) | [104](findings/indexes/venues/emnlp.md) |
| NeurIPS | [298](main/indexes/venues/neurips.md) | — |
| AAAI | [160](main/indexes/venues/aaai.md) | — |

## 按金融任务浏览

金融任务允许多标签，计数存在重叠；每篇另有唯一主方向。子方向描述具体任务，技术方法独立标注 LLM、强化学习、图学习、扩散、因果等，避免把技术名称当成金融任务。

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

## 分类说明

- **金融核心研究（core）**：研究问题直接面向金融。
- **金融应用（application）**：通用方法含有实质性的金融数据、实验、业务场景、建模或领域综述；不等同于金融专用方法。

筛选与核验说明见[筛查审计](checks/track_screening/README.md)。

## 资源

PDF 位于 `<main|findings>/pdfs/<venue>/<year>/`；官方版本与作者 arXiv 版本分别标注，并记录 SHA-256。未下载的已收录论文保留在线链接。论文版权归作者与出版方。维护方式见 [CONTRIBUTING.md](CONTRIBUTING.md)。
