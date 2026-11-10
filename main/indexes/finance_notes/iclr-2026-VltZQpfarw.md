# STABLE: Shift-Tolerant Allocation via Black-Litterman Using Conditional Diffusion Estimates

ICLR 2026 · main · core

以金融任务或金融数据为核心研究对象。 主题：Time Series / 时间序列；Portfolio & Investment / 投资组合与投资管理；Market Prediction / 股价、收益与波动率预测；Macro & Economic Forecasting / 宏观经济与预测。

- 官方论文页：https://openreview.net/forum?id=VltZQpfarw
- 摘要来源：https://iclr.cc/virtual/2026/poster/10009107
- PDF 状态：access_blocked
- 金融依据类型：title_abstract_review
- 主方向：Portfolio & Investment / 投资组合与投资管理
- 细分方向：Causality & Dynamics / 序列因果与动力学；Asset Allocation / 资产配置；Portfolio Selection & Optimization / 组合选择与优化；Stock Movement & Returns / 股价方向与收益预测；Macro Indicators & Policy / 宏观指标与政策；Investment Evaluation & Decisions / 投资评价与决策
- 技术方法标签：Reinforcement Learning / 强化学习；Diffusion & Flow / 扩散与流模型；Generative Modeling / 生成建模；Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：diffusion；Diffusion；Reinforcement learning
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

In dynamic financial market characterized by shifting regimes, how can we make effective investment decisions under the changing 1) market regimes and 2) their impact? / Among many research fields in financial AI, portfolio allocation stands out as one of the most practically significant areas. / Consequently, numerous researchers and financial institutions continually seek approaches that improve the risk–reward trade-off and strive to apply them in real-world investment scenarios. / In response, modern portfolio theory (MPT) addresses this issue by solving for asset weights that maximize a risk–reward objective, using estimates of the return mean and covariance from historical returns. / Reinforcement learning (RL) frameworks have been introduced to directly decide portfolio allocations by optimizing risk‑adjusted objectives using asset prices and macroeconomic indices. / In this work, we propose STABLE (Shift-Tolerant Allocation with Black-Litterman Using Conditional Diffusion Estimates), which combines a diffusion-based generative model that captures regime shifts with an estimation-based portfolio allocation module that maximizes expected risk-adjusted return. / STABLE takes macroeconomic context and asset-specific signals as inputs and generates per-stock return trajectories that reflect the prevailing macro regime while preserving firm-specific dynamics. / This yields regime-aware predictive return distributions at the single-stock level together with a coherent covariance structure, which are then incorporated as investor views within a Black-Litterman allocation module to obtain risk-diversified portfolio weights. / Empirically, STABLE delivers superior portfolio outcomes, achieving up to 122.9% higher Sharpe ratios with reduced drawdowns across major equity markets.

## 原始摘要

In dynamic financial market characterized by shifting regimes, how can we make effective investment decisions under the changing 1) market regimes and 2) their impact? Among many research fields in financial AI, portfolio allocation stands out as one of the most practically significant areas. Consequently, numerous researchers and financial institutions continually seek approaches that improve the risk–reward trade-off and strive to apply them in real-world investment scenarios. However, achieving robust risk-adjusted performance is extremely challenging, because each asset's return and volatility fluctuate according to the shifting market regime.  In response, modern portfolio theory (MPT) addresses this issue by solving for asset weights that maximize a risk–reward objective, using estimates of the return mean and covariance from historical returns. Reinforcement learning (RL) frameworks have been introduced to directly decide portfolio allocations by optimizing risk‑adjusted objectives using asset prices and macroeconomic indices.  In this work, we propose STABLE (Shift-Tolerant Allocation with Black-Litterman Using Conditional Diffusion Estimates), which combines a diffusion-based generative model that captures regime shifts with an estimation-based portfolio allocation module that maximizes expected risk-adjusted return. STABLE takes macroeconomic context and asset-specific signals as inputs and generates per-stock return trajectories that reflect the prevailing macro regime while preserving firm-specific dynamics. This yields regime-aware predictive return distributions at the single-stock level together with a coherent covariance structure, which are then incorporated as investor views within a Black-Litterman allocation module to obtain risk-diversified portfolio weights. Empirically, STABLE delivers superior portfolio outcomes, achieving up to 122.9% higher Sharpe ratios with reduced drawdowns across major equity markets. It also attains state‑of‑the‑art time‑series estimation, lowering MSE by up to 15.7% compared with generative baselines.
