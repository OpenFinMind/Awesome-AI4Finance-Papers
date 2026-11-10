# Fair Decisions from Calibrated Scores: Achieving Optimal Classification While Satisfying Sufficiency

ICML 2026 · main · application

正文包含明确金融数据、金融任务或金融案例；金融应用可属于通用方法的一个实验。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=XiD5RhcEDK
- 摘要来源：https://icml.cc/virtual/2026/poster/63370
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-XiD5RhcEDK__Fair_Decisions_from_Calibrated_Scores_Achieving_Optimal_Classification_While_Satisfying_Sufficiency.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Credit Scoring & Default / 信用评分与违约；Financial Risk / 金融风险管理
- 技术方法标签：Fairness & Recourse / 公平性与算法追索
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

erg et al., 2017). Nevertheless, among classifiers vided in Appendix I. that satisfy sufficiency, the extent to which separation is violated can vary. In this section, we adopt the deviation- 7.1. FICO from-separation measure ∆sep (R) introduced in (Benger & Ligett, 2025), and study classifiers that satisfy predictive FICO scores are used to predict creditworthiness. We use parity while minimizing ∆sep (R). We show that the optimal the aggregate score statistics from Barocas et al. (2023), classifier is attained on the bounda

## 原始摘要

Binary classification based on predicted probabilities (scores) is a fundamental task in supervised machine learning. While thresholding scores is Bayes-optimal in the unconstrained setting, using a single threshold generally violates statistical group fairness constraints. Under independence (statistical parity) and separation (equalized odds), such thresholding suffices when the scores already satisfy the corresponding criterion. However, this does not extend to sufficiency: even perfectly group-calibrated scores---including true class probabilities---violate predictive parity after thresholding. In this work, we present an exact solution for optimal binary (randomized) classification under sufficiency, assuming finite sets of group-calibrated scores. We provide a geometric characterization of the feasible pairs of positive predictive value (PPV) and false omission rate (FOR) achievable by such classifiers, and use it to derive a simple post-processing algorithm that attains the optimal classifier using only group-calibrated scores and group membership. Finally, since sufficiency and separation are generally incompatible, we identify the classifier that minimizes deviation from separation subject to sufficiency, and show that it can also be obtained by our algorithm, often achieving performance comparable to the optimum.
