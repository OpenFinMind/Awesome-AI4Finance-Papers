# Winner-takes-all for Multivariate Probabilistic Time Series Forecasting

ICML 2025 · main · application

正文包含金融数据、金融任务或金融领域评测。 主题：Time Series / 时间序列；Market Prediction / 股价、收益与波动率预测；Blockchain & Digital Assets / 区块链与数字资产。

- 官方论文页：https://openreview.net/forum?id=4QcFfTu6UT
- 摘要来源：https://icml.cc/virtual/2025/poster/46485
- 本地 PDF：[打开](../../pdfs/ICML/2025/icml-2025-4QcFfTu6UT__Winner_takes_all_for_Multivariate_Probabilistic_Time_Series_Forecasting.pdf)；版本：publisher_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；Probabilistic Forecasting & Calibration / 概率预测与校准；FX & Crypto Forecasts / 汇率与加密资产预测；Crypto & Blockchain Transactions / 加密资产与链上交易
- 技术方法标签：Generative Modeling / 生成建模
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

8 Winner-takes-all for Multivariate Probabilistic Time Series Forecasting Figure 4. Cryptocurrency price forecasting for January 4, 2025 with K = 4 hypotheses. Setup in described in Section 6.4. Legend is the same as in Figure 3. We see that TimeMCL produces at least one hypothesis that closely matches the realized trajectory. We expect each hypothesis to specialize in a distinct market scenario, for example, a trend reversal or a sudden collap

## 原始摘要

We introduce $\texttt{TimeMCL}$, a method leveraging the Multiple Choice Learning (MCL) paradigm to forecast multiple plausible time series futures. Our approach employs a neural network with multiple heads and utilizes the Winner-Takes-All (WTA) loss to promote diversity among predictions. MCL has recently gained attention due to its simplicity and ability to address ill-posed and ambiguous tasks. We propose an adaptation of this framework for time-series forecasting, presenting it as an efficient method to predict diverse futures, which we relate to its implicit *quantization* objective. We provide insights into our approach using synthetic data and evaluate it on real-world time series, demonstrating its promising performance at a light computational cost.
