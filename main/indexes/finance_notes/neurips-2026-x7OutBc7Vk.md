# DiffPTS: Rethinking Diffusion ELBO for Probabilistic Time Series Forecasting

NeurIPS 2026 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：Exchange Rate。 主题：Time Series / 时间序列；Market Prediction / 股价、收益与波动率预测。

- 官方论文页：https://openreview.net/forum?id=x7OutBc7Vk
- 摘要来源：https://neurips.cc/Downloads/2026
- 本地 PDF：[打开](../../pdfs/NeurIPS/2026/neurips-2026-x7OutBc7Vk__DiffPTS_Rethinking_Diffusion_ELBO_for_Probabilistic_Time_Series_Forecasting.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；Probabilistic Forecasting & Calibration / 概率预测与校准；FX & Crypto Forecasts / 汇率与加密资产预测
- 技术方法标签：Diffusion & Flow / 扩散与流模型；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：diffusion；Diffusion；optimization；time series；variational
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

4 Experiments 4.1 Experiment Setup Datasets. Following previous work [8, 33], we evaluate on nine real-world datasets: ETT {h1, h2, m1, m2}, Electricity (ECL), Influenza-like Illness (ILI), Exchange Rate (EXR), Traffic, and Solar Energy (Solar). All experiments adopt a input sequence length of 168 time steps, ILI uses 32 prediction steps, and other datasets follow 192 prediction steps. Data splits follow domain conventions: ETT datasets use 12/4/4-month partitions for training, validation, and testing; all other datasets employ a chronological 7:1:2 split ratio. We provide dataset details in Appendix B.1. Baselines.

## 原始摘要

Probabilistic time series forecasting requires modeling and predicting complex and time-varying distributions. Recently, Denoising Diffusion Probabilistic Model~(DDPM)-based approaches have shown promise by equipping the diffusion process with pretrained mean and variance estimators to accommodate distributional shift. However, these methods typically follow the standard DDPM framework and consider only partial components of the evidence lower bound (ELBO), treating the training of estimators as designed regression tasks separate from the variational inference framework.  To address this, we rethink the ELBO under the Location-Scale Noise Model (LSNM) and find that it naturally induces a Gaussian negative log likelihood objective for the estimators and inherently defines a joint training objective that unifies recent the diffusion paradigms for probabilistic forecasting. Building on this principled ELBO reformulation, we propose DiffPTS, a general framework that enables end-to-end optimization of all components within the ELBO. Across multiple benchmarks, DiffPTS consistently outperforms recent models, achieving state-of-the-art performance with an average CRPS/MSE reduction of over 14.53\%/16.55\% compared to existing diffusion-based methods. The code is provided at \url{https://anonymous.4open.science/r/DiffPTS}.
