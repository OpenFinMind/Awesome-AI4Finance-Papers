# The SEC Filings Dataset: Reconstructing U.S. Corporate and Financial Disclosures into Layout-Faithful and Token-Efficient Pretraining Data

NeurIPS 2026 · main · core

以金融任务或金融数据为核心研究对象。 主题：Financial QA & Reasoning / 金融问答与数值推理；Document AI / 票据、财报与图表理解；Corporate Finance & Accounting / 公司金融与会计；Financial Safety & Compliance / 金融安全与合规；Financial Models & Benchmarks / 金融模型与评测资源。

- 官方论文页：https://openreview.net/forum?id=a7IEj5MRk0
- 摘要来源：https://neurips.cc/virtual/2026/poster/151510
- PDF 状态：access_blocked
- 金融依据类型：title_abstract_review
- 主方向：Document AI / 票据、财报与图表理解
- 细分方向：Numerical & Table Reasoning / 数值与表格推理；Report Layout & Structured Extraction / 财报版面与结构提取；Earnings & Corporate Disclosures / 盈利与公司披露；Trust, Compliance & Bias / 可信、合规与偏差审计；Financial Pretraining & Adaptation / 金融预训练与领域适配
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：language models；LLMs
- 数据 / 评测名称（题名和摘要可确认）：EDGAR；SEC
- 代码链接：摘要未提供可确认链接

## 纳入依据

We introduce the Stanford EDGAR Filings Dataset (SFD), an open reconstruction of SEC filings into layout-faithful MultiMarkdown for financial language modeling and evaluation. / SFD makes audited financial statements, risk disclosures, ownership reports, accounting notes, and market-moving event filings usable as long-context pretraining data and as a basis for financial reasoning, forecasting, compliance, and document understanding. / We further introduce two SFD-derived benchmarks: EDGAR-Forecast, which evaluates filing-grounded numerical forecasting after model knowledge cutoffs, and EDGAR-OCR, which evaluates transcription of complex financial tables.

## 原始摘要

As high-quality public web corpora become increasingly exhausted, clean long-context documents have become a scarce and expensive source of training data for large language models (LLMs). Existing long-context corpora are often proprietary and costly to acquire, synthetically generated, or concentrated in narrow domains such as programming. We introduce the Stanford EDGAR Filings Dataset (SFD), an open reconstruction of SEC filings into layout-faithful MultiMarkdown for financial language modeling and evaluation. SFD makes audited financial statements, risk disclosures, ownership reports, accounting notes, and market-moving event filings usable as long-context pretraining data and as a basis for financial reasoning, forecasting, compliance, and document understanding. The resulting corpus is token-efficient, model-ready, and has less than 0.1\% overlap with Common Crawl-derived corpora. We release SFD-v1, a 152B-token snapshot of a larger 18.4M-filing corpus estimated at 500B tokens. We further introduce two SFD-derived benchmarks: EDGAR-Forecast, which evaluates filing-grounded numerical forecasting after model knowledge cutoffs, and EDGAR-OCR, which evaluates transcription of complex financial tables.
