# iTransformer: Inverted Transformers Are Effective for Time Series Forecasting

ICLR 2024 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：Exchange benchmark (currency series)。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=JePfAI8fah
- 摘要来源：https://iclr.cc/virtual/2024/poster/18933
- 本地 PDF：[打开](../../pdfs/ICLR/2024/iclr-2024-JePfAI8fah__iTransformer_Inverted_Transformers_Are_Effective_for_Time_Series_Forecasting.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测
- 技术方法标签：Transformer / Transformer模型；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：time series；Transformer；Transformers
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/thuml/iTransformer.

## 纳入依据

338 ETT (Avg) 0.383 0.399 0.380 0.392 0.381 0.397 0.685 0.578 0.482 0.470 0.391 0.404 0.442 0.444 0.689 0.597 0.408 0.428 0.471 0.464 0.465 0.459 Exchange 0.360 0.403 0.378 0.417 0.367 0.404 0.940 0.707 0.370 0.413 0.416 0.443 0.354 0.414 0.750 0.626 0.519 0.429 0.461 0.454 0.613 0.539 Traffic 0.428 0.282 0.626 0.378 0.481 0.304 0.550 0.304 0.760 0.473 0.620 0.336 0.625 0.383 0.804 0.509 0.610 0.376 0.624 0.340 0.628 0.379 Weather 0.258 0.278 0.272 0.291 0.259 0.281 0.259 0.315 0.271 0.320 0.259 0.287 0.265 0.317 0.292 0.363 0.309 0.360 0.288 0.314 0

## 原始摘要

The recent boom of linear forecasting models questions the ongoing passion for architectural modifications of Transformer-based forecasters. These forecasters leverage Transformers to model the global dependencies over temporal tokens of time series, with each token formed by multiple variates of the same timestamp. However, Transformers are challenged in forecasting series with larger lookback windows due to performance degradation and computation explosion. Besides, the embedding for each temporal token fuses multiple variates that represent potential delayed events and distinct physical measurements, which may fail in learning variate-centric representations and result in meaningless attention maps. In this work, we reflect on the competent duties of Transformer components and repurpose the Transformer architecture without any modification to the basic components. We propose iTransformer that simply applies the attention and feed-forward network on the inverted dimensions. Specifically, the time points of individual series are embedded into variate tokens which are utilized by the attention mechanism to capture multivariate correlations; meanwhile, the feed-forward network is applied for each variate token to learn nonlinear representations. The iTransformer model achieves state-of-the-art on challenging real-world datasets, which further empowers the Transformer family with promoted performance, generalization ability across different variates, and better utilization of arbitrary lookback windows, making it a nice alternative as the fundamental backbone of time series forecasting. Code is available at this repository: https://github.com/thuml/iTransformer.
