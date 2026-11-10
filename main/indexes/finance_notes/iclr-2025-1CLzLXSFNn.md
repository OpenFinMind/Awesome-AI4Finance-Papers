# TimeMixer++: A General Time Series Pattern Machine for Universal Predictive Analysis

ICLR 2025 · main · application

正文包含金融领域数据、模型、实验或分领域评测。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=1CLzLXSFNn
- 摘要来源：https://iclr.cc/virtual/2025/poster/31219
- 本地 PDF：[打开](../../pdfs/ICLR/2025/iclr-2025-1CLzLXSFNn__TimeMixer_A_General_Time_Series_Pattern_Machine_for_Universal_Predictive_Analysis.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_domain_data_or_experiment
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；Representation & Foundation Models / 表征与基础模型；Generation & Simulation / 序列生成与仿真；Anomaly Detection / 序列异常检测；Imputation & Irregular Series / 缺失与不规则序列
- 技术方法标签：未明确标注
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Time series；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

ly 1 6 (23000, 0, 23000) Yearly 0.43 Demographic M4-Quarterly 1 8 (24000, 0, 24000) Quarterly 0.47 Finance M4-Monthly 1 18 (48000, 0, 48000) Monthly 0.44 Industry M4-Weakly 1 13 (359, 0, 359) Weakly 0.43 Macro M4-Daily 1 14 (4227, 0, 4227) Daily 0

## 原始摘要

Time series analysis plays a critical role in numerous applications, supporting tasks such as forecasting, classification, anomaly detection, and imputation. In this work, we present the time series pattern machine (TSPM), a model designed to excel in a broad range of time series tasks through powerful representation and pattern extraction capabilities. Traditional time series models often struggle to capture universal patterns, limiting their effectiveness across diverse tasks. To address this, we define multiple scales in the time domain and various resolutions in the frequency domain, employing various mixing strategies to extract intricate, task-adaptive time series patterns. Specifically, we introduce TimeMixer++, a general-purpose TSPM that processes multi-scale time series using (1) multi-resolution time imaging (MRTI), (2) time image decomposition (TID), (3) multi-scale mixing (MCM), and (4) multi-resolution mixing (MRM) to extract comprehensive temporal patterns. MRTI transforms multi-scale time series into multi-resolution time images, capturing patterns across both temporal and frequency domains. TID leverages dual-axis attention to extract seasonal and trend patterns, while MCM hierarchically aggregates these patterns across scales. MRM adaptively integrates all representations across resolutions. TimeMixer++ achieves state-of-the-art performance across 8 time series analytical tasks, consistently surpassing both general-purpose and task-specific models. Our work marks a promising step toward the next generation of TSPMs, paving the way for further advancements in time series analysis.
