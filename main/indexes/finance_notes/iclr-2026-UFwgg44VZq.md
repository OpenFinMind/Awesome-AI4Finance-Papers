# ReTabAD: A Benchmark for Restoring Semantic Context in Tabular Anomaly Detection

ICLR 2026 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：Credit card。 主题：Credit & Financial Risk / 信贷与金融风险；Fraud & AML / 欺诈检测与反洗钱。

- 官方论文页：https://openreview.net/forum?id=UFwgg44VZq
- 摘要来源：https://iclr.cc/virtual/2026/poster/10009247
- 本地 PDF：[打开](../../pdfs/ICLR/2026/iclr-2026-UFwgg44VZq__ReTabAD_A_Benchmark_for_Restoring_Semantic_Context_in_Tabular_Anomaly_Detection.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Payment & Transaction Fraud / 支付与交易欺诈；Lending & Credit Data / 借贷与信贷数据应用
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Tabular Learning / 表格学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：LLM
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

anomalies, while Lodgepole Pine forests (mid to high elevation coniferous) are normal. credit Credit card dataset with demographics and payment history. Customers who defaulted on their credit card payment are considered anomalies, while customers who did

## 原始摘要

In tabular anomaly detection (AD), textual semantic context often carries critical signals, as the definition of an anomaly is closely tied to domain-specific context. However, existing benchmarks provide only raw data points without semantic context, overlooking rich textual metadata such as feature descriptions and domain knowledge that experts rely on in practice. This limitation restricts research flexibility and prevents models from fully leveraging domain knowledge for detection. ReTabAD addresses this gap by Restoring textual semantics to enable context-aware Tabular AD research. We provide (1) 20 carefully curated tabular datasets enriched with structured textual metadata, together with implementations of state-of-the-art AD algorithms—including classical, deep learning, and LLM-based approaches—and (2) a zero-shot LLM framework that leverages semantic context without task-specific training, establishing a strong baseline for future research. Furthermore, this work provides insights into the role and utility of textual metadata in AD through experiments and analysis. Results show that semantic context improves detection performance and enhances interpretability by supporting domain-aware reasoning. These findings establish ReTabAD as a benchmark for systematic exploration of context-aware AD.
