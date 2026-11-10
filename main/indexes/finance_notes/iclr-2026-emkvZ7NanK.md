# Tackling Time-Series Forecasting Generalization via Mitigating Concept Drift

ICLR 2026 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：Exchange benchmark (currency series)。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=emkvZ7NanK
- 摘要来源：https://iclr.cc/virtual/2026/poster/10008286
- 本地 PDF：[打开](../../pdfs/ICLR/2026/iclr-2026-emkvZ7NanK__Tackling_Time_Series_Forecasting_Generalization_via_Mitigating_Concept_Drift.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测
- 技术方法标签：Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

2.0% 7.1% 13.8% 6.5% 96 0.338 0.475 0.102 0.237 0.130 0.265 0.102 0.236 0.135 0.272 0.115 0.255 Exchange 192 0.566 0.622 0.203 0.338 0.247 0.394 0.194 0.332 0.250 0.376 0.209 0.343 336 1.078 0.867 0.407 0.484 0.522 0.557 0.388 0.477 0.450 0.503 0.426 0.495 720 1.292 0.963 1.165 0.813 1.171 0.824 0.995 0.747 1.501 0.941 1.138 0.827 IMP. 53.5% 38.9% 20.9% 12.6% 15.

## 原始摘要

Time-series forecasting finds broad applications in real-world scenarios. Due to the dynamic nature of time series data, it is important for time-series forecasting models to handle potential distribution shifts over time. In this paper, we initially identify two types of distribution shifts in time series: concept drift and temporal shift. We acknowledge that while existing studies primarily focus on addressing temporal shift issues in time series forecasting, designing proper concept drift methods for time series forecasting has received comparatively less attention.  Motivated by the need to address potential concept drift, while conventional concept drift methods via invariant learning face certain challenges in time-series forecasting, we propose a soft attention mechanism that finds invariant patterns from both lookback and horizon time series. Additionally, we emphasize the critical importance of mitigating temporal shifts as a preliminary to addressing concept drift. In this context, we introduce ShifTS, a method-agnostic framework designed to tackle temporal shift first and then concept drift within a unified approach. Extensive experiments demonstrate the efficacy of ShifTS in consistently enhancing the forecasting accuracy of agnostic models across multiple datasets, and outperforming existing concept drift, temporal shift, and combined baselines.
