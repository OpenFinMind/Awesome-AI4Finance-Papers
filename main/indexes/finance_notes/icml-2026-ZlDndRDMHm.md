# Reviving Error Correction in Modern Deep Time-Series Forecasting

ICML 2026 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：Exchange-Rate。 主题：Time Series / 时间序列；Market Prediction / 股价、收益与波动率预测。

- 官方论文页：https://openreview.net/forum?id=ZlDndRDMHm
- 摘要来源：https://icml.cc/virtual/2026/poster/63134
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-ZlDndRDMHm__Reviving_Error_Correction_in_Modern_Deep_Time_Series_Forecasting.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；FX & Crypto Forecasts / 汇率与加密资产预测
- 技术方法标签：Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

denote performance degradation. We further extend our evaluation to additional datasets, in- cluding Solar-Energy, Exchange-Rate, and ILI, using two Table 1 and Appendix Table 8 summarize the results for im- representative backbones (TimeMixer and TimesNet). The provements in MSE and MAE, respectively. Overall, most results in Table 3 show that UEC-STD remains effective, architectures, particularly MLP and

## 原始摘要

Modern deep-learning models have achieved remarkable success in time-series forecasting. Yet, their performance degrades in long-term prediction due to error accumulation in autoregressive inference, where predictions are recursively used as inputs. While classical error correction mechanisms (ECMs) have long been used in statistical methods, their applicability to deep learning models remains limited or ineffective. In this work, we revisit the error accumulation problem in deep time-series forecasting and investigate the role and necessity of ECMs in this new context. We propose a simple, architecture-agnostic error correction model that can be integrated with any existing forecaster without requiring retraining. By explicitly decomposing predictions into trend and seasonal components and training the corrector to adjust each separately, we introduce the Universal Error Corrector with Seasonal–Trend Decomposition (UEC-STD), which significantly improves correction accuracy and robustness across 4 backbones and 10 datasets. Our findings provide a practical tool for enhancing forecasts while offering new insights into mitigating autoregressive errors in deep time-series models.
