# Towards a General Time Series Anomaly Detector with Adaptive Bottlenecks and Dual Adversarial Decoders

ICLR 2025 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：Creditcard。 主题：Time Series / 时间序列；Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=aKcd7ImG5e
- 摘要来源：https://iclr.cc/virtual/2025/poster/29176
- 本地 PDF：[打开](../../pdfs/ICLR/2025/iclr-2025-aKcd7ImG5e__Towards_a_General_Time_Series_Anomaly_Detector_with_Adaptive_Bottlenecks_and_Dual_Adversarial_Decoders.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Representation & Foundation Models / 表征与基础模型；Anomaly Detection / 序列异常检测；Lending & Credit Data / 借贷与信贷数据应用
- 技术方法标签：Uncertainty & Robustness / 不确定性与鲁棒性；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Time series；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

61.59 94.59 74.60 74.31 92.11 82.26 Table 2: Overall results for the NeurIPS-TS datasets. Dataset CICIDS Creditcard GECCO SWAN Metric F1 AUC F1 AUC F1 AUC F1 AUC A.T. 34.71 49.00 65.14 52.55 64.27 51.60 33.67 44.74 DCdetector 40.02 53.95 58.28 42.36 66.18 45.38

## 原始摘要

Time series anomaly detection plays a vital role in a wide range of applications. Existing methods require training one specific model for each dataset, which exhibits limited generalization capability across different target datasets, hindering anomaly detection performance in various scenarios with scarce training data. Aiming at this problem, we propose constructing a general time series anomaly detection model, which is pre-trained on extensive multi-domain datasets and can subsequently apply to a multitude of downstream scenarios. The significant divergence of time series data across different domains presents two primary challenges in building such a general model: (1) meeting the diverse requirements of appropriate information bottlenecks tailored to different datasets in one unified model, and (2) enabling distinguishment between multiple normal and abnormal patterns, both are crucial for effective anomaly detection in various target scenarios. To tackle these two challenges, we propose a General time series anomaly Detector with Adaptive Bottlenecks and Dual Adversarial Decoders (DADA), which enables flexible selection of bottlenecks based on different data and explicitly enhances clear differentiation between normal and abnormal series. We conduct extensive experiments on nine target datasets from different domains. After pre-training on multi-domain data, DADA, serving as a zero-shot anomaly detector for these datasets, still achieves competitive or even superior results compared to those models tailored to each specific dataset.
