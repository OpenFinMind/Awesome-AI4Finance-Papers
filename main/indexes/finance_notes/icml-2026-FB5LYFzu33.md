# Error Propagation in Dynamic Programming: From Stochastic Control to American Option Pricing

ICML 2026 · main · core

以金融任务或金融数据为核心研究对象。 主题：Derivatives & Hedging / 衍生品定价与对冲。

- 官方论文页：https://openreview.net/forum?id=FB5LYFzu33
- 摘要来源：https://icml.cc/virtual/2026/poster/65273
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-FB5LYFzu33__Error_Propagation_in_Dynamic_Programming_From_Stochastic_Control_to_American_Option_Pricing.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_review
- 主方向：Derivatives & Hedging / 衍生品定价与对冲
- 细分方向：Option Pricing & PDEs / 期权定价与PDE
- 技术方法标签：Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Finally, we illustrate how our analysis naturally applies to a key financial application: the pricing of American options.

## 原始摘要

This paper investigates theoretical and methodological foundations for stochastic optimal control (SOC) in discrete time. We start formulating the control problem in a general dynamic programming framework, introducing the mathematical structure needed for a detailed convergence analysis. The associate value function is estimated through a sequence of approximations combining nonparametric regression methods and Monte Carlo subsampling. The regression step is performed within reproducing kernel Hilbert spaces (RKHSs), exploiting the classical KRR algorithm, while Monte Carlo sampling methods are introduced to estimate the continuation value. To assess the accuracy of our value function estimator, we propose a natural error decomposition and rigorously control the resulting error terms at each time step. We then analyze how this error propagates backward in time-from maturity to the initial stage-a relatively underexplored aspect of the SOC literature. Finally, we illustrate how our analysis naturally applies to a key financial application: the pricing of American options.
