# CombinationTS: A Modular Framework for Understanding Time-Series Forecasting Models

ICML 2026 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：Exchange-Rate。 主题：Time Series / 时间序列；Market Prediction / 股价、收益与波动率预测。

- 官方论文页：https://openreview.net/forum?id=CwHRT46VmC
- 摘要来源：https://icml.cc/virtual/2026/poster/65509
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-CwHRT46VmC__CombinationTS_A_Modular_Framework_for_Understanding_Time_Series_Forecasting_Models.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；FX & Crypto Forecasts / 汇率与加密资产预测
- 技术方法标签：Uncertainty & Robustness / 不确定性与鲁棒性；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

generalization. On Multi-Scale Downsampling, and Residual Cycle Forecast- the volatile Exchange-Rate dataset, Identity-based models ing—with RevIN as the shared normalization baseline. (PatchLinear) still achieve the lowest average MSE (Ta- ble 19), ruling out benchmark periodicity as a confound.

## 原始摘要

Recent progress in time-series forecasting has led to rapidly increasing architectural complexity, yet many reported State-of-the-Art gains are statistically fragile or misattributed. We argue that progress requires a shift from model selection to modular attribution, identifying which components truly drive performance. We propose CombinationTS, a self-contained probabilistic evaluation framework grounded in Evaluatology, the science of uncovering the effects. It decomposes forecasting models into orthogonal modules—Input Transformation, Embedding, Encoder, Decoder, and Output Transformation—and evaluates them under a shared evaluation condition space. By quantifying each component via marginalized performance ($\mu$) and stability ($\sigma$), CombinationTS enables robust attribution beyond fragile point estimates. Through large-scale paired evaluation, we uncover the Identity Paradox: once the data view (Embedding) is well-designed, a parameter-free Identity Encoder often matches or outperforms complex backbones.
