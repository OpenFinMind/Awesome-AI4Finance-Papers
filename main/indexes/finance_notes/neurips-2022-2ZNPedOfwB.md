# Zeroth-Order Hard-Thresholding: Gradient Error vs. Expansivity

NeurIPS 2022 · main · application

包含明确的金融任务、金融领域数据或金融案例验证。 主题：Portfolio & Investment / 投资组合与投资管理。

- 官方论文页：https://openreview.net/forum?id=2ZNPedOfwB
- 摘要来源：https://neurips.cc/virtual/2022/poster/54390
- 本地 PDF：[打开](../../pdfs/NeurIPS/2022/neurips-2022-2ZNPedOfwB__Zeroth_Order_Hard_Thresholding_Gradient_Error_vs_Expansivity.pdf)；版本：publisher_version
- 金融依据类型：title_abstract_financial_task_or_data
- 主方向：Portfolio & Investment / 投资组合与投资管理
- 细分方向：Portfolio Selection & Optimization / 组合选择与优化
- 技术方法标签：Uncertainty & Robustness / 不确定性与鲁棒性；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：optimization
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Finally, we illustrate the utility of our method on a portfolio optimization problem as well as black-box adversarial attacks.

## 原始摘要

$\ell_0$ constrained optimization is prevalent in machine learning, particularly for high-dimensional problems, because it is a fundamental approach to achieve sparse learning. Hard-thresholding gradient descent is a dominant technique to solve this problem. However, first-order gradients of the objective function may be either unavailable or expensive to calculate in a lot of real-world problems, where zeroth-order (ZO) gradients could be a good surrogate. Unfortunately, whether ZO gradients can work with the hard-thresholding operator is still an unsolved problem.To solve this puzzle, in this paper, we focus on the $\ell_0$ constrained black-box stochastic optimization problems, and propose a new stochastic zeroth-order gradient hard-thresholding (SZOHT) algorithm with  a general ZO gradient estimator powered by a novel random support sampling. We provide the convergence analysis of SZOHT under standard assumptions.   Importantly, we   reveal a conflict between  the deviation of  ZO estimators and  the expansivity of the hard-thresholding operator,  and provide a theoretical   minimal value of the number of random directions in ZO gradients. In addition,  we find that the query complexity of SZOHT is independent or weakly dependent on the dimensionality under different settings.  Finally, we illustrate the utility of our method on a portfolio optimization problem as well as black-box adversarial attacks.
