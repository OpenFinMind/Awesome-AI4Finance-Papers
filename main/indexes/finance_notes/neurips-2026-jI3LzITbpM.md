# TSQAgent: Rating Time Series Data Quality via Dedicated Agentic Reasoning

NeurIPS 2026 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：exchange rates。 主题：Time Series / 时间序列；Market Prediction / 股价、收益与波动率预测。

- 官方论文页：https://openreview.net/forum?id=jI3LzITbpM
- 摘要来源：https://neurips.cc/Downloads/2026
- 本地 PDF：[打开](../../pdfs/NeurIPS/2026/neurips-2026-jI3LzITbpM__TSQAgent_Rating_Time_Series_Data_Quality_via_Dedicated_Agentic_Reasoning.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；FX & Crypto Forecasts / 汇率与加密资产预测
- 技术方法标签：Language Models & LLM / 语言模型与LLM
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：language models；LLMs；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

een 2012 and 2014. In our experiments, we use the series labeled MT_320 as the target variable in the univariate setting. • ExchangeRate (Lai et al., 2018): This dataset records daily exchange rates of eight currencies spanning from 1990 to 2016. We follow prior work and select the Singapore dollar series as the prediction target. • Traffic (tra): This dataset consists of hourly occupancy rates collected from freeway sensors in the San Francisco Bay Area between 2015 and 2016. We use sensor 861 as the target series. • Weather (wea): This dataset contains high-fr

## 原始摘要

Assessing the quality of time series (TS) data is fundamental yet inherently challenging due to the multifaceted nature of quality dimensions. Recently, large language models (LLMs) have emerged as a promising paradigm for TS quality assessment via pairwise comparison and per-dimension evaluation. However, existing approaches rely on manually predefined quality dimensions and purely text-based reasoning, leaving it unknown whether LLMs can identify truly relevant quality dimensions or perform grounded and quantitative quality comparisons. To investigate this, we construct TSQBench, a dedicated benchmark for evaluating LLMs’ capabilities in TS quality assessment, which measures two progressive capabilities: (i) understanding and identifying relevant quality dimensions, and (ii) performing quality comparison under specific dimensions. Our analysis reveals that both open-source and proprietary LLMs consistently struggle with identifying critical quality dimensions and conducting precise, evidence-grounded reasoning over quality characteristics. To address these limitations, we propose TSQAgent, a novel agentic reasoning framework for dedicated TS data quality rating, comprising three collaborative roles: Perceiver for focused dimension selection, Inspector for dimension-wise quantitative analysis, and Adjudicator that aggregates and refines the final judgment. In particular, we introduce an agentic reasoning strategy that instills the ability to identify and prioritize the most relevant quality dimensions, and further propose an agent workflow equipped with external analytical tools to enable precise quantitative comparisons over selected dimensions. Experiments on both the proposed benchmark and eleven real-world datasets demonstrate that our framework not only substantially improves LLMs’ capabilities in quality understanding and quantitative comparison but also effectively translates these improvements into better quality-aware data selection, leading to enhanced downstream performance and data efficiency.
