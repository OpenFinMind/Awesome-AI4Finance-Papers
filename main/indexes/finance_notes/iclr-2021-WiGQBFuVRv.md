# Multivariate Probabilistic Time Series Forecasting via Conditioned Normalizing Flows

ICLR 2021 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：Exchange benchmark (currency series)。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=WiGQBFuVRv
- 摘要来源：https://iclr.cc/virtual/2021/poster/3117
- 本地 PDF：[打开](../../pdfs/ICLR/2021/iclr-2021-WiGQBFuVRv__Multivariate_Probabilistic_Time_Series_Forecasting_via_Conditioned_Normalizing_Flows.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；Causality & Dynamics / 序列因果与动力学；Probabilistic Forecasting & Calibration / 概率预测与校准
- 技术方法标签：Diffusion & Flow / 扩散与流模型
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Time series；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

ind-scaling lowrank-Copula scaling Copula Real-NVP MAF MAF Exchange 0.008±0.001 0.007±0.000 0.009±0.000 0.007±0.000 0.0064±0.003 0.005±0.003 0.005±0.003 Solar 0.391±0.017 0.319±0.011 0.368±0.012 0.337±0.024 0.331±0.02 0.315±0.023 0.301±0.014 Electricity 0.025±0.001 0.064±0.008 0.022±0.000 0.024±0.002 0.024±0.001

## 原始摘要

Time series forecasting is often fundamental to scientific and engineering problems and enables decision making. With ever increasing data set sizes, a trivial solution to scale up predictions is to assume independence between interacting time series. However, modeling statistical dependencies can improve accuracy and enable analysis of interaction effects. Deep learning methods are well suited for this problem, but multi-variate models often assume a simple parametric distribution and do not scale to high dimensions. In this work we model the multi-variate temporal dynamics of time series via an autoregressive deep learning model, where the data distribution  is represented by a conditioned normalizing flow. This combination retains the power of autoregressive models, such as good performance in extrapolation into the future, with the flexibility of flows as a general purpose high-dimensional distribution model, while remaining computationally tractable. We show that it improves over the state-of-the-art for standard metrics on many real-world data sets with several thousand interacting time-series.
