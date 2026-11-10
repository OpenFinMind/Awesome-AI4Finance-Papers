# Latent Variable Estimation in Bayesian Black-Litterman Models

ICML 2025 · main · core

以金融任务或金融数据为核心研究对象。 主题：Time Series / 时间序列；Portfolio & Investment / 投资组合与投资管理。

- 官方论文页：https://openreview.net/forum?id=v8ipdsBPEx
- 摘要来源：https://icml.cc/virtual/2025/poster/43691
- 本地 PDF：[打开](../../pdfs/ICML/2025/icml-2025-v8ipdsBPEx__Latent_Variable_Estimation_in_Bayesian_Black_Litterman_Models.pdf)；版本：publisher_version
- 金融依据类型：title_abstract_review
- 主方向：Portfolio & Investment / 投资组合与投资管理
- 细分方向：Probabilistic Forecasting & Calibration / 概率预测与校准；Asset Allocation / 资产配置；Portfolio Selection & Optimization / 组合选择与优化
- 技术方法标签：Uncertainty & Robustness / 不确定性与鲁棒性；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Bayesian；optimization
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

We revisit the Bayesian Black–Litterman (BL) portfolio model and remove its reliance on subjective investor views. / Classical BL requires an investor “view”: a forecast vector $q$ and its uncertainty matrix $\Omega$ that describe how much a chosen portfolio should outperform the market.Our key idea is to treat $(q,\Omega)$ as latent variables and learn them from market data within a single Bayesian network.Consequently, the resulting posterior estimation admits closed-form expression, enabling fast inference and stable portfolio weights.Building on these, we propose two mechanisms to capture how features interact with returns: shared-latent parametrization and feature-influenced views; both recover classical BL and Markowitz portfolios as special cases.Empirically, on 30-year Dow-Jones and 20-year sector-ETF data, we improve Sharpe ratios by 50\% and cut turnover by 55\% relative to Markowitz and the index baselines.This work turns BL into a fully data-driven, view-free, and coherent Bayesian framework for portfolio optimization.

## 原始摘要

We revisit the Bayesian Black–Litterman (BL) portfolio model and remove its reliance on subjective investor views. Classical BL requires an investor “view”: a forecast vector $q$ and its uncertainty matrix $\Omega$ that describe how much a chosen portfolio should outperform the market.Our key idea is to treat $(q,\Omega)$ as latent variables and learn them from market data within a single Bayesian network.Consequently, the resulting posterior estimation admits closed-form expression, enabling fast inference and stable portfolio weights.Building on these, we propose two mechanisms to capture how features interact with returns: shared-latent parametrization and feature-influenced views; both recover classical BL and Markowitz portfolios as special cases.Empirically, on 30-year Dow-Jones and 20-year sector-ETF data, we improve Sharpe ratios by 50\% and cut turnover by 55\% relative to Markowitz and the index baselines.This work turns BL into a fully data-driven, view-free, and coherent Bayesian framework for portfolio optimization.
