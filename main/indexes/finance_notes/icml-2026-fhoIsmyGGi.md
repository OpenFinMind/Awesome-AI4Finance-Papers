# Decomposition-Based Modular Conformal Prediction for Two-Stage Modeling

ICML 2026 · main · application

通用方法在金融任务、数据或明确案例上开展应用验证。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=fhoIsmyGGi
- 摘要来源：https://icml.cc/virtual/2026/poster/62540
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-fhoIsmyGGi__Decomposition_Based_Modular_Conformal_Prediction_for_Two_Stage_Modeling.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_review
- 主方向：Time Series / 时间序列
- 细分方向：Financial Stochastic Processes / 金融随机过程
- 技术方法标签：Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Conformal；conformal
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Experiments on synthetic distribution shifts, as well as real-world supply chain and stock market data, demonstrate that our approach improves coverage under structural, stage-wise shifts compared to standard conformal methods, while identifying stage-wise error contribution.

## 原始摘要

Conformal prediction offers finite-sample coverage guarantees under minimal assumptions. However, existing methods treat the entire modeling process as a black box, overlooking opportunities to exploit and understand modular  structure. We introduce a conformal prediction framework for two-stage sequential models, where an upstream predictor generates intermediate representations for a downstream model. By decomposing the overall prediction residual into stage-specific components, our method enables practitioners to attribute uncertainty to specific pipeline stages. We develop a risk-controlled parameter selection procedure using family-wise error rate (FWER) control to calibrate stage-wise scaling parameters, and introduce an adaptive extension for non-stationary settings. Experiments on synthetic distribution shifts, as well as real-world supply chain and stock market data, demonstrate that our approach improves coverage under structural, stage-wise shifts compared to standard conformal methods, while identifying stage-wise error contribution. This framework offers diagnostic advantages and robust coverage that standard conformal methods lack.
