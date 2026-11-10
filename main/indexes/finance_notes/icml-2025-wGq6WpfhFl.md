# Clipped SGD Algorithms for Performative Prediction: Tight Bounds for Stochastic Bias and Remedies

ICML 2025 · main · application

正文包含明确金融数据、金融任务或金融案例；金融应用可属于通用方法的一个实验。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=wGq6WpfhFl
- 摘要来源：https://icml.cc/virtual/2025/poster/43628
- 本地 PDF：[打开](../../pdfs/ICML/2025/icml-2025-wGq6WpfhFl__Clipped_SGD_Algorithms_for_Performative_Prediction_Tight_Bounds_for_Stochastic_Bias_and_Remedies.pdf)；版本：publisher_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Credit Scoring & Default / 信用评分与违约
- 技术方法标签：Uncertainty & Robustness / 不确定性与鲁棒性；Privacy & Federated Learning / 隐私与联邦学习；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：optimization
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

p̄a 1 θP S = − 1−aβ , where p̄ = m Z̃ i=1 i is the sample mean. GiveMeSomeCredit (Kaggle, 2011) with m = 15776 samples and d = 10 features. We split the training/test sets We set p = 0.1, ε = 0.1, δ = 1/m, β ∈ {0.01, 0.05}, a =

## 原始摘要

This paper studies the convergence of clipped stochastic gradient descent (SGD) algorithms with decision-dependent data distribution. Our setting is motivated by privacy preserving optimization algorithms that interact with performative data where the prediction models can influence future outcomes. This challenging setting involves the non-smooth clipping operator and non-gradient dynamics due to distribution shifts. We make two contributions in pursuit for a performative stable solution with these algorithms. First, we characterize the stochastic bias with projected clipped SGD (PCSGD) algorithm which is caused by the clipping operator that prevents PCSGD from reaching a stable solution. When the loss function is strongly convex, we quantify the lower and upper bounds for this stochastic bias and demonstrate a bias amplification phenomenon with the sensitivity of data distribution. When the loss function is non-convex, we bound the magnitude of stationarity bias. Second, we propose remedies to mitigate the bias either by utilizing an optimal step size design for PCSGD, or to apply the recent DiceSGD algorithm [Zhang et al., 2024]. Our analysis is also extended to show that the latter algorithm is free from stochastic bias in the performative setting. Numerical experiments verify our findings.
