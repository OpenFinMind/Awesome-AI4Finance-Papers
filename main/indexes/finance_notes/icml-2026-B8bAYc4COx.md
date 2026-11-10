# What if Tomorrow is the World Cup Final? Counterfactual Time Series Forecasting with Textual Conditions

ICML 2026 · main · application

实验使用汇率、宏观金融、信用评估或财务文档等金融相关基准。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=B8bAYc4COx
- 摘要来源：https://icml.cc/virtual/2026/poster/65690
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-B8bAYc4COx__What_if_Tomorrow_is_the_World_Cup_Final_Counterfactual_Time_Series_Forecasting_with_Textual_Conditions.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_benchmark
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测
- 技术方法标签：未明确标注
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Time series；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

1±0.22 81.38±0.15 ↓ MAE 0.15±0.00 0.14±0.00 0.14±0.00 0.21±0.00 0.15±0.00 0.22±0.00 0.23±0.01 0.12±0.00 0.15±0.01 Exchange ↓ MSE 0.04±0.00 0.04±0.00 0.04±0.00 0.10±0.00 0.04±0.00 0.08±0.00 0.10±0.01 0.04±0.00 0.04±0.00 ↑ DTTC-I 16.62±0.02 16.78±0.17 17.04±0.02 15.62±0.03 16.62±0.02 16.03±0.03 15.71±0.02 16.33±0.03 17.37±0.04 ↑ DTTC-E 204.90±0.17 208.68±0.67 206.49±0.31 212.13±0.12 204.64±0.10 184.25±1.58 199.23±1.38 209.12±0.33 216.03±3.11 ↓ MAE 0.26±0.00 0.19±

## 原始摘要

Time series forecasting has become increasingly critical in real-world scenarios, where future sequences are influenced not only by historical patterns but also by forthcoming events. In this context, forecasting must dynamically adapt to complex and stochastic future conditions, which introduces fundamental challenges in both forecasting and evaluation. Traditional methods typically rely on historical data or factual future conditions, while overlooking counterfactual scenarios. Furthermore, many existing approaches are restricted to simple structured conditions, limiting their ability to generalize to the real-world complexities. To address these gaps, we introduce the task of counterfactual time series forecasting with textual conditions, enabling more flexible and condition-aware forecasting. We propose a comprehensive evaluation framework that encompasses both factual and counterfactual settings, even in the absence of ground truth time series. Additionally, we present a novel text-attribution mechanism that distinguishes mutable from immutable factors, thereby improving forecast accuracy under sophisticated and stochastic textual conditions.
