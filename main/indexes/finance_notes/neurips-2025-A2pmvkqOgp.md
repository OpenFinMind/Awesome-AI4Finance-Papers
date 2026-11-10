# Forging Time Series with Language: A Large Language Model Approach to Synthetic Data Generation

NeurIPS 2025 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：Exchange Rate。 主题：Time Series / 时间序列；Market Prediction / 股价、收益与波动率预测。

- 官方论文页：https://openreview.net/forum?id=A2pmvkqOgp
- 摘要来源：https://neurips.cc/virtual/2025/poster/119486
- 本地 PDF：[打开](../../pdfs/NeurIPS/2025/neurips-2025-A2pmvkqOgp__Forging_Time_Series_with_Language_A_Large_Language_Model_Approach_to_Synthetic_Data_Generation.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；Representation & Foundation Models / 表征与基础模型；Generation & Simulation / 序列生成与仿真；Causality & Dynamics / 序列因果与动力学；FX & Crypto Forecasts / 汇率与加密资产预测
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Generative Modeling / 生成建模；Tabular Learning / 表格学习；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：fine-tuning；LLM；LLMs；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/IBM/fms-dgt/tree/main/fms_dgt/public/databuilders/time_series.

## 纳入依据

0.536 0.686 0.775 0.635 0.754 0.823 ECL 0.809 0.941 0.971 0.991 0.997 0.999 Exchange Rate 0.776 0.907 0.942 0.957 0.982 0.989 NN5 0.336 0.479 0.590 0.719 0.780 0.826 Tourism 0.869 0.954 0.977 0.986 0.995 0.998 Traffic 0.376 0.564 0.697 0.408 0.591 0.714 T

## 原始摘要

SDForger is a flexible and efficient framework for generating high-quality multivariate time series using LLMs. Leveraging a compact data representation, SDForger provides synthetic time series generation from a few samples and low-computation fine-tuning of any autoregressive LLM. Specifically, the framework transforms univariate and multivariate signals into tabular embeddings, which are then encoded into text and used to fine-tune the LLM. At inference, new textual embeddings are sampled and decoded into synthetic time series that retain the original data's statistical properties and temporal dynamics. Across a diverse range of datasets, SDForger outperforms existing generative models in many scenarios, both in similarity-based evaluations and downstream forecasting tasks. By enabling textual conditioning in the generation process, SDForger paves the way for multimodal modeling and the streamlined integration of time series with textual information. The model is open-sourced at https://github.com/IBM/fms-dgt/tree/main/fms_dgt/public/databuilders/time_series.
