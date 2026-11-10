# TabDPT: Scaling Tabular Foundation Models on Real Data

NeurIPS 2025 · main · application

正文包含金融数据、金融训练数据、金融任务评测或具体金融场景案例。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=pIZxEOZCId
- 摘要来源：https://neurips.cc/virtual/2025/poster/115970
- 本地 PDF：[打开](../../pdfs/NeurIPS/2025/neurips-2025-pIZxEOZCId__TabDPT_Scaling_Tabular_Foundation_Models_on_Real_Data.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Credit Scoring & Default / 信用评分与违约；Lending & Credit Data / 借贷与信贷数据应用
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Generative Modeling / 生成建模；Tabular Learning / 表格学习；Retrieval & RAG / 检索与RAG；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：language models；LLMs；retrieval
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/layer6ai-labs/TabDPT-inference；https://github.com/layer6ai-labs/TabDPT-training

## 纳入依据

g. Other or not provided SGEMM_GPU_kernel_ 44069 241600 9 2.4M 0.0 Reg. Computing performance 44089 credit 16714 10 184K 0.0 Class. Financial/demographic 44122 pol 10082 26 272K 0.0 Class. Industrial/operational 44136 wine_quality 6497 11 78K 0.0 Reg. Human behaviour 44137 Ailerons 13750 33 468K 0.0 Reg. Other or not provided 44145 sulfur 10081 6 71K 0.0 Reg. Other science 45020 default-of-credit-card-clients 13272 20 279K 0.0 Class. Financial/demographic 45022 Diabetes130US 71090 7 569K 0.0 Class. Medical/human sensor 45026 heloc 10000 22 230K 0.0 Class. Financial/demographic 45032 yprop_4_1 8885 42 382K 0.0 Reg. Medical/human sensor 45038 road-safety 111762 32 3.7M 0.0 Class. Human behaviour 45039 compas-two-years 4966 1

## 原始摘要

Tabular data is one of the most ubiquitous sources of information worldwide, spanning a wide variety of domains. This inherent heterogeneity has slowed the development of Tabular Foundation Models (TFMs) capable of fast generalization to unseen datasets. In-Context Learning (ICL) has recently emerged as a promising solution for TFMs, enabling dynamic adaptation to new tasks without additional tuning. While many studies have attempted to re-purpose large language models for tabular ICL, they have had limited success, so recent works have focused on developing tabular-specific foundation models. In this work, we propose an approach to combine ICL-based retrieval with self supervised learning to train tabular foundation models. We also investigate the utility of real vs. synthetic data for model pre-training, and show that real data can contain useful signal not easily captured in synthetic training. Specifically, we show that incorporating real data during the pre-training phase can lead to significantly faster training and better downstream generalization to unseen data. Our resulting model, **TabDPT**, achieves strong performance on both regression (CTR23) and classification (CC18) benchmarks. Importantly, we also demonstrate that with our pre-training procedure, scaling both model and data size leads to consistent performance improvements that follow power laws. This echoes scaling laws in LLMs and other foundation models, and suggests that large-scale TFMs can be achievable. We open-source our full pipeline: inference code including trained model weights can be found [here](https://github.com/layer6ai-labs/TabDPT-inference), and the training code to reproduce experiments can be found [here](https://github.com/layer6ai-labs/TabDPT-training).
