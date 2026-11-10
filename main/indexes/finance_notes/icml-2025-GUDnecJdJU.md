# Retrieval Augmented Time Series Forecasting

ICML 2025 · main · application

实验使用汇率、宏观金融、信用评估或财务文档等金融相关基准。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=GUDnecJdJU
- 摘要来源：https://icml.cc/virtual/2025/poster/45826
- 本地 PDF：[打开](../../pdfs/ICML/2025/icml-2025-GUDnecJdJU__Retrieval_Augmented_Time_Series_Forecasting.pdf)；版本：publisher_version
- 金融依据类型：fulltext_financial_benchmark
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测
- 技术方法标签：Retrieval & RAG / 检索与RAG
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：retrieval；Time series；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

.327 1.410 Electricity 0.160 0.182 0.216 0.193 0.196 0.225 0.214 0.193 0.227 0.311 Exchange 0.441 0.386 0.564 0.416 0.315 0.643 1.195 0.461 1.447 2.478 Illness 2.097 2.024 1.480 2.139 2.664 2.169 2.847 2.077 3.006 5.137 Solar 0.231 0.216 0.287 0.403 0.283 0.330 0.328 0.350 0.586 0.331 Traffic 0.434 0.484

## 原始摘要

Time series forecasting uses historical data to predict future trends, leveraging the relationships between past observations and available features. In this paper, we propose RAFT, a retrieval-augmented time series forecasting method to provide sufficient inductive biases and complement the model's learning capacity. When forecasting the subsequent time frames, we directly retrieve historical data candidates from the training dataset with patterns most similar to the input, and utilize the future values of these candidates alongside the inputs to obtain predictions. This simple approach augments the model's capacity by externally providing information about past patterns via retrieval modules. Our empirical evaluations on ten benchmark datasets show that RAFT consistently outperforms contemporary baselines with an average win ratio of 86%.
