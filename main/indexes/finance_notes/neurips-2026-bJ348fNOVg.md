# SurvivalPFN: Amortizing Survival Prediction via In-Context Bayesian Inference

NeurIPS 2026 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：German Credit。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=bJ348fNOVg
- 摘要来源：https://neurips.cc/virtual/2026/poster/151336
- 本地 PDF：[打开](../../pdfs/NeurIPS/2026/neurips-2026-bJ348fNOVg__SurvivalPFN_Amortizing_Survival_Prediction_via_In_Context_Bayesian_Inference.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Credit Scoring & Default / 信用评分与违约；Lending & Credit Data / 借贷与信贷数据应用
- 技术方法标签：未明确标注
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Bayesian
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

[95]. • kidney_transplant: The kidney_transplant dataset records post-transplant death times with recipient age, gender, and race [49]. • credit: The PySurvival [19] credit-risk dataset adapts the German Credit data to model the time until a loan is fully repaid. • PDM: The PySurvival [19] predictive-maintenance (PDM) dataset models the time until an industrial machine breaks. • COVID: The COVID-19 Asian discharge dataset models time to hospital discharge for patients with COVID-19 diagnosis [52]. • WHAS: T

## 原始摘要

Survival analysis provides a powerful statistical framework for modeling time-to-event outcomes in the presence of censoring. However, selecting an appropriate estimator from the many specialized survival approaches often requires substantial methodological and domain expertise. We introduce SurvivalPFN, a prior-data fitted network that amortizes Bayesian inference for censored observations through in-context learning. SurvivalPFN is pretrained on a diverse family of synthetic, identifiable, and right-censored data-generating processes, enabling it to amortize survival analysis in a single forward pass during inference. As a result, the model adapts to the effective complexity of each dataset without task-specific training or hyperparameter tuning, avoids restrictive parametric assumptions, and produces calibrated survival distributions. In a large-scale benchmark spanning 61 survival datasets, 21 methods, and 5 evaluation metrics, SurvivalPFN achieves strong predictive performance and often improves upon established survival models. These results suggest that SurvivalPFN offers a principled and practical foundation model for survival analysis, with potential applications in high-impact domains such as healthcare, finance, and engineering.
