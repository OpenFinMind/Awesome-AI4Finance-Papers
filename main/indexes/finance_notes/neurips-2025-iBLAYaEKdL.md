# Constrained Posterior Sampling: Time Series Generation with Hard Constraints

NeurIPS 2025 · main · application

通用方法在金融任务、数据或明确案例上开展应用验证。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=iBLAYaEKdL
- 摘要来源：https://neurips.cc/virtual/2025/poster/116583
- 本地 PDF：[打开](../../pdfs/NeurIPS/2025/neurips-2025-iBLAYaEKdL__Constrained_Posterior_Sampling_Time_Series_Generation_with_Hard_Constraints.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_review
- 主方向：Time Series / 时间序列
- 细分方向：Generation & Simulation / 序列生成与仿真
- 技术方法标签：Diffusion & Flow / 扩散与流模型；Generative Modeling / 生成建模
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：diffusion；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Empirically, CPS outperforms state-of-the-art methods in sample quality and similarity to real time series by around 70\% and 22\%, respectively, on real-world stocks, traffic, and air quality datasets.

## 原始摘要

Generating realistic time series samples is crucial for stress-testing models and protecting user privacy by using synthetic data. In engineering and safety-critical applications, these samples must meet certain hard constraints that are domain-specific or naturally imposed by physics or nature. Consider, for example, generating electricity demand patterns with constraints on peak demand times. This can be used to stress-test the functioning of power grids during adverse weather conditions. Existing approaches for generating constrained time series are either not scalable or degrade sample quality. To address these challenges, we introduce Constrained Posterior Sampling (CPS), a diffusion-based sampling algorithm that aims to project the posterior mean estimate into the constraint set after each denoising update. Notably, CPS scales to a large number of constraints ($\sim100$) without requiring additional training. We provide theoretical justifications highlighting the impact of our projection step on sampling. Empirically, CPS outperforms state-of-the-art methods in sample quality and similarity to real time series by around 70\% and 22\%, respectively, on real-world stocks, traffic, and air quality datasets.
