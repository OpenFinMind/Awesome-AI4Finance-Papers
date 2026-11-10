# Deep FlexQP: Accelerated Nonlinear Programming via Deep Unfolding

ICLR 2026 · main · application

通用方法在金融任务、数据或明确案例上开展应用验证。 主题：Portfolio & Investment / 投资组合与投资管理。

- 官方论文页：https://openreview.net/forum?id=HL3TvE4Afm
- 摘要来源：https://iclr.cc/virtual/2026/poster/10010399
- 本地 PDF：[打开](../../pdfs/ICLR/2026/iclr-2026-HL3TvE4Afm__Deep_FlexQP_Accelerated_Nonlinear_Programming_via_Deep_Unfolding.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_review
- 主方向：Portfolio & Investment / 投资组合与投资管理
- 细分方向：Portfolio Selection & Optimization / 组合选择与优化
- 技术方法标签：Uncertainty & Robustness / 不确定性与鲁棒性；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：fine-tuning；optimization
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Deep FlexQP outperforms state-of-the-art learned QP solvers on a suite of benchmarks including portfolio optimization, classification, and regression problems, and scales to dense QPs with over 10k variables and constraints via fine-tuning.

## 原始摘要

We propose FlexQP, an always-feasible convex quadratic programming (QP) solver based on an $\ell_1$ elastic relaxation of the QP constraints. If the original constraints are feasible, FlexQP provably recovers the optimal solution. If the constraints are infeasible, FlexQP identifies a solution that minimizes the constraint violation while keeping the number of violated constraints sparse. Such infeasibilities arise naturally in sequential quadratic programming (SQP) subproblems due to the linearization of the constraints. We prove the convergence of FlexQP under mild coercivity assumptions, making it robust to both feasible and infeasible QPs. We then apply deep unfolding to learn LSTM-based, dimension-agnostic feedback policies for the algorithm parameters, yielding an accelerated Deep FlexQP. To preserve the exactness guarantees of the relaxation, we propose a normalized training loss that incorporates the Lagrange multipliers. We additionally design a log-scaled loss for PAC-Bayes generalization bounds that yields substantially tighter performance certificates, which we use to construct an accelerated SQP solver with guaranteed QP subproblem performance. Deep FlexQP outperforms state-of-the-art learned QP solvers on a suite of benchmarks including portfolio optimization, classification, and regression problems, and scales to dense QPs with over 10k variables and constraints via fine-tuning. When deployed within SQP, our approach solves nonlinear trajectory optimization problems 4-16x faster than SQP with OSQP while substantially improving success rates. On predictive safety filter problems, Deep FlexQP reduces safety violations by over 70\% and increases task completion by 43\% compared to existing methods.
