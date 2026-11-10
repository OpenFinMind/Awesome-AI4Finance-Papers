# $K^2$VAE: A Koopman-Kalman Enhanced Variational AutoEncoder for Probabilistic Time Series Forecasting

ICML 2025 · main · application

实验使用汇率、宏观金融、信用评估或财务文档等金融相关基准。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=71Mm8GDGYd
- 摘要来源：https://icml.cc/virtual/2025/poster/46346
- 本地 PDF：[打开](../../pdfs/ICML/2025/icml-2025-71Mm8GDGYd__K_2_VAE_A_Koopman_Kalman_Enhanced_Variational_AutoEncoder_for_Probabilistic_Time_Series_Forecasting.pdf)；版本：publisher_version
- 金融依据类型：fulltext_financial_benchmark
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；Generation & Simulation / 序列生成与仿真；Probabilistic Forecasting & Calibration / 概率预测与校准
- 技术方法标签：Generative Modeling / 生成建模；Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Time Series；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

eans and standard errors are based on 5 independent runs of retraining and evaluation. Red: the best, Blue: the 2nd best. Model Metric Exchange-S Solar-S Electricity-S Traffic-S ETTh1-S ETTh2-S ETTm1-S ETTm2-S CRPS 0.012±0.002 0.516±0.011 0.068±0.003 0.298±0.022 0.320±0.017 0.212±0.012 0.193±0.005 0.199±0.003 FITS NMAE 0.017±0.003 0.701±0.014 0.092±0.004 0.392±0.028 0.423±0.033 0.278±0.009 0.249±0.007 0.260±0.011

## 原始摘要

Probabilistic Time Series Forecasting (PTSF) plays a crucial role in decision-making across various fields, including economics, energy, and transportation. Most existing methods excell at short-term forecasting, while overlooking the hurdles of Long-term Probabilistic Time Series Forecasting (LPTSF). As the forecast horizon extends, the inherent nonlinear dynamics have a significant adverse effect on prediction accuracy, and make generative models inefficient by increasing the cost of each iteration. To overcome these limitations, we introduce $K^2$VAE, an efficient VAE-based generative model that leverages a KoopmanNet to transform nonlinear time series into a linear dynamical system, and devises a KalmanNet to refine predictions and model uncertainty in such linear system, which reduces error accumulation in long-term forecasting. Extensive experiments demonstrate that $K^2$VAE outperforms state-of-the-art methods in both short- and long-term PTSF, providing a more efficient and accurate solution.
