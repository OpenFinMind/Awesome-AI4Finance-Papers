## Research summary / 研究总结

**Pricing / 定价 · Main / Core**

2026-11-20 · 18 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 关注风险溢价、公允价值和定价关系。衍生品数值求解、模型校准与经济定价因子属于不同问题；预测未来成交价格与估计无套利价值需要分别评价。

**当前收录与方法。** 本页仅总结 Main / core 中的论文。当前较常见的子分类：Asset Pricing and Risk Premia / 资产定价与风险溢价 (9); Option and Derivative Pricing / 期权及衍生品定价 (8); No-Arbitrage Constraints and Calibration / 无套利约束与模型校准 (1)。已标注的方法：Uncertainty & Robustness / 不确定性与鲁棒性 (11); Optimization & Numerical Methods / 优化与数值方法 (5); Graph Learning / 图学习 (4); Representation Learning / 表征学习 (3); Generative Modeling / 生成建模 (1)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 核验无套利约束、定价误差、对冲误差及交易假设。 代表论文的摘要、金融关联证据及原文链接见 [1](../indexes/finance_notes/neurips-2026-NZHuWIlAUx.md) · [2](../indexes/finance_notes/kdd-2025-83375757b800.md) · [3](../indexes/finance_notes/neurips-2025-vBtfIafffU.md) · [4](../indexes/finance_notes/aaai-2022-20369.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 把数值精度、经济约束和真实交易可实现性共同纳入检验，明确模型假设的适用范围。

### English

**Problem and subdirections.** This task concerns risk premia, fair value and pricing relationships. Derivative solvers, calibration and economic pricing factors solve different problems; future-price prediction and no-arbitrage valuation need separate evaluation.

**Current coverage and methods.** This page covers only Main / core. Frequent subcategories: Asset Pricing and Risk Premia / 资产定价与风险溢价 (9); Option and Derivative Pricing / 期权及衍生品定价 (8); No-Arbitrage Constraints and Calibration / 无套利约束与模型校准 (1). Recorded methods: Uncertainty & Robustness / 不确定性与鲁棒性 (11); Optimization & Numerical Methods / 优化与数值方法 (5); Graph Learning / 图学习 (4); Representation Learning / 表征学习 (3); Generative Modeling / 生成建模 (1). Counts overlap and are not performance rankings.

**Data and evaluation.** Test no-arbitrage constraints, pricing error, hedging error and trading assumptions. Representative abstracts, financial evidence and original sources are linked at [1](../indexes/finance_notes/neurips-2026-NZHuWIlAUx.md) · [2](../indexes/finance_notes/kdd-2025-83375757b800.md) · [3](../indexes/finance_notes/neurips-2025-vBtfIafffU.md) · [4](../indexes/finance_notes/aaai-2022-20369.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Evaluate numerical accuracy, economic constraints and trading feasibility together, while making model assumptions explicit.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. Stable Alpha: Adversarial Invariant Representation Learning for Nonlinear Asset Pricing  under Temporal Distribution Shifts](../indexes/finance_notes/neurips-2026-NZHuWIlAUx.md) · NeurIPS 2026 | 对抗式不变表征应对市场阶段变化<br>Adversarial invariant representations address regime shifts | 因果启发的目标不自动识别真实因果关系<br>Causality-inspired objectives do not establish causal identification |
| [2. Hexagon-Net: Heterogeneous Cross-View Aligned Graph Attention Networks for Implied Volatility Surface Prediction](../indexes/finance_notes/kdd-2025-83375757b800.md) · KDD 2025 | 跨视图对齐图网络预测未来波动率曲面<br>Cross-view aligned graphs forecast volatility surfaces | 预测指标与期权策略收益不能混用<br>Forecast metrics and option-strategy returns are distinct |
| [3. Distributional Adversarial Attacks and Training in Deep Hedging](../indexes/finance_notes/neurips-2025-vBtfIafffU.md) · NeurIPS 2025 | Wasserstein 分布扰动下的鲁棒对冲训练<br>Robust hedging under Wasserstein distributional perturbations | 扰动集合限定了鲁棒性含义<br>Robustness depends on the chosen perturbation set |
| [4. FactorVAE: A Probabilistic Dynamic Factor Model Based on Variational Autoencoder for Predicting Cross-Sectional Stock Returns](../indexes/finance_notes/aaai-2022-20369.md) · AAAI 2022 | VAE 动态因子联合建模收益与风险<br>VAE dynamic factors model returns and risk | 未来信息后验只能用于合法训练阶段<br>Future-informed posteriors require careful training/inference separation |
