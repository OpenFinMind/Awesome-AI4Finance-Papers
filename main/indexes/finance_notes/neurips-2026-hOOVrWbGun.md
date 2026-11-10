# Online Decision-Focused Learning under Semi-Bandit Feedback

NeurIPS 2026 · main · application

官方摘要明确报告 portfolio 组合优化基准上的实验；属于通用决策学习方法的金融应用。 主题：Portfolio & Investment / 投资组合与投资管理。

- 官方论文页：https://openreview.net/forum?id=hOOVrWbGun
- 摘要来源：https://neurips.cc/Downloads/2026
- PDF 状态：access_blocked
- 金融依据类型：official_abstract_financial_experiment
- 主方向：Portfolio & Investment / 投资组合与投资管理
- 细分方向：Portfolio Selection & Optimization / 组合选择与优化
- 技术方法标签：Reinforcement Learning / 强化学习；Uncertainty & Robustness / 不确定性与鲁棒性；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Bayesian；optimization
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Decision-focused learning (DFL) improves on the Predict-then-optimize (PtO) pipeline by training predictive models to minimize decision regret rather than prediction loss. Most DFL methods assume offline full-feedback data with complete action cost vectors. Many real-world decision systems instead operate in an online setting: in each round, the agent acts using past feedback and observes costs only for the selected components, yielding semi-bandit feedback. Bandit methods optimize regret in this regime, but train models with predictive updates rather than decision-focused updates.  In this paper, we formalize online semi-bandit DFL: decision-focused learning for online optimization problems with semi-bandit feedback. The most straightforward extension would impute unobserved components with the model's own predictions and compute the decision-focused gradient. But this creates a self-confirming imputation degeneracy: imputation errors can flip counterfactual decisions that define the decision-focused gradient, biasing the representation update and reinforcing errors in later imputations. To address this degeneracy, we propose BayesianSPO, which combines an analytically updated Bayesian last-layer head with masked decision-focused learning. The Bayesian head supplies both (i) uncertainty to balance exploration and exploitation and (ii) stable imputations for unobserved components, while masking unobserved component gradients prevents those imputations from directly corrupting the representation update. Across knapsack, shortest-path, and portfolio benchmarks, BayesianSPO achieves the lowest mean cumulative regret on all five instances and the improvement is statistically significant on four of them.

## 原始摘要

Decision-focused learning (DFL) improves on the Predict-then-optimize (PtO) pipeline by training predictive models to minimize decision regret rather than prediction loss. Most DFL methods assume offline full-feedback data with complete action cost vectors. Many real-world decision systems instead operate in an online setting: in each round, the agent acts using past feedback and observes costs only for the selected components, yielding semi-bandit feedback. Bandit methods optimize regret in this regime, but train models with predictive updates rather than decision-focused updates.  In this paper, we formalize online semi-bandit DFL: decision-focused learning for online optimization problems with semi-bandit feedback. The most straightforward extension would impute unobserved components with the model's own predictions and compute the decision-focused gradient. But this creates a self-confirming imputation degeneracy: imputation errors can flip counterfactual decisions that define the decision-focused gradient, biasing the representation update and reinforcing errors in later imputations. To address this degeneracy, we propose BayesianSPO, which combines an analytically updated Bayesian last-layer head with masked decision-focused learning. The Bayesian head supplies both (i) uncertainty to balance exploration and exploitation and (ii) stable imputations for unobserved components, while masking unobserved component gradients prevents those imputations from directly corrupting the representation update. Across knapsack, shortest-path, and portfolio benchmarks, BayesianSPO achieves the lowest mean cumulative regret on all five instances and the improvement is statistically significant on four of them.
