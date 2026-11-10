# ReNF: Rethinking the Design of Neural Long-Term Time Series Forecasters

ICML 2026 · main · application

正文包含明确金融数据、金融任务或金融案例；金融应用可属于通用方法的一个实验。 主题：Time Series / 时间序列；Trading & Microstructure / 交易与市场微观结构；Macro & Economic Forecasting / 宏观经济与预测。

- 官方论文页：https://openreview.net/forum?id=emDhH9VFqm
- 摘要来源：https://icml.cc/virtual/2026/poster/62639
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-emDhH9VFqm__ReNF_Rethinking_the_Design_of_Neural_Long_Term_Time_Series_Forecasters.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；Probabilistic Forecasting & Calibration / 概率预测与校准；Trading & Execution / 交易策略与执行；Order Books & Market Impact / 订单簿与市场冲击；Macro Indicators & Policy / 宏观指标与政策
- 技术方法标签：Causal Learning / 因果学习；Uncertainty & Robustness / 不确定性与鲁棒性；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：causal；optimization；Time Series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/Luoauoa/ReNF}.

## 纳入依据

s Angeles during the spring of 2012, specifically from March to June. This data was collected at an interval of five minutes. The NASDAQ includes the daily NASDAQ index and key economic indicators from 2010 to 2024. The SP500 records daily SP500 index data (e.g., opening price, closing price, and trading volume) from January 1993 to February 2025. CarSales collects daily sales of 10 vehicle brands (e.g., Toyota, Honda) in the U.S. from January 2005 to June 2023. The data are compiled from the Vehicle Sales dataset on Kaggle. Power contains daily wind and solar energy p

## 原始摘要

Neural Forecasters (NFs) have become a cornerstone of Long-term Time Series Forecasting (LTSF). However, recent progress has been hampered by an overemphasis on architectural complexity at the expense of fundamental forecasting structures. In this work, we revisit principled designs of LTSF. We begin by formulating a Variance Reduction Hypothesis (VRH), positing that generating and combining multiple forecasts is essential to reducing the inherent uncertainty of NFs. Guided by this, we propose Boosted Direct Output (BDO), a streamlined paradigm that synergistically hybridizes the causal structure of Auto-Regressive (AR) with the stability of Direct Output (DO), while implicitly realizing the principle of forecast combination within a single network. Furthermore, we mitigate a critical validation-test generalization gap by employing parameter smoothing to stabilize optimization. Extensive experiments demonstrate that these trivial yet principled improvements enable a direct temporal MLP to outperform recent, complex state-of-the-art models in nearly all benchmarks, without relying on intricate inductive biases. Finally, we empirically verify our hypothesis, establishing a dynamic performance bound that highlights promising directions for future research. The code is publicly available at: \url{https://github.com/Luoauoa/ReNF}.
