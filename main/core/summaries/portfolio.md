## Research summary / 研究总结

**Portfolio / 投资组合 · Main / Core**

2026-11-20 · 45 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 核心输出是资产集合、权重或再平衡方案。组合层面表现同时受到预测信号、约束、成本和配置算法影响，不能把全部收益归因于单个模块。

**当前收录与方法。** 本页仅总结 Main / core 中的论文。当前较常见的子分类：Asset Selection and Weight Allocation / 资产选择与权重配置 (41); Risk-Return and Multi-Objective Optimization / 风险收益及多目标优化 (7); Dynamic Allocation and Rebalancing / 动态配置与再平衡 (6); Transaction Costs and Investment Constraints / 交易成本与投资约束 (4)。已标注的方法：Optimization & Numerical Methods / 优化与数值方法 (22); Uncertainty & Robustness / 不确定性与鲁棒性 (16); Reinforcement Learning / 强化学习 (11); Representation Learning / 表征学习 (4); Language Models & LLM / 语言模型与LLM (4)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 统一成本与调仓频率，报告收益、回撤、风险及换手。 代表论文的摘要、金融关联证据及原文链接见 [1](../indexes/finance_notes/icml-2026-KV7XHF0IbK.md) · [2](../indexes/finance_notes/kdd-2026-f59c8ff60d76.md) · [3](../indexes/finance_notes/aaai-2025-33225.md) · [4](../indexes/finance_notes/neurips-2018-11788.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 在统一资产池、再平衡频率和成本假设下比较配置方法，考察极端行情与长期资金目标。

### English

**Problem and subdirections.** The output is an asset set, portfolio weights or a rebalancing plan. Performance depends jointly on signals, constraints, costs and allocation, so aggregate gains cannot be attributed to one module without controls.

**Current coverage and methods.** This page covers only Main / core. Frequent subcategories: Asset Selection and Weight Allocation / 资产选择与权重配置 (41); Risk-Return and Multi-Objective Optimization / 风险收益及多目标优化 (7); Dynamic Allocation and Rebalancing / 动态配置与再平衡 (6); Transaction Costs and Investment Constraints / 交易成本与投资约束 (4). Recorded methods: Optimization & Numerical Methods / 优化与数值方法 (22); Uncertainty & Robustness / 不确定性与鲁棒性 (16); Reinforcement Learning / 强化学习 (11); Representation Learning / 表征学习 (4); Language Models & LLM / 语言模型与LLM (4). Counts overlap and are not performance rankings.

**Data and evaluation.** Match costs and rebalancing frequency; report return, drawdown, risk and turnover. Representative abstracts, financial evidence and original sources are linked at [1](../indexes/finance_notes/icml-2026-KV7XHF0IbK.md) · [2](../indexes/finance_notes/kdd-2026-f59c8ff60d76.md) · [3](../indexes/finance_notes/aaai-2025-33225.md) · [4](../indexes/finance_notes/neurips-2018-11788.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Compare allocation methods under matched universes, rebalancing frequencies and costs, including stressed markets and long-horizon objectives.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. Decision-focused Sparse Tangent Portfolio Optimization](../indexes/finance_notes/icml-2026-KV7XHF0IbK.md) · ICML 2026 | 通过凸优化层联合学习稀疏切点组合<br>A convex layer supports decision-focused sparse tangency portfolios | 目标与协方差估计及风险设定相关<br>Results depend on covariance estimation and risk assumptions |
| [2. Regime-Adaptive Continual Learning for Portfolio Management](../indexes/finance_notes/kdd-2026-f59c8ff60d76.md) · KDD 2026 | 阶段检测、策略库与门控持续适应<br>Regime detection, policy libraries and gated continual adaptation | 阶段划分与在线更新必须保持时间合法<br>Regime detection and updates must respect chronological availability |
| [3. DCC: Differentiable Cardinality Constraints for Partial Index Tracking](../indexes/finance_notes/aaai-2025-33225.md) · AAAI 2025 | 可微基数约束用于部分指数复制<br>Differentiable cardinality constraints for partial replication | 持仓约束保证与收益表现是不同结论<br>Constraint guarantees and return performance are distinct claims |
| [4. Efficient Online Portfolio with Logarithmic Regret](../indexes/finance_notes/neurips-2018-11788.md) · NeurIPS 2018 | 在线镜像下降实现对数遗憾的组合选择<br>Online mirror descent achieves logarithmic portfolio regret | 理论比较器和市场假设决定保证范围<br>Comparator and market assumptions bound the guarantee |
