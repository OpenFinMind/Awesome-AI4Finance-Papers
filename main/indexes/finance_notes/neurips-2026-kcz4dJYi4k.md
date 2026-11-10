# Counterfactual Online Conformal Prediction Under Adaptive Logging

NeurIPS 2026 · main · application

通用方法在金融任务、数据或明确案例上开展应用验证。 主题：Portfolio & Investment / 投资组合与投资管理。

- 官方论文页：https://openreview.net/forum?id=kcz4dJYi4k
- 摘要来源：https://neurips.cc/virtual/2026/poster/150109
- 本地 PDF：[打开](../../pdfs/NeurIPS/2026/neurips-2026-kcz4dJYi4k__Counterfactual_Online_Conformal_Prediction_Under_Adaptive_Logging.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_review
- 主方向：Portfolio & Investment / 投资组合与投资管理
- 细分方向：Investment Evaluation & Decisions / 投资评价与决策
- 技术方法标签：Reinforcement Learning / 强化学习；Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Conformal；conformal
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Experiments on synthetic decision tasks, open bandit data, and financial rebalancing show that PW-OCP and DR-OCP improve counterfactual coverage and downstream regret without sacrificing prediction-set sharpness.

## 原始摘要

Online conformal prediction can fail when predictions shape actions and actions determine which outcomes enter calibration. Standard adaptive methods may retain marginal coverage while systematically miscovering the counterfactual outcomes of rarely selected actions. This paper formalizes the failure through counterfactual coverage and introduces Propensity-Weighted Online Conformal Prediction, an inverse-propensity-weighted recursion that debiases calibration. A doubly robust variant further reduces nuisance bias to the product of outcome-model and propensity errors. Under positivity, the resulting coverage rate matches an information-theoretic lower bound up to logarithmic factors. Experiments on synthetic decision tasks, open bandit data, and financial rebalancing show that PW-OCP and DR-OCP improve counterfactual coverage and downstream regret without sacrificing prediction-set sharpness.
