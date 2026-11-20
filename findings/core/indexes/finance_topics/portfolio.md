# Portfolio / 投资组合

Select, allocate, rebalance and evaluate portfolios across assets. / 跨资产组合选择、配置、再平衡与评价。

2 Findings long papers. Topic memberships can overlap.

[All topics](../ai_for_finance.md) · [Classification definitions](../finance_taxonomy.md) · [CSV](portfolio.csv) · [Excel](../../finance_catalog.xlsx)

<!-- task-summary:start -->

## Research summary / 研究总结

**Portfolio / 投资组合 · Findings / Core**

2026-11-20 · 2 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 核心输出是资产集合、权重或再平衡方案。组合层面表现同时受到预测信号、约束、成本和配置算法影响，不能把全部收益归因于单个模块。

**当前收录与方法。** 本页仅总结 Findings / core 中的论文。当前较常见的子分类：Risk-Return and Multi-Objective Optimization / 风险收益及多目标优化 (2)。已标注的方法：Language Models & LLM / 语言模型与LLM (2); Causal Learning / 因果学习 (1); Graph Learning / 图学习 (1)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 统一成本与调仓频率，报告收益、回撤、风险及换手。 代表论文的摘要、金融关联证据及原文链接见 [1](../finance_notes/2025.findings-acl.1239.md) · [2](../finance_notes/2026.findings-acl.1555.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 在统一资产池、再平衡频率和成本假设下比较配置方法，考察极端行情与长期资金目标。

### English

**Problem and subdirections.** The output is an asset set, portfolio weights or a rebalancing plan. Performance depends jointly on signals, constraints, costs and allocation, so aggregate gains cannot be attributed to one module without controls.

**Current coverage and methods.** This page covers only Findings / core. Frequent subcategories: Risk-Return and Multi-Objective Optimization / 风险收益及多目标优化 (2). Recorded methods: Language Models & LLM / 语言模型与LLM (2); Causal Learning / 因果学习 (1); Graph Learning / 图学习 (1). Counts overlap and are not performance rankings.

**Data and evaluation.** Match costs and rebalancing frequency; report return, drawdown, risk and turnover. Representative abstracts, financial evidence and original sources are linked at [1](../finance_notes/2025.findings-acl.1239.md) · [2](../finance_notes/2026.findings-acl.1555.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Compare allocation methods under matched universes, rebalancing frequencies and costs, including stressed markets and long-horizon objectives.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. Are LLMs Rational Investors? A Study on the Financial Bias in LLMs](../finance_notes/2025.findings-acl.1239.md) · ACL 2025 | 诊断与缓解 LLM 的金融投资偏差<br>Diagnose and mitigate financial investment biases in LLMs | 偏差评分改善不等于投资收益改善<br>Better bias scores do not imply higher investment returns |
| [2. Analyze Like a Venture Capitalist: Information-Gain and Knowledge Enhanced Graph Reasoning for Startup Success Prediction](../finance_notes/2026.findings-acl.1555.md) · ACL 2026 | 知识与证据子图支持创业成功预测<br>Knowledge and evidence subgraphs support startup-success prediction | 结果标签和真实投资退出收益不同<br>Outcome labels differ from realized investment exits |

<!-- task-summary:end -->

## Subtopic statistics / 子方向统计

| Subtopic | Papers |
|---|---:|
| Asset Selection and Weight Allocation / 资产选择与权重配置 | 0 |
| Dynamic Allocation and Rebalancing / 动态配置与再平衡 | 0 |
| Multi-Asset and Cross-Market Allocation / 多资产与跨市场配置 | 0 |
| Risk-Return and Multi-Objective Optimization / 风险收益及多目标优化 | 2 |
| Transaction Costs and Investment Constraints / 交易成本与投资约束 | 0 |
| Long-Term Wealth and Goal-Based Investing / 长期财富与目标投资 | 0 |

## Full paper list / 完整论文列表

| Year | Venue | Paper | Scope | Primary topic | Subtopics | Methods | Resources |
|---|---|---|---|---|---|---|---|
| 2026 | ACL | [Analyze Like a Venture Capitalist: Information-Gain and Knowledge Enhanced Graph Reasoning for Startup Success Prediction](../finance_notes/2026.findings-acl.1555.md) | core | Valuation Prediction / 估值预测 | Stock Price and Return Prediction / 股票价格与收益预测; Risk-Return and Multi-Objective Optimization / 风险收益及多目标优化 | Language Models & LLM / 语言模型与LLM; Graph Learning / 图学习 | [PDF](../../pdfs/ACL/2026/2026.findings-acl.1555.pdf) |
| 2025 | ACL | [Are LLMs Rational Investors? A Study on the Financial Bias in LLMs](../finance_notes/2025.findings-acl.1239.md) | core | Portfolio / 投资组合 | Risk-Return and Multi-Objective Optimization / 风险收益及多目标优化 | Language Models & LLM / 语言模型与LLM; Causal Learning / 因果学习 | [PDF](../../pdfs/ACL/2025/2025.findings-acl.1239.pdf) |
