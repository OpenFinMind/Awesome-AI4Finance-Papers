# Unlocking the Value of Text: Event-Driven Reasoning and Multi-Level Alignment for Time Series Forecasting

ICLR 2026 · main · application

正文包含金融数据、金融训练数据、金融任务评测或具体金融场景案例。 主题：Time Series / 时间序列；Macro & Economic Forecasting / 宏观经济与预测。

- 官方论文页：https://openreview.net/forum?id=0TAFiyHgEl
- 摘要来源：https://iclr.cc/virtual/2026/poster/10011937
- 本地 PDF：[打开](../../pdfs/ICLR/2026/iclr-2026-0TAFiyHgEl__Unlocking_the_Value_of_Text_Event_Driven_Reasoning_and_Multi_Level_Alignment_for_Time_Series_Forecasting.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；Macro Indicators & Policy / 宏观指标与政策
- 技术方法标签：Language Models & LLM / 语言模型与LLM
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：LLMs；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/decisionintelligence/VoT.

## 纳入依据

990 2000 2010 2020 petitive performance (Nie et al., 2023; Chen et al., 2024; Qiu et al., Figure 1: Unemployment rate time series (Liu et al., 2024a) 2025d; Wu et al., 2025; 2022) on this (1970-2020). While certain patterns (pink) exhibit pre- task. However, they solely rely on dictable temporal regularities, abrupt changes (green) driven numerical time series data, limiting by external events necessitate the integration of textual in- their ability to capture more complex formation to complement numerical forecasting. patterns. Taking the unemployment rate data (Liu et al., 2024a) as an example, Figure 1 illustrates that certain abrupt changes in the time series are difficult to predict solely from historical numerical patterns. However,

## 原始摘要

Existing time series forecasting methods primarily rely on the numerical data itself. However, real-world time series exhibit complex patterns associated with multimodal information, making them difficult to predict with numerical data alone. While several multimodal time series forecasting methods have emerged, they either utilize text with limited supplementary information or focus merely on representation extraction, extracting minimal textual information for forecasting. To unlock the Value of Text, we propose VoT, a method with Event-driven Reasoning and Multi-level Alignment. Event-driven Reasoning combines the rich information in exogenous text with the powerful reasoning capabilities of LLMs for time series forecasting. To guide the LLMs in effective reasoning, we propose the Historical In-context Learning that retrieves and applies historical examples as in-context guidance. To maximize the utilization of text, we propose Multi-level Alignment. At the representation level, we utilize the Endogenous Text Alignment to integrate the endogenous text information with the time series. At the prediction level, we design the Adaptive Frequency Fusion to fuse the frequency components of event-driven prediction and numerical prediction to achieve complementary advantages. Experiments on real-world datasets across 10 domains demonstrate significant improvements over existing methods, validating the effectiveness of our approach in the utilization of text. The code is made available at https://github.com/decisionintelligence/VoT.
