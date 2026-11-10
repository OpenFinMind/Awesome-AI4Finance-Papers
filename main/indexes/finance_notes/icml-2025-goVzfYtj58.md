# Exploring Representations and Interventions in Time Series Foundation Models

ICML 2025 · main · application

实验使用汇率、宏观金融、信用评估或财务文档等金融相关基准。 主题：Time Series / 时间序列；Market Prediction / 股价、收益与波动率预测。

- 官方论文页：https://openreview.net/forum?id=goVzfYtj58
- 摘要来源：https://icml.cc/virtual/2025/poster/44453
- 本地 PDF：[打开](../../pdfs/ICML/2025/icml-2025-goVzfYtj58__Exploring_Representations_and_Interventions_in_Time_Series_Foundation_Models.pdf)；版本：publisher_version
- 金融依据类型：fulltext_financial_benchmark
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；Representation & Foundation Models / 表征与基础模型；FX & Crypto Forecasts / 汇率与加密资产预测
- 技术方法标签：未明确标注
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

18 0.107 0.178 0.076 0.220 0.112 Electricity 0.372 0.250 0.446 0.342 0.716 0.757 0.428 0.327 0.727 0.819 Exchange rate 0.125 0.034 0.124 0.032 0.170 0.061 0.111 0.027 0.174 0.067 Illness 0.393 0.421 0.448 0.502 0.547 0.669 0.423 0.446 0.552 0.648 Traffic 0.492 0.790 0.552 0.906 0.861 1.562 0.606 0.940 0.878 1.633 Weather 0.129 0.079

## 原始摘要

Time series foundation models (TSFMs) promise to be powerful tools for a wide range of applications. However, their internal representations and learned concepts are still not well understood. In this study, we investigate the structure and redundancy of representations across various TSFMs, examining the self-similarity of model layers within and across different model sizes. This analysis reveals block-like redundancy in the representations, which can be utilized for informed pruning to improve inference speed and efficiency. We also explore the concepts learned by these models, such as periodicity and trends. We demonstrate how conceptual priors can be derived from TSFM representations and leveraged to steer its outputs toward concept-informed predictions. Our work bridges representational analysis from language and vision models to TSFMs, offering new methods for building more computationally efficient and transparent TSFMs.
