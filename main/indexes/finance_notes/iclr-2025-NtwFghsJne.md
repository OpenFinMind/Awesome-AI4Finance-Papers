# From Search to Sampling: Generative Models for Robust Algorithmic Recourse

ICLR 2025 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：FICO。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=NtwFghsJne
- 摘要来源：https://iclr.cc/virtual/2025/poster/29854
- 本地 PDF：[打开](../../pdfs/ICLR/2025/iclr-2025-NtwFghsJne__From_Search_to_Sampling_Generative_Models_for_Robust_Algorithmic_Recourse.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Credit Scoring & Default / 信用评分与违约
- 技术方法标签：Generative Modeling / 生成建模；Fairness & Recourse / 公平性与算法追索；Uncertainty & Robustness / 不确定性与鲁棒性；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：optimization
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

n Figure 2. In this section we focus on real datasets. 5.1 E XPERIMENTAL S ETUP Datasets: We experimented with benchmark datasets commonly used to evaluate recourse al- gorithms: Adult Income (Becker & Kohavi, 1996), FICO HELOC (FICO, 2018), and COM- PAS (Angwin et al., 2016). These datasets contain a mix of continuous and categorical features. All continuous attributes are normalized to the range of [0, 1], while categorical attributes are one-hot encoded. We defer detailed descriptions of these datasets to Appendix C.1 and present a summary in Table 1. For each d

## 原始摘要

Algorithmic Recourse provides recommendations to individuals who are adversely impacted by automated model decisions, on how to alter their profiles to achieve a favorable outcome. Effective recourse methods must balance three conflicting goals: proximity to the original profile to minimize cost, plausibility for realistic recourse, and validity to ensure the desired outcome. We show that existing methods train for these objectives separately and then search for recourse through a joint optimization over the recourse goals during inference, leading to poor recourse recommendations. We introduce GenRe, a generative recourse model designed to train the three recourse objectives jointly. Training such generative models is non-trivial due to lack of direct recourse supervision. We propose efficient ways to synthesize such supervision and further show that GenRe's training leads to a consistent estimator. Unlike most prior methods, that employ non-robust gradient descent based search during inference, GenRe simply performs a forward sampling over the generative model to produce minimum cost recourse, leading to superior performance across multiple metrics. We also demonstrate GenRe provides the best trade-off between cost, plausibility and validity, compared to state-of-art baselines. We release anonymized code at: https://anonymous.4open.science/r/GenRe-BD71
