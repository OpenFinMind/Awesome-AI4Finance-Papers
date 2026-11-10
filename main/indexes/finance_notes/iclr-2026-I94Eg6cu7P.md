# SRT: Super-Resolution for Time Series via Disentangled Rectified Flow

ICLR 2026 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：exchange rates。 主题：Time Series / 时间序列；Trading & Microstructure / 交易与市场微观结构；Market Prediction / 股价、收益与波动率预测。

- 官方论文页：https://openreview.net/forum?id=I94Eg6cu7P
- 摘要来源：https://iclr.cc/virtual/2026/poster/10010334
- 本地 PDF：[打开](../../pdfs/ICLR/2026/iclr-2026-I94Eg6cu7P__SRT_Super_Resolution_for_Time_Series_via_Disentangled_Rectified_Flow.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：General Time-Series Methods / 综合序列方法；Trading & Execution / 交易策略与执行；FX & Crypto Forecasts / 汇率与加密资产预测
- 技术方法标签：Diffusion & Flow / 扩散与流模型；Uncertainty & Robustness / 不确定性与鲁棒性；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

ily spot prices for gold, crude oil, and natural gas. For all commodities, data is collected for all trading days within the period from June 15, 2022 to June 13, 2025. Currency rate. We select daily exchange rates of major currency pairs against the US dollar, in- cluding EUR/USD, JPY/USD, GBP/USD, CNY/USD, AUD/USD, CAD/USD, and CHF/USD. His- torical data from June 15, 2020 to June 13, 2025 is collected, corresponding to trading days within this period. Power. The public dataset ‘ElectricityLoadDiagrams20112014’ 3 is utilized. We follow the idea of Informer and preprocess the dataset into hourly format. Retail. The public dat

## 原始摘要

Fine-grained time series data with high temporal resolution is critical for accurate analytics across a wide range of applications. However, the acquisition of such data is often limited by cost and feasibility. This problem can be tackled by reconstructing high-resolution signals from low-resolution inputs based on specific priors, known as super-resolution. While extensively studied in computer vision, directly transferring image super-resolution techniques to time series is not trivial. To address this challenge at a fundamental level, we propose **S**uper-**R**esolution for **T**ime series (SRT), a novel framework that reconstructs temporal patterns lost in low-resolution inputs via disentangled rectified flow. SRT decomposes the input into trend and seasonal components, aligns them to the target resolution using an implicit neural representation, and leverages a novel cross-resolution attention mechanism to guide the generation of high-resolution details. We further introduce SRT-large, a scaled-up version with extensive pretraining, which enables strong zero-shot super-resolution capability. Extensive experiments on nine public datasets demonstrate that SRT and SRT-large consistently outperform existing methods across multiple scale factors, showing both robust performance and the effectiveness of each component in our architecture.
