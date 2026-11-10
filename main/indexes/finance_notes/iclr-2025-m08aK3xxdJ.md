# CATCH: Channel-Aware Multivariate Time Series Anomaly Detection via Frequency Patching

ICLR 2025 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：Credit card。 主题：Time Series / 时间序列；Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=m08aK3xxdJ
- 摘要来源：https://iclr.cc/virtual/2025/poster/28489
- 本地 PDF：[打开](../../pdfs/ICLR/2025/iclr-2025-m08aK3xxdJ__CATCH_Channel_Aware_Multivariate_Time_Series_Anomaly_Detection_via_Frequency_Patching.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Anomaly Detection / 序列异常检测；Lending & Credit Data / 借贷与信贷数据应用
- 技术方法标签：Generative Modeling / 生成建模；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：optimization；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/decisionintelligence/CATCH.

## 纳入依据

Machine 38 2.08 1,416,825 708,420 Telemetry dataset collected from 28 different server machines at a large Internet company Creditcard Finance 29 0.17 284,807 142,404 Credit card dataset includes a subset of online transactions that occurred over two days GECCO Water treatment 9 1.25 138,521 69,261 Water quality dataset published in the GECCO Industrial Challenge SWAT Water treatment 51 5.78 944,919 449,919 Obtained from 51 sensors of the critical infrastructure

## 原始摘要

Anomaly detection in multivariate time series is challenging as heterogeneous subsequence anomalies may occur. Reconstruction-based methods, which focus on learning normal patterns in the frequency domain to detect diverse abnormal subsequences, achieve promising results, while still falling short on capturing fine-grained frequency characteristics and channel correlations. To contend with the limitations, we introduce CATCH, a framework based on frequency patching. We propose to patchify the frequency domain into frequency bands, which enhances its ability to capture fine-grained frequency characteristics. To perceive appropriate channel correlations, we propose a Channel Fusion Module (CFM), which features a patch-wise mask generator and a masked-attention mechanism. Driven by a bi-level multi-objective optimization algorithm, the CFM is encouraged to iteratively discover appropriate patch-wise channel correlations, and to cluster relevant channels while isolating adverse effects from irrelevant channels. Extensive experiments on 10 real-world datasets and 12 synthetic datasets demonstrate that CATCH achieves state-of-the-art performance. We make our code and datasets available at https://github.com/decisionintelligence/CATCH.
