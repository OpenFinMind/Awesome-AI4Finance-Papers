# Joint Distribution–Informed Shapley Values for Sparse Counterfactual Explanations

ICLR 2026 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：HELOC。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=3vIe5pNiUN
- 摘要来源：https://iclr.cc/virtual/2026/poster/10011598
- 本地 PDF：[打开](../../pdfs/ICLR/2026/iclr-2026-3vIe5pNiUN__Joint_Distribution_Informed_Shapley_Values_for_Sparse_Counterfactual_Explanations.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Credit Scoring & Default / 信用评分与违约
- 技术方法标签：Fairness & Recourse / 公平性与算法追索
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

026 Table 1: [Experiment Scenarios Setup] Four datasets are used to benchmark five CE algorithms over 12 models. A “scenario” is defined to be a combination of dataset, ACE algorithm, and a model f . Dataset HELOC (FICO, 2018), German Credit (Hofmann, 1994), Hotel Bookings (Antonio et al., 2019), COMPAS (Jeff Larson et al., 2016) ACE DiCE (Mothilal et al., 2020), AReS (Rawal & Lakkaraju, 2020), GlobeCE (Ley et al., 2023), KNN (Albini et al., 2022; Contardo et al.; Forel et al., 2023), Discount (You et

## 原始摘要

Counterfactual explanations (CE) aim to reveal how small input changes flip a model’s prediction, yet many methods modify more features than necessary, reducing clarity and actionability. We introduce COLA, a model- and generator-agnostic post-hoc framework that refines any given CE by computing a coupling via optimal transport (OT) between factual and counterfactual sets and using it to drive a Shapley-based attribution p-SHAP that selects a minimal set of edits while preserving the target effect. Theoretically, OT minimizes an upper bound on the $W_1$ divergence between factual and counterfactual outcomes and that, under mild conditions, refined counterfactuals are guaranteed not to move farther from the factuals than the originals. Empirically, across four datasets, twelve models, and five CE generators, COLA achieves the same target effects with only 26–45% of the original feature edits. On a small-scale benchmark, COLA shows near-optimality.
