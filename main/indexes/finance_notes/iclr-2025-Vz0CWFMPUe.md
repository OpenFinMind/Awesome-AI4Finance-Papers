# TimeInf: Time Series Data Contribution via Influence Functions

ICLR 2025 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：Exchange benchmark (currency series)。 主题：Time Series / 时间序列；Market Prediction / 股价、收益与波动率预测。

- 官方论文页：https://openreview.net/forum?id=Vz0CWFMPUe
- 摘要来源：https://iclr.cc/virtual/2025/poster/29389
- 本地 PDF：[打开](../../pdfs/ICLR/2025/iclr-2025-Vz0CWFMPUe__TimeInf_Time_Series_Data_Contribution_via_Influence_Functions.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；Anomaly Detection / 序列异常检测；FX & Crypto Forecasts / 汇率与加密资产预测
- 技术方法标签：Tabular Learning / 表格学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

a less rapid decrease or even an increase in performance. Alabama State. The Electricity dataset includes the electricity consumption patterns of 321 clients from 2012 to 2014 (Trindade, 2015). The Exchange Rate dataset includes daily exchange rates for 8 countries, covering the period from 1990 to 2016 (Lai et al., 2018). Baselines. For each block in the training dataset, we assess its impact by averaging the score Iblock from Equation (4) across all blocks in the validation set. We fix the block length as 100. For anomaly detection, standard methods are available, but for data pruning, no established method exists. Theref

## 原始摘要

Evaluating the contribution of individual data points to a model's prediction is critical for interpreting model predictions and improving model performance. Existing data contribution methods have been applied to various data types, including tabular data, images, and text; however, their primary focus has been on i.i.d. settings. Despite the pressing need for principled approaches tailored to time series datasets, the problem of estimating data contribution in such settings remains under-explored, possibly due to challenges associated with handling inherent temporal dependencies. This paper introduces TimeInf, a model-agnostic data contribution estimation method for time-series datasets. By leveraging influence scores, TimeInf attributes model predictions to individual time points while preserving temporal structures between the time points. Our empirical results show that TimeInf effectively detects time series anomalies and outperforms existing data attribution techniques as well as state-of-the-art anomaly detection methods. Moreover, TimeInf offers interpretable attributions of data values, allowing us to distinguish diverse anomalous patterns through visualizations. We also showcase a potential application of TimeInf in identifying mislabeled anomalies in the ground truth annotations.
