# The Forecast After the Forecast: A Post-Processing Shift in Time Series

ICLR 2026 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：Exchange benchmark (currency series)。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=syfWdclGE1
- 摘要来源：https://iclr.cc/virtual/2026/poster/10007022
- 本地 PDF：[打开](../../pdfs/ICLR/2026/iclr-2026-syfWdclGE1__The_Forecast_After_the_Forecast_A_Post_Processing_Shift_in_Time_Series.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；Probabilistic Forecasting & Calibration / 概率预测与校准
- 技术方法标签：Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Conformal；Time series；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

0.220 0.301 6% 0.224 0.302 5% 0.517 0.344 0.492 0.329 5% 0.492 0.325 5% Exchange 0.249 0.332 0.241 0.332 2% 0.235 0.329 3% 0.094 0.213 0.090 0.206 3% 0.092 0.210 1% Weather 0.427 0.463 0.025 0.005 96% 0.039 0.059 89% 0.150 0.196 0.148 0.193 2% 0.143 0.191 4% ETTm1 0.121 0.217 0.078 0.190 24% 0.087 0

## 原始摘要

Time series forecasting has long been dominated by advances in model architecture, with recent progress driven by deep learning and hybrid statistical techniques. However, as forecasting models approach diminishing returns in accuracy, a critical yet underexplored opportunity emerges: the strategic use of post-processing. In this paper, we address the last-mile gap in time-series forecasting, which is to improve accuracy and uncertainty without retraining or modifying a deployed backbone. We propose $\delta$-Adapter, a lightweight, architecture-agnostic way to boost deployed time series forecasters without retraining. $\delta$-Adapter learns tiny, bounded modules at two interfaces: input nudging (soft edits to covariates) and output residual correction. We provide local descent guarantees, $O(\delta)$ drift bounds, and compositional stability for combined adapters. Meanwhile, it can act as a feature selector by learning a sparse, horizon-aware mask over inputs to select important features, thereby improving interpretability. In addition, it can also be used as a distribution calibrator to measure uncertainty. Thus, we introduce a Quantile Calibrator and a Conformal Corrector that together deliver calibrated, personalized intervals with finite-sample coverage.   Our experiments across diverse backbones and datasets show that $\delta$-Adapter improves accuracy and calibration with negligible compute and no interface changes.
