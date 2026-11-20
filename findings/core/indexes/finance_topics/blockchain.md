# Blockchain / 区块链

Blockchain transactions, digital assets, smart contracts and DeFi mechanisms. / 链上交易、数字资产、智能合约与 DeFi 机制。

3 Findings long papers. Topic memberships can overlap.

[All topics](../ai_for_finance.md) · [Classification definitions](../finance_taxonomy.md) · [CSV](blockchain.csv) · [Excel](../../finance_catalog.xlsx)

<!-- task-summary:start -->

## Research summary / 研究总结

**Blockchain / 区块链 · Findings / Core**

2026-11-20 · 3 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 以链上交易、账户、智能合约、代币及 DeFi 机制为对象。区块链背景与具体金融任务允许交叉标注；数字资产价格预测、攻击检测与机制研究分别确定主方向。

**当前收录与方法。** 本页仅总结 Findings / core 中的论文。当前较常见的子分类：On-Chain Transaction and Account Analysis / 链上交易与账户分析 (2); Smart Contract Analysis / 智能合约分析 (1)。已标注的方法：Language Models & LLM / 语言模型与LLM (1); Uncertainty & Robustness / 不确定性与鲁棒性 (1)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 关注链与协议差异、时间切分、攻击假设及链上成本。 代表论文的摘要、金融关联证据及原文链接见 [1](../finance_notes/2026.findings-emnlp.366.md) · [2](../finance_notes/2026.findings-emnlp.1343.md) · [3](../finance_notes/2022.findings-emnlp.471.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 检验跨链、跨协议和时间变化下的泛化，把链上成本与可观察信息边界纳入评价。

### English

**Problem and subdirections.** Objects include on-chain transactions, accounts, contracts, tokens and DeFi mechanisms. Blockchain context can overlap with a financial task; price forecasting, attack detection and mechanism analysis have distinct primary tasks.

**Current coverage and methods.** This page covers only Findings / core. Frequent subcategories: On-Chain Transaction and Account Analysis / 链上交易与账户分析 (2); Smart Contract Analysis / 智能合约分析 (1). Recorded methods: Language Models & LLM / 语言模型与LLM (1); Uncertainty & Robustness / 不确定性与鲁棒性 (1). Counts overlap and are not performance rankings.

**Data and evaluation.** Check chain/protocol differences, chronological splits, attack assumptions and on-chain costs. Representative abstracts, financial evidence and original sources are linked at [1](../finance_notes/2026.findings-emnlp.366.md) · [2](../finance_notes/2026.findings-emnlp.1343.md) · [3](../finance_notes/2022.findings-emnlp.471.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Test transfer across chains, protocols and time, accounting for on-chain costs and limits of observable information.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. TxSum: User-Centered Ethereum Transaction Understanding with Micro-Level Semantic Grounding](../finance_notes/2026.findings-emnlp.366.md) · EMNLP 2026 | 交易轨迹级事实核验和面向用户的解释<br>Trace-level factual checks and user-centered transaction explanation | 用户实验规模与任务范围需保留<br>Preserve user-study size and task scope |
| [2. CyberChainBench: Can AI Agents Secure Smart Contracts Against Real-World On-Chain Vulnerabilities?](../finance_notes/2026.findings-emnlp.1343.md) · EMNLP 2026 | 历史链状态中的合约安全检测与修复评价<br>Evaluate contract-security detection and repair on historical chain states | 安全任务经济计分不是实盘盈利<br>Economic task scores are not live trading profit |
| [3. Tweet Based Reach Aware Temporal Attention Network for NFT Valuation](../finance_notes/2022.findings-emnlp.471.md) · EMNLP 2022 | 推文影响范围与时间注意力预测 NFT 趋势<br>Tweet reach and temporal attention forecast NFT trends | 特定集合及市场阶段限制外推<br>Collection and market-period coverage limit extrapolation |

<!-- task-summary:end -->

## Subtopic statistics / 子方向统计

| Subtopic | Papers |
|---|---:|
| On-Chain Transaction and Account Analysis / 链上交易与账户分析 | 2 |
| Digital Assets and Token Economics / 数字资产及代币经济 | 0 |
| DeFi and On-Chain Financial Mechanisms / DeFi 与链上金融机制 | 0 |
| Smart Contract Analysis / 智能合约分析 | 1 |
| Fees, MEV and On-Chain Markets / 交易费、MEV 与链上市场机制 | 0 |
| Blockchain Financial Infrastructure / 区块链金融基础设施 | 0 |

## Full paper list / 完整论文列表

| Year | Venue | Paper | Scope | Primary topic | Subtopics | Methods | Resources |
|---|---|---|---|---|---|---|---|
| 2026 | EMNLP | [CyberChainBench: Can AI Agents Secure Smart Contracts Against Real-World On-Chain Vulnerabilities?](../finance_notes/2026.findings-emnlp.1343.md) | core | Financial Evaluation / 金融评测 | On-Chain Transaction and Account Analysis / 链上交易与账户分析; Smart Contract Analysis / 智能合约分析; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Financial Decision and Agent Evaluation / 金融决策与智能体评测 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/EMNLP/2026/2026.findings-emnlp.1343.pdf) |
| 2026 | EMNLP | [TxSum: User-Centered Ethereum Transaction Understanding with Micro-Level Semantic Grounding](../finance_notes/2026.findings-emnlp.366.md) | core | Blockchain / 区块链 | On-Chain Transaction and Account Analysis / 链上交易与账户分析 | Uncertainty & Robustness / 不确定性与鲁棒性 | [PDF](../../pdfs/EMNLP/2026/2026.findings-emnlp.366.pdf) |
| 2022 | EMNLP | [Tweet Based Reach Aware Temporal Attention Network for NFT Valuation](../finance_notes/2022.findings-emnlp.471.md) | core | Valuation Prediction / 估值预测 | FX, Commodity and Digital Asset Forecasting / 汇率、商品及数字资产行情预测; Enterprise and Equity Valuation / 企业价值与股权估值 |  | [PDF](../../pdfs/EMNLP/2022/2022.findings-emnlp.471.pdf) |
