# Diffusion-TS: Interpretable Diffusion for General Time Series Generation

ICLR 2024 · main · application

正文包含金融数据、金融训练数据、金融任务评测或具体金融场景案例。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=4h1apFjO99
- 摘要来源：https://iclr.cc/virtual/2024/poster/19451
- 本地 PDF：[打开](../../pdfs/ICLR/2024/iclr-2024-4h1apFjO99__Diffusion_TS_Interpretable_Diffusion_for_General_Time_Series_Generation.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；Generation & Simulation / 序列生成与仿真；Imputation & Irregular Series / 缺失与不规则序列
- 技术方法标签：Diffusion & Flow / 扩散与流模型；Generative Modeling / 生成建模；Transformer / Transformer模型
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：diffusion；Diffusion；time series；transformer；transformers
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

5 Published as a conference paper at ICLR 2024 4.1 DATASETS We use 4 real-world datasets and 2 simulated datasets in Table 11 to evaluate our method. Stocks is the Google stock price data from 2004 to 2019. Each observation represents one day and has 6 features. ETTh dataset contains the data collected from electricity transformers, including load and oil temperature that are recorded every 15 minutes between July 2016 and July 2018. Energy is a UCI appliance energy prediction dataset with 28 values. fMRI is a benchmark for ca

## 原始摘要

Denoising diffusion probabilistic models (DDPMs) are becoming the leading paradigm for generative models. It has recently shown breakthroughs in audio synthesis, time series imputation and forecasting. In this paper, we propose Diffusion-TS, a novel diffusion-based framework that generates multivariate time series samples of high quality by using an encoder-decoder transformer with disentangled temporal representations, in which the decomposition technique guides Diffusion-TS to capture the semantic meaning of time series while transformers mine detailed sequential information from the noisy model input. Different from existing diffusion-based approaches, we train the model to directly reconstruct the sample instead of the noise in each diffusion step, combining a Fourier-based loss term. Diffusion-TS is expected to generate time series satisfying both interpretablity and realness. In addition, it is shown that the proposed Diffusion-TS can be easily extended to conditional generation tasks, such as forecasting and imputation, without any model changes. This also motivates us to further explore the performance of Diffusion-TS under irregular settings. Finally, through qualitative and quantitative experiments, results show that Diffusion-TS achieves the state-of-the-art results on various realistic analyses of time series.
