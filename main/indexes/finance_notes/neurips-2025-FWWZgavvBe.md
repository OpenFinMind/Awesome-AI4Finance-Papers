# Beyond the Average: Distributional Causal Inference under Imperfect Compliance

NeurIPS 2025 · main · application

包含明确的金融任务、金融领域数据或金融案例验证。 主题：Insurance & Actuarial / 保险与精算。

- 官方论文页：https://openreview.net/forum?id=FWWZgavvBe
- 摘要来源：https://neurips.cc/virtual/2025/poster/119035
- 本地 PDF：[打开](../../pdfs/NeurIPS/2025/neurips-2025-FWWZgavvBe__Beyond_the_Average_Distributional_Causal_Inference_under_Imperfect_Compliance.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_financial_task_or_data
- 主方向：Insurance & Actuarial / 保险与精算
- 细分方向：Insurance & Claims / 承保与理赔
- 技术方法标签：Causal Learning / 因果学习；Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Simulation results demonstrate favorable finite-sample performance, and we demonstrate the method’s practical relevance in an application to the Oregon Health Insurance Experiment.

## 原始摘要

We study the estimation of distributional treatment effects in randomized experiments with imperfect compliance. When participants do not adhere to their assigned treatments, we leverage treatment assignment as an instrumental variable to identify the local distributional treatment effect—the difference in outcome distributions between treatment and control groups for the subpopulation of compliers. We propose a regression-adjusted estimator based on a distribution regression framework with Neyman-orthogonal moment conditions, enabling robustness and flexibility with high-dimensional covariates. Our approach accommodates continuous, discrete, and mixed discrete-continuous outcomes, and applies under a broad class of covariate-adaptive randomization schemes, including stratified block designs and simple random sampling. We derive the estimator’s asymptotic distribution and show that it achieves the semiparametric efficiency bound. Simulation results demonstrate favorable finite-sample performance, and we demonstrate the method’s practical relevance in an application to the Oregon Health Insurance Experiment.
