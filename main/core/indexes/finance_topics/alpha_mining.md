# Factor Mining / 因子挖掘

Discover and select reusable alpha signals or formulas; distinguish predictive alpha from economic pricing factors. / 发现与筛选可复用的收益信号或公式，区别于经济定价因子。

11 Main long papers. Topic memberships can overlap.

[All topics](../ai_for_finance.md) · [Classification definitions](../finance_taxonomy.md) · [CSV](alpha_mining.csv) · [Excel](../../finance_catalog.xlsx)

<!-- task-summary:start -->

## Research summary / 研究总结

**Factor Mining / 因子挖掘 · Main / Core**

2026-11-20 · 11 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 研究对象是可以复用、组合和检验的收益信号。公式生成、筛选与组合是不同环节，搜索到低相关信号并不自动证明它具有稳定的样本外预测能力。

**当前收录与方法。** 本页仅总结 Main / core 中的论文。当前较常见的子分类：Factor Discovery and Formula Generation / 因子发现与公式生成 (11); Factor Validity and Stability / 因子有效性与稳定性 (4); Factor Decay and Updating / 因子衰减与更新 (1)。已标注的方法：Reinforcement Learning / 强化学习 (7); Uncertainty & Robustness / 不确定性与鲁棒性 (7); Language Models & LLM / 语言模型与LLM (7); Generative Modeling / 生成建模 (3); Optimization & Numerical Methods / 优化与数值方法 (3)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 检查样本外 IC、因子冗余、搜索预算、换手与成本。 代表论文的摘要、金融关联证据及原文链接见 [1](../finance_notes/aaai-2025-33365.md) · [2](../finance_notes/icml-2025-3sXMHlhBSs.md) · [3](../finance_notes/kdd-2025-dde09d0647f8.md) · [4](../finance_notes/iclr-2026-d97Q8r7ZKZ.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 将新颖性、经济含义与样本外有效性分开检验，并研究不同市场状态下的因子更新机制。

### English

**Problem and subdirections.** The object is a reusable return signal. Formula discovery, selection and combination are distinct stages; finding a low-correlation signal does not establish stable out-of-sample predictability.

**Current coverage and methods.** This page covers only Main / core. Frequent subcategories: Factor Discovery and Formula Generation / 因子发现与公式生成 (11); Factor Validity and Stability / 因子有效性与稳定性 (4); Factor Decay and Updating / 因子衰减与更新 (1). Recorded methods: Reinforcement Learning / 强化学习 (7); Uncertainty & Robustness / 不确定性与鲁棒性 (7); Language Models & LLM / 语言模型与LLM (7); Generative Modeling / 生成建模 (3); Optimization & Numerical Methods / 优化与数值方法 (3). Counts overlap and are not performance rankings.

**Data and evaluation.** Check out-of-sample IC, signal redundancy, search budget, turnover and costs. Representative abstracts, financial evidence and original sources are linked at [1](../finance_notes/aaai-2025-33365.md) · [2](../finance_notes/icml-2025-3sXMHlhBSs.md) · [3](../finance_notes/kdd-2025-dde09d0647f8.md) · [4](../finance_notes/iclr-2026-d97Q8r7ZKZ.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Test novelty, economic interpretation and out-of-sample validity separately, and study signal updating across market regimes.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. AlphaForge: A Framework to Mine and Dynamically Combine Formulaic Alpha Factors](../finance_notes/aaai-2025-33365.md) · AAAI 2025 | 因子生成与动态权重组合<br>Factor generation and dynamic weighting | 组合模块收益需与因子本身贡献分开<br>Separate combination gains from factor quality |
| [2. AlphaQCM: Alpha Discovery in Finance with Distributional Reinforcement Learning](../finance_notes/icml-2025-3sXMHlhBSs.md) · ICML 2025 | 分布强化学习寻找协同公式因子<br>Distributional RL searches for synergistic formulaic signals | 比较需要一致的算子库与搜索预算<br>Comparisons need matched operators and search budgets |
| [3. AlphaAgent: LLM-Driven Alpha Mining with Regularized Exploration to Counteract Alpha Decay](../finance_notes/kdd-2025-dde09d0647f8.md) · KDD 2025 | AST 新颖性、复杂度与假设一致性约束<br>AST novelty, complexity and hypothesis-alignment constraints | 低相似度本身不证明持续预测能力<br>Low similarity alone does not establish persistent predictability |
| [4. AlphaBench: Benchmarking Large Language Models in Formulaic Alpha Factor Mining](../finance_notes/iclr-2026-d97Q8r7ZKZ.md) · ICLR 2026 | 分任务评估 LLM 因子挖掘能力<br>Task-separated evaluation of LLM factor mining | 基准能力不直接等于可交易盈利<br>Benchmark ability does not directly establish tradable profit |

<!-- task-summary:end -->

## Subtopic statistics / 子方向统计

| Subtopic | Papers |
|---|---:|
| Factor Discovery and Formula Generation / 因子发现与公式生成 | 11 |
| Factor Combination and Interaction / 因子组合与交互 | 0 |
| Factor Selection and Deduplication / 因子筛选与去冗余 | 0 |
| Factor Validity and Stability / 因子有效性与稳定性 | 4 |
| Factor Decay and Updating / 因子衰减与更新 | 1 |
| Factor Interpretation and Economic Meaning / 因子解释与经济含义 | 0 |

## Full paper list / 完整论文列表

| Year | Venue | Paper | Scope | Primary topic | Subtopics | Methods | Resources |
|---|---|---|---|---|---|---|---|
| 2026 | AAAI | [Navigating the Alpha Jungle: An LLM-Powered MCTS Framework for Formulaic Alpha Factor Mining](../finance_notes/aaai-2026-37069.md) | core | Factor Mining / 因子挖掘 | Factor Discovery and Formula Generation / 因子发现与公式生成 | Language Models & LLM / 语言模型与LLM; Reinforcement Learning / 强化学习 | [PDF](../../pdfs/AAAI/2026/aaai-2026-37069__Navigating_the_Alpha_Jungle_An_LLM_Powered_MCTS_Framework_for_Formulaic_Alpha_Factor_Mining.pdf) |
| 2026 | ACL | [Cognitive Alpha Mining via LLM-Driven Code-Based Evolution](../finance_notes/2026.acl-long.538.md) | core | Factor Mining / 因子挖掘 | Factor Discovery and Formula Generation / 因子发现与公式生成 | Language Models & LLM / 语言模型与LLM; Uncertainty & Robustness / 不确定性与鲁棒性; Optimization & Numerical Methods / 优化与数值方法 | [PDF](../../pdfs/ACL/2026/2026.acl-long.538__Cognitive_Alpha_Mining_via_LLM_Driven_Code_Based_Evolution.pdf) |
| 2026 | ICLR | [AlphaBench: Benchmarking Large Language Models in Formulaic Alpha Factor Mining](../finance_notes/iclr-2026-d97Q8r7ZKZ.md) | core | Financial Evaluation / 金融评测 | Factor Discovery and Formula Generation / 因子发现与公式生成; Factor Validity and Stability / 因子有效性与稳定性; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Financial Understanding and Multimodal Evaluation / 金融理解及多模态评测 | Language Models & LLM / 语言模型与LLM; Uncertainty & Robustness / 不确定性与鲁棒性 | [Online](https://openreview.net/forum?id=d97Q8r7ZKZ) |
| 2026 | ICLR | [AlphaSAGE: Structure-Aware Alpha Mining via GFlowNets for Robust Exploration](../finance_notes/iclr-2026-zRKF4ln2VE.md) | core | Factor Mining / 因子挖掘 | Factor Discovery and Formula Generation / 因子发现与公式生成; Factor Validity and Stability / 因子有效性与稳定性 | Reinforcement Learning / 强化学习; Graph Learning / 图学习; Generative Modeling / 生成建模; Uncertainty & Robustness / 不确定性与鲁棒性 | [PDF](../../pdfs/ICLR/2026/iclr-2026-zRKF4ln2VE__AlphaSAGE_Structure_Aware_Alpha_Mining_via_GFlowNets_for_Robust_Exploration.pdf) |
| 2026 | KDD | [AlphaEval: A Comprehensive and Efficient Evaluation Framework for Formula Alpha Mining](../finance_notes/kdd-2026-ccd584a46e66.md) | core | Financial Evaluation / 金融评测 | Factor Discovery and Formula Generation / 因子发现与公式生成; Factor Validity and Stability / 因子有效性与稳定性; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Evaluation Protocols and Metrics / 评测协议与指标 | Language Models & LLM / 语言模型与LLM; Reinforcement Learning / 强化学习; Uncertainty & Robustness / 不确定性与鲁棒性 | [PDF](../../pdfs/KDD/2026/kdd-2026-ccd584a46e66__AlphaEval_A_Comprehensive_and_Efficient_Evaluation_Framework_for_Formula_Alpha_Mining.pdf) |
| 2026 | KDD | [AlphaMaster: Dual-Chain Feedback for Scalable and Diverse Alpha Factor Discovery](../finance_notes/kdd-2026-46f2d631d6cf.md) | core | Factor Mining / 因子挖掘 | Factor Discovery and Formula Generation / 因子发现与公式生成 | Language Models & LLM / 语言模型与LLM; Reinforcement Learning / 强化学习; Generative Modeling / 生成建模; Optimization & Numerical Methods / 优化与数值方法 | [Online](https://doi.org/10.1145/3770855.3818120) |
| 2026 | NeurIPS | [AlphaPareto: Formulaic Alpha Discovery with LLM-Guided Multi-Objective Reinforcement Learning](../finance_notes/neurips-2026-H8C7jHFbSI.md) | core | Factor Mining / 因子挖掘 | Factor Discovery and Formula Generation / 因子发现与公式生成; Trading Strategies and Buy/Sell Decisions / 交易策略与买卖决策 | Language Models & LLM / 语言模型与LLM; Reinforcement Learning / 强化学习; Uncertainty & Robustness / 不确定性与鲁棒性 | [PDF](../../pdfs/NeurIPS/2026/neurips-2026-H8C7jHFbSI__AlphaPareto_Formulaic_Alpha_Discovery_with_LLM_Guided_Multi_Objective_Reinforcement_Learning.pdf) |
| 2026 | NeurIPS | [AlphaPROBE: Alpha Mining via principled retriveval and on-graph biased evolution](../finance_notes/neurips-2026-jnNAuSXHv2.md) | core | Factor Mining / 因子挖掘 | Factor Discovery and Formula Generation / 因子发现与公式生成; Sequence Representation and Pattern Discovery / 序列表示与模式发现 | Uncertainty & Robustness / 不确定性与鲁棒性; Optimization & Numerical Methods / 优化与数值方法 | [Online](https://openreview.net/forum?id=jnNAuSXHv2) |
| 2025 | AAAI | [AlphaForge: A Framework to Mine and Dynamically Combine Formulaic Alpha Factors](../finance_notes/aaai-2025-33365.md) | core | Factor Mining / 因子挖掘 | Factor Discovery and Formula Generation / 因子发现与公式生成; Factor Validity and Stability / 因子有效性与稳定性 | Reinforcement Learning / 强化学习; Generative Modeling / 生成建模; Uncertainty & Robustness / 不确定性与鲁棒性 | [PDF](../../pdfs/AAAI/2025/aaai-2025-33365__AlphaForge_A_Framework_to_Mine_and_Dynamically_Combine_Formulaic_Alpha_Factors.pdf) |
| 2025 | ICML | [AlphaQCM: Alpha Discovery in Finance with Distributional Reinforcement Learning](../finance_notes/icml-2025-3sXMHlhBSs.md) | core | Factor Mining / 因子挖掘 | Factor Discovery and Formula Generation / 因子发现与公式生成 | Reinforcement Learning / 强化学习 | [PDF](../../pdfs/ICML/2025/icml-2025-3sXMHlhBSs__AlphaQCM_Alpha_Discovery_in_Finance_with_Distributional_Reinforcement_Learning.pdf) |
| 2025 | KDD | [AlphaAgent: LLM-Driven Alpha Mining with Regularized Exploration to Counteract Alpha Decay](../finance_notes/kdd-2025-dde09d0647f8.md) | core | Factor Mining / 因子挖掘 | Factor Discovery and Formula Generation / 因子发现与公式生成; Factor Decay and Updating / 因子衰减与更新 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/KDD/2025/kdd-2025-dde09d0647f8__AlphaAgent_LLM-Driven_Alpha_Mining_with_Regularized_Exploration_to_Counteract_Alpha_Decay.pdf) |
