# Neural MJD: Neural Non-Stationary Merton Jump Diffusion for Time Series Prediction

NeurIPS 2025 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：S&P 500。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=Xic1sPAmfC
- 摘要来源：https://neurips.cc/virtual/2025/poster/117485
- 本地 PDF：[打开](../../pdfs/NeurIPS/2025/neurips-2025-Xic1sPAmfC__Neural_MJD_Neural_Non_Stationary_Merton_Jump_Diffusion_for_Time_Series_Prediction.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Causality & Dynamics / 序列因果与动力学
- 技术方法标签：Diffusion & Flow / 扩散与流模型；Uncertainty & Robustness / 不确定性与鲁棒性；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：diffusion；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/DSL-Lab/neural-MJD.

## 纳入依据

models like DDPM [45], EDM [84], and flow matching (FM) [47]. We include recent neural ODE or SDE based learning methods such as NeuralCDE [33] and LatentSDE [59] for comparisons. NJ-ODE [85] was further included on the S&P 500 dataset. We also design a baseline model, Neural BS, which shares the same architecture as Neural MJD but omits the jump component. For DDPM, EDM, FM, Neural BS, and Neural MJD, we share the same transformer-based backbone to ensure a fair comparison. Since some datasets contain graph-structured data as seen in the following section, we incorporat

## 原始摘要

While deep learning methods have achieved strong performance in time series prediction, their black-box nature and inability to explicitly model underlying stochastic processes often limit their robustness handling non-stationary data, especially in the presence of abrupt changes. In this work, we introduce Neural MJD, a neural network based non-stationary Merton jump diffusion (MJD) model. Our model explicitly formulates forecasting as a stochastic differential equation (SDE) simulation problem, combining a time-inhomogeneous Itô diffusion to capture non-stationary stochastic dynamics with a time-inhomogeneous compound Poisson process to model abrupt jumps. To enable tractable learning, we introduce a likelihood truncation mechanism that caps the number of jumps within small time intervals and provide a theoretical error bound for this approximation. Additionally, we propose an Euler-Maruyama with restart solver, which achieves a provably lower error bound in estimating expected states and reduced variance compared to the standard solver. Experiments on both synthetic and real-world datasets demonstrate that Neural MJD consistently outperforms state-of-the-art deep learning and statistical learning methods. Our code is available at https://github.com/DSL-Lab/neural-MJD.
