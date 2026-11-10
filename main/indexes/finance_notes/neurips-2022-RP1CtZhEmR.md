# Generating multivariate time series with COmmon Source CoordInated GAN (COSCI-GAN)

NeurIPS 2022 · main · application

通用方法在金融任务、数据或明确案例上开展应用验证。 主题：Time Series / 时间序列；Financial Safety & Compliance / 金融安全与合规。

- 官方论文页：https://openreview.net/forum?id=RP1CtZhEmR
- 摘要来源：https://neurips.cc/virtual/2022/poster/54727
- 本地 PDF：[打开](../../pdfs/NeurIPS/2022/neurips-2022-RP1CtZhEmR__Generating_multivariate_time_series_with_COmmon_Source_CoordInated_GAN_COSCI_GAN.pdf)；版本：publisher_version
- 金融依据类型：title_abstract_review
- 主方向：Time Series / 时间序列
- 细分方向：Generation & Simulation / 序列生成与仿真；Trust, Compliance & Bias / 可信、合规与偏差审计
- 技术方法标签：Generative Modeling / 生成建模
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Generating multivariate time series is a promising approach for sharing sensitive data in many medical, financial, and IoT applications. / We demonstrate empirically that our method helps preserve channel/feature correlations and that our synthetic data performs very well in downstream tasks with medical and financial data.

## 原始摘要

Generating multivariate time series is a promising approach for sharing sensitive data in many medical, financial, and IoT applications. A common type of multivariate time series originates from a single source such as the biometric measurements from a medical patient. This leads to complex dynamical patterns between individual time series that are hard to learn by typical generation models such as GANs. There is valuable information in those patterns that machine learning models can use to better classify, predict or perform other downstream tasks. We propose a novel framework that takes time series’ common origin into account and favors channel/feature relationships preservation. The two key points of our method are: 1) the individual time series are generated from a common point in latent space and 2) a central discriminator favors the preservation of inter-channel/feature dynamics. We demonstrate empirically that our method helps preserve channel/feature correlations and that our synthetic data performs very well in downstream tasks with medical and financial data.
