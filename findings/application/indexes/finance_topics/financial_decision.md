# Financial Decision Making / 金融决策

Trading, execution, market simulation and financial agent decisions; portfolio allocation has its own task. / 交易、执行、市场仿真与金融 Agent 决策；组合配置单列。

7 Findings long papers. Topic memberships can overlap.

[All topics](../ai_for_finance.md) · [Classification definitions](../finance_taxonomy.md) · [CSV](financial_decision.csv) · [Excel](../../finance_catalog.xlsx)

<!-- task-summary:start -->

## Research summary / 研究总结

**Financial Decision Making / 金融决策 · Findings / Application**

2026-11-20 · 7 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 核心输出是买卖、执行、做市、对冲或业务行动。金融智能体的工具调用与市场仿真需要与实际决策结果相联系，组合权重配置单列为投资组合。

**当前收录与方法。** 本页仅总结 Findings / application 中的论文。当前较常见的子分类：Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策 (7)。已标注的方法：Language Models & LLM / 语言模型与LLM (7); Uncertainty & Robustness / 不确定性与鲁棒性 (2); Reinforcement Learning / 强化学习 (2); Retrieval & RAG / 检索与RAG (2); Causal Learning / 因果学习 (1)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 区分离线预测与闭环决策，显式计入交易成本、延迟和市场冲击。 代表论文的摘要、金融关联证据及原文链接见 [1](../finance_notes/2026.findings-acl.931.md) · [2](../finance_notes/2026.findings-emnlp.1316.md) · [3](../finance_notes/2026.findings-emnlp.354.md) · [4](../finance_notes/2026.findings-emnlp.505.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 用闭环实验和消融分离信息、推理、工具与执行贡献，纳入延迟、市场冲击和失败恢复。

### English

**Problem and subdirections.** Outputs are trading, execution, quoting, hedging or business actions. Agent tool use and market simulation need to connect to decision outcomes; portfolio weight allocation has its own category.

**Current coverage and methods.** This page covers only Findings / application. Frequent subcategories: Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策 (7). Recorded methods: Language Models & LLM / 语言模型与LLM (7); Uncertainty & Robustness / 不确定性与鲁棒性 (2); Reinforcement Learning / 强化学习 (2); Retrieval & RAG / 检索与RAG (2); Causal Learning / 因果学习 (1). Counts overlap and are not performance rankings.

**Data and evaluation.** Separate offline prediction from closed-loop decisions; include costs, latency and market impact. Representative abstracts, financial evidence and original sources are linked at [1](../finance_notes/2026.findings-acl.931.md) · [2](../finance_notes/2026.findings-emnlp.1316.md) · [3](../finance_notes/2026.findings-emnlp.354.md) · [4](../finance_notes/2026.findings-emnlp.505.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Use closed-loop experiments and ablations to separate information, reasoning, tool and execution effects, including latency, market impact and recovery from failure.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. ToolDNA: Autonomous Evolution of Tool Metadata for Robust Dialogue Agents](../finance_notes/2026.findings-acl.931.md) · ACL 2026 | 通过 RL 协同改进策略及工具元数据<br>RL coevolves policies and tool metadata | 贷款计算案例不代表完整银行部署<br>Loan-calculation cases do not establish full banking deployment |
| [2. AEL: Evolving Agent Harness in Open-Ended Environments](../finance_notes/2026.findings-emnlp.1316.md) · EMNLP 2026 | 研究主题：AEL: Evolving Agent Harness in Open-Ended Environments<br>Research topic: AEL: Evolving Agent Harness in Open-Ended Environments | 按原文的任务、数据和实验设置解释结果。<br>Interpret results within the original task, data and experimental setting. |
| [3. BizSage: A Self-Evolving Multi-Agent Framework for Business Research with Efficient Knowledge Retrieval](../finance_notes/2026.findings-emnlp.354.md) · EMNLP 2026 | 研究主题：BizSage: A Self-Evolving Multi-Agent Framework for Business Research with Efficient Knowledge Retrieval<br>Research topic: BizSage: A Self-Evolving Multi-Agent Framework for Business Research with Efficient Knowledge Retrieval | 按原文的任务、数据和实验设置解释结果。<br>Interpret results within the original task, data and experimental setting. |
| [4. Can Large Language Models Uncover the Structure of Social Opinions?](../finance_notes/2026.findings-emnlp.505.md) · EMNLP 2026 | 研究主题：Can Large Language Models Uncover the Structure of Social Opinions?<br>Research topic: Can Large Language Models Uncover the Structure of Social Opinions? | 按原文的任务、数据和实验设置解释结果。<br>Interpret results within the original task, data and experimental setting. |

<!-- task-summary:end -->

## Subtopic statistics / 子方向统计

| Subtopic | Papers |
|---|---:|
| Trading Strategies and Buy/Sell Decisions / 交易策略与买卖决策 | 0 |
| Order Execution / 订单执行 | 0 |
| Market Making and Quoting / 做市与报价策略 | 0 |
| Dynamic Hedging / 动态对冲 | 0 |
| Corporate Financing and Cash Management / 企业融资及现金管理决策 | 0 |
| Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策 | 7 |

## Full paper list / 完整论文列表

| Year | Venue | Paper | Scope | Primary topic | Subtopics | Methods | Resources |
|---|---|---|---|---|---|---|---|
| 2026 | ACL | [ToolDNA: Autonomous Evolution of Tool Metadata for Robust Dialogue Agents](../finance_notes/2026.findings-acl.931.md) | application | Financial Services / 金融服务 | Lending, Payment and Banking Workflows / 贷款、支付及银行业务流程; Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策 | Language Models & LLM / 语言模型与LLM; Reinforcement Learning / 强化学习; Uncertainty & Robustness / 不确定性与鲁棒性 | [PDF](../../pdfs/ACL/2026/2026.findings-acl.931.pdf) |
| 2026 | EMNLP | [AEL: Evolving Agent Harness in Open-Ended Environments](../finance_notes/2026.findings-emnlp.1316.md) | application | Financial Decision Making / 金融决策 | Asset Selection and Weight Allocation / 资产选择与权重配置; Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策 | Language Models & LLM / 语言模型与LLM; Reinforcement Learning / 强化学习; Causal Learning / 因果学习; Retrieval & RAG / 检索与RAG | [PDF](../../pdfs/EMNLP/2026/2026.findings-emnlp.1316.pdf) |
| 2026 | EMNLP | [BizSage: A Self-Evolving Multi-Agent Framework for Business Research with Efficient Knowledge Retrieval](../finance_notes/2026.findings-emnlp.354.md) | application | Financial Decision Making / 金融决策 | Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策 | Language Models & LLM / 语言模型与LLM; Retrieval & RAG / 检索与RAG | [PDF](../../pdfs/EMNLP/2026/2026.findings-emnlp.354.pdf) |
| 2026 | EMNLP | [Can Large Language Models Uncover the Structure of Social Opinions?](../finance_notes/2026.findings-emnlp.505.md) | application | Financial Decision Making / 金融决策 | Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/EMNLP/2026/2026.findings-emnlp.505.pdf) |
| 2025 | ACL | [DeFine: Decision-Making with Analogical Reasoning over Factor Profiles](../finance_notes/2025.findings-acl.238.md) | application | Financial Decision Making / 金融决策 | Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策 | Language Models & LLM / 语言模型与LLM; Uncertainty & Robustness / 不确定性与鲁棒性 | [PDF](../../pdfs/ACL/2025/2025.findings-acl.238.pdf) |
| 2025 | EMNLP | [DecisionFlow: Advancing Large Language Model as Principled Decision Maker](../finance_notes/2025.findings-emnlp.905.md) | application | Financial Decision Making / 金融决策 | Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/EMNLP/2025/2025.findings-emnlp.905.pdf) |
| 2024 | EMNLP | [How Personality Traits Influence Negotiation Outcomes? A Simulation based on Large Language Models](../finance_notes/2024.findings-emnlp.605.md) | application | Financial Decision Making / 金融决策 | Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/EMNLP/2024/2024.findings-emnlp.605.pdf) |
