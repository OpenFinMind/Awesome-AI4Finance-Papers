# Retrieval Over Training: Similarity search-based Model Selection for Time Series Anomaly Detection

NeurIPS 2026 · main · application

正文包含金融数据、金融训练数据、金融任务评测或具体金融场景案例。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=WpZao8pAB7
- 摘要来源：https://neurips.cc/Downloads/2026
- 本地 PDF：[打开](../../pdfs/NeurIPS/2026/neurips-2026-WpZao8pAB7__Retrieval_Over_Training_Similarity_search_based_Model_Selection_for_Time_Series_Anomaly_Detection.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Representation & Foundation Models / 表征与基础模型；Anomaly Detection / 序列异常检测
- 技术方法标签：Retrieval & RAG / 检索与RAG；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：retrieval；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

rature Review Time-series anomaly detection (TSAD) has been studied extensively in recent years because of its importance in monitoring, diagnosis, and decision support across domains such as healthcare, manufacturing, finance, energy, and cybersecurity [8, 54]. A central challenge in TSAD is that anomalies may take very different forms, and the statistical properties of time series vary widely across datasets. As a result, the literature has produced a large variety of detectors, each relying on different assumptions about temporal structure, recurrence, noise, and ano

## 原始摘要

Anomaly detection is a fundamental task for time-series analytics, with important implications for the downstream performance of many applications. Despite the large number of anomaly detection methods proposed in the literature, recent benchmark studies have shown that no single detector performs best across highly heterogeneous time series. Therefore, a practical and scalable solution is to develop a model-selection method that, for a given time series, selects the anomaly detector most likely to perform well. Nevertheless, the model selection approach proposed in the literature suffers from a significant drop in accuracy when applied in Out-of-Distribution (OOD) settings. In this paper, we tackle the aforementioned limitation and propose \textbf{\textsc{RAMSAD}}, a train-free, retrieval-based framework for model selection in time-series anomaly detection. Given a new time series, our method queries a knowledge base of previously observed instances, retrieves the top-${k}$ most similar series, and transfers detector recommendations from their performance profiles. The framework can operate with standard similarity measures as well as embedding-based representations. Overall, we demonstrate that similarity-based retrieval constitutes a strong and efficient foundation for model selection in time-series anomaly detection.
