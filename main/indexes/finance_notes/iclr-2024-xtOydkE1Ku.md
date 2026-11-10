# TACTiS-2: Better, Faster, Simpler Attentional Copulas for Multivariate Time Series

ICLR 2024 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：fred-md。 主题：Time Series / 时间序列；Macro & Economic Forecasting / 宏观经济与预测。

- 官方论文页：https://openreview.net/forum?id=xtOydkE1Ku
- 摘要来源：https://iclr.cc/virtual/2024/poster/17439
- 本地 PDF：[打开](../../pdfs/ICLR/2024/iclr-2024-xtOydkE1Ku__TACTiS_2_Better_Faster_Simpler_Attentional_Copulas_for_Multivariate_Time_Series.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；Probabilistic Forecasting & Calibration / 概率预测与校准；Macro Indicators & Policy / 宏观指标与政策
- 技术方法标签：Transformer / Transformer模型
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：copula；copulas；time series；transformer
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/ServiceNow/TACTiS.

## 纳入依据

994) estimator. Average ranks report the average ranking of methods across all evaluation windows and datasets. Lower is better and the best results are in bold. Model electricity fred-md kdd-cup solar-10min traffic Avg. Rank Auto-ARIMA 0.077 ± 0.016 0.043 ± 0.005 0.625 ± 0.066 0.994 ± 0.216 0.222 ± 0.005 6.2 ± 0.3 ETS 0.059 ± 0.011 0.037 ± 0.010 0.408 ± 0.030 0.678 ± 0.097 0.353 ± 0.011 6.0 ± 0.2 TempFlow 0.075 ± 0.024 0.095 ± 0.004 0.250 ± 0.010

## 原始摘要

We introduce a new model for multivariate probabilistic time series prediction, designed to flexibly address a range of tasks including forecasting, interpolation, and their combinations. Building on copula theory, we propose a simplified objective for the recently-introduced transformer-based attentional copulas (TACTiS), wherein the number of distributional parameters now scales linearly with the number of variables instead of factorially. The new objective requires the introduction of a training curriculum, which goes hand-in-hand with necessary changes to the original architecture. We show that the resulting model has significantly better training dynamics and achieves state-of-the-art performance across diverse real-world forecasting tasks, while maintaining the flexibility of prior work, such as seamless handling of unaligned and unevenly-sampled time series. Code is made available at https://github.com/ServiceNow/TACTiS.
