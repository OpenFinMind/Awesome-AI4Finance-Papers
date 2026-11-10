# In-Context Learning of Stochastic Differential Equations with Foundation Inference Models

NeurIPS 2025 · main · application

通用方法在金融任务、数据或明确案例上开展应用验证。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=ceCJPoZOKJ
- 摘要来源：https://neurips.cc/virtual/2025/poster/117073
- 本地 PDF：[打开](../../pdfs/NeurIPS/2025/neurips-2025-ceCJPoZOKJ__In_Context_Learning_of_Stochastic_Differential_Equations_with_Foundation_Inference_Models.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_review
- 主方向：Time Series / 时间序列
- 细分方向：Causality & Dynamics / 序列因果与动力学
- 技术方法标签：Diffusion & Flow / 扩散与流模型；Uncertainty & Robustness / 不确定性与鲁棒性；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：diffusion；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

We demonstrate that FIM-SDE achieves robust *in-context* function estimation across a wide range of synthetic and real-world processes --- from canonical SDE systems (*e.g*., double-well dynamics or weakly perturbed Lorenz attractors) to stock price recordings and oil-price and wind-speed fluctuations --- while matching the performance of symbolic, Gaussian process and Neural SDE baselines trained on the target datasets.

## 原始摘要

Stochastic differential equations (SDEs) describe dynamical systems where deterministic flows, governed by a drift function, are superimposed with random fluctuations, dictated by a diffusion function. The accurate estimation (*or discovery*) of these functions from data is a central problem in machine learning, with wide application across the natural and social sciences. Yet current solutions either rely heavily on prior knowledge of the dynamics or involve intricate training procedures. We introduce FIM-SDE (Foundation Inference Model for SDEs), a pretrained recognition model that delivers accurate *in-context* (or zero-shot) estimation of the drift and diffusion functions of *low-dimensional* SDEs, from noisy time series data, and allows rapid *finetuning* to target datasets. Leveraging concepts from amortized inference and neural operators, we (pre)train FIM-SDE in a supervised fashion to map a large set of noisy, discretely observed SDE paths onto the space of drift and diffusion functions. We demonstrate that FIM-SDE achieves robust *in-context* function estimation across a wide range of synthetic and real-world processes --- from canonical SDE systems (*e.g*., double-well dynamics or weakly perturbed Lorenz attractors) to stock price recordings and oil-price and wind-speed fluctuations --- while matching the performance of symbolic, Gaussian process and Neural SDE baselines trained on the target datasets. When *finetuned* to the target processes, we show that FIM-SDE consistently outperforms all these baselines.
