# Financial Decision Making / 金融决策

Trading, execution, market simulation and financial agent decisions; portfolio allocation has its own task. / 交易、执行、市场仿真与金融 Agent 决策；组合配置单列。

25 Findings long papers. Topic memberships can overlap.

[All topics](../ai_for_finance.md) · [Classification definitions](../finance_taxonomy.md) · [CSV](financial_decision.csv) · [Excel](../../finance_catalog.xlsx)

<!-- task-summary:start -->

## Research summary / 研究总结

**Financial Decision Making / 金融决策 · Findings / Core**

2026-11-20 · 25 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 核心输出是买卖、执行、做市、对冲或业务行动。金融智能体的工具调用与市场仿真需要与实际决策结果相联系，组合权重配置单列为投资组合。

**当前收录与方法。** 本页仅总结 Findings / core 中的论文。当前较常见的子分类：Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策 (21); Trading Strategies and Buy/Sell Decisions / 交易策略与买卖决策 (12); Corporate Financing and Cash Management / 企业融资及现金管理决策 (1)。已标注的方法：Language Models & LLM / 语言模型与LLM (22); Retrieval & RAG / 检索与RAG (4); Uncertainty & Robustness / 不确定性与鲁棒性 (4); Reinforcement Learning / 强化学习 (3); Optimization & Numerical Methods / 优化与数值方法 (3)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 区分离线预测与闭环决策，显式计入交易成本、延迟和市场冲击。 代表论文的摘要、金融关联证据及原文链接见 [1](../finance_notes/2026.findings-acl.430.md) · [2](../finance_notes/2026.findings-acl.1799.md) · [3](../finance_notes/2026.findings-acl.746.md) · [4](../finance_notes/2026.findings-emnlp.971.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 用闭环实验和消融分离信息、推理、工具与执行贡献，纳入延迟、市场冲击和失败恢复。

### English

**Problem and subdirections.** Outputs are trading, execution, quoting, hedging or business actions. Agent tool use and market simulation need to connect to decision outcomes; portfolio weight allocation has its own category.

**Current coverage and methods.** This page covers only Findings / core. Frequent subcategories: Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策 (21); Trading Strategies and Buy/Sell Decisions / 交易策略与买卖决策 (12); Corporate Financing and Cash Management / 企业融资及现金管理决策 (1). Recorded methods: Language Models & LLM / 语言模型与LLM (22); Retrieval & RAG / 检索与RAG (4); Uncertainty & Robustness / 不确定性与鲁棒性 (4); Reinforcement Learning / 强化学习 (3); Optimization & Numerical Methods / 优化与数值方法 (3). Counts overlap and are not performance rankings.

**Data and evaluation.** Separate offline prediction from closed-loop decisions; include costs, latency and market impact. Representative abstracts, financial evidence and original sources are linked at [1](../finance_notes/2026.findings-acl.430.md) · [2](../finance_notes/2026.findings-acl.1799.md) · [3](../finance_notes/2026.findings-acl.746.md) · [4](../finance_notes/2026.findings-emnlp.971.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Use closed-loop experiments and ablations to separate information, reasoning, tool and execution effects, including latency, market impact and recovery from failure.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. Cogito: A Cognitive Agentic Framework Driven by Dynamic Graph of Thoughts for Financial Report Generation](../finance_notes/2026.findings-acl.430.md) · ACL 2026 | 动态图思维和多角色协同生成投研报告<br>Dynamic thought graphs and collaboration generate research reports | 报告评分需拆分事实、分析与呈现<br>Report scores should separate facts, analysis and presentation |
| [2. Do LLM Agents Really Mimic Humans? Diagnosing and Aligning Microeconomic Behaviors in Macro-ABMs](../finance_notes/2026.findings-acl.1799.md) · ACL 2026 | 用人类调查校准微观行为并检查宏观仿真<br>Calibrate micro behavior against surveys and test macro simulation | 特定人群校准不证明总体代表性<br>Calibration to a population does not establish universal representativeness |
| [3. FinToolSyn: A forward synthesis Framework for Financial Tool-Use Dialogue Data with Dynamic Tool Retrieval](../finance_notes/2026.findings-acl.746.md) · ACL 2026 | 正向合成金融工具对话及动态候选检索<br>Forward synthesis of financial tool dialogues with dynamic candidates | 合成工具空间与真实接口仍存在差异<br>Synthetic tool spaces still differ from real APIs |
| [4. Can Agentic Trading Systems Pay for Their Own Intelligence?](../finance_notes/2026.findings-emnlp.971.md) · EMNLP 2026 | 由运行轨迹诊断利润、择时及智能成本<br>Trace-based diagnosis of profit, timing and intelligence costs | 归因口径和资本规模影响可行性判断<br>Attribution and capital scale affect viability conclusions |

<!-- task-summary:end -->

## Subtopic statistics / 子方向统计

| Subtopic | Papers |
|---|---:|
| Trading Strategies and Buy/Sell Decisions / 交易策略与买卖决策 | 12 |
| Order Execution / 订单执行 | 0 |
| Market Making and Quoting / 做市与报价策略 | 0 |
| Dynamic Hedging / 动态对冲 | 0 |
| Corporate Financing and Cash Management / 企业融资及现金管理决策 | 1 |
| Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策 | 21 |

## Full paper list / 完整论文列表

| Year | Venue | Paper | Scope | Primary topic | Subtopics | Methods | Resources |
|---|---|---|---|---|---|---|---|
| 2026 | ACL | [AlphaQuanter: An End-to-End Tool-Augmented Agentic Reinforcement Learning Framework for Stock Trading](../finance_notes/2026.findings-acl.456.md) | core | Financial Decision Making / 金融决策 | Trading Strategies and Buy/Sell Decisions / 交易策略与买卖决策; Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策 | Language Models & LLM / 语言模型与LLM; Reinforcement Learning / 强化学习; Optimization & Numerical Methods / 优化与数值方法 | [PDF](../../pdfs/ACL/2026/2026.findings-acl.456.pdf) |
| 2026 | ACL | [Behavioral Consistency Validation for LLM Agents: An Analysis of Trading-Style Switching through Stock-Market Simulation](../finance_notes/2026.findings-acl.2006.md) | core | Financial Decision Making / 金融决策 | Trading Strategies and Buy/Sell Decisions / 交易策略与买卖决策; Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/ACL/2026/2026.findings-acl.2006.pdf) |
| 2026 | ACL | [Cogito: A Cognitive Agentic Framework Driven by Dynamic Graph of Thoughts for Financial Report Generation](../finance_notes/2026.findings-acl.430.md) | core | Financial Decision Making / 金融决策 | Financial Summarization and Report Generation / 金融摘要与报告生成; Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策; Report and Disclosure Understanding / 财报与公告理解 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/ACL/2026/2026.findings-acl.430.pdf) |
| 2026 | ACL | [Do LLM Agents Really Mimic Humans? Diagnosing and Aligning Microeconomic Behaviors in Macro-ABMs](../finance_notes/2026.findings-acl.1799.md) | core | Financial Decision Making / 金融决策 | General Sequence Forecasting / 通用序列预测; Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策 | Language Models & LLM / 语言模型与LLM; Causal Learning / 因果学习 | [PDF](../../pdfs/ACL/2026/2026.findings-acl.1799.pdf) |
| 2026 | ACL | [FinToolSyn: A forward synthesis Framework for Financial Tool-Use Dialogue Data with Dynamic Tool Retrieval](../finance_notes/2026.findings-acl.746.md) | core | Financial Decision Making / 金融决策 | Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策 | Language Models & LLM / 语言模型与LLM; Generative Modeling / 生成建模; Uncertainty & Robustness / 不确定性与鲁棒性; Retrieval & RAG / 检索与RAG | [PDF](../../pdfs/ACL/2026/2026.findings-acl.746.pdf) |
| 2026 | ACL | [From Heard to Lived Opinions: Simulating Opinion Dynamics with Grounded LLM Agents in Economic Environments](../finance_notes/2026.findings-acl.580.md) | core | Financial Decision Making / 金融决策 | Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策; Sequence Representation and Pattern Discovery / 序列表示与模式发现; Sequence Generation and Augmentation / 序列生成与数据增强 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/ACL/2026/2026.findings-acl.580.pdf) |
| 2026 | ACL | [From Tasks to Teams: A Risk-First Evaluation Framework for Multi-Agent LLM Systems in Finance](../finance_notes/2026.findings-acl.1934.md) | core | Financial Evaluation / 金融评测 | Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策; Privacy and Sensitive Information Protection / 隐私与敏感信息保护; Financial Model and Agent Safety / 金融模型及智能体安全; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Financial Decision and Agent Evaluation / 金融决策与智能体评测; Evaluation Protocols and Metrics / 评测协议与指标 | Language Models & LLM / 语言模型与LLM; Uncertainty & Robustness / 不确定性与鲁棒性 | [PDF](../../pdfs/ACL/2026/2026.findings-acl.1934.pdf) |
| 2026 | EMNLP | [Can Agentic Trading Systems Pay for Their Own Intelligence?](../finance_notes/2026.findings-emnlp.971.md) | core | Financial Decision Making / 金融决策 | Trading Strategies and Buy/Sell Decisions / 交易策略与买卖决策; Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/EMNLP/2026/2026.findings-emnlp.971.pdf) |
| 2026 | EMNLP | [Chain-of-Alpha: Unleashing the Power of Large Language Models for Alpha Mining in Quantitative Trading](../finance_notes/2026.findings-emnlp.506.md) | core | Factor Mining / 因子挖掘 | Factor Discovery and Formula Generation / 因子发现与公式生成; Trading Strategies and Buy/Sell Decisions / 交易策略与买卖决策 | Language Models & LLM / 语言模型与LLM; Optimization & Numerical Methods / 优化与数值方法 | [PDF](../../pdfs/EMNLP/2026/2026.findings-emnlp.506.pdf) |
| 2026 | EMNLP | [CrossAlpha: An Annual-Report Benchmark for Cross-Market Factor Research with LLM Agents](../finance_notes/2026.findings-emnlp.914.md) | core | Financial Evaluation / 金融评测 | Report and Disclosure Understanding / 财报与公告理解; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Financial Decision and Agent Evaluation / 金融决策与智能体评测; Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/EMNLP/2026/2026.findings-emnlp.914.pdf) |
| 2026 | EMNLP | [EnterpriseBench: Benchmarking LLM Agents on Enterprise-Level Strategic Reasoning and Decision-Making](../finance_notes/2026.findings-emnlp.932.md) | core | Financial Evaluation / 金融评测 | Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Financial Decision and Agent Evaluation / 金融决策与智能体评测 | Language Models & LLM / 语言模型与LLM; Uncertainty & Robustness / 不确定性与鲁棒性 | [PDF](../../pdfs/EMNLP/2026/2026.findings-emnlp.932.pdf) |
| 2026 | EMNLP | [FaVOR: LLM-Based Agentic Framework for Factor Mining via Empirical Validation](../finance_notes/2026.findings-emnlp.1514.md) | core | Factor Mining / 因子挖掘 | Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策; Factor Discovery and Formula Generation / 因子发现与公式生成 | Language Models & LLM / 语言模型与LLM; Uncertainty & Robustness / 不确定性与鲁棒性 | [PDF](../../pdfs/EMNLP/2026/2026.findings-emnlp.1514.pdf) |
| 2026 | EMNLP | [FinanceHarness: Autonomous Financial Deep Research Framework](../finance_notes/2026.findings-emnlp.2251.md) | core | Financial Decision Making / 金融决策 | Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/EMNLP/2026/2026.findings-emnlp.2251.pdf) |
| 2026 | EMNLP | [FinHopper: A Progressive Multi-Hop Benchmark for Complex Financial Agents with Step-wise Evaluation](../finance_notes/2026.findings-emnlp.2384.md) | core | Financial Evaluation / 金融评测 | Numerical Calculation and Program Reasoning / 数值计算与程序推理; Financial Factual QA / 金融事实问答; Financial Semantic Matching and Ranking / 金融语义匹配与排序; Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Financial Decision and Agent Evaluation / 金融决策与智能体评测; Evaluation Protocols and Metrics / 评测协议与指标; Trading Strategies and Buy/Sell Decisions / 交易策略与买卖决策; Multi-Document and Multi-Hop QA / 多文档与多跳问答 | Language Models & LLM / 语言模型与LLM; Retrieval & RAG / 检索与RAG | [PDF](../../pdfs/EMNLP/2026/2026.findings-emnlp.2384.pdf) |
| 2026 | EMNLP | [FinRAQ: Financial News Reasoning through Importance Ranking and Socratic Questioning](../finance_notes/2026.findings-emnlp.1432.md) | core | Financial Decision Making / 金融决策 | Trading Strategies and Buy/Sell Decisions / 交易策略与买卖决策 |  | [PDF](../../pdfs/EMNLP/2026/2026.findings-emnlp.1432.pdf) |
| 2026 | EMNLP | [OpenFinGym: A Verifiable, Multi-Task Gym Environment for Evaluating Quant Agents](../finance_notes/2026.findings-emnlp.2258.md) | core | Financial Evaluation / 金融评测 | Trading Strategies and Buy/Sell Decisions / 交易策略与买卖决策; Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Financial Decision and Agent Evaluation / 金融决策与智能体评测; Evaluation Protocols and Metrics / 评测协议与指标 | Language Models & LLM / 语言模型与LLM; Reinforcement Learning / 强化学习 | [PDF](../../pdfs/EMNLP/2026/2026.findings-emnlp.2258.pdf) |
| 2026 | EMNLP | [RealFin: Benchmarking Agent Workflow Orchestration Beyond MCP-Style Tool Connectivity](../finance_notes/2026.findings-emnlp.341.md) | core | Financial Evaluation / 金融评测 | Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Financial Decision and Agent Evaluation / 金融决策与智能体评测 | Retrieval & RAG / 检索与RAG | [PDF](../../pdfs/EMNLP/2026/2026.findings-emnlp.341.pdf) |
| 2026 | EMNLP | [Scaling Multi-Agent Systems with Prospect-State Propagation](../finance_notes/2026.findings-emnlp.1585.md) | core | Financial Decision Making / 金融决策 | General Sequence Forecasting / 通用序列预测; Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/EMNLP/2026/2026.findings-emnlp.1585.pdf) |
| 2025 | ACL | [FLAG-TRADER: Fusion LLM-Agent with Gradient-based Reinforcement Learning for Financial Trading](../finance_notes/2025.findings-acl.716.md) | core | Financial Decision Making / 金融决策 | Trading Strategies and Buy/Sell Decisions / 交易策略与买卖决策; Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策 | Language Models & LLM / 语言模型与LLM; Reinforcement Learning / 强化学习; Optimization & Numerical Methods / 优化与数值方法 | [PDF](../../pdfs/ACL/2025/2025.findings-acl.716.pdf) |
| 2025 | EMNLP | [Agent Trading Arena: A Study on Numerical Understanding in LLM-Based Agents](../finance_notes/2025.findings-emnlp.294.md) | core | Financial Decision Making / 金融决策 | Trading Strategies and Buy/Sell Decisions / 交易策略与买卖决策; Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/EMNLP/2025/2025.findings-emnlp.294.pdf) |
| 2025 | EMNLP | [FinHEAR: Human Expertise and Adaptive Risk-Aware Temporal Reasoning for Financial Decision-Making](../finance_notes/2025.findings-emnlp.87.md) | core | Financial Decision Making / 金融决策 | Trading Strategies and Buy/Sell Decisions / 交易策略与买卖决策 | Language Models & LLM / 语言模型与LLM; Retrieval & RAG / 检索与RAG | [PDF](../../pdfs/EMNLP/2025/2025.findings-emnlp.87.pdf) |
| 2025 | EMNLP | [Large Language Model Agents in Finance: A Survey Bridging Research, Practice, and Real-World Deployment](../finance_notes/2025.findings-emnlp.972.md) | core | Financial Decision Making / 金融决策 | Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Financial Understanding and Multimodal Evaluation / 金融理解及多模态评测; Financial Decision and Agent Evaluation / 金融决策与智能体评测 | Language Models & LLM / 语言模型与LLM; Multimodal Learning / 多模态学习 | [PDF](../../pdfs/EMNLP/2025/2025.findings-emnlp.972.pdf) |
| 2025 | EMNLP | [QuantAgents: Towards Multi-agent Financial System via Simulated Trading](../finance_notes/2025.findings-emnlp.945.md) | core | Financial Decision Making / 金融决策 | Trading Strategies and Buy/Sell Decisions / 交易策略与买卖决策; Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/EMNLP/2025/2025.findings-emnlp.945.pdf) |
| 2024 | ACL | [Can Large Language Models Mine Interpretable Financial Factors More Effectively? A Neural-Symbolic Factor Mining Agent Model](../finance_notes/2024.findings-acl.233.md) | core | Factor Mining / 因子挖掘 | Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策; Factor Discovery and Formula Generation / 因子发现与公式生成 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/ACL/2024/2024.findings-acl.233.pdf) |
| 2021 | ACL | [Trade the Event: Corporate Events Detection for News-Based Event-Driven Trading](../finance_notes/2021.findings-acl.186.md) | core | Financial Decision Making / 金融决策 | Trading Strategies and Buy/Sell Decisions / 交易策略与买卖决策; Stock Price and Return Prediction / 股票价格与收益预测; News and Social Media Sentiment / 新闻与社交媒体情感; Corporate Financing and Cash Management / 企业融资及现金管理决策; Financial Event Detection and Linking / 金融事件识别与关联 |  | [PDF](../../pdfs/ACL/2021/2021.findings-acl.186.pdf) |
