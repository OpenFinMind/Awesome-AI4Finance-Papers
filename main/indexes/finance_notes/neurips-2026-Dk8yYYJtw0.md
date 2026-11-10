# Retrieval-Augmented Diffusion Modeling for Stochastic Discount Factor Portfolios

NeurIPS 2026 · main · core

以金融市场为研究对象，或包含明确的金融领域数据和应用评测。 主题：Asset Pricing / 资产定价；Portfolio & Investment / 投资组合与投资管理；Financial IR & RAG / 金融检索与RAG。

- 官方论文页：https://openreview.net/forum?id=Dk8yYYJtw0
- 摘要来源：https://neurips.cc/Downloads/2026
- 本地 PDF：[打开](../../pdfs/NeurIPS/2026/neurips-2026-Dk8yYYJtw0__Retrieval_Augmented_Diffusion_Modeling_for_Stochastic_Discount_Factor_Portfolios.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_financial_task_or_data
- 主方向：Asset Pricing / 资产定价
- 细分方向：Pricing Models & Risk Premia / 定价模型与风险溢价；Portfolio Selection & Optimization / 组合选择与优化；Retrieval, Embedding & Reranking / 检索、嵌入与重排；Financial RAG & Long Documents / 金融RAG与长文档
- 技术方法标签：Diffusion & Flow / 扩散与流模型；Uncertainty & Robustness / 不确定性与鲁棒性；Retrieval & RAG / 检索与RAG；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：diffusion；optimization；retrieval
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

In this work, we study portfolio optimization under the stochastic discount factor (SDF) framework by learning market state representations that capture the underlying risk structures of financial data. / This is challenging due to several factors: financial markets exhibit non-stationary dynamics with shifting regimes, multimodal inputs such as price and news data often contain stochastic noise, and existing diffusion-based approaches, while effective for modeling stochastic dynamics, rely on assumptions such as isotropic Gaussian noise that fail to capture the state-dependent nature of financial uncertainty.

## 原始摘要

In this work, we study portfolio optimization under the stochastic discount factor (SDF) framework by learning market state representations that capture the underlying risk structures of financial data. This is challenging due to several factors: financial markets exhibit non-stationary dynamics with shifting regimes, multimodal inputs such as price and news data often contain stochastic noise, and existing diffusion-based approaches, while effective for modeling stochastic dynamics, rely on assumptions such as isotropic Gaussian noise that fail to capture the state-dependent nature of financial uncertainty. To address these challenges, we introduce RADAR, a retrieval-augmented diffusion framework that learns market representations by conditioning on similar historical regimes. RADAR leverages retrieval to construct context-dependent noise distributions, applies conditional diffusion to denoise multimodal representations, and initializes the diffusion process using empirical statistics to reflect state-dependent uncertainty. Experiments show that RADAR achieves state-of-the-art performance on key risk-adjusted metrics while producing economically meaningful signals on asset returns and correlations.
