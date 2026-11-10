# Small Models are LLM Knowledge Triggers for Medical Tabular Prediction

ICLR 2025 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：GiveMeSomeCredit。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=WoPovNkM5h
- 摘要来源：https://iclr.cc/virtual/2025/poster/29343
- 本地 PDF：[打开](../../pdfs/ICLR/2025/iclr-2025-WoPovNkM5h__Small_Models_are_LLM_Knowledge_Triggers_for_Medical_Tabular_Prediction.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Credit Scoring & Default / 信用评分与违约
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Tabular Learning / 表格学习；Multimodal Learning / 多模态学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：language models；LLM；LLMs
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/jyansir/sersal.

## 纳入依据

0.57 https://www.kaggle.com/datasets/serhathoca/anemia-disease Churn Modeling - 10000 10 0.26 - Give Me Some Credit - 16714 10 1.00 https://www.kaggle.com/c/GiveMeSomeCredit US Adult Income - 48842 14 0.31 https://www.kaggle.com/datasets/johnolafenwa/us-census-data Table 6: Detailed data information of used tabular datasets (10 from the medical domain and 3 from others). “P/N” denotes the amount ratio of positive samples and negative ones. C R ESULTS ON C LINICAL T RIAL DATASET

## 原始摘要

Recent development in large language models (LLMs) has demonstrated impressive domain proficiency on unstructured textual or multi-modal tasks. However, despite with intrinsic world knowledge, their application on structured tabular data prediction still lags behind, primarily due to the numerical insensitivity and modality discrepancy that brings a gap between LLM reasoning and statistical tabular learning. Unlike textual or vision data (e.g., electronic clinical notes or medical imaging data), tabular data is often presented in heterogeneous numerical values (e.g., CBC reports). This ubiquitous data format requires intensive expert annotation, and its numerical nature limits LLMs' capability to effectively transfer untapped domain expertise. In this paper, we propose SERSAL, a general self-prompting method by synergy learning with small models to enhance LLM tabular prediction in an unsupervised manner. Specifically, SERSAL utilizes the LLM's prior outcomes as original soft noisy annotations, which are dynamically leveraged to teach a better small student model. Reversely, the outcomes from the trained small model are used to teach the LLM to further refine its real capability. This process can be repeatedly applied to gradually distill refined knowledge for continuous progress. Comprehensive experiments on widely used medical domain tabular datasets show that, without access to gold labels, applying SERSAL to OpenAI GPT reasoning process attains substantial improvement compared to linguistic prompting methods, which serves as an orthogonal direction for tabular LLM, and increasing prompting bonus is observed as more powerful LLMs appear. Codes are available at https://github.com/jyansir/sersal.
