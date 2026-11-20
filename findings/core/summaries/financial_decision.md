## Research summary / 研究总结

**Financial Decision Making / 金融决策 · Findings / Core**

2026-11-20 · 25 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 核心输出是买卖、执行、做市、对冲或业务行动。金融智能体的工具调用与市场仿真需要与实际决策结果相联系，组合权重配置单列为投资组合。

**当前收录与方法。** 本页仅总结 Findings / core 中的论文。当前较常见的子分类：Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策 (21); Trading Strategies and Buy/Sell Decisions / 交易策略与买卖决策 (12); Corporate Financing and Cash Management / 企业融资及现金管理决策 (1)。已标注的方法：Language Models & LLM / 语言模型与LLM (22); Retrieval & RAG / 检索与RAG (4); Uncertainty & Robustness / 不确定性与鲁棒性 (4); Reinforcement Learning / 强化学习 (3); Optimization & Numerical Methods / 优化与数值方法 (3)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 区分离线预测与闭环决策，显式计入交易成本、延迟和市场冲击。 代表论文的摘要、金融关联证据及原文链接见 [1](../indexes/finance_notes/2026.findings-acl.430.md) · [2](../indexes/finance_notes/2026.findings-acl.1799.md) · [3](../indexes/finance_notes/2026.findings-acl.746.md) · [4](../indexes/finance_notes/2026.findings-emnlp.971.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 用闭环实验和消融分离信息、推理、工具与执行贡献，纳入延迟、市场冲击和失败恢复。

### English

**Problem and subdirections.** Outputs are trading, execution, quoting, hedging or business actions. Agent tool use and market simulation need to connect to decision outcomes; portfolio weight allocation has its own category.

**Current coverage and methods.** This page covers only Findings / core. Frequent subcategories: Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策 (21); Trading Strategies and Buy/Sell Decisions / 交易策略与买卖决策 (12); Corporate Financing and Cash Management / 企业融资及现金管理决策 (1). Recorded methods: Language Models & LLM / 语言模型与LLM (22); Retrieval & RAG / 检索与RAG (4); Uncertainty & Robustness / 不确定性与鲁棒性 (4); Reinforcement Learning / 强化学习 (3); Optimization & Numerical Methods / 优化与数值方法 (3). Counts overlap and are not performance rankings.

**Data and evaluation.** Separate offline prediction from closed-loop decisions; include costs, latency and market impact. Representative abstracts, financial evidence and original sources are linked at [1](../indexes/finance_notes/2026.findings-acl.430.md) · [2](../indexes/finance_notes/2026.findings-acl.1799.md) · [3](../indexes/finance_notes/2026.findings-acl.746.md) · [4](../indexes/finance_notes/2026.findings-emnlp.971.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Use closed-loop experiments and ablations to separate information, reasoning, tool and execution effects, including latency, market impact and recovery from failure.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. Cogito: A Cognitive Agentic Framework Driven by Dynamic Graph of Thoughts for Financial Report Generation](../indexes/finance_notes/2026.findings-acl.430.md) · ACL 2026 | 动态图思维和多角色协同生成投研报告<br>Dynamic thought graphs and collaboration generate research reports | 报告评分需拆分事实、分析与呈现<br>Report scores should separate facts, analysis and presentation |
| [2. Do LLM Agents Really Mimic Humans? Diagnosing and Aligning Microeconomic Behaviors in Macro-ABMs](../indexes/finance_notes/2026.findings-acl.1799.md) · ACL 2026 | 用人类调查校准微观行为并检查宏观仿真<br>Calibrate micro behavior against surveys and test macro simulation | 特定人群校准不证明总体代表性<br>Calibration to a population does not establish universal representativeness |
| [3. FinToolSyn: A forward synthesis Framework for Financial Tool-Use Dialogue Data with Dynamic Tool Retrieval](../indexes/finance_notes/2026.findings-acl.746.md) · ACL 2026 | 正向合成金融工具对话及动态候选检索<br>Forward synthesis of financial tool dialogues with dynamic candidates | 合成工具空间与真实接口仍存在差异<br>Synthetic tool spaces still differ from real APIs |
| [4. Can Agentic Trading Systems Pay for Their Own Intelligence?](../indexes/finance_notes/2026.findings-emnlp.971.md) · EMNLP 2026 | 由运行轨迹诊断利润、择时及智能成本<br>Trace-based diagnosis of profit, timing and intelligence costs | 归因口径和资本规模影响可行性判断<br>Attribution and capital scale affect viability conclusions |
