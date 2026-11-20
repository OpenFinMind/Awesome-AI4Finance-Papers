# Awesome AI4Finance Papers

[English](README.md) | [中文](README.zh-CN.md)

按金融任务、子分类和技术方法整理的 AI for Finance 长文论文库，由 [OpenFinMind](https://github.com/OpenFinMind) 维护。

## 收录范围

收录 **2017–2026** 年 **ICML、ICLR、ACL、EMNLP、NeurIPS、AAAI Main**、**KDD Research Track** 及 **ACL、EMNLP Findings** 中与金融相关的长文，涵盖金融核心研究与金融应用；不收录短文。

## 独立目录

| Track / 轨道 | Scope / 范围 | Long papers / 长文 | PDFs | Browse / 浏览 | Exports / 导出 |
|---|---|---:|---:|---|---|
| Main | [Core](main/core/README.zh-CN.md) | 300 | 249 | [Tasks / 金融任务](main/core/indexes/ai_for_finance.md) · [Subcategories / 子分类](main/core/indexes/subtopics.md) · [Methods / 技术方法](main/core/indexes/methods.md) | [CSV](main/core/finance_catalog.csv) · [JSONL](main/core/finance_catalog.jsonl) · [Excel](main/core/finance_catalog.xlsx) · [BibTeX](main/core/finance_references.bib) |
| Main | [Application](main/application/README.zh-CN.md) | 1,144 | 1,107 | [Tasks / 金融任务](main/application/indexes/ai_for_finance.md) · [Subcategories / 子分类](main/application/indexes/subtopics.md) · [Methods / 技术方法](main/application/indexes/methods.md) | [CSV](main/application/finance_catalog.csv) · [JSONL](main/application/finance_catalog.jsonl) · [Excel](main/application/finance_catalog.xlsx) · [BibTeX](main/application/finance_references.bib) |
| Findings | [Core](findings/core/README.zh-CN.md) | 112 | 112 | [Tasks / 金融任务](findings/core/indexes/ai_for_finance.md) · [Subcategories / 子分类](findings/core/indexes/subtopics.md) · [Methods / 技术方法](findings/core/indexes/methods.md) | [CSV](findings/core/finance_catalog.csv) · [JSONL](findings/core/finance_catalog.jsonl) · [Excel](findings/core/finance_catalog.xlsx) · [BibTeX](findings/core/finance_references.bib) |
| Findings | [Application](findings/application/README.zh-CN.md) | 75 | 75 | [Tasks / 金融任务](findings/application/indexes/ai_for_finance.md) · [Subcategories / 子分类](findings/application/indexes/subtopics.md) · [Methods / 技术方法](findings/application/indexes/methods.md) | [CSV](findings/application/finance_catalog.csv) · [JSONL](findings/application/finance_catalog.jsonl) · [Excel](findings/application/finance_catalog.xlsx) · [BibTeX](findings/application/finance_references.bib) |

四个集合各自提供分类索引、逐篇笔记、任务总结、数据导出和 PDF；每篇 PDF 只保留一份。任务页上半部分提供该集合独立的中英文研究总结。

## 按金融方向浏览

每篇有一个主方向；关联方向允许重叠，表中计数为任务关联篇数。技术方法单独标注。

| Task / 方向 | Main Core | Main Application | Findings Core | Findings Application |
|---|---:|---:|---:|---:|
| Factor Mining / 因子挖掘 | [11](main/core/indexes/finance_topics/alpha_mining.md) | [0](main/application/indexes/finance_topics/alpha_mining.md) | [7](findings/core/indexes/finance_topics/alpha_mining.md) | [0](findings/application/indexes/finance_topics/alpha_mining.md) |
| Time Series / 时间序列 | [41](main/core/indexes/finance_topics/time_series.md) | [338](main/application/indexes/finance_topics/time_series.md) | [7](findings/core/indexes/finance_topics/time_series.md) | [2](findings/application/indexes/finance_topics/time_series.md) |
| Pricing / 定价 | [18](main/core/indexes/finance_topics/pricing.md) | [11](main/application/indexes/finance_topics/pricing.md) | [0](findings/core/indexes/finance_topics/pricing.md) | [1](findings/application/indexes/finance_topics/pricing.md) |
| Valuation Prediction / 估值预测 | [82](main/core/indexes/finance_topics/valuation_prediction.md) | [68](main/application/indexes/finance_topics/valuation_prediction.md) | [18](findings/core/indexes/finance_topics/valuation_prediction.md) | [3](findings/application/indexes/finance_topics/valuation_prediction.md) |
| Portfolio / 投资组合 | [45](main/core/indexes/finance_topics/portfolio.md) | [53](main/application/indexes/finance_topics/portfolio.md) | [2](findings/core/indexes/finance_topics/portfolio.md) | [3](findings/application/indexes/finance_topics/portfolio.md) |
| Insurance and Actuarial Science / 保险精算 | [3](main/core/indexes/finance_topics/insurance.md) | [10](main/application/indexes/finance_topics/insurance.md) | [0](findings/core/indexes/finance_topics/insurance.md) | [3](findings/application/indexes/finance_topics/insurance.md) |
| Financial Sentiment / 金融情感 | [10](main/core/indexes/finance_topics/financial_sentiment.md) | [10](main/application/indexes/finance_topics/financial_sentiment.md) | [6](findings/core/indexes/finance_topics/financial_sentiment.md) | [1](findings/application/indexes/finance_topics/financial_sentiment.md) |
| Financial Question Answering / 金融问答 | [32](main/core/indexes/finance_topics/financial_qa.md) | [62](main/application/indexes/finance_topics/financial_qa.md) | [19](findings/core/indexes/finance_topics/financial_qa.md) | [12](findings/application/indexes/finance_topics/financial_qa.md) |
| Financial Understanding / 金融理解 | [62](main/core/indexes/finance_topics/financial_understanding.md) | [110](main/application/indexes/finance_topics/financial_understanding.md) | [26](findings/core/indexes/finance_topics/financial_understanding.md) | [21](findings/application/indexes/finance_topics/financial_understanding.md) |
| Financial Decision Making / 金融决策 | [74](main/core/indexes/finance_topics/financial_decision.md) | [58](main/application/indexes/finance_topics/financial_decision.md) | [25](findings/core/indexes/finance_topics/financial_decision.md) | [7](findings/application/indexes/finance_topics/financial_decision.md) |
| Sustainable Finance / 可持续金融 | [11](main/core/indexes/finance_topics/sustainable_finance.md) | [6](main/application/indexes/finance_topics/sustainable_finance.md) | [3](findings/core/indexes/finance_topics/sustainable_finance.md) | [1](findings/application/indexes/finance_topics/sustainable_finance.md) |
| Financial Services / 金融服务 | [5](main/core/indexes/finance_topics/financial_services.md) | [61](main/application/indexes/finance_topics/financial_services.md) | [3](findings/core/indexes/finance_topics/financial_services.md) | [10](findings/application/indexes/finance_topics/financial_services.md) |
| Blockchain / 区块链 | [26](main/core/indexes/finance_topics/blockchain.md) | [22](main/application/indexes/finance_topics/blockchain.md) | [3](findings/core/indexes/finance_topics/blockchain.md) | [0](findings/application/indexes/finance_topics/blockchain.md) |
| Financial Safety / 金融安全 | [41](main/core/indexes/finance_topics/financial_safety.md) | [162](main/application/indexes/finance_topics/financial_safety.md) | [19](findings/core/indexes/finance_topics/financial_safety.md) | [7](findings/application/indexes/finance_topics/financial_safety.md) |
| Financial Retrieval / 金融检索 | [17](main/core/indexes/finance_topics/financial_ir.md) | [95](main/application/indexes/finance_topics/financial_ir.md) | [8](findings/core/indexes/finance_topics/financial_ir.md) | [8](findings/application/indexes/finance_topics/financial_ir.md) |
| Financial Evaluation / 金融评测 | [72](main/core/indexes/finance_topics/financial_evaluation.md) | [46](main/application/indexes/finance_topics/financial_evaluation.md) | [48](findings/core/indexes/finance_topics/financial_evaluation.md) | [5](findings/application/indexes/finance_topics/financial_evaluation.md) |
| Financial Models / 金融模型 | [5](main/core/indexes/finance_topics/financial_models.md) | [22](main/application/indexes/finance_topics/financial_models.md) | [3](findings/core/indexes/finance_topics/financial_models.md) | [4](findings/application/indexes/finance_topics/financial_models.md) |
| Financial Risk / 金融风险 | [18](main/core/indexes/finance_topics/financial_risk.md) | [251](main/application/indexes/finance_topics/financial_risk.md) | [2](findings/core/indexes/finance_topics/financial_risk.md) | [2](findings/application/indexes/finance_topics/financial_risk.md) |

## 分类说明

- **Core / 金融核心研究**: the main research problem or contribution concerns finance. / 主要研究问题或贡献直接面向金融。
- **Application / 金融应用**: finance is a substantive application of a general method. / 金融是通用方法的实质性应用。

完整子分类及边界见各集合的 **Classification / 分类说明**；证据不足的细分归类保留待核对状态。金融风险与金融安全独立分类。

## 按会议浏览

| Venue / 会议 | Main | Findings |
|---|---:|---:|
| ICML | [core: 24](main/core/indexes/venues/icml.md) · [application: 249](main/application/indexes/venues/icml.md) | — |
| ICLR | [core: 20](main/core/indexes/venues/iclr.md) · [application: 174](main/application/indexes/venues/iclr.md) | — |
| ACL | [core: 50](main/core/indexes/venues/acl.md) · [application: 119](main/application/indexes/venues/acl.md) | [core: 49](findings/core/indexes/venues/acl.md) · [application: 34](findings/application/indexes/venues/acl.md) |
| EMNLP | [core: 47](main/core/indexes/venues/emnlp.md) · [application: 169](main/application/indexes/venues/emnlp.md) | [core: 63](findings/core/indexes/venues/emnlp.md) · [application: 41](findings/application/indexes/venues/emnlp.md) |
| NeurIPS | [core: 39](main/core/indexes/venues/neurips.md) · [application: 259](main/application/indexes/venues/neurips.md) | — |
| AAAI | [core: 77](main/core/indexes/venues/aaai.md) · [application: 83](main/application/indexes/venues/aaai.md) | — |
| KDD Research Track | [core: 43](main/core/indexes/venues/kdd.md) · [application: 91](main/application/indexes/venues/kdd.md) | — |

## 资源

PDF: `<main|findings>/<core|application>/pdfs/<venue>/<year>/`. Missing PDFs retain official online links. / 暂无本地 PDF 的已收录论文保留官方链接。

[Contributing / 维护说明](CONTRIBUTING.md) · [Screening evidence / 收录依据](checks/track_screening/README.md) · [Classification migration / 分类迁移记录](checks/taxonomy_v3/README.md)

[GitHub](https://github.com/OpenFinMind/Awesome-AI4Finance-Papers) · [Hugging Face](https://huggingface.co/datasets/OpenFinMind/Awesome-AI4Finance-Papers)
