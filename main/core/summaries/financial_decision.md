## Research summary / 研究总结

**Financial Decision Making / 金融决策 · Main / Core**

2026-11-20 · 74 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 核心输出是买卖、执行、做市、对冲或业务行动。金融智能体的工具调用与市场仿真需要与实际决策结果相联系，组合权重配置单列为投资组合。

**当前收录与方法。** 本页仅总结 Main / core 中的论文。当前较常见的子分类：Trading Strategies and Buy/Sell Decisions / 交易策略与买卖决策 (42); Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策 (40); Market Making and Quoting / 做市与报价策略 (14); Dynamic Hedging / 动态对冲 (3); Order Execution / 订单执行 (1)。已标注的方法：Language Models & LLM / 语言模型与LLM (26); Uncertainty & Robustness / 不确定性与鲁棒性 (24); Reinforcement Learning / 强化学习 (19); Optimization & Numerical Methods / 优化与数值方法 (10); Generative Modeling / 生成建模 (9)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 区分离线预测与闭环决策，显式计入交易成本、延迟和市场冲击。 代表论文的摘要、金融关联证据及原文链接见 [1](../indexes/finance_notes/aaai-2026-40027.md) · [2](../indexes/finance_notes/2026.acl-long.265.md) · [3](../indexes/finance_notes/2026.emnlp-main.510.md) · [4](../indexes/finance_notes/2024.acl-long.829.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 用闭环实验和消融分离信息、推理、工具与执行贡献，纳入延迟、市场冲击和失败恢复。

### English

**Problem and subdirections.** Outputs are trading, execution, quoting, hedging or business actions. Agent tool use and market simulation need to connect to decision outcomes; portfolio weight allocation has its own category.

**Current coverage and methods.** This page covers only Main / core. Frequent subcategories: Trading Strategies and Buy/Sell Decisions / 交易策略与买卖决策 (42); Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策 (40); Market Making and Quoting / 做市与报价策略 (14); Dynamic Hedging / 动态对冲 (3); Order Execution / 订单执行 (1). Recorded methods: Language Models & LLM / 语言模型与LLM (26); Uncertainty & Robustness / 不确定性与鲁棒性 (24); Reinforcement Learning / 强化学习 (19); Optimization & Numerical Methods / 优化与数值方法 (10); Generative Modeling / 生成建模 (9). Counts overlap and are not performance rankings.

**Data and evaluation.** Separate offline prediction from closed-loop decisions; include costs, latency and market impact. Representative abstracts, financial evidence and original sources are linked at [1](../indexes/finance_notes/aaai-2026-40027.md) · [2](../indexes/finance_notes/2026.acl-long.265.md) · [3](../indexes/finance_notes/2026.emnlp-main.510.md) · [4](../indexes/finance_notes/2024.acl-long.829.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Use closed-loop experiments and ablations to separate information, reasoning, tool and execution effects, including latency, market impact and recovery from failure.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. MetaTrader: Learning to Generalize RL Trading Policies Beyond Offline Data](../indexes/finance_notes/aaai-2026-40027.md) · AAAI 2026 | 双层训练和保守 TD 缓解离线策略过拟合<br>Bilevel training and conservative TD address offline overfitting | 数据变换不是所有市场变化的替代品<br>Data transformations do not represent every market shift |
| [2. FinSight: Towards Real-World Financial Deep Research](../indexes/finance_notes/2026.acl-long.265.md) · ACL 2026 | 可执行分析、来源引用与视觉反馈的投研报告<br>Research reports with executable analysis, citations and visual feedback | 报告质量不直接验证投资预测能力<br>Report quality does not directly establish predictive investment skill |
| [3. Summoning the Oracle to Slay It: Mitigating Look-Ahead Bias in Financial Backtesting with Large Language Models](../indexes/finance_notes/2026.emnlp-main.510.md) · EMNLP 2026 | FinCAD 诊断并缓解参数化前视偏差<br>FinCAD diagnoses and attenuates parametric look-ahead bias | 校正后回测仍需截止日之后验证<br>Corrected backtests still need post-cutoff validation |
| [4. EconAgent: Large Language Model-Empowered Agents for Simulating Macroeconomic Activities](../indexes/finance_notes/2024.acl-long.829.md) · ACL 2024 | 异质 LLM 主体模拟工作与消费决策<br>Heterogeneous LLM agents simulate work and consumption | 仿真合理性仍需现实校准<br>Simulation plausibility still requires real-world calibration |
