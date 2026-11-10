# A Surrogate Objective Framework for Prediction+Programming with Soft Constraints

NeurIPS 2021 · main · application

通用方法在金融任务、数据或明确案例上开展应用验证。 主题：Portfolio & Investment / 投资组合与投资管理。

- 官方论文页：https://openreview.net/forum?id=9Sa2xh4mGR
- 摘要来源：https://neurips.cc/virtual/2021/poster/26621
- 本地 PDF：[打开](../../pdfs/NeurIPS/2021/neurips-2021-9Sa2xh4mGR__A_Surrogate_Objective_Framework_for_Prediction_Programming_with_Soft_Constraints.pdf)；版本：publisher_version
- 金融依据类型：title_abstract_review
- 主方向：Portfolio & Investment / 投资组合与投资管理
- 细分方向：Portfolio Selection & Optimization / 组合选择与优化
- 技术方法标签：Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：optimization
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

We evaluate our method in three applications extended with soft constraints: synthetic linear programming, portfolio optimization, and resource provisioning, demonstrating that our method outperforms traditional two-staged methods and other decision-focused approaches

## 原始摘要

Prediction+optimization is a common real-world paradigm where we have to predict problem parameters before solving the optimization problem. However, the criteria by which the prediction model is trained are often inconsistent with the goal of the downstream optimization problem.  Recently, decision-focused prediction approaches, such as SPO+ and direct optimization, have been proposed to fill this gap.  However, they cannot directly handle the soft constraints with the max operator required in many real-world objectives.  This paper proposes a novel analytically differentiable surrogate objective framework for real-world linear and semi-definite negative quadratic programming problems with soft linear and non-negative hard constraints. This framework gives the theoretical bounds on constraints’ multipliers, and derives the closed-form solution with respect to predictive parameters and thus gradients for any variable in the problem.  We evaluate our method in three applications extended with soft constraints: synthetic linear programming, portfolio optimization, and resource provisioning, demonstrating that our method outperforms traditional two-staged methods and other decision-focused approaches
