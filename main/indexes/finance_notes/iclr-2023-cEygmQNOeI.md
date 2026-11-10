# Language Models are Realistic Tabular Data Generators

ICLR 2023 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：HELOC。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=cEygmQNOeI
- 摘要来源：https://iclr.cc/virtual/2023/poster/11269
- 本地 PDF：[打开](../../pdfs/ICLR/2023/iclr-2023-cEygmQNOeI__Language_Models_are_Realistic_Tabular_Data_Generators.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Credit Scoring & Default / 信用评分与违约
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Generative Modeling / 生成建模；Transformer / Transformer模型；Uncertainty & Robustness / 不确定性与鲁棒性；Tabular Learning / 表格学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：language models；LLM；LLMs；transformer；variational
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

99.28±0.06 94.91±0.06 94.57±0.01 94.57±0.00 97.72±0.10 98.30±0.13 LR 71.80±0.00 71.04±0.00 42.03±0.00 57.72±0.00 70.58±0.00 71.90±0.00 HELOC (↑) DT 81.90±0.02 76.39±0.10 42.36±0.10 61.34±0.09 81.40±0.15 79.10±0.07 RF 83.19±0.21 77.24±0.25 42.35±0.34 62.35±0.35 82.14±0.13 80.93±0.28 LR 85.00±0.00 80.53±0.00 80.61±0.00 83.20±0.00 84.65±0.00 84.77±0.00

## 原始摘要

Tabular data is among the oldest and most ubiquitous forms of data. However, the generation of synthetic samples with the original data’s characteristics remains a significant challenge for tabular data. While many generative models from the computer vision domain, such as variational autoencoders or generative adversarial networks, have been adapted for tabular data generation, less research has been directed towards recent transformer-based large language models (LLMs), which are also generative in nature. To this end, we propose GReaT (Generation of Realistic Tabular data), which exploits an auto-regressive generative LLM to sample synthetic and yet highly realistic tabular data. Furthermore, GReaT can model tabular data distributions by conditioning on any subset of features; the remaining features are sampled without additional overhead. We demonstrate the effectiveness of the proposed approach in a series of experiments that quantify the validity and quality of the produced data samples from multiple angles. We find that GReaT maintains state-of-the-art performance across numerous real-world and synthetic data sets with heterogeneous feature types coming in various sizes.
