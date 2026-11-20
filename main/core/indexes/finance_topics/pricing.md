# Pricing / 定价

Asset pricing mechanisms, risk premia, derivative valuation and calibration; distinguish pricing relationships from predictive price targets. / 资产定价机制、风险溢价、衍生品估价与校准，区别于价格预测。

18 Main long papers. Topic memberships can overlap.

[All topics](../ai_for_finance.md) · [Classification definitions](../finance_taxonomy.md) · [CSV](pricing.csv) · [Excel](../../finance_catalog.xlsx)

<!-- task-summary:start -->

## Research summary / 研究总结

**Pricing / 定价 · Main / Core**

2026-11-20 · 18 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 关注风险溢价、公允价值和定价关系。衍生品数值求解、模型校准与经济定价因子属于不同问题；预测未来成交价格与估计无套利价值需要分别评价。

**当前收录与方法。** 本页仅总结 Main / core 中的论文。当前较常见的子分类：Asset Pricing and Risk Premia / 资产定价与风险溢价 (9); Option and Derivative Pricing / 期权及衍生品定价 (8); No-Arbitrage Constraints and Calibration / 无套利约束与模型校准 (1)。已标注的方法：Uncertainty & Robustness / 不确定性与鲁棒性 (11); Optimization & Numerical Methods / 优化与数值方法 (5); Graph Learning / 图学习 (4); Representation Learning / 表征学习 (3); Generative Modeling / 生成建模 (1)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 核验无套利约束、定价误差、对冲误差及交易假设。 代表论文的摘要、金融关联证据及原文链接见 [1](../finance_notes/neurips-2026-NZHuWIlAUx.md) · [2](../finance_notes/kdd-2025-83375757b800.md) · [3](../finance_notes/neurips-2025-vBtfIafffU.md) · [4](../finance_notes/aaai-2022-20369.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 把数值精度、经济约束和真实交易可实现性共同纳入检验，明确模型假设的适用范围。

### English

**Problem and subdirections.** This task concerns risk premia, fair value and pricing relationships. Derivative solvers, calibration and economic pricing factors solve different problems; future-price prediction and no-arbitrage valuation need separate evaluation.

**Current coverage and methods.** This page covers only Main / core. Frequent subcategories: Asset Pricing and Risk Premia / 资产定价与风险溢价 (9); Option and Derivative Pricing / 期权及衍生品定价 (8); No-Arbitrage Constraints and Calibration / 无套利约束与模型校准 (1). Recorded methods: Uncertainty & Robustness / 不确定性与鲁棒性 (11); Optimization & Numerical Methods / 优化与数值方法 (5); Graph Learning / 图学习 (4); Representation Learning / 表征学习 (3); Generative Modeling / 生成建模 (1). Counts overlap and are not performance rankings.

**Data and evaluation.** Test no-arbitrage constraints, pricing error, hedging error and trading assumptions. Representative abstracts, financial evidence and original sources are linked at [1](../finance_notes/neurips-2026-NZHuWIlAUx.md) · [2](../finance_notes/kdd-2025-83375757b800.md) · [3](../finance_notes/neurips-2025-vBtfIafffU.md) · [4](../finance_notes/aaai-2022-20369.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Evaluate numerical accuracy, economic constraints and trading feasibility together, while making model assumptions explicit.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. Stable Alpha: Adversarial Invariant Representation Learning for Nonlinear Asset Pricing  under Temporal Distribution Shifts](../finance_notes/neurips-2026-NZHuWIlAUx.md) · NeurIPS 2026 | 对抗式不变表征应对市场阶段变化<br>Adversarial invariant representations address regime shifts | 因果启发的目标不自动识别真实因果关系<br>Causality-inspired objectives do not establish causal identification |
| [2. Hexagon-Net: Heterogeneous Cross-View Aligned Graph Attention Networks for Implied Volatility Surface Prediction](../finance_notes/kdd-2025-83375757b800.md) · KDD 2025 | 跨视图对齐图网络预测未来波动率曲面<br>Cross-view aligned graphs forecast volatility surfaces | 预测指标与期权策略收益不能混用<br>Forecast metrics and option-strategy returns are distinct |
| [3. Distributional Adversarial Attacks and Training in Deep Hedging](../finance_notes/neurips-2025-vBtfIafffU.md) · NeurIPS 2025 | Wasserstein 分布扰动下的鲁棒对冲训练<br>Robust hedging under Wasserstein distributional perturbations | 扰动集合限定了鲁棒性含义<br>Robustness depends on the chosen perturbation set |
| [4. FactorVAE: A Probabilistic Dynamic Factor Model Based on Variational Autoencoder for Predicting Cross-Sectional Stock Returns](../finance_notes/aaai-2022-20369.md) · AAAI 2022 | VAE 动态因子联合建模收益与风险<br>VAE dynamic factors model returns and risk | 未来信息后验只能用于合法训练阶段<br>Future-informed posteriors require careful training/inference separation |

<!-- task-summary:end -->

## Subtopic statistics / 子方向统计

| Subtopic | Papers |
|---|---:|
| Asset Pricing and Risk Premia / 资产定价与风险溢价 | 9 |
| Option and Derivative Pricing / 期权及衍生品定价 | 8 |
| Interest Rates and Fixed Income / 利率与固定收益定价 | 0 |
| Credit Instrument Pricing / 信用工具定价 | 0 |
| No-Arbitrage Constraints and Calibration / 无套利约束与模型校准 | 1 |
| Market Microstructure and Price Formation / 市场微观结构与价格形成 | 0 |

## Full paper list / 完整论文列表

| Year | Venue | Paper | Scope | Primary topic | Subtopics | Methods | Resources |
|---|---|---|---|---|---|---|---|
| 2026 | EMNLP | [Temporal Leakage in Financial News NLP: A Multi-Architecture Audit with a Regime-Specific M&A Signal](../finance_notes/2026.emnlp-main.2386.md) | core | Financial Evaluation / 金融评测 | Evaluation Protocols and Metrics / 评测协议与指标; Asset Pricing and Risk Premia / 资产定价与风险溢价; Financial Event Detection and Linking / 金融事件识别与关联; Financial Model and Agent Safety / 金融模型及智能体安全; Financial Text Classification / 金融文本分类; Regulatory Compliance and Violation Detection / 监管合规与违规检测 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/EMNLP/2026/2026.emnlp-main.2386__Temporal_Leakage_in_Financial_News_NLP_A_Multi_Architecture_Audit_with_a_Regime_Specific_M_A_Signal.pdf) |
| 2026 | ICML | [Error Propagation in Dynamic Programming: From Stochastic Control to American Option Pricing](../finance_notes/icml-2026-FB5LYFzu33.md) | core | Pricing / 定价 | Option and Derivative Pricing / 期权及衍生品定价 | Optimization & Numerical Methods / 优化与数值方法 | [PDF](../../pdfs/ICML/2026/icml-2026-FB5LYFzu33__Error_Propagation_in_Dynamic_Programming_From_Stochastic_Control_to_American_Option_Pricing.pdf) |
| 2026 | ICML | [Joint-Embedding Predictive Learning of Latent Market States in U.S. Equities](../finance_notes/icml-2026-BZfkxSasd3.md) | core | Time Series / 时间序列 | Sequence Representation and Pattern Discovery / 序列表示与模式发现; Asset Pricing and Risk Premia / 资产定价与风险溢价 | Representation Learning / 表征学习 | [Online](https://openreview.net/forum?id=BZfkxSasd3) |
| 2026 | NeurIPS | [Retrieval-Augmented Diffusion Modeling for Stochastic Discount Factor Portfolios](../finance_notes/neurips-2026-Dk8yYYJtw0.md) | core | Pricing / 定价 | Asset Pricing and Risk Premia / 资产定价与风险溢价; Asset Selection and Weight Allocation / 资产选择与权重配置; Financial Semantic Matching and Ranking / 金融语义匹配与排序; Evidence Retrieval and Reranking for Financial RAG / 金融 RAG 的证据检索与重排序 | Diffusion & Flow / 扩散与流模型; Uncertainty & Robustness / 不确定性与鲁棒性; Retrieval & RAG / 检索与RAG; Optimization & Numerical Methods / 优化与数值方法 | [PDF](../../pdfs/NeurIPS/2026/neurips-2026-Dk8yYYJtw0__Retrieval_Augmented_Diffusion_Modeling_for_Stochastic_Discount_Factor_Portfolios.pdf) |
| 2026 | NeurIPS | [Stable Alpha: Adversarial Invariant Representation Learning for Nonlinear Asset Pricing  under Temporal Distribution Shifts](../finance_notes/neurips-2026-NZHuWIlAUx.md) | core | Pricing / 定价 | Asset Pricing and Risk Premia / 资产定价与风险溢价 | Causal Learning / 因果学习; Uncertainty & Robustness / 不确定性与鲁棒性; Representation Learning / 表征学习 | [Online](https://openreview.net/forum?id=NZHuWIlAUx) |
| 2025 | AAAI | [FactorGCL: A Hypergraph-Based Factor Model with Temporal Residual Contrastive Learning for Stock Returns Prediction](../finance_notes/aaai-2025-31993.md) | core | Pricing / 定价 | Asset Pricing and Risk Premia / 资产定价与风险溢价; Stock Price and Return Prediction / 股票价格与收益预测; Earnings, Revenue and Fundamental Prediction / 盈利、营收与基本面预测 | Graph Learning / 图学习; Representation Learning / 表征学习 | [PDF](../../pdfs/AAAI/2025/aaai-2025-31993__FactorGCL_A_Hypergraph_Based_Factor_Model_with_Temporal_Residual_Contrastive_Learning_for_Stock_Returns_Prediction.pdf) |
| 2025 | ICLR | [Operator Deep Smoothing for Implied Volatility](../finance_notes/iclr-2025-DPlUWG4WMw.md) | core | Pricing / 定价 | Option and Derivative Pricing / 期权及衍生品定价; Trading Strategies and Buy/Sell Decisions / 交易策略与买卖决策 | Graph Learning / 图学习; Uncertainty & Robustness / 不确定性与鲁棒性 | [PDF](../../pdfs/ICLR/2025/iclr-2025-DPlUWG4WMw__Operator_Deep_Smoothing_for_Implied_Volatility.pdf) |
| 2025 | ICML | [HyperIV: Real-time Implied Volatility Smoothing](../finance_notes/icml-2025-o9jtS7HupI.md) | core | Pricing / 定价 | Option and Derivative Pricing / 期权及衍生品定价; Trading Strategies and Buy/Sell Decisions / 交易策略与买卖决策 | Uncertainty & Robustness / 不确定性与鲁棒性 | [PDF](../../pdfs/ICML/2025/icml-2025-o9jtS7HupI__HyperIV_Real_time_Implied_Volatility_Smoothing.pdf) |
| 2025 | KDD | [Hexagon-Net: Heterogeneous Cross-View Aligned Graph Attention Networks for Implied Volatility Surface Prediction](../finance_notes/kdd-2025-83375757b800.md) | core | Pricing / 定价 | Dynamic Hedging / 动态对冲; Option and Derivative Pricing / 期权及衍生品定价 | Graph Learning / 图学习 | [PDF](../../pdfs/KDD/2025/kdd-2025-83375757b800__Hexagon-Net_Heterogeneous_Cross-View_Aligned_Graph_Attention_Networks_for_Implied_Volatility_Surface.pdf) |
| 2025 | NeurIPS | [Distributional Adversarial Attacks and Training in Deep Hedging](../finance_notes/neurips-2025-vBtfIafffU.md) | core | Pricing / 定价 | No-Arbitrage Constraints and Calibration / 无套利约束与模型校准; Dynamic Hedging / 动态对冲 | Uncertainty & Robustness / 不确定性与鲁棒性; Optimization & Numerical Methods / 优化与数值方法 | [PDF](../../pdfs/NeurIPS/2025/neurips-2025-vBtfIafffU__Distributional_Adversarial_Attacks_and_Training_in_Deep_Hedging.pdf) |
| 2025 | NeurIPS | [OPHR: Mastering Volatility Trading with Multi-Agent Deep Reinforcement Learning](../finance_notes/neurips-2025-2p4AtivyZz.md) | core | Financial Decision Making / 金融决策 | Dynamic Hedging / 动态对冲; Option and Derivative Pricing / 期权及衍生品定价; Trading Strategies and Buy/Sell Decisions / 交易策略与买卖决策; Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策; On-Chain Transaction and Account Analysis / 链上交易与账户分析 | Reinforcement Learning / 强化学习; Uncertainty & Robustness / 不确定性与鲁棒性 | [Online](https://openreview.net/forum?id=2p4AtivyZz) |
| 2023 | AAAI | [Tighter Robust Upper Bounds for Options via No-Regret Learning](../finance_notes/aaai-2023-25666.md) | core | Pricing / 定价 | Option and Derivative Pricing / 期权及衍生品定价 | Uncertainty & Robustness / 不确定性与鲁棒性 | [PDF](../../pdfs/AAAI/2023/aaai-2023-25666__Tighter_Robust_Upper_Bounds_for_Options_via_No_Regret_Learning.pdf) |
| 2022 | AAAI | [FactorVAE: A Probabilistic Dynamic Factor Model Based on Variational Autoencoder for Predicting Cross-Sectional Stock Returns](../finance_notes/aaai-2022-20369.md) | core | Pricing / 定价 | Asset Pricing and Risk Premia / 资产定价与风险溢价; Stock Price and Return Prediction / 股票价格与收益预测 | Generative Modeling / 生成建模 | [PDF](../../pdfs/AAAI/2022/aaai-2022-20369__FactorVAE_A_Probabilistic_Dynamic_Factor_Model_Based_on_Variational_Autoencoder_for_Predicting_Cross_Sectional_Stock_Returns.pdf) |
| 2021 | AAAI | [Deep Portfolio Optimization via Distributional Prediction of Residual Factors](../finance_notes/aaai-2021-16095.md) | core | Portfolio / 投资组合 | Asset Selection and Weight Allocation / 资产选择与权重配置; Asset Pricing and Risk Premia / 资产定价与风险溢价 | Uncertainty & Robustness / 不确定性与鲁棒性; Optimization & Numerical Methods / 优化与数值方法 | [PDF](../../pdfs/AAAI/2021/aaai-2021-16095__Deep_Portfolio_Optimization_via_Distributional_Prediction_of_Residual_Factors.pdf) |
| 2021 | NeurIPS | [Graphical Models in Heavy-Tailed Markets](../finance_notes/neurips-2021-w1FvEPcwTnI.md) | core | Pricing / 定价 | Asset Pricing and Risk Premia / 资产定价与风险溢价; On-Chain Transaction and Account Analysis / 链上交易与账户分析 | Graph Learning / 图学习; Optimization & Numerical Methods / 优化与数值方法 | [PDF](../../pdfs/NeurIPS/2021/neurips-2021-w1FvEPcwTnI__Graphical_Models_in_Heavy_Tailed_Markets.pdf) |
| 2020 | ICML | [Uncertainty-Aware Lookahead Factor Models for Quantitative Investing](../finance_notes/icml-2020-5869.md) | core | Pricing / 定价 | Asset Pricing and Risk Premia / 资产定价与风险溢价; Asset Selection and Weight Allocation / 资产选择与权重配置 | Uncertainty & Robustness / 不确定性与鲁棒性 | [PDF](../../pdfs/ICML/2020/icml-2020-5869__Uncertainty_Aware_Lookahead_Factor_Models_for_Quantitative_Investing.pdf) |
| 2020 | NeurIPS | [Deep Smoothing of the Implied Volatility Surface](../finance_notes/neurips-2020-19076.md) | core | Pricing / 定价 | Option and Derivative Pricing / 期权及衍生品定价; Trading Strategies and Buy/Sell Decisions / 交易策略与买卖决策; Volatility Prediction / 波动率预测 | Uncertainty & Robustness / 不确定性与鲁棒性 | [PDF](../../pdfs/NeurIPS/2020/neurips-2020-19076__Deep_Smoothing_of_the_Implied_Volatility_Surface.pdf) |
| 2017 | AAAI | [Gated Neural Networks for Option Pricing: Rationality by Design](../finance_notes/aaai-2017-10505.md) | core | Pricing / 定价 | Option and Derivative Pricing / 期权及衍生品定价 | Uncertainty & Robustness / 不确定性与鲁棒性 | [PDF](../../pdfs/AAAI/2017/aaai-2017-10505__Gated_Neural_Networks_for_Option_Pricing_Rationality_by_Design.pdf) |
