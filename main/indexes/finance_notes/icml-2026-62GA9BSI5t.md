# Primal-Spectral Generative Modeling: Fast Analytical Generation via Pseudoinverse Lévy Inversion

ICML 2026 · main · application

通用方法在金融任务、数据或明确案例上开展应用验证。 主题：Time Series / 时间序列；Market Prediction / 股价、收益与波动率预测。

- 官方论文页：https://openreview.net/forum?id=62GA9BSI5t
- 摘要来源：https://icml.cc/virtual/2026/poster/66180
- PDF 状态：access_blocked
- 金融依据类型：title_abstract_review
- 主方向：Market Prediction / 股价、收益与波动率预测
- 细分方向：Forecasting / 序列预测；Generation & Simulation / 序列生成与仿真；Stock Movement & Returns / 股价方向与收益预测
- 技术方法标签：Generative Modeling / 生成建模
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

We test our PriSpecNet in two applications: for time series, it unifies generation and forecasting, outperforming state-of-the-art (SOTA) baselines with Context-FID reductions of 50.0\%, 41.5\%, 80.6\%, and 63.1\% on Sines, Solar, ETTh, and Stock benchmarks, respectively, also decreasing forecasting MSE by 29.8\% on Solar and 23.8\% on Stock.

## 原始摘要

A probability distribution $\mathbb{P}$ is a measure on a $\sigma$-algebra, assigning mass to sets rather than points, which poses a challenge for the training of neural networks that often struggle to reconstruct the global topology of continuous manifolds from sparse samples. We mitigate this issue by transforming $\mathbb{P}$ into a continuous function via spectral methods, providing theoretical guarantees for the convergence of the learned distribution to the true distribution. Specifically, we introduce a network, PriSpecNet, with a single-function evaluation (1-NFE) Pseudoinverse L\'evy Inversion (PiLI) solver that regards generation as a fast analytical problem, eliminating the need for iterative numerical integration while maintaining full compatibility with the stochastic interpolants. We test our PriSpecNet in two applications: for time series, it unifies generation and forecasting, outperforming state-of-the-art (SOTA) baselines with Context-FID reductions of 50.0\%, 41.5\%, 80.6\%, and 63.1\% on Sines, Solar, ETTh, and Stock benchmarks, respectively, also decreasing forecasting MSE by 29.8\% on Solar and 23.8\% on Stock. For ImageNet $256 \times 256$, 1-NFE PiLI achieves a competitive FID of **1.66** using only **26** Gflops, representing a **170$\times$** reduction in total Gflops compared to the 4,436 Gflops required by the 25-NFE DPM-Solver++.
