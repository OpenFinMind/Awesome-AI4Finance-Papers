# Beyond the convexity assumption: Realistic tabular data generation under quantifier-free real linear constraints

ICLR 2025 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：Heloc。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=rx0TCew0Lj
- 摘要来源：https://iclr.cc/virtual/2025/poster/28159
- 本地 PDF：[打开](../../pdfs/ICLR/2025/iclr-2025-rx0TCew0Lj__Beyond_the_convexity_assumption_Realistic_tabular_data_generation_under_quantifier_free_real_linear_const.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Credit Scoring & Default / 信用评分与违约
- 技术方法标签：Generative Modeling / 生成建模；Tabular Learning / 表格学习；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

build our DRL on top of each to create DGM+DRL models. A description of these models is in Appendix H. Datasets. We consider five real-world datasets and associated constraints. Four datasets (i.e., URL, CCS, LCLD, and Heloc) are used for classification tasks, while one dataset (i.e., House) is used for regression. A detailed description of the datasets and their respective constraints are in Appendix G. 4.1 S YNTHETIC DATA Q UALITY Background knowledge align- Table 1: CVR for each model and dataset. Cases with ment. To assess how often the CVR≥50% are under

## 原始摘要

Synthetic tabular data generation has traditionally been a challenging problem due to the high complexity of the underlying distributions that characterise this type of data. Despite recent advances in deep generative models (DGMs), existing methods often fail to produce realistic datapoints that are well-aligned with available background knowledge.In this paper, we address this limitation by introducing Disjunctive Refinement Layer (DRL), a novel layer designedto enforce the alignment of generated data with the background knowledge specified in user-defined constraints.DRL is the first method able to automatically make deep learning models inherently compliant with constraints as expressive as quantifier-free linear formulas, which can define non-convex and even disconnected spaces. Our experimental analysis shows that DRL not only guarantees constraint satisfaction but also improves efficacy in downstream tasks. Notably, when applied to DGMs that frequently violate constraints, DRL eliminates violations entirely. Further, it improves performance metrics by up to 21.4\% in F1-score and 20.9\% in Area Under the ROC Curve, thus demonstrating its practical impact on data generation.
