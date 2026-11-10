# SteerCast: Retrieval-Based Latent Steering for Decoder-Only Time Series Forecasting

NeurIPS 2026 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：Exchange benchmark (currency series)。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=DRNgEw9MBD
- 摘要来源：https://neurips.cc/Downloads/2026
- 本地 PDF：[打开](../../pdfs/NeurIPS/2026/neurips-2026-DRNgEw9MBD__SteerCast_Retrieval_Based_Latent_Steering_for_Decoder_Only_Time_Series_Forecasting.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测
- 技术方法标签：Retrieval & RAG / 检索与RAG
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：fine-tuning；retrieval；Time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

0.336 0.265 0.256 0.296 0.398 0.305 0.403 0.306 0.400 0.319 0.409 0.392 0.430 0.410 0.445 0.405 0.440 0.269 0.288 Exchange 336 0.366 0.455 0.371 0.457 0.371 0.456 0.497 0.656 0.515 0.543 0.551 0.563 0.520 0.545 0.552 0.686 0.488 0.500 0.505 0.515 0.500 0.510 0.529 0.584 720 0.998 0.806 1.021 0.808 1.081 0.812 0.864 1.088 1.110 0.819 1.158 0.837 1.129 0.823 1.218 1.376 0.575 0.570 0.594 0.585 0.589 0.580 1.047 1.222

## 原始摘要

Time series forecasting aims to predict future values from historical observations and auxiliary features. We propose \textbf{SteerCast}, a retrieval-based latent steering method that improves decoder-only forecaster at inference time, without updating its parameters. SteerCast constructs a database from the training set by storing a representation of each history window together with a \emph{steering vector} computed in the forecaster's latent space, defined as the difference between representations induced by the ground-truth continuation and by the model's own prediction. At test time, SteerCast retrieves nearest neighbors for a query history, aggregates their steering vectors, and injects the resulting signal into the forecaster's hidden states at every step of autoregressive generation, guiding predictions toward trajectories consistent with similar training cases. Experiments across diverse multivariate benchmarks and multiple horizons show that SteerCast consistently improves forecasting accuracy over the fine-tuned backbone and retrieval-based baselines, while requiring no additional training beyond the original fine-tuning and using only the training set as a retrieval corpus.
