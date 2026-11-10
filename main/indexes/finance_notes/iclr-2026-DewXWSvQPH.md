# TimeSeriesExamAgent: Creating Time Series Reasoning Benchmarks at Scale

ICLR 2026 · main · application

通用方法在金融任务、数据或明确案例上开展应用验证。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=DewXWSvQPH
- 摘要来源：https://iclr.cc/virtual/2026/poster/10010760
- 本地 PDF：[打开](../../pdfs/ICLR/2026/iclr-2026-DewXWSvQPH__TimeSeriesExamAgent_Creating_Time_Series_Reasoning_Benchmarks_at_Scale.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_review
- 主方向：Time Series / 时间序列
- 细分方向：Generation & Simulation / 序列生成与仿真；Anomaly Detection / 序列异常检测；Causality & Dynamics / 序列因果与动力学
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Causal Learning / 因果学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Language Models；LLM；LLMs；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/magwiazda/TimeSeriesExamAgent

## 纳入依据

Then, with $\texttt{TimeSeriesExamAgent}$, we scale our approach by automatically generating benchmarks from real-world datasets spanning healthcare, finance and weather domains.

## 原始摘要

Large Language Models (LLMs) have shown promising performance in time series modeling tasks, but do they truly understand time series data? While multiple benchmarks have been proposed to answer this fundamental question, most are manually curated and focus on narrow domains or specific skill sets. To address this limitation, we propose scalable methods for creating comprehensive time series reasoning benchmarks that combine the flexibility of templates with the creativity of LLM agents. We first develop $\texttt{TimeSeriesExam}$, a multiple-choice benchmark using synthetic time series to evaluate LLMs across five core reasoning categories: pattern recognition, noise understanding, similarity analysis, anomaly detection, and causality. Then, with $\texttt{TimeSeriesExamAgent}$, we scale our approach by automatically generating benchmarks from real-world datasets spanning healthcare, finance and weather domains. Through multi-dimensional quality evaluation, we demonstrate that our automatically generated benchmarks achieve diversity comparable to manually curated alternatives. However, our experiments reveal that LLM performance remains limited in both abstract time series reasoning and domain-specific applications, highlighting ongoing challenges in enabling effective time series understanding in these models. $\texttt{TimeSeriesExamAgent}$ is available at https://github.com/magwiazda/TimeSeriesExamAgent
