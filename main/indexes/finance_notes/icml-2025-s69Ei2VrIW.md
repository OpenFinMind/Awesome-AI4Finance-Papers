# TimePro: Efficient Multivariate Long-term Time Series Forecasting with Variable- and Time-Aware Hyper-state

ICML 2025 · main · application

实验使用汇率、宏观金融、信用评估或财务文档等金融相关基准。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=s69Ei2VrIW
- 摘要来源：https://icml.cc/virtual/2025/poster/43851
- 本地 PDF：[打开](../../pdfs/ICML/2025/icml-2025-s69Ei2VrIW__TimePro_Efficient_Multivariate_Long_term_Time_Series_Forecasting_with_Variable_and_Time_Aware_Hyper_state.pdf)；版本：publisher_version
- 金融依据类型：fulltext_financial_benchmark
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测
- 技术方法标签：未明确标注
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/xwmaxwma/TimePro.

## 纳入依据

AE ECL 0.169 0.262 0.170 0.265 0.174 0.264 0.178 0.270 0.189 0.276 0.244 0.334 0.251 0.344 0.192 0.295 0.212 0.300 0.268 0.365 0.193 0.296 Exchange 0.352 0.399 0.367 0.408 0.361 0.402 0.360 0.403 0.367 0.404 0.940 0.707 0.370 0.413 0.416 0.443 0.354 0.414 0.750 0.626 0.461 0.454 Weather 0.251 0.276 0.251 0.276 0.255 0.278 0.258 0.278 0.256 0.279 0.259 0.315 0.271 0.320 0.259 0.287 0.265 0.317 0.292 0.363 0.288 0.314 Solar-Energy 0.232 0.266 0.240 0.273 0.229 0.256 0.233 0.262 0.236 0.266 0.641 0.639 0.347 0.417 0.301 0.319 0.330 0.401 0.282 0.375 0.261

## 原始摘要

In long-term time series forecasting, different variables often influence the target variable over distinct time intervals, a challenge known as the multi-delay issue. Traditional models typically process all variables or time points uniformly, which limits their ability to capture complex variable relationships and obtain non-trivial time representations. To address this issue, we propose TimePro, an innovative Mamba-based model that constructs variate- and time-aware hyper-states. Unlike conventional approaches that merely transfer plain states across variable or time dimensions, TimePro preserves the fine-grained temporal features of each variate token and adaptively selects the focused time points to tune the plain state. The reconstructed hyper-state can perceive both variable relationships and salient temporal information, which helps the model make accurate forecasting. In experiments, TimePro performs competitively on eight real-world long-term forecasting benchmarks with satisfactory linear complexity. Code is available at https://github.com/xwmaxwma/TimePro.
