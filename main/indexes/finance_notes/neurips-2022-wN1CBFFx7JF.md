# Theoretical analysis of deep neural networks for temporally dependent observations

NeurIPS 2022 · main · application

包含明确的金融任务、金融领域数据或金融案例验证。 主题：Time Series / 时间序列；Macro & Economic Forecasting / 宏观经济与预测。

- 官方论文页：https://openreview.net/forum?id=wN1CBFFx7JF
- 摘要来源：https://neurips.cc/virtual/2022/poster/53665
- 本地 PDF：[打开](../../pdfs/NeurIPS/2022/neurips-2022-wN1CBFFx7JF__Theoretical_analysis_of_deep_neural_networks_for_temporally_dependent_observations.pdf)；版本：publisher_version
- 金融依据类型：title_abstract_financial_task_or_data
- 主方向：Macro & Economic Forecasting / 宏观经济与预测
- 细分方向：General Time-Series Methods / 综合序列方法；Macro Indicators & Policy / 宏观指标与政策
- 技术方法标签：未明确标注
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

The theoretical results are supported via various numerical simulation settings as well as an application to a macroeconomic data set.

## 原始摘要

Deep neural networks are powerful tools to model observations over time with non-linear patterns. Despite the widespread useof neural networks in such settings, most theoretical developments of deep neural networks are under the assumption of independent observations, and theoretical results for temporally dependent observations are scarce. To bridge this gap, we study theoretical properties of deep neural networks on modeling non-linear time series data. Specifically, non-asymptotic bounds for prediction error of (sparse) feed-forward neural network with ReLU activation function is established under mixing-type assumptions. These assumptions are mild such that they include a wide range of time series models including auto-regressive models. Compared to independent observations, established convergence rates have additional logarithmic factors to compensate for additional complexity due to dependence among data points. The theoretical results are supported via various numerical simulation settings as well as an application to a macroeconomic data set.
