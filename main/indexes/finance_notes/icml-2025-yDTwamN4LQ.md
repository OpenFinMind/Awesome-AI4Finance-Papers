# Learning with Expected Signatures: Theory and Applications

ICML 2025 · main · application

正文包含金融领域数据、模型、实验或分领域评测。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=yDTwamN4LQ
- 摘要来源：https://icml.cc/virtual/2025/poster/43548
- 本地 PDF：[打开](../../pdfs/ICML/2025/icml-2025-yDTwamN4LQ__Learning_with_Expected_Signatures_Theory_and_Applications.pdf)；版本：publisher_version
- 金融依据类型：fulltext_financial_domain_data_or_experiment
- 主方向：Time Series / 时间序列
- 细分方向：General Time-Series Methods / 综合序列方法
- 技术方法标签：Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

H -D EPENDENT D ERIVATIVES Figure 2. Distributions of expected signature estimators for BM. The next application we consider is a purely financial one. The y-axis is in log-scale. The objective is to price (and hedge) path-dependent deriva- tives by decomposing them into a set of atomic Arrow- 10 In both simulations we fix T = 1 and consider π to be uniform Debreu-like securities. Let X = {Xt , t ∈ [0, T ]} be a price with mesh |π| = 2−⌊N/10⌋+1 . This choice ensures the sequences process, i.e. a semimartingale over some probability space. of partitions are signature-defining for both processes

## 原始摘要

The expected signature maps a collection of data streams to a lower dimensional representation, with a remarkable property: the resulting feature tensor can fully characterize the data generating distribution. This "model-free"' embedding has been successfully leveraged to build multiple domain-agnostic machine learning (ML) algorithms for time series and sequential data. The convergence results proved in this paper bridge the gap between the expected signature's empirical discrete-time estimator and its theoretical continuous-time value, allowing for a more complete probabilistic interpretation of expected signature-based ML methods. Moreover, when the data generating process is a martingale, we suggest a simple modification of the expected signature estimator with significantly lower mean squared error and empirically demonstrate how it can be effectively applied to improve predictive performance.
