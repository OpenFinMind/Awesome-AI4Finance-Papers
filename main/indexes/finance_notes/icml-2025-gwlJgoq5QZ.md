# Slimming the Fat-Tail: Morphing-Flow for Adaptive Time Series Modeling

ICML 2025 · main · application

实验使用汇率、宏观金融、信用评估或财务文档等金融相关基准。 主题：Time Series / 时间序列；Market Prediction / 股价、收益与波动率预测。

- 官方论文页：https://openreview.net/forum?id=gwlJgoq5QZ
- 摘要来源：https://icml.cc/virtual/2025/poster/44444
- 本地 PDF：[打开](../../pdfs/ICML/2025/icml-2025-gwlJgoq5QZ__Slimming_the_Fat_Tail_Morphing_Flow_for_Adaptive_Time_Series_Modeling.pdf)；版本：publisher_version
- 金融依据类型：fulltext_financial_benchmark
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；Causality & Dynamics / 序列因果与动力学；FX & Crypto Forecasts / 汇率与加密资产预测
- 技术方法标签：Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

itor by 6.3% on average, achieving 21.7% gains fat-tailed distributions. on datasets with pronounced heavy-tailed behavior (e.g., Exchange-Rate). The MOF operates as a plug-and-play Visualization of the training process is shown in Figure 2. module, requiring no architectural modifications to existing The fat-tailed nature of Cauchy distributions (evident in the models. Q-Q plots and PDFs of Figure 2) has a significant impact on

## 原始摘要

Temporal sequences, even after stationarization, often exhibit leptokurtic distributions with fat tails and persistent distribution shifts. These properties destabilize feature dynamics, amplify model variance, and hinder model convergence in time series forecasting. To address this, we propose Morphing-Flow (MoF), a framework that combines a spline-based transform layer (Flow) and a test-time-trained method (Morph), which adaptively normalizes non-stationary, fat-tailed distributions while preserving critical extreme features. MoF ensures that inputs remain within a network’s effective activation space—a structured, normal-like distribution—even under distributional drift. Experiments across eight datasets show that MoF achieves state-of-the-art performance: With a simple linear backbone architecture, it matches the performance of state-of-the-art models on datasets such as Electricity and ETTh2. When paired with a patch-based Mamba architecture, MoF outperforms its closest competitor by 6.3% on average and reduces forecasting errors in fat-tailed datasets such as Exchange by 21.7%. Moreover, MoF acts as a plug-and-play module, boosting performance in existing models without architectural changes.
