# Kernel-based Optimally Weighted Conformal Time-Series Prediction

ICLR 2025 · main · application

正文包含金融数据、金融训练数据、金融任务评测或具体金融场景案例。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=oP7arLOWix
- 摘要来源：https://iclr.cc/virtual/2025/poster/28361
- 本地 PDF：[打开](../../pdfs/ICLR/2025/iclr-2025-oP7arLOWix__Kernel_based_Optimally_Weighted_Conformal_Time_Series_Prediction.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Probabilistic Forecasting & Calibration / 概率预测与校准
- 技术方法标签：Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Conformal；conformal
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

eves the narrowest intervals while maintaining valid coverage. For qualitative explanations, we also include Figure A.3 that demonstrates the performance of KOWCPI, SPCI, and ACI on the Solar dataset. C.2 AAPL daily stock price We compare KOWCPI with baseline methods using Apple’s daily closing stock price data from January 1, 2020, to December 12, 2022. This publicly available dataset can be accessed on Kaggle (https: //www.kaggle.com/datasets/paultimothymooney/stock-market-data). The goal is to construct confidence intervals for the daily closing prices. The first

## 原始摘要

Conformal prediction has been a popular distribution-free framework for uncertainty quantification. In this work, we present a novel conformal prediction method for time-series, which we call Kernel-based Optimally Weighted Conformal Prediction Intervals ($\texttt{KOWCPI}$). Specifically, $\texttt{KOWCPI}$ adapts the classic Reweighted Nadaraya-Watson (RNW) estimator for quantile regression on dependent data and learns optimal data-adaptive weights. Theoretically, we tackle the challenge of establishing a conditional coverage guarantee for non-exchangeable data under strong mixing conditions on the non-conformity scores. We demonstrate the superior performance of $\texttt{KOWCPI}$ on real time-series against state-of-the-art methods, where $\texttt{KOWCPI}$ achieves narrower confidence intervals without losing coverage.
