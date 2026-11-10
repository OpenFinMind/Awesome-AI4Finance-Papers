# Towards Neural Scaling Laws for Time Series Foundation Models

ICLR 2025 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：M4 Daily。M4 年度至日度子集包含金融序列，未把仅使用 M4 Hourly 的论文据此纳入。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=uCqxDfLYrB
- 摘要来源：https://iclr.cc/virtual/2025/poster/27992
- 本地 PDF：[打开](../../pdfs/ICLR/2025/iclr-2025-uCqxDfLYrB__Towards_Neural_Scaling_Laws_for_Time_Series_Foundation_Models.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；Representation & Foundation Models / 表征与基础模型
- 技术方法标签：Transformer / Transformer模型；Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：time series；Transformers
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Weather Climate H 192 1029 M4 Hourly Finance H 48 414 M4 Daily Finance D 14 4227 M4 Weekly Finance W 13 359 20 Published as a conference paper at ICLR 2025 Table 3 continued from previous page Dataset Domain Frequency # Predictio

## 原始摘要

Scaling laws offer valuable insights into the design of time series foundation models (TSFMs). However, previous research has largely focused on the scaling laws of TSFMs for in-distribution (ID) data, leaving their out-of-distribution (OOD) scaling behavior and the influence of model architectures less explored. In this work, we examine two common TSFM architectures—encoder-only and decoder-only Transformers—and investigate their scaling behavior on both ID and OOD data. These models are trained and evaluated across varying parameter counts, compute budgets, and dataset sizes. Our experiments reveal that the log-likelihood loss of TSFMs exhibits similar scaling behavior in both OOD and ID settings. We further compare the scaling properties across different architectures, incorporating two state-of-the-art TSFMs as case studies, showing that model architecture plays a significant role in scaling. The encoder-only Transformers demonstrate better scalability than the decoder-only Transformers, while the architectural enhancements in the two advanced TSFMs primarily improve ID performance but reduce OOD scalability. While scaling up TSFMs is expected to drive performance breakthroughs, the lack of a comprehensive understanding of TSFM scaling laws has hindered the development of a robust framework to guide model scaling. We fill this gap in this work by synthesizing our findings and providing practical guidelines for designing and scaling larger TSFMs with enhanced model capabilities.
