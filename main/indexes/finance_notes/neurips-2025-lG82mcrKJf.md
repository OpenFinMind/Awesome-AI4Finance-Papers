# Fortifying Time Series: DTW-Certified Robust Anomaly Detection

NeurIPS 2025 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：CREDITCARD。 主题：Time Series / 时间序列；Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=lG82mcrKJf
- 摘要来源：https://neurips.cc/virtual/2025/poster/116296
- 本地 PDF：[打开](../../pdfs/NeurIPS/2025/neurips-2025-lG82mcrKJf__Fortifying_Time_Series_DTW_Certified_Robust_Anomaly_Detection.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；Anomaly Detection / 序列异常检测；Lending & Credit Data / 借贷与信贷数据应用
- 技术方法标签：Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

44 0.830 0.227 2.242 0.196 71.05% COUTA 0.192 0.900 0.003 0.300 0.232 0.450 0.046 99.86% NIPS-TS-CREDITCARD TimesNet 0.422 0.942 0.450 0.846 0.028 0.262 0.035 51.75% DeepSVDDTS 0.132 0.772 0.119 0.719 0.105 0.817 0.056 91.55% COUTA 0.515 0.537 0.598 0.989 0.070 0.359 0.034 95.18% NIPS-TS-WATER TimesNet 0.778 0.997

## 原始摘要

Time-series anomaly detection is critical for ensuring safety in high-stakes applications, where robustness is a fundamental requirement rather than a mere performance metric. Addressing the vulnerability of these systems to adversarial manipulation is therefore essential. Existing defenses are largely heuristic or provide certified robustness only under $\ell_p$-norm constraints, which are incompatible with time-series data. In particular, $\ell_p$-norm fails to capture the intrinsic temporal structure in time series, causing small temporal distortions to significantly alter the $\ell_p$-norm measures. Instead, the similarity metric Dynamic Time Warping (DTW) is more suitable and widely adopted in the time-series domain, as DTW accounts for temporal alignment and remains robust to temporal variations. To date, however, there has been no certifiable robustness result in this metric that provides guarantees. In this work, we introduce the first DTW-certified robust defense in time-series anomaly detection by adapting the randomized smoothing paradigm. We develop this certificate by bridging the $\ell_p$-norm to DTW distance through a lower-bound transformation. Extensive experiments across various datasets and models validate the effectiveness and practicality of our theoretical approach. Results demonstrate significantly improved performance, e.g., up to 18.7\% in F1-score under DTW-based adversarial attacks compared to traditional certified models.
