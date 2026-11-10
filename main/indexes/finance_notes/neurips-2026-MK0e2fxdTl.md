# TimeClaw: A Time-Series AI Agent with Exploratory Execution Learning

NeurIPS 2026 · main · application

以金融市场为研究对象，或包含明确的金融领域数据和应用评测。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=MK0e2fxdTl
- 摘要来源：https://neurips.cc/Downloads/2026
- 本地 PDF：[打开](../../pdfs/NeurIPS/2026/neurips-2026-MK0e2fxdTl__TimeClaw_A_Time_Series_AI_Agent_with_Exploratory_Execution_Learning.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_financial_task_or_data
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；Representation & Foundation Models / 表征与基础模型
- 技术方法标签：Language Models & LLM / 语言模型与LLM
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：LLMs；Time series；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Time series analysis underpins forecasting, monitoring, and decision making in domains such as finance and weather, where solving a task often requires both numerical accuracy and contextual reasoning. / In an MTBench-aligned evaluation with 17 tasks that span finance and weather prediction and reasoning tasks, TimeClaw delivers consistent gains over the baselines.

## 原始摘要

Time series analysis underpins forecasting, monitoring, and decision making in domains such as finance and weather, where solving a task often requires both numerical accuracy and contextual reasoning. Recent progress has moved from specialized neural predictors to approaches built on LLMs and foundation models that can reason over time series inputs and use external tools. However, most such systems remain execution-centric: they focus on solving the current instance but learn little from exploratory execution. This is especially limiting in verifiable numeric settings, where multiple candidate executions and tool-use procedures may all be task-valid yet differ sharply in quantitative quality, and where early success can trigger tool-prior collapse that suppresses further exploration. To address this limitation, we present TimeClaw, an exploratory execution learning framework that turns exploratory execution into reusable hierarchical distilled experience through a four-stage loop: Explore, Compare, Distill, and Reinject. TimeClaw combines metric-supervised exploratory execution learning, task-aware tool dropout, and hierarchical distilled experience for inference-time reinjection, while keeping the base model frozen and avoiding online test-time adaptation. In an MTBench-aligned evaluation with 17 tasks that span finance and weather prediction and reasoning tasks, TimeClaw delivers consistent gains over the baselines. These results suggest that, for scientific systems, the bottleneck is not only execution-time capability, but how exploratory experience is compared, distilled, and reused.
