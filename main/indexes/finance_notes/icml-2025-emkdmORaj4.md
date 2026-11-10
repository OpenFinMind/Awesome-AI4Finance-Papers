# Shifting Time: Time-series Forecasting with Khatri-Rao Neural Operators

ICML 2025 · main · application

正文包含金融数据、金融任务或金融领域评测。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=emkdmORaj4
- 摘要来源：https://icml.cc/virtual/2025/poster/44565
- 本地 PDF：[打开](../../pdfs/ICML/2025/icml-2025-emkdmORaj4__Shifting_Time_Time_series_Forecasting_with_Khatri_Rao_Neural_Operators.pdf)；版本：publisher_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测
- 技术方法标签：未明确标注
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

series containing the positions of NBA is a collection of 100,000 univariate time series from diverse basketball players. The goal here is to forecast the positions domains such as finance and demographics. This collection of the players. For both datasets, we utilized the same train- comprises six datasets corresponding to different seasonal- ing, validation, and test data as used by Wang et al. (2023). ities, varying from hourly to yearly. On thi

## 原始摘要

We present an operator-theoretic framework for temporal and spatio-temporal forecasting based on learning a *continuous time-shift operator*. Our operator learning paradigm offers a continuous relaxation of the discrete lag factor used in traditional autoregressive models, enabling the history of a system up to a given time to be mapped to its future values. We parametrize the time-shift operator using Khatri-Rao neural operators (KRNOs), a novel architecture based on non-stationary integral transforms with nearly linear computational scaling. Our framework naturally handles irregularly sampled observations and enables forecasting at super-resolution in both space and time. Extensive numerical studies across diverse temporal and spatio-temporal benchmarks demonstrate that our approach achieves state-of-the-art or competitive performance with leading methods.
