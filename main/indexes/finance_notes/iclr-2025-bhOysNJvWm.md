# Diffusion Transformers for Tabular Data Time Series Generation

ICLR 2025 · main · application

正文包含金融数据、金融训练数据、金融任务评测或具体金融场景案例。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=bhOysNJvWm
- 摘要来源：https://iclr.cc/virtual/2025/poster/29095
- 本地 PDF：[打开](../../pdfs/ICLR/2025/iclr-2025-bhOysNJvWm__Diffusion_Transformers_for_Tabular_Data_Time_Series_Generation.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Generation & Simulation / 序列生成与仿真
- 技术方法标签：Diffusion & Flow / 扩散与流模型；Generative Modeling / 生成建模；Transformer / Transformer模型；Tabular Learning / 表格学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Diffusion；time series；Transformers
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

n tasks and different metrics. More details are provided in App. C and E. Datasets. We use six public datasets, whose statistics are provided in App. E. Age1, Age2, Leaving, taken from (Fursov et al., 2021), and PKDD’99 Financial Dataset, taken from (Berka, 1999), are composed of bank transaction time series of different real banks with different attributes. Each time 7 Published as a conference paper at ICLR 2025 series is the temporally ordered sequence of bank transactions of a given bank client. On the othe

## 原始摘要

Tabular data generation has recently attracted a growing interest due to its different application scenarios. However, generating time series of tabular data, where each element of the series depends on the others,remains a largely unexplored domain. This gap is probably due to the difficulty of jointly solving different problems, the main of which are the heterogeneity of tabular data (a problem common to non-time-dependent approaches) and the variable length of a time series.In this paper, we propose a Diffusion Transformers (DiTs) based approach for tabular data series generation. Inspired by the recent success of DiTs in image and video generation, we extend this framework to deal with heterogeneous data and variable-length sequences. Using extensive experiments on six datasets, we show that the proposed approach  outperforms previous work by a large margin.
