# Decision Making under the Exponential Family: Distributionally Robust Optimisation with Bayesian Ambiguity Sets

ICML 2025 · main · application

通用方法在金融任务、数据或明确案例上开展应用验证。 主题：Portfolio & Investment / 投资组合与投资管理。

- 官方论文页：https://openreview.net/forum?id=r9HlTuCQfr
- 摘要来源：https://icml.cc/virtual/2025/poster/43906
- 本地 PDF：[打开](../../pdfs/ICML/2025/icml-2025-r9HlTuCQfr__Decision_Making_under_the_Exponential_Family_Distributionally_Robust_Optimisation_with_Bayesian_Ambiguity.pdf)；版本：publisher_version
- 金融依据类型：title_abstract_review
- 主方向：Portfolio & Investment / 投资组合与投资管理
- 细分方向：Investment Evaluation & Decisions / 投资评价与决策
- 技术方法标签：Uncertainty & Robustness / 不确定性与鲁棒性；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Bayesian
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Our DRO-BAS formulations outperform existing Bayesian DRO on the Newsvendor problem and achieve faster solve times with comparable robustness on the Portfolio problem.

## 原始摘要

Decision making under uncertainty is challenging as the data-generating process (DGP) is often unknown. Bayesian inference proceeds by estimating the DGP through posterior beliefs on the model’s parameters. However, minimising the expected risk under these beliefs can lead to suboptimal decisions due to model uncertainty or limited, noisy observations. To address this, we introduce Distributionally Robust Optimisation with Bayesian Ambiguity Sets (DRO-BAS) which hedges against model uncertainty by optimising the worst-case risk over a posterior-informed ambiguity set. We provide two such sets, based on the posterior expectation (DRO-BAS(PE)) or the posterior predictive (DRO-BAS(PP)) and prove that both admit, under conditions, strong dual formulations leading to efficient single-stage stochastic programs which are solved with a sample average approximation. For DRO-BAS(PE), this covers all conjugate exponential family members while for DRO-BAS(PP) this is shown under conditions on the predictive's moment generating function. Our DRO-BAS formulations outperform existing Bayesian DRO on the Newsvendor problem and achieve faster solve times with comparable robustness on the Portfolio problem.
