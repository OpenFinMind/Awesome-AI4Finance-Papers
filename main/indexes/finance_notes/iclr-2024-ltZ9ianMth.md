# RobustTSF: Towards Theory and Design of Robust Time Series Forecasting with Anomalies

ICLR 2024 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：Exchange benchmark (currency series)。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=ltZ9ianMth
- 摘要来源：https://iclr.cc/virtual/2024/poster/17914
- 本地 PDF：[打开](../../pdfs/ICLR/2024/iclr-2024-ltZ9ianMth__RobustTSF_Towards_Theory_and_Design_of_Robust_Time_Series_Forecasting_with_Anomalies.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；Anomaly Detection / 序列异常检测
- 技术方法标签：Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Time series；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/haochenglouis/RobustTSF.

## 纳入依据

we report best epoch MAE for each setting ETT-h1 with Anomaly Position Exchange with Anomaly Position Anomaly Type front middle back front middle back Clean 0.051 0.051 0.051 0.047 0.047 0.047 Const. (η = 0.1) 0.051 0.051 0.052

## 原始摘要

Time series forecasting is an important and forefront task whose techniques have been applied to electricity forecasting, trajectory prediction, labor planning, etc. However, most of time series forecasting techniques assume that the training data is clean without anomalies. This assumption is unrealistic since the collected time series data can be contaminated in practice. The forecasting model will be inferior if it is directly trained by time series with anomalies. Thus it is essential to develop methods to automatically learn a robust forecasting model from the contaminated data. In this paper, we first statistically define three types of anomalies, then theoretically and experimentally analyze the loss robustness and sample robustness when these anomalies exist. Based on our analyses, we propose a simple and efficient algorithm to learn a robust forecasting model. Extensive experiments show that our method is highly robust and outperforms all existing approaches. The code is available at https://github.com/haochenglouis/RobustTSF.
