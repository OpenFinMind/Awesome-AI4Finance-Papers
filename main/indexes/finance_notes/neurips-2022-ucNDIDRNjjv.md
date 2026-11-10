# Non-stationary Transformers: Exploring the Stationarity in Time Series Forecasting

NeurIPS 2022 · main · application

实验使用汇率、宏观金融、信用评估或财务文档等金融相关基准。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=ucNDIDRNjjv
- 摘要来源：https://neurips.cc/virtual/2022/poster/55235
- 本地 PDF：[打开](../../pdfs/NeurIPS/2022/neurips-2022-ucNDIDRNjjv__Non_stationary_Transformers_Exploring_the_Stationarity_in_Time_Series_Forecasting.pdf)；版本：publisher_version
- 金融依据类型：fulltext_financial_benchmark
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测
- 技术方法标签：Transformer / Transformer模型
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：time series；Transformer；Transformers
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/thuml/Nonstationary_Transformers.

## 纳入依据

tatistic indicates more stationary dataset. Dataset Variable Number Sampling Frequency Total Observations ADF Test Statistic Exchange 8 1 Day 7,588 -1.889 ILI 7 1 Week 966 -5.406 ETTm2 7 15 Minutes 69,680 -6.225 Electricity 321 1 Hour 26,304 -8.483 Traffic 862 1 Hou

## 原始摘要

Transformers have shown great power in time series forecasting due to their global-range modeling ability. However, their performance can degenerate terribly on non-stationary real-world data in which the joint distribution changes over time. Previous studies primarily adopt stationarization to attenuate the non-stationarity of original series for better predictability. But the stationarized series deprived of inherent non-stationarity can be less instructive for real-world bursty events forecasting. This problem, termed over-stationarization in this paper, leads Transformers to generate indistinguishable temporal attentions for different series and impedes the predictive capability of deep models. To tackle the dilemma between series predictability and model capability, we propose Non-stationary Transformers as a generic framework with two interdependent modules: Series Stationarization and De-stationary Attention. Concretely, Series Stationarization unifies the statistics of each input and converts the output with restored statistics for better predictability. To address the over-stationarization problem, De-stationary Attention is devised to recover the intrinsic non-stationary information into temporal dependencies by approximating distinguishable attentions learned from raw series. Our Non-stationary Transformers framework consistently boosts mainstream Transformers by a large margin, which reduces MSE by 49.43% on Transformer, 47.34% on Informer, and 46.89% on Reformer, making them the state-of-the-art in time series forecasting. Code is available at this repository: https://github.com/thuml/Nonstationary_Transformers.
