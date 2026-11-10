# Adaptive Conformal Inference Under Distribution Shift

NeurIPS 2021 · main · application

正文包含金融领域数据、模型、实验或分领域评测。 主题：Market Prediction / 股价、收益与波动率预测。

- 官方论文页：https://openreview.net/forum?id=6vaActvpcp3
- 摘要来源：https://neurips.cc/virtual/2021/poster/28041
- 本地 PDF：[打开](../../pdfs/NeurIPS/2021/neurips-2021-6vaActvpcp3__Adaptive_Conformal_Inference_Under_Distribution_Shift.pdf)；版本：publisher_version
- 金融依据类型：fulltext_financial_domain_data_or_experiment
- 主方向：Market Prediction / 股价、收益与波动率预测
- 细分方向：Stock Movement & Returns / 股价方向与收益预测；Volatility & Tail Forecasts / 波动率与尾部预测
- 技术方法标签：Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：conformal
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Time Figure 1: Local coverage frequencies for adaptive conformal (blue), a non-adaptive method that holds ↵t = ↵ fixed (red), and an i.i.d. Bernoulli(0.1) sequence (grey) for the prediction of stock market volatility. The coloured dotted lines mark the average coverage obtained across all time points, while the black line indicates the target level of 1 ↵ = 0.9. Daily open prices were obtained from publicly available datasets published by The Wall Street Journal. The realized local coverage frequencies for the non-adaptive and adaptive conformal m

## 原始摘要

We develop methods for forming prediction sets in an online setting where the data generating distribution is allowed to vary over time in an unknown fashion. Our framework builds on ideas from conformal inference to provide a general wrapper that can be combined with any black box method that produces point predictions of the unseen label or estimated quantiles of its distribution. While previous conformal inference methods rely on the assumption that the data are exchangeable, our adaptive approach provably achieves the desired coverage frequency over long-time intervals irrespective of the true data generating process. We accomplish this by modelling the distribution shift as a learning problem in a single parameter whose optimal value is varying over time and must be continuously re-estimated. We test our method, adaptive conformal inference, on two real world datasets and find that its predictions are robust to visible and significant distribution shifts.
