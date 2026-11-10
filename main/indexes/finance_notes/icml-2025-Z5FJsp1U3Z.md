# LightGTS: A Lightweight General Time Series Forecasting Model

ICML 2025 · main · application

实验使用汇率、宏观金融、信用评估或财务文档等金融相关基准。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=Z5FJsp1U3Z
- 摘要来源：https://icml.cc/virtual/2025/poster/44879
- 本地 PDF：[打开](../../pdfs/ICML/2025/icml-2025-Z5FJsp1U3Z__LightGTS_A_Lightweight_General_Time_Series_Forecasting_Model.pdf)；版本：publisher_version
- 金融依据类型：fulltext_financial_benchmark
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；Representation & Foundation Models / 表征与基础模型
- 技术方法标签：Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

0.266 0.208 0.256 0.292 0.313 0.26 0.275 0.288 0.309 - - 0.270 0.300 Exchange 0.345 0.395 0.347 0.396 0.392 0.425 0.385 0.417 0.370 0.412 0.390 0.417 0.432 0.454 Solar 0.219 0.305 0.191 0.271 0.771 0.604 0.714 0.704 0.393 0.319 0.500 0.397 0.411 0.428 Electricity 0.233 0.319 0.213 0.308 0.297 0.375 0.18

## 原始摘要

Existing works on general time series forecasting build foundation models with heavy model parameters through large-scale multi-source pretraining. These models achieve superior generalization ability across various datasets at the cost of significant computational burdens and limitations in resource-constrained scenarios. This paper introduces LightGTS, a lightweight general time series forecasting model designed from the perspective of consistent periodical modeling. To handle diverse scales and intrinsic periods in multi-source pre-training, we introduce Periodical Tokenization, which extracts consistent periodic patterns across different datasets with varying scales. To better utilize the periodicity in the decoding process, we further introduce Periodical Parallel Decoding, which leverage historical tokens to improve forecasting. Based on the two techniques above which fully leverage the inductive bias of periods inherent in time series, LightGTS uses a lightweight model to achieve outstanding performance on general time series forecasting. It achieves state-of-the-art forecasting performance on 9 real-world benchmarks in both zero-shot and full-shot setting with much better efficiency compared with existing time series foundation models
