# TimeBridge: Non-Stationarity Matters for Long-term Time Series Forecasting

ICML 2025 · main · application

通用方法在金融任务、数据或明确案例上开展应用验证。 主题：Time Series / 时间序列；Market Prediction / 股价、收益与波动率预测。

- 官方论文页：https://openreview.net/forum?id=pyKO0ZZ5lz
- 摘要来源：https://icml.cc/virtual/2025/poster/43973
- 本地 PDF：[打开](../../pdfs/ICML/2025/icml-2025-pyKO0ZZ5lz__TimeBridge_Non_Stationarity_Matters_for_Long_term_Time_Series_Forecasting.pdf)；版本：publisher_version
- 金融依据类型：title_abstract_review
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；Stock Movement & Returns / 股价方向与收益预测
- 技术方法标签：Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：time series
- 数据 / 评测名称（题名和摘要可确认）：CSI 500；S&P 500
- 代码链接：https://github.com/Hank0626/TimeBridge.

## 纳入依据

Additionally, TimeBridge demonstrates exceptional performance in financial forecasting on the CSI 500 and S&P 500 indices, further validating its robustness and effectiveness.

## 原始摘要

Non-stationarity poses significant challenges for multivariate time series forecasting due to the inherent short-term fluctuations and long-term trends that can lead to spurious regressions or obscure essential long-term relationships. Most existing methods either eliminate or retain non-stationarity without adequately addressing its distinct impacts on short-term and long-term modeling. Eliminating non-stationarity is essential for avoiding spurious regressions and capturing local dependencies in short-term modeling, while preserving it is crucial for revealing long-term cointegration across variates. In this paper, we propose TimeBridge, a novel framework designed to bridge the gap between non-stationarity and dependency modeling in long-term time series forecasting. By segmenting input series into smaller patches, TimeBridge applies Integrated Attention to mitigate short-term non-stationarity and capture stable dependencies within each variate, while Cointegrated Attention preserves non-stationarity to model long-term cointegration across variates. Extensive experiments show that TimeBridge consistently achieves state-of-the-art performance in both short-term and long-term forecasting. Additionally, TimeBridge demonstrates exceptional performance in financial forecasting on the CSI 500 and S&P 500 indices, further validating its robustness and effectiveness. Code is available at https://github.com/Hank0626/TimeBridge.
