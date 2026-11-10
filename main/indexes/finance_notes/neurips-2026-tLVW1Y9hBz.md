# Generating Financial Time Series by Matching Random Convolutional Features

NeurIPS 2026 · main · core

以金融市场为研究对象，或包含明确的金融领域数据和应用评测。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=tLVW1Y9hBz
- 摘要来源：https://neurips.cc/Downloads/2026
- 本地 PDF：[打开](../../pdfs/NeurIPS/2026/neurips-2026-tLVW1Y9hBz__Generating_Financial_Time_Series_by_Matching_Random_Convolutional_Features.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_financial_task_or_data
- 主方向：Time Series / 时间序列
- 细分方向：Representation & Foundation Models / 表征与基础模型；Generation & Simulation / 序列生成与仿真
- 技术方法标签：Diffusion & Flow / 扩散与流模型；Generative Modeling / 生成建模；Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：diffusion；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Generating realistic financial time series is challenging as training data is often limited to a single historical path. / We show that generators trained by matching random SOCK features consistently outperform signature and diffusion baselines across a wide range of small-sample financial datasets.

## 原始摘要

Generating realistic financial time series is challenging as training data is often limited to a single historical path. With such scarce data, overfitting is hard to avoid, especially under adversarial training where a trained discriminator can memorize the training samples. To mitigate this, recent approaches train generators to minimize the discrepancy between untrained feature representations of real and generated time series. In these works, the feature maps are based on path signatures, which can fail to capture relevant time series properties at tractable truncation depths. In this work, we instead train generators by matching random convolutional features of real and generated time series. Existing random convolutional feature maps, such as Rocket and Hydra, have been shown to provide informative representations of real-world time series, but cannot supervise generative models because they are non-differentiable. We introduce **SOCK** (***SO**ft **C**ompeting **K**ernels*), a fully differentiable random convolutional feature map, suited to train generative time series models. We show that generators trained by matching random SOCK features consistently outperform signature and diffusion baselines across a wide range of small-sample financial datasets. We further demonstrate SOCK's expressiveness on two-sample hypothesis testing and time series classification tasks, where SOCK matches or outperforms existing unsupervised feature maps.
