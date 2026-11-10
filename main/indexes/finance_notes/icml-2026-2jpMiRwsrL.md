# A Penalty Approach For Differentiation Through Black-box Quadratic Programming Solvers

ICML 2026 · main · application

通用方法在金融任务、数据或明确案例上开展应用验证。 主题：Portfolio & Investment / 投资组合与投资管理。

- 官方论文页：https://openreview.net/forum?id=2jpMiRwsrL
- 摘要来源：https://icml.cc/virtual/2026/poster/66543
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-2jpMiRwsrL__A_Penalty_Approach_For_Differentiation_Through_Black_box_Quadratic_Programming_Solvers.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_review
- 主方向：Portfolio & Investment / 投资组合与投资管理
- 细分方向：Portfolio Selection & Optimization / 组合选择与优化
- 技术方法标签：Uncertainty & Robustness / 不确定性与鲁棒性；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：optimization
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/mmmmmmlinghu/dXPP.

## 纳入依据

We evaluate dXPP on various tasks, including randomly generated QPs, large-scale sparse projection problems, and a real-world multi-period portfolio optimization task.

## 原始摘要

Differentiating through the solution of a quadratic program (QP) is a central problem in differentiable optimization. Most existing approaches differentiate through the Karush--Kuhn--Tucker (KKT) system, but their computational cost and numerical robustness can degrade at scale. To address these limitations, we propose dXPP, a penalty-based differentiation framework that decouples QP solving from differentiation. In the solving step (forward pass), dXPP is solver-agnostic and can leverage any black-box QP solver. In the differentiation step (backward pass), we map the solution to a smooth approximate penalty problem and implicitly differentiate through it, requiring only the solution of a much smaller linear system in the primal variables. This approach bypasses the difficulties inherent in explicit KKT differentiation and significantly improves computational efficiency and robustness. We evaluate dXPP on various tasks, including randomly generated QPs, large-scale sparse projection problems, and a real-world multi-period portfolio optimization task. Empirical results demonstrate that dXPP is competitive with KKT-based differentiation methods and achieves substantial speedups on large-scale problems. Our implementation is open source and available at https://github.com/mmmmmmlinghu/dXPP.
