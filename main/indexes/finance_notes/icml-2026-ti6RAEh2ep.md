# TsLLM: Augmenting LLMs for General Time Series Understanding and Prediction

ICML 2026 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：S&P 500。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=ti6RAEh2ep
- 摘要来源：https://icml.cc/virtual/2026/poster/61098
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-ti6RAEh2ep__TsLLM_Augmenting_LLMs_for_General_Time_Series_Understanding_and_Prediction.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；Representation & Foundation Models / 表征与基础模型
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Language Models；LLM；LLMs；Time series；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

that provide rich contextual information for time series analysis. Financial Dataset Development For our data collection efforts, we focused particularly on the financial domain, creating a novel dataset that combines S&P 500 daily closing prices with corresponding news articles. This pairing enables exploration of contextual forecasting tasks where models must consider both numerical trends and relevant textual information when making predictions. Our financial dataset construction process involves several key steps: first, we collect historical S&P 500 price data; se

## 原始摘要

Time series data is fundamental to decision-making across many domains including healthcare, finance, power systems, and logistics. However, analyzing this data correctly often requires incorporating unstructured contextual information, answering domain-specific questions, and generating natural language explanations – capabilities that traditional time series models lack. While Large Language Models (LLMs) excel at contextual reasoning and knowledge integration, they struggle with numerical time series due to inefficient text-based representations and limited exposure to numerical data during pretraining. We address this gap by augmenting an LLM with specialized time series perception through a patch-based encoder-decoder architecture. We train this time series-augmented LLM (TsLLM) on a large corpus of over 25 billion tokens of interleaved time series and text spanning diverse tasks: forecasting with contextual information, question-answering, anomaly detection, classification, report generation, and more, all unified as autoregressive next token prediction. This training enables TsLLM to leverage both its natural language skills and newly acquired understanding of numerical time series signals. While not designed to surpass specialized models on traditional benchmarks, TsLLM demonstrates strong performance on tasks requiring the integration of time series analysis with natural language – capabilities that conventional approaches cannot provide. It also exhibits strong zero-shot and few-shot performance, showing it can adapt to new data without additional training.
