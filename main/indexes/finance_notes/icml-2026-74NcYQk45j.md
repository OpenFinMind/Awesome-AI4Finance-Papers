# Algorithmic Recourse of In-Context Learning for Tabular Data

ICML 2026 · main · application

研究金融风险度量、金融决策或信贷场景的建模与理论方法。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=74NcYQk45j
- 摘要来源：https://icml.cc/virtual/2026/poster/66098
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-74NcYQk45j__Algorithmic_Recourse_of_In_Context_Learning_for_Tabular_Data.pdf)；版本：arxiv_author_version
- 金融依据类型：financial_method_or_formal_case
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Credit Scoring & Default / 信用评分与违约
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Fairness & Recourse / 公平性与算法追索；Tabular Learning / 表格学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：language models
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

As predictive models are increasingly deployed in high-stakes settings such as credit approval, there is a growing need for post-hoc methods that provide recourse to affected individuals.

## 原始摘要

As predictive models are increasingly deployed in high-stakes settings such as credit approval, there is a growing need for post-hoc methods that provide recourse to affected individuals. Many such models operate on tabular data, where features correspond to real-world attributes. Recently, in-context learning (ICL) has enabled large language models to perform tabular prediction by conditioning on labeled examples at inference time, without explicit training. However, algorithmic recourse for tabular decision-making under ICL remains largely unexplored. In this work, we present the first study of algorithmic recourse for tabular data under ICL. We carry out a theoretical analysis, showing that recourse remains well-defined and bounded, and we characterize how recourse converges toward classical solutions as the context size increases. In practice, we propose a novel zeroth-order recourse framework, Adaptive Subspace Recourse for In-Context Learning (ASR-ICL), that efficiently generates actionable and sparse recourse for black-box ICL models. The proposed framework naturally extends to multi-class tabular tasks. Experiments across multiple real-world datasets and models demonstrate that ASR-ICL achieves recourse quality comparable to existing methods with fewer queries and empirically confirm the predicted convergence behavior, supporting our theoretical analysis.
