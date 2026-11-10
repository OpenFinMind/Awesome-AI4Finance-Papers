# ARM: Refining Multivariate Forecasting with Adaptive Temporal-Contextual Learning

ICLR 2024 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：Exchange benchmark (currency series)。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=JWpwDdVbaM
- 摘要来源：https://iclr.cc/virtual/2024/poster/18939
- 本地 PDF：[打开](../../pdfs/ICLR/2024/iclr-2024-JWpwDdVbaM__ARM_Refining_Multivariate_Forecasting_with_Adaptive_Temporal_Contextual_Learning.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测
- 技术方法标签：Transformer / Transformer模型
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：time series；Transformer；Transformers
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

95 Traffic (720) 0.425 0.294 0.432 0.286 0.466 0.315 0.626 0.382 0.660 0.408 0.864 0.472 2.811 1.097 Exchange (96) 0.078 0.197 0.087 0.207 0.081 0.203 0.148 0.278 0.197 0.323 0.847 0.752 0.081 0.196 Exchange (192) 0.150 0.280 0.194 0.316 0.157 0.293 0.271 0.380 0.300 0.369 1.204 0.895 0.167 0.289 Exchange (336) 0.252 0.367 0.351 0.432 0.305 0.414 0.460 0.500 0.509 0.524 1.672 1.036 0.305 0.396 Exchan

## 原始摘要

Long-term time series forecasting (LTSF) is important for various domains but is confronted by challenges in handling the complex temporal-contextual relationships. As multivariate input models underperforming some recent univariate counterparts, we posit that the issue lies in the inefficiency of existing multivariate LTSF Transformers to model series-wise relationships: the characteristic differences between series are often captured incorrectly. To address this, we introduce ARM: a multivariate temporal-contextual adaptive learning method, which is an enhanced architecture specifically designed for multivariate LTSF modelling. ARM employs Adaptive Univariate Effect Learning (**A**UEL), Random Dropping (**R**D) training strategy, and Multi-kernel Local Smoothing (**M**KLS), to better handle individual series temporal patterns and correctly learn inter-series dependencies. ARM demonstrates superior performance on multiple benchmarks without significantly increasing computational costs compared to vanilla Transformer, thereby advancing the state-of-the-art in LTSF. ARM is also generally applicable to other LTSF architecture beyond vanilla Transformer.
