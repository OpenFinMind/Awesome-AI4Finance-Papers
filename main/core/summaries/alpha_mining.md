## Research summary / 研究总结

**Factor Mining / 因子挖掘 · Main / Core**

2026-11-20 · 11 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 研究对象是可以复用、组合和检验的收益信号。公式生成、筛选与组合是不同环节，搜索到低相关信号并不自动证明它具有稳定的样本外预测能力。

**当前收录与方法。** 本页仅总结 Main / core 中的论文。当前较常见的子分类：Factor Discovery and Formula Generation / 因子发现与公式生成 (11); Factor Validity and Stability / 因子有效性与稳定性 (4); Factor Decay and Updating / 因子衰减与更新 (1)。已标注的方法：Reinforcement Learning / 强化学习 (7); Uncertainty & Robustness / 不确定性与鲁棒性 (7); Language Models & LLM / 语言模型与LLM (7); Generative Modeling / 生成建模 (3); Optimization & Numerical Methods / 优化与数值方法 (3)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 检查样本外 IC、因子冗余、搜索预算、换手与成本。 代表论文的摘要、金融关联证据及原文链接见 [1](../indexes/finance_notes/aaai-2025-33365.md) · [2](../indexes/finance_notes/icml-2025-3sXMHlhBSs.md) · [3](../indexes/finance_notes/kdd-2025-dde09d0647f8.md) · [4](../indexes/finance_notes/iclr-2026-d97Q8r7ZKZ.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 将新颖性、经济含义与样本外有效性分开检验，并研究不同市场状态下的因子更新机制。

### English

**Problem and subdirections.** The object is a reusable return signal. Formula discovery, selection and combination are distinct stages; finding a low-correlation signal does not establish stable out-of-sample predictability.

**Current coverage and methods.** This page covers only Main / core. Frequent subcategories: Factor Discovery and Formula Generation / 因子发现与公式生成 (11); Factor Validity and Stability / 因子有效性与稳定性 (4); Factor Decay and Updating / 因子衰减与更新 (1). Recorded methods: Reinforcement Learning / 强化学习 (7); Uncertainty & Robustness / 不确定性与鲁棒性 (7); Language Models & LLM / 语言模型与LLM (7); Generative Modeling / 生成建模 (3); Optimization & Numerical Methods / 优化与数值方法 (3). Counts overlap and are not performance rankings.

**Data and evaluation.** Check out-of-sample IC, signal redundancy, search budget, turnover and costs. Representative abstracts, financial evidence and original sources are linked at [1](../indexes/finance_notes/aaai-2025-33365.md) · [2](../indexes/finance_notes/icml-2025-3sXMHlhBSs.md) · [3](../indexes/finance_notes/kdd-2025-dde09d0647f8.md) · [4](../indexes/finance_notes/iclr-2026-d97Q8r7ZKZ.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Test novelty, economic interpretation and out-of-sample validity separately, and study signal updating across market regimes.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. AlphaForge: A Framework to Mine and Dynamically Combine Formulaic Alpha Factors](../indexes/finance_notes/aaai-2025-33365.md) · AAAI 2025 | 因子生成与动态权重组合<br>Factor generation and dynamic weighting | 组合模块收益需与因子本身贡献分开<br>Separate combination gains from factor quality |
| [2. AlphaQCM: Alpha Discovery in Finance with Distributional Reinforcement Learning](../indexes/finance_notes/icml-2025-3sXMHlhBSs.md) · ICML 2025 | 分布强化学习寻找协同公式因子<br>Distributional RL searches for synergistic formulaic signals | 比较需要一致的算子库与搜索预算<br>Comparisons need matched operators and search budgets |
| [3. AlphaAgent: LLM-Driven Alpha Mining with Regularized Exploration to Counteract Alpha Decay](../indexes/finance_notes/kdd-2025-dde09d0647f8.md) · KDD 2025 | AST 新颖性、复杂度与假设一致性约束<br>AST novelty, complexity and hypothesis-alignment constraints | 低相似度本身不证明持续预测能力<br>Low similarity alone does not establish persistent predictability |
| [4. AlphaBench: Benchmarking Large Language Models in Formulaic Alpha Factor Mining](../indexes/finance_notes/iclr-2026-d97Q8r7ZKZ.md) · ICLR 2026 | 分任务评估 LLM 因子挖掘能力<br>Task-separated evaluation of LLM factor mining | 基准能力不直接等于可交易盈利<br>Benchmark ability does not directly establish tradable profit |
