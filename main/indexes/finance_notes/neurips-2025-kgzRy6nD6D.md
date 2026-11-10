# Selective Learning for Deep Time Series Forecasting

NeurIPS 2025 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：Exchange benchmark (currency series)。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=kgzRy6nD6D
- 摘要来源：https://neurips.cc/virtual/2025/poster/116357
- 本地 PDF：[打开](../../pdfs/NeurIPS/2025/neurips-2025-kgzRy6nD6D__Selective_Learning_for_Deep_Time_Series_Forecasting.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；Anomaly Detection / 序列异常检测
- 技术方法标签：Transformer / Transformer模型；Uncertainty & Robustness / 不确定性与鲁棒性；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：optimization；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

learning. Full results of ETTh2 and ETTm1 are provided in Appendix G.1. ETTh1 ETTm2 Electricity Exchange Weather ILI Method MSE MAE MSE MAE MSE MAE MSE MAE MSE MAE MSE MAE Informer 1.289 0.917 1.485 0.919 0.342 0.420 1.520 0.985 0.337 0.374 4.953 1.544 +SL 0.538 0.534 0.494 0.527 0.292 0.386 0.814 0.712 0.273 0.299 3.997 1.360 ∆ -58.3% -41.8% -66.8% -42.6% -14.4% -8.21% -46.4% -27.8% -19.1

## 原始摘要

Benefiting from high capacity for capturing complex temporal patterns, deep learning (DL) has significantly advanced time series forecasting (TSF). However, deep models tend to suffer from severe overfitting due to the inherent vulnerability of time series to noise and anomalies. The prevailing DL paradigm uniformly optimizes all timesteps through the MSE loss and learns those uncertain and anomalous timesteps without difference, ultimately resulting in overfitting. To address this, we propose a novel selective learning strategy for deep TSF. Specifically, selective learning screens a subset of the whole timesteps to calculate the MSE loss in optimization, guiding the model to focus on generalizable timesteps while disregarding non-generalizable ones. Our framework introduces a dual-mask mechanism to target timesteps: (1) an uncertainty mask leveraging residual entropy to filter uncertain timesteps, and (2) an anomaly mask employing residual lower bound estimation to exclude anomalous timesteps. Extensive experiments across eight real-world datasets demonstrate that selective learning can significantly improve the predictive performance for typical state-of-the-art deep models, including 37.4% MSE reduction for Informer, 8.4% for TimesNet, and 6.5% for iTransformer.
