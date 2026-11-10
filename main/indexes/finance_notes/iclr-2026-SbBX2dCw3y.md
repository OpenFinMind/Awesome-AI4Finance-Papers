# Multi-Scale Hypergraph Meets LLMs: Aligning Large Language Models for Time Series Analysis

ICLR 2026 · main · application

正文包含金融数据、金融训练数据、金融任务评测或具体金融场景案例。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=SbBX2dCw3y
- 摘要来源：https://iclr.cc/virtual/2026/poster/10009396
- 本地 PDF：[打开](../../pdfs/ICLR/2026/iclr-2026-SbBX2dCw3y__Multi_Scale_Hypergraph_Meets_LLMs_Aligning_Large_Language_Models_for_Time_Series_Analysis.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Representation & Foundation Models / 表征与基础模型
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Graph Learning / 图学习；Multimodal Learning / 多模态学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Language Models；language models；LLM；LLMs；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

earning. Detailed descriptions of M3 and M4 datasets are given as follows: • M3 datasets: The M3 datasets comprise 3,003 time series with varying granularities, including micro, industry, macro, and finance. It presents a diverse collection of seasonal and non-seasonal sequences, with frequencies spanning from yearly to monthly. • M4 datasets: The M4 datasets are larger than M3 datasets and expands the collection to 100,000 individual time series. The M4 datasets encompass a vast array of temporal patterns ac

## 原始摘要

Recently, there has been great success in leveraging pre-trained large language models (LLMs) for time series analysis. The core idea lies in effectively aligning the modality between natural language and time series. However, the multi-scale structures of natural language and time series have not been fully considered, resulting in insufficient utilization of LLMs capabilities. To this end, we propose MSH-LLM, a Multi-Scale Hypergraph method that aligns Large Language Models for time series analysis. Specifically, a hyperedging mechanism is designed to enhance the multi-scale semantic information of time series semantic space. Then, a cross-modality alignment (CMA) module is introduced to align the modality between natural language and time series at different scales. In addition, a mixture of prompts (MoP) mechanism is introduced to provide contextual information and enhance the ability of LLMs to understand the multi-scale temporal patterns of time series. Experimental results on 27 real-world datasets across 5 different applications demonstrate that MSH-LLM achieves the state-of-the-art results.
