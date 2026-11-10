# Identifiable Markov Switching Models with Instantaneous Effects and Exponential Families

ICML 2026 · main · application

通用方法在金融任务、数据或明确案例上开展应用验证。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=IjrmQgIvHU
- 摘要来源：https://icml.cc/virtual/2026/poster/64905
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-IjrmQgIvHU__Identifiable_Markov_Switching_Models_with_Instantaneous_Effects_and_Exponential_Families.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_review
- 主方向：Time Series / 时间序列
- 细分方向：Causality & Dynamics / 序列因果与动力学
- 技术方法标签：Causal Learning / 因果学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：causal；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Experiments on synthetic benchmarks and a financial economics dataset demonstrate the effectiveness of our approach to detect latent regimes and discover causal structures from non-stationary time series.

## 原始摘要

Temporal systems often exhibit non-stationary behaviour, such as seasonal climate variation or glucose fluctuations in patients with type-1 diabetes.  One way to model non-stationarity is through discrete latent *regimes*, *i.e.*, stationary segments of time.  Such systems induce a *Markov Switching Model* (MSM), a class of Hidden Markov Models with autoregressive dependencies among latent regimes and observed variables.  Identifying latent regimes is challenging in the presence of frequent regime switches and nonlinear and non-Gaussian dynamics, particularly when there are *instantaneous effects* between the variables, *e.g.*, due to slow rates of measurements. In this work, we establish the identifiability of both latent regimes and regime-dependent causal structures under temporal regime dependencies, nonlinear lagged and instantaneous effects, and independent noise from the exponential family. Our identifiability theory subsumes non-temporal mixtures of causal models.  Furthermore, we introduce $\texttt{FlowMSM}$, a regime detection framework that can be paired with any stationary causal discovery method to recover regime-dependent causal structures.  Experiments on synthetic benchmarks and a financial economics dataset demonstrate the effectiveness of our approach to detect latent regimes and discover causal structures from non-stationary time series.
