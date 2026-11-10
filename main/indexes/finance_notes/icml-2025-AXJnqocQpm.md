# Quantifying Prediction Consistency Under Fine-tuning Multiplicity in Tabular LLMs

ICML 2025 · main · application

正文包含明确金融数据、金融任务或金融案例；金融应用可属于通用方法的一个实验。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=AXJnqocQpm
- 摘要来源：https://icml.cc/virtual/2025/poster/46165
- 本地 PDF：[打开](../../pdfs/ICML/2025/icml-2025-AXJnqocQpm__Quantifying_Prediction_Consistency_Under_Fine_tuning_Multiplicity_in_Tabular_LLMs.pdf)；版本：publisher_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Credit Scoring & Default / 信用评分与违约
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Tabular Learning / 表格学习；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Fine-tuning；fine-tuning；LLMs
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

data points under actual fine-tuned multiplicity for several Existing approaches to measure multiplicity in machine datasets, namely, the German Credit, Bank, Heart, learning often involve retraining and ensembling multiple Car, Diabetes, and Adult datasets (Kahn; Hofmann, models (Marx et al., 2020). However, such approaches can 1994; Becker & Kohavi,

## 原始摘要

Fine-tuning LLMs on tabular classification tasks can lead to the phenomenon of *fine-tuning multiplicity* where equally well-performing models make conflicting predictions on the same input. Fine-tuning multiplicity can arise due to variations in the training process, e.g., seed, weight initialization, minor changes to training data, etc., raising concerns about the reliability of Tabular LLMs in high-stakes applications such as finance, hiring, education, healthcare. Our work formalizes this unique challenge of fine-tuning multiplicity in Tabular LLMs and proposes a novel measure to quantify the consistency of individual predictions without expensive model retraining. Our measure quantifies a prediction's consistency by analyzing (sampling) the model's local behavior around that input in the embedding space. Interestingly, we show that sampling in the local neighborhood can be leveraged to provide probabilistic guarantees on prediction consistency under a broad class of fine-tuned models, i.e., inputs with sufficiently high local stability (as defined by our measure) also remain consistent across several fine-tuned models with high probability. We perform experiments on multiple real-world datasets to show that our local stability measure preemptively captures consistency under actual multiplicity across several fine-tuned models, outperforming competing measures.
