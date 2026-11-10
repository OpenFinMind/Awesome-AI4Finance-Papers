# Universal Time Series Generation with Neural Controlled Differential Equations

NeurIPS 2026 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：Exchange benchmark (currency series)。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=iqICKB71X4
- 摘要来源：https://neurips.cc/virtual/2026/poster/150341
- 本地 PDF：[打开](../../pdfs/NeurIPS/2026/neurips-2026-iqICKB71X4__Universal_Time_Series_Generation_with_Neural_Controlled_Differential_Equations.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Generation & Simulation / 序列生成与仿真；Causality & Dynamics / 序列因果与动力学；Probabilistic Forecasting & Calibration / 概率预测与校准
- 技术方法标签：Diffusion & Flow / 扩散与流模型；Generative Modeling / 生成建模；Causal Learning / 因果学习；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：causal
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

sponding dataset. Results are reported as mean ± standard deviation over five random seeds. Best scores are in bold. Method Electr. Exchange KDDCup M4 (H) Solar Traffic UberTLC Wiki2000 TSFlow 2.050±0.308 1.060±0.366 7.192±0.481 3.687±0.194 5.758±0.125 3.971±0.135 13.521±2.936 13.685±6.216 G-SLiCE 1.958±0.264 1.059±0.384 7.192±0.481 3.441±0.213 4.086±0.280 3.175±0.163 13.431±3.052 13.874±6.394

## 原始摘要

Recent work on the sequence universality of State Space Models (SSMs) has introduced efficient, maximally expressive continuous-time approaches for time-series modelling. While these works focus on discriminative settings, we extend this perspective to generative time-series modelling by proving    that maximally expressive Structured Linear Controlled Differential Equations (SLiCEs) are universal time-series generators, in the sense that they can approximate the induced path laws of continuous causal pushforwards on compact latent sets in $W_\infty$. Building on these theoretical results, we propose Generative SLiCEs (G-SLiCEs), a maximally expressive continuous-time model for flow matching on path-space. Empirically, we show that expressivity improves performance in probabilistic forecasting and downstream tasks, while retaining the advantages of continuous-time models such as generalising to arbitrary observation grids. This is particularly beneficial for irregular grids, where fixed-grid models often struggle.
