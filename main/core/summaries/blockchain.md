## Research summary / 研究总结

**Blockchain / 区块链 · Main / Core**

2026-11-20 · 26 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 以链上交易、账户、智能合约、代币及 DeFi 机制为对象。区块链背景与具体金融任务允许交叉标注；数字资产价格预测、攻击检测与机制研究分别确定主方向。

**当前收录与方法。** 本页仅总结 Main / core 中的论文。当前较常见的子分类：On-Chain Transaction and Account Analysis / 链上交易与账户分析 (20); Smart Contract Analysis / 智能合约分析 (8); Digital Assets and Token Economics / 数字资产及代币经济 (4); DeFi and On-Chain Financial Mechanisms / DeFi 与链上金融机制 (1)。已标注的方法：Language Models & LLM / 语言模型与LLM (10); Uncertainty & Robustness / 不确定性与鲁棒性 (6); Representation Learning / 表征学习 (5); Generative Modeling / 生成建模 (3); Graph Learning / 图学习 (3)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 关注链与协议差异、时间切分、攻击假设及链上成本。 代表论文的摘要、金融关联证据及原文链接见 [1](../indexes/finance_notes/aaai-2025-32026.md) · [2](../indexes/finance_notes/kdd-2024-c8f737f65bdf.md) · [3](../indexes/finance_notes/icml-2026-K5S8N5NgD8.md) · [4](../indexes/finance_notes/2025.acl-long.126.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 检验跨链、跨协议和时间变化下的泛化，把链上成本与可观察信息边界纳入评价。

### English

**Problem and subdirections.** Objects include on-chain transactions, accounts, contracts, tokens and DeFi mechanisms. Blockchain context can overlap with a financial task; price forecasting, attack detection and mechanism analysis have distinct primary tasks.

**Current coverage and methods.** This page covers only Main / core. Frequent subcategories: On-Chain Transaction and Account Analysis / 链上交易与账户分析 (20); Smart Contract Analysis / 智能合约分析 (8); Digital Assets and Token Economics / 数字资产及代币经济 (4); DeFi and On-Chain Financial Mechanisms / DeFi 与链上金融机制 (1). Recorded methods: Language Models & LLM / 语言模型与LLM (10); Uncertainty & Robustness / 不确定性与鲁棒性 (6); Representation Learning / 表征学习 (5); Generative Modeling / 生成建模 (3); Graph Learning / 图学习 (3). Counts overlap and are not performance rankings.

**Data and evaluation.** Check chain/protocol differences, chronological splits, attack assumptions and on-chain costs. Representative abstracts, financial evidence and original sources are linked at [1](../indexes/finance_notes/aaai-2025-32026.md) · [2](../indexes/finance_notes/kdd-2024-c8f737f65bdf.md) · [3](../indexes/finance_notes/icml-2026-K5S8N5NgD8.md) · [4](../indexes/finance_notes/2025.acl-long.126.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Test transfer across chains, protocols and time, accounting for on-chain costs and limits of observable information.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. SCALM: Detecting Bad Practices in Smart Contracts Through LLMs](../indexes/finance_notes/aaai-2025-32026.md) · AAAI 2025 | 用 LLM 与检索检测合约不良实践<br>LLMs and retrieval detect smart-contract bad practices | 不良实践不一定是可利用漏洞<br>Bad practices are not necessarily exploitable vulnerabilities |
| [2. BitLINK: Temporal Linkage of Address Clusters in Bitcoin Blockchain](../indexes/finance_notes/kdd-2024-c8f737f65bdf.md) · KDD 2024 | 以自监督时间同步关联地址簇<br>Self-supervised temporal synchrony links address clusters | 地址关联与真实身份确认不同<br>Address linkage differs from verified real-world identity |
| [3. EVMbench: Evaluating AI Agents on Smart Contract Security](../indexes/finance_notes/icml-2026-K5S8N5NgD8.md) · ICML 2026 | 用执行测试及链状态评价合约安全 Agent<br>Execution tests and chain state evaluate contract-security agents | 本地任务环境不代表任意线上系统<br>Local task environments do not represent arbitrary live systems |
| [4. INVESTORBENCH: A Benchmark for Financial Decision-Making Tasks with LLM-based Agent](../indexes/finance_notes/2025.acl-long.126.md) · ACL 2025 | 跨股票、加密资产及 ETF 的决策基准<br>Decision benchmarks across equities, crypto and ETFs | 收益比较依赖相同环境与信息权限<br>Return comparisons need matched environments and information access |
