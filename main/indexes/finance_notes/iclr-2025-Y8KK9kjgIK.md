# SigDiffusions: Score-Based Diffusion Models for Time Series via Log-Signature Embeddings

ICLR 2025 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：Exchange Rates。 主题：Time Series / 时间序列；Market Prediction / 股价、收益与波动率预测。

- 官方论文页：https://openreview.net/forum?id=Y8KK9kjgIK
- 摘要来源：https://iclr.cc/virtual/2025/poster/32077
- 本地 PDF：[打开](../../pdfs/ICLR/2025/iclr-2025-Y8KK9kjgIK__SigDiffusions_Score_Based_Diffusion_Models_for_Time_Series_via_Log_Signature_Embeddings.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Representation & Foundation Models / 表征与基础模型；Generation & Simulation / 序列生成与仿真；FX & Crypto Forecasts / 汇率与加密资产预测
- 技术方法标签：Diffusion & Flow / 扩散与流模型；Generative Modeling / 生成建模；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：diffusion；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

0.551±.028 SigDiffusion (ours) 0.278±.062 0.057±.001 DDO (γ = 1) 0.326±.102 0.094±.004 Exchange Rates Diffusion-TS 0.401±.196 0.120±.016 CSPD-GP (RNN) 0.500±.001 0.273±.100 CSPD-GP (Transformer) 0.500±.000 0.432±.074 SigDiffusion (ours) 0.350±.080 0.168±.001 DDO (γ = 10) 0.356

## 原始摘要

Score-based diffusion models have recently emerged as state-of-the-art generativemodels for a variety of data modalities. Nonetheless, it remains unclear how toadapt these models to generate long multivariate time series. Viewing a timeseries as the discretisation of an underlying continuous process, we introduceSigDiffusion, a novel diffusion model operating on log-signature embeddingsof the data. The forward and backward processes gradually perturb and denoiselog-signatures while preserving their algebraic structure. To recover a signal fromits log-signature, we provide new closed-form inversion formulae expressing thecoefficients obtained by expanding the signal in a given basis (e.g. Fourier ororthogonal polynomials) as explicit polynomial functions of the log-signature.Finally, we show that combining SigDiffusions with these inversion formulaeresults in high-quality long time series generation, competitive with the currentstate-of-the-art on various datasets of synthetic and real-world examples.
