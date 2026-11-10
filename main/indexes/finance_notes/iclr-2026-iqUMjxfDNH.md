# Test-Time Efficient Pretrained Model Portfolios for Time Series Forecasting

ICLR 2026 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：m4_daily。M4 年度至日度子集包含金融序列，未把仅使用 M4 Hourly 的论文据此纳入。 主题：Time Series / 时间序列；Blockchain & Digital Assets / 区块链与数字资产。

- 官方论文页：https://openreview.net/forum?id=iqUMjxfDNH
- 摘要来源：https://iclr.cc/virtual/2026/poster/10007930
- 本地 PDF：[打开](../../pdfs/ICLR/2026/iclr-2026-iqUMjxfDNH__Test_Time_Efficient_Pretrained_Model_Portfolios_for_Time_Series_Forecasting.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；Representation & Foundation Models / 表征与基础模型；Crypto & Blockchain Transactions / 加密资产与链上交易
- 技术方法标签：未明确标注
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：fine-tuning；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

,379 0.0% 401 daily transport uber_tlc_daily 262 47,422 0.0% 181 daily transport m4_daily 4,227 10,023,836 0.0% 2371 daily various monash/bitcoin 18 82,458 9.8% 4581 daily various monash/bitcoin_without_missing_values 18 75,364 0.0% 4187 daily various monash/us_births

## 原始摘要

Is bigger always better for time series foundation models? With the question in mind, we explore an alternative to training a single, large monolithic model: building a portfolio of smaller, pretrained forecasting models. By applying ensembling or model selection over these portfolios, we achieve competitive performance on large-scale benchmarks using much fewer parameters. We explore strategies for designing such portfolios and find that collections of specialist models consistently outperform portfolios of independently trained generalists. Remarkably, we demonstrate that post-training a base model is a compute-effective approach for creating sufficiently diverse specialists, and provide evidences that ensembling and model selection are more compute-efficient than test-time fine-tuning.
