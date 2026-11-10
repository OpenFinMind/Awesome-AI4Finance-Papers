# Zero-shot Forecasting by Simulation Alone

ICLR 2026 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：M4-yearly。M4 年度至日度子集包含金融序列，未把仅使用 M4 Hourly 的论文据此纳入。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=ZOLUTSU5gk
- 摘要来源：https://iclr.cc/virtual/2026/poster/10008812
- 本地 PDF：[打开](../../pdfs/ICLR/2026/iclr-2026-ZOLUTSU5gk__Zero_shot_Forecasting_by_Simulation_Alone.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；Representation & Foundation Models / 表征与基础模型；Generation & Simulation / 序列生成与仿真
- 技术方法标签：Generative Modeling / 生成建模
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

clude large portions of the M4 competition data, whose dominant frequencies are annual (A), quarterly (Q), and monthly (M). In fact, the Annual and Quarterly splits in GiftEval consist exclusively of M4-yearly and M4-quarterly, respectively. The Monthly split aggregates five 35 10S 10T 15T 5T A D H M Q W Chronos-Base 2.481 1.088 0.887 0.862 0.918 0.714 0.791 0.857 0.768 0.762 Chronos-Small 2.479 1.204 0.919 0.872 0.943 0.737 0.

## 原始摘要

Zero-shot time-series forecasting holds great promise, but is still in its infancy, hindered by limited and biased data corpora, leakage-prone evaluation, and privacy and licensing constraints. Motivated by these challenges, we propose the first practical univariate time series simulation pipeline which is simultaneously fast enough for on-the-fly data generation and enables notable zero-shot forecasting performance on M-Series and GiftEval benchmarks that capture trend/seasonality/intermittency patterns, typical of industrial forecasting applications. Our simulator, which we call SarSim (SARIMA Simulator for Zero-Shot Forecasting), is based off of a seasonal autoregressive integrated moving average (SARIMA) model as its core data source. Due to instability in the autoregressive component, naive SARIMA simulation often leads to unusable paths. Instead, we follow a three-step procedure: (1) we sample well-behaved trajectories from its characteristic polynomial stability region; (2) we introduce a superposition scheme that combines multiple paths into rich multi-seasonality traces; and (3) we add rate-based heavy-tailed noise models to capture burstiness and intermittency alongside seasonalities and trends. SarSim is orders of magnitude faster than kernel-based generators, and it enables training on circa 1B unique purely simulated series, generated on the fly; after which well-established neural network backbones exhibit strong zero-shot generalization, surpassing strong statistical forecasters and recent foundation baselines, while operating under strict zero-shot protocol. Notably, on GiftEval we observe a "student-beats-teacher" effect: models trained on our simulations exceed the forecasting accuracy of the AutoARIMA generating processes.
