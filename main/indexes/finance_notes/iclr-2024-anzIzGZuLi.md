# Making Pre-trained Language Models Great on Tabular Prediction

ICLR 2024 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：Bank marketing。 主题：Banking & Customer Service / 银行业务与客户服务。

- 官方论文页：https://openreview.net/forum?id=anzIzGZuLi
- 摘要来源：https://iclr.cc/virtual/2024/poster/18356
- 本地 PDF：[打开](../../pdfs/ICLR/2024/iclr-2024-anzIzGZuLi__Making_Pre_trained_Language_Models_Great_on_Tabular_Prediction.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Banking & Customer Service / 银行业务与客户服务
- 细分方向：Bank Marketing & Churn / 银行营销与客户流失
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Tabular Learning / 表格学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：language models
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

9 1728 HSI-Futures 87645 5 0 12 0080 BNG(vote) 100000 0 16 Customer-Churn 10000 4 10 13 Bank marketing data 45211 7 9 2672 kings county 21613 13 8 14 2149 electricity 38474 7 1 dataset sales 10738 4 10 15 BNG(breast-w) 39366 9 0 2707 seattlecrime6 52031

## 原始摘要

The transferability of deep neural networks (DNNs) has made significant progress in image and language processing. However, due to the heterogeneity among tables, such DNN bonus is still far from being well exploited on tabular data prediction (e.g., regression or classification tasks). Condensing knowledge from diverse domains, language models (LMs) possess the capability to comprehend feature names from various tables, potentially serving as versatile learners in transferring knowledge across distinct tables and diverse prediction tasks, but their discrete text representation space is inherently incompatible with numerical feature values in tables. In this paper, we present TP-BERTa, a specifically pre-trained LM for tabular data prediction. Concretely, a novel relative magnitude tokenization converts scalar numerical feature values to finely discrete, high-dimensional tokens, and an intra-feature attention approach integrates feature values with the corresponding feature names. Comprehensive experiments demonstrate that our pre-trained TP-BERTa leads the performance among tabular DNNs and is competitive with Gradient Boosted Decision Tree models in typical tabular data regime.
