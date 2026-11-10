# Dynamic TMoE: A Drift-Aware Dynamic Mixture of Experts Framework for Non-Stationary Time Series Forecasting

ICML 2026 · main · application

实验使用汇率、宏观金融、信用评估或财务文档等金融相关基准。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=JabkBcaoa9
- 摘要来源：https://icml.cc/virtual/2026/poster/64808
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-JabkBcaoa9__Dynamic_TMoE_A_Drift_Aware_Dynamic_Mixture_of_Experts_Framework_for_Non_Stationary_Time_Series_Forecastin.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_benchmark
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测
- 技术方法标签：Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/andone-07/Dynamic-TMoE.

## 纳入依据

0.293 0.271 0.311 0.240 0.272 0.249 0.277 0.258 0.281 0.259 0.287 0.267 0.317 0.309 0.360 Exchange 0.351 0.397 0.395 0.414 0.408 0.432 0.407 0.418 0.374 0.411 0.353 0.400 0.385 0.411 0.416 0.443 0.337 0.402 0.519 0.500 ETTh1 0.429 0.430 0.448 0.443 0.432 0.433 0.432 0.438 0.447 0.440 0.439 0.429 0.451 0.441 0.458 0.450 0.459 0.452 0.440 0.460

## 原始摘要

Non-stationary time series forecasting is challenged by evolving distribution shifts that static models struggle to capture. While Mixture-of-Experts (MoE) architectures offer a promising paradigm for decoupling complex drift patterns, existing approaches are limited by fixed expert pools and memoryless routing, hampering their ability to adapt to abrupt regime shifts. To address this, we propose **Dynamic TMoE**, a framework that unifies architectural evolution with temporal continuity during learning phase. By detecting distribution shifts via Maximum Mean Discrepancy (MMD), we dynamically instantiate heterogeneous experts and prune redundant ones to optimize capacity. Additionally, a temporal memory router leverages recurrent states and an anomaly repository to ensure stable, context-aware expert selection without requiring test-time updates. Experiments on nine benchmarks demonstrate state-of-the-art performance, reducing MSE by 10.4\% and MAE by 7.8\%. Code is available at https://github.com/andone-07/Dynamic-TMoE.
