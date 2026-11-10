# Expanding the Chaos: Neural Operator for Stochastic (Partial) Differential Equations

ICML 2026 · main · application

通用方法在金融任务、数据或明确案例上开展应用验证。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=uZWpKAqjEg
- 摘要来源：https://icml.cc/virtual/2026/poster/61011
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-uZWpKAqjEg__Expanding_the_Chaos_Neural_Operator_for_Stochastic_Partial_Differential_Equations.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_review
- 主方向：Time Series / 时间序列
- 细分方向：Causality & Dynamics / 序列因果与动力学
- 技术方法标签：Diffusion & Flow / 扩散与流模型；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：diffusion
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/EEthanShi/SDENO.

## 纳入依据

Empirically, we achieve competitive accuracy across several tasks, including standard SPDE benchmarks and SDE-based diffusion one-step image sampling, topological graph interpolation, financial extrapolation, parameter estimation, and manifold SDE flood forecasting.

## 原始摘要

Stochastic differential equations (SDEs) and stochastic partial differential equations (SPDEs) are fundamental for modeling stochastic dynamics across the natural sciences and modern machine learning. Learning their solution operators with deep learning models promises fast solvers and new perspectives on classical learning tasks. In this work, we build on Wiener--chaos expansions (WCE) to design neural operator (NO) architectures for SDEs and SPDEs: we project driving noise paths onto orthonormal Wick--Hermite features and use NO backbones to parameterize the corresponding chaos coefficients governed by deterministic equations, enabling reconstruction of S(P)DE solutions from the observed noise trajectories. Empirically, we achieve competitive accuracy across several tasks, including standard SPDE benchmarks and SDE-based diffusion one-step image sampling, topological graph interpolation, financial extrapolation, parameter estimation, and manifold SDE flood forecasting. We further explore a law-matching setting where the Brownian trajectories paired with training solutions are unobserved, and show that the proposed framework remains effective by sampling auxiliary Brownian paths from the prescribed noise prior. These results suggest WCE-based neural operators are a practical and scalable approach to learning SDE/SPDE solution operators across domains. Our source code can be found in https://github.com/EEthanShi/SDENO.
