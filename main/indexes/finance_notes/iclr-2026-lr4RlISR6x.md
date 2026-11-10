# PHAT: Modeling Period Heterogeneity for Multivariate Time Series Forecasting

ICLR 2026 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：NASDAQ。 主题：Time Series / 时间序列；Macro & Economic Forecasting / 宏观经济与预测。

- 官方论文页：https://openreview.net/forum?id=lr4RlISR6x
- 摘要来源：https://iclr.cc/virtual/2026/poster/10007638
- 本地 PDF：[打开](../../pdfs/ICLR/2026/iclr-2026-lr4RlISR6x__PHAT_Modeling_Period_Heterogeneity_for_Multivariate_Time_Series_Forecasting.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；Macro Indicators & Policy / 宏观指标与政策
- 技术方法标签：Transformer / Transformer模型
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：time series；Transformer
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Table 1: Statistics of used datasets. Datasets NN5 Exchange FRED-MD ETTh ETTm AQShunyi AQWan ILI CzeLan ZafNoo NASDAQ NYSE # Samples 791 7,588 728 14,440 57,600 35,064 35,064 966 19,934 19,225 1,244 1,243 # Frequency 1 day 1 day 1 month 1 hour 15 mins 1 hour 1 hour 1 week 30 mins 30 mins 1 day 1 day Split Ration 7:1:2 7:1:2

## 原始摘要

While existing multivariate time series forecasting models have advanced significantly in modeling periodicity, they largely neglect the periodic heterogeneity common in real-world data, where variables exhibit distinct and dynamically changing periods. To effectively capture this periodic heterogeneity, we propose PHAT (Period Heterogeneity-Aware Transformer). Specifically, PHAT arranges multivariate inputs into a three-dimensional "periodic bucket" tensor, where the dimensions correspond to variable group characteristics with similar periodicity, time steps aligned by phase, and offsets within the period. By restricting interactions within buckets and masking cross-bucket connections, PHAT effectively avoids interference from inconsistent periods. We also propose a positive-negative attention mechanism, which captures periodic dependencies from two perspectives: periodic alignment and periodic deviation. Additionally, the periodic alignment attention scores are decomposed into positive and negative components, with a modulation term encoding periodic priors. This modulation constrains the attention mechanism to more faithfully reflect the underlying periodic trends. A mathematical explanation is provided to support this property. We evaluate PHAT comprehensively on 14 real-world datasets against 18 baselines, and the results show that it significantly outperforms existing methods, achieving highly competitive forecasting performance. Our sources is available at GitHub.
