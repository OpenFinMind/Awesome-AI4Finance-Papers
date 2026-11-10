# TS-RAG: Retrieval-Augmented Generation based Time Series Foundation Models are Stronger Zero-Shot Forecaster

NeurIPS 2025 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：Exchange rate。 主题：Time Series / 时间序列；Market Prediction / 股价、收益与波动率预测。

- 官方论文页：https://openreview.net/forum?id=PymOnHw4Ty
- 摘要来源：https://neurips.cc/virtual/2025/poster/118173
- 本地 PDF：[打开](../../pdfs/NeurIPS/2025/neurips-2025-PymOnHw4Ty__TS_RAG_Retrieval_Augmented_Generation_based_Time_Series_Foundation_Models_are_Stronger_Zero_Shot_Forecast.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；Representation & Foundation Models / 表征与基础模型；Generation & Simulation / 序列生成与仿真；FX & Crypto Forecasts / 汇率与加密资产预测
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Uncertainty & Robustness / 不确定性与鲁棒性；Retrieval & RAG / 检索与RAG
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：fine-tuning；Language Models；LLMs；RAG；retrieval；Retrieval；Time Series；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/UConn-DSIS/TS-RAG.

## 纳入依据

.1711 0.1912 — — 0.1897 0.2107 Electricity 0.1120 0.2002 0.1132 0.2004 0.1967 0.3028 0.1715 0.2643 0.1832 0.2814 — — 0.1460 0.2237 Exchange rate 0.0627 0.1718 0.0673 0.1780 0.0979 0.2059 0.0657 0.1725 0.0663 0.1720 0.0695 0.1802 0.0831 0.1879 of 5 million data points to construct the multi-domain retrieval knowledge base. To facilitate efficient indexing and retrieval, both the pretraining dataset and the retrieval knowledge base are segmented using a predefined context window. This process results in a total of 26 mill

## 原始摘要

Large Language Models (LLMs) and Foundation Models (FMs) have recently become prevalent for time series forecasting tasks. While fine-tuning LLMs enables domain adaptation, they often struggle to generalize across diverse and unseen datasets. Moreover, existing Time Series Foundation Models (TSFMs) still face challenges in handling non-stationary dynamics and distribution shifts, largely due to the lack of effective mechanisms for adaptation. To this end, we present TS-RAG, a retrieval-augmented generation framework for time series forecasting that enhances the generalization and interpretability of TSFMs. Specifically, TS-RAG leverages pre-trained time series encoders to retrieve semantically relevant segments from a dedicated knowledge base, enriching the contextual representation of the input query. Furthermore, we propose an Adaptive Retrieval Mixer (ARM) module that dynamically fuses the retrieved patterns with the TSFM's internal representation, improving forecasting accuracy without requiring task-specific fine-tuning. Thorough empirical studies on seven public benchmark datasets demonstrate that TS-RAG achieves state-of-the-art zero-shot forecasting performance, outperforming the existing TSFMs by up to 6.84\% across diverse domains while also providing desirable interpretability. Our code and data are available at: https://github.com/UConn-DSIS/TS-RAG.
