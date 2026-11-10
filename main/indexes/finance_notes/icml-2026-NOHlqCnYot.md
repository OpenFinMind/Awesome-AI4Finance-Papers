# Overcoming the Modality Gap in Context-Aided Forecasting

ICML 2026 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：m4_daily。M4 年度至日度子集包含金融序列，未把仅使用 M4 Hourly 的论文据此纳入。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=NOHlqCnYot
- 摘要来源：https://icml.cc/virtual/2026/poster/64459
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-NOHlqCnYot__Overcoming_the_Modality_Gap_in_Context_Aided_Forecasting.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：General Time-Series Methods / 综合序列方法
- 技术方法标签：Generative Modeling / 生成建模；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

le 4 Train and Test split datasets used for CAF-7M. train test electricity_15min dominick m4_daily ercot m4_hourly exchange_rate m4_weekly m4_quarterly m4_monthly m5 mexico_city_bikes monash_car_parts monash_electricity_hourly monash_austr

## 原始摘要

Context-aided forecasting (CAF) holds promise for integrating domain knowledge and forward-looking information, enabling AI systems to surpass traditional statistical methods. However, recent empirical studies reveal a puzzling gap: multimodal models often fail to outperform their unimodal counterparts. We hypothesize that this underperformance stems partly from insufficiently verified context usefulness in existing datasets. To address these limitations, we introduce a semi-synthetic data augmentation method that generates contexts both descriptive of temporal dynamics and verifiably complementary to numerical histories. This approach enables massive-scale dataset creation, resulting in CAF-7M, a corpus of 7 million context-augmented time series windows, including a rigorously verified test set. We demonstrate that semi-synthetic pre-training transfers effectively to real-world evaluation, and show clear evidence of context utilization. Our results suggest that dataset quality is a major bottleneck in context-aided forecasting, and that verified context can substantially improve the usefulness of CAF training data.
