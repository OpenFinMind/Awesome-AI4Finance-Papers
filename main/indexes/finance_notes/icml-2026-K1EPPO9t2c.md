# Loss-aware distributionally robust optimization via trainable optimal transport ambiguity sets

ICML 2026 · main · application

通用方法在金融任务、数据或明确案例上开展应用验证。 主题：Portfolio & Investment / 投资组合与投资管理。

- 官方论文页：https://openreview.net/forum?id=K1EPPO9t2c
- 摘要来源：https://icml.cc/virtual/2026/poster/64772
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-K1EPPO9t2c__Loss_aware_distributionally_robust_optimization_via_trainable_optimal_transport_ambiguity_sets.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_review
- 主方向：Portfolio & Investment / 投资组合与投资管理
- 细分方向：Portfolio Selection & Optimization / 组合选择与优化
- 技术方法标签：Uncertainty & Robustness / 不确定性与鲁棒性；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：optimization
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

We present experiments validating our method on standard portfolio optimization and linear regression tasks.

## 原始摘要

Optimal-transport distributionally robust optimization (OT-DRO) robustifies data-driven decision-making under uncertainty by capturing the sampling-induced statistical error via optimal transport ambiguity sets. The standard OT-DRO pipeline consists of a two-step procedure, where the ambiguity set is first designed and subsequently embedded into the downstream OT-DRO problem. However, this separation between uncertainty quantification and optimization may lead to excessive conservatism. We introduce an end-to-end pipeline to automatically learn decision-focused ambiguity sets for OT-DRO problems, where the loss function informs the shape of the ambiguity set, leading to less conservative decisions whose distributional robustness is enforced via data-driven bootstrapping. We formulate the learning problem as a bilevel optimization program and solve it via a hypergradient-based method. By leveraging the recently introduced nonsmooth conservative implicit function theorem, we establish convergence to a critical point of the bilevel problem. We present experiments validating our method on standard portfolio optimization and linear regression tasks.
