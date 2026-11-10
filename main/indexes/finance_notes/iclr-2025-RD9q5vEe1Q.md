# Error-quantified Conformal Inference for Time Series

ICLR 2025 · main · application

正文包含金融数据、金融训练数据、金融任务评测或具体金融场景案例。 主题：Time Series / 时间序列；Market Prediction / 股价、收益与波动率预测。

- 官方论文页：https://openreview.net/forum?id=RD9q5vEe1Q
- 摘要来源：https://iclr.cc/virtual/2025/poster/29659
- 本地 PDF：[打开](../../pdfs/ICLR/2025/iclr-2025-RD9q5vEe1Q__Error_quantified_Conformal_Inference_for_Time_Series.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Probabilistic Forecasting & Calibration / 概率预测与校准；Stock Movement & Returns / 股价方向与收益预测
- 技术方法标签：Uncertainty & Robustness / 不确定性与鲁棒性；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Conformal；conformal；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

riginal papers and open-source codes. Overview of experimental results. We have conducted extensive experiments, including stock data in Section 4.2, electricity data in Section 4.3, climate data in Section 4.4, syn- thetic data in Section 4.5, and ablation study of hyperparameters in Section D. Experimen- tal results with Transformer as the base model can be found in Section F. More com- prehensive experimental results and discussion on the scorecaster and learning rates can be found in Section G. Our code is available at https://github.com/creator-xi/ Error-quantified-Conformal-Inference. 4.2 R ESULTS IN FINANCE DOMAIN We consider the uncertainty problem of forecasting stock prices, including Amazon (AMZN) and Google (GOOGL), collected over

## 原始摘要

Uncertainty quantification in time series prediction is challenging due to the temporal dependence and distribution shift on sequential data. Conformal prediction provides a pivotal and flexible instrument for assessing the uncertainty of machine learning models through prediction sets. Recently, a series of online conformal inference methods updated thresholds of prediction sets by performing online gradient descent on a sequence of quantile loss functions. A drawback of such methods is that they only use the information of revealed non-conformity scores via miscoverage indicators but ignore error quantification, namely the distance between the non-conformity score and the current threshold. To accurately leverage the dynamic of miscoverage error, we propose Error-quantified Conformal Inference (ECI) by smoothing the quantile loss function. ECI introduces a continuous and adaptive feedback scale with the miscoverage error, rather than simple binary feedback in existing methods. We establish a long-term coverage guarantee for ECI under arbitrary dependence and distribution shift. The extensive experimental results show that ECI can achieve valid miscoverage control and output tighter prediction sets than other baselines.
