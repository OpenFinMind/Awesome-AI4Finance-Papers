# Adapt Data to Model: Adaptive Transformation Optimization for Domain-shared Time Series Foundation Models

ICLR 2026 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：Exchange benchmark (currency series)。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=uTK1SNgi1N
- 摘要来源：https://iclr.cc/virtual/2026/poster/10006894
- 本地 PDF：[打开](../../pdfs/ICLR/2026/iclr-2026-uTK1SNgi1N__Adapt_Data_to_Model_Adaptive_Transformation_Optimization_for_Domain_shared_Time_Series_Foundation_Models.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；Representation & Foundation Models / 表征与基础模型
- 技术方法标签：Uncertainty & Robustness / 不确定性与鲁棒性；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：optimization；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/thulab/TATO.

## 纳入依据

6 0.0705 0.1962 48 0.1509 0.2901 0.1450 0.2849 0.1676 0.3137 0.1502 0.2870 0.1640 0.3025 0.1383 0.2752 Exchange 96 0.3634 0.4396 0.3027 0.4098 0.3160 0.4109 0.2909 0.3986 0.3099 0.4087 0.2929 0.3962 192 0.6367 0.6191 0.6314 0.5948 0.5525 0.5821 0.5094 0.5401 0.5080 0.5604 0.5099 0.5488 24 0.0557 0.1307 0.0570 0.1335 0.3166 0.4608 0.2860 0.4302 0.2427 0.3675 0.0644 0.1370 48 0.0586 0.

## 原始摘要

Large time series models (LTMs) have emerged as powerful tools for universal forecasting, yet they often struggle with the inherent diversity and nonstationarity of real-world time series data, leading to an unsatisfactory trade-off between forecasting accuracy and generalization. Rather than continually finetuning new LTM instances for each domain, we propose a data-centric framework, time-series adaptive transformation optimization (TATO), that enables a single frozen pre-trained LTM to adapt to diverse downstream domains through an optimally configured transformation pipeline. Specifically, TATO constructs three representative types of transformations, including context slicing, scale normalization, and outlier correction, to help LTMs better align with target domain characteristics. To ensure robustness, we incorporate carefully selected time series augmentations and a two-stage ranking mechanism that filters out pipelines underperforming on specific metrics. Extensive experiments on state-of-the-art LTMs and widely used datasets demonstrate that TATO consistently and significantly improves domain-adaptive forecasting performance, achieving a maximum reduction in MSE of 65.4\% and an average reduction of 13.6\%. Moreover, TATO is highly efficient, typically completing optimization in under 2 minutes, making it practical for real-world deployment. The source code is available at https://github.com/thulab/TATO.
