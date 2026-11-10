# ResCP: Reservoir Conformal Prediction for Time Series Forecasting

ICLR 2026 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：Exchange benchmark (currency series)。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=WGqibe5H3W
- 摘要来源：https://iclr.cc/virtual/2026/poster/10009058
- 本地 PDF：[打开](../../pdfs/ICLR/2026/iclr-2026-WGqibe5H3W__ResCP_Reservoir_Conformal_Prediction_for_Time_Series_Forecasting.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；Representation & Foundation Models / 表征与基础模型；Probabilistic Forecasting & Calibration / 概率预测与校准
- 技术方法标签：Uncertainty & Robustness / 不确定性与鲁棒性；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Conformal；conformal；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

05 0.0517 0.0492 0.0264±0.0002 .. ... ....±0.0005 Exchange ∆Cov 4.44±0.35 2.98±0.07 -0.57±1.58 0.82±1.89 4.57 3.25 1.46±0.18 PI-Width 0.0255±0.0005 0.0399±0.0001 0.0337±0.0016 0.0365±0.0013 0.0544 0.0509 0.0229±0.0001 Winkler 0.0300±0.0005 0.0479±0.0001 0.0480±0.0009 0.04

## 原始摘要

Conformal prediction offers a powerful framework for building distribution-free prediction intervals for exchangeable data.      Existing methods that extend conformal prediction to sequential data rely on fitting a relatively complex model to capture temporal dependencies.      However, these methods can fail if the sample size is small and often require expensive retraining when the underlying data distribution changes.      To overcome these limitations, we propose Reservoir Conformal Prediction (ResCP), a novel training-free conformal prediction method for time series.      Our approach leverages the efficiency and representation learning capabilities of reservoir computing to dynamically reweight conformity scores.      In particular, we compute similarity scores among reservoir states and use them to adaptively reweight the observed residuals at each step. With this approach, ResCP enables us to account for local temporal dynamics when modeling the error distribution without compromising computational scalability. We prove that, under reasonable assumptions, ResCP achieves asymptotic conditional coverage, and we empirically demonstrate its effectiveness across diverse forecasting tasks.
