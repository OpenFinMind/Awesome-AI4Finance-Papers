# Autoformer: Decomposition Transformers with Auto-Correlation for Long-Term Series Forecasting

NeurIPS 2021 · main · application

实验使用汇率、宏观金融、信用评估或财务文档等金融相关基准。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=J4gRj6d5Qm
- 摘要来源：https://neurips.cc/virtual/2021/poster/28217
- 本地 PDF：[打开](../../pdfs/NeurIPS/2021/neurips-2021-J4gRj6d5Qm__Autoformer_Decomposition_Transformers_with_Auto_Correlation_for_Long_Term_Series_Forecasting.pdf)；版本：publisher_version
- 金融依据类型：fulltext_financial_benchmark
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测
- 技术方法标签：Transformer / Transformer模型
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：time series；Transformer；Transformers
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/thuml/Autoformer.

## 纳入依据

9 2.568 1.238 3.105 1.348 720 0.422 0.419 3.379 1.388 3.048 1.328 2.631 1.242 3.171 1.368 2.720 1.287 3.135 1.354 Exchange Electricity 96 0.201 0.317 0.274 0.368 0.258 0.357 0.312 0.402 0.680 0.645 0.375 0.437 0.985 0.813 192 0.222 0.334 0.296 0.386 0.266 0.368 0.348 0.433 0.725 0.676 0.442 0.473 0.996 0.821 336 0.231 0.338 0.300 0.394 0.280 0.380 0.350 0.433 0.828 0.727 0.439 0.473 1.000 0.824 720

## 原始摘要

Extending the forecasting time is a critical demand for real applications, such as extreme weather early warning and long-term energy consumption planning. This paper studies the long-term forecasting problem of time series. Prior Transformer-based models adopt various self-attention mechanisms to discover the long-range dependencies. However, intricate temporal patterns of the long-term future prohibit the model from finding reliable dependencies. Also, Transformers have to adopt the sparse versions of point-wise self-attentions for long series efficiency, resulting in the information utilization bottleneck. Going beyond Transformers, we design Autoformer as a novel decomposition architecture with an Auto-Correlation mechanism. We break with the pre-processing convention of series decomposition and renovate it as a basic inner block of deep models. This design empowers Autoformer with progressive decomposition capacities for complex time series. Further, inspired by the stochastic process theory, we design the Auto-Correlation mechanism based on the series periodicity, which conducts the dependencies discovery and representation aggregation at the sub-series level. Auto-Correlation outperforms self-attention in both efficiency and accuracy. In long-term forecasting, Autoformer yields state-of-the-art accuracy, with a 38% relative improvement on six benchmarks, covering five practical applications: energy, traffic, economics, weather and disease. Code is available at this repository: https://github.com/thuml/Autoformer.
