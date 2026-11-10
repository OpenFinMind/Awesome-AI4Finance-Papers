# Cascaded Flow Matching for Heterogeneous Tabular Data with Mixed-Type Features

ICML 2026 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：credit_g。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=l2ywV9sV0L
- 摘要来源：https://icml.cc/virtual/2026/poster/61978
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-l2ywV9sV0L__Cascaded_Flow_Matching_for_Heterogeneous_Tabular_Data_with_Mixed_Type_Features.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Credit Scoring & Default / 信用评分与违约
- 技术方法标签：Diffusion & Flow / 扩散与流模型；Generative Modeling / 生成建模；Tabular Learning / 表格学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：diffusion
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/muellermarkus/tabcascade.

## 纳入依据

bCascade’s ability to explicitly datasets from the TabZilla tabular data benchmark (McEl- incorporate mixed-type feature distributions greatly fresh et al., 2023), including airlines, credit_g, improves the sample quality for numerical features over electricity, kc1 and phoneme. The selected the baselines. The average WD decreases by more than datasets include inflated values. The missing values are 50% relative to the best baseline. For categorical features, added (10%) via a simulated MNAR mechanism (Muzellec it perf

## 原始摘要

Advances in generative modeling have recently been adapted to tabular data containing discrete and continuous features.  However, generating mixed-type features that combine discrete states with an otherwise continuous distribution in a single feature remains challenging. We advance the state-of-the-art in diffusion models for tabular data with a cascaded approach. We first generate a low-resolution version of a tabular data row, that is, the collection of the purely categorical features and a coarse categorical representation of numerical features. Next, this information is leveraged in the high-resolution flow matching model via a novel guided conditional probability path and data-dependent coupling. The low-resolution representation of numerical features explicitly accounts for discrete outcomes, such as missing or inflated values, and therewith enables a more faithful generation of mixed-type features. We formally prove that this cascade tightens the transport cost bound. The results indicate that our model generates significantly more realistic samples and captures distributional details more accurately, for example, the detection score improves by 51.9%. Code is available at https://github.com/muellermarkus/tabcascade.
