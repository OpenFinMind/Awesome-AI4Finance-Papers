# Blockchain / 区块链

Blockchain transactions, digital assets, smart contracts and DeFi mechanisms. / 链上交易、数字资产、智能合约与 DeFi 机制。

26 Main long papers. Topic memberships can overlap.

[All topics](../ai_for_finance.md) · [Classification definitions](../finance_taxonomy.md) · [CSV](blockchain.csv) · [Excel](../../finance_catalog.xlsx)

<!-- task-summary:start -->

## Research summary / 研究总结

**Blockchain / 区块链 · Main / Core**

2026-11-20 · 26 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 以链上交易、账户、智能合约、代币及 DeFi 机制为对象。区块链背景与具体金融任务允许交叉标注；数字资产价格预测、攻击检测与机制研究分别确定主方向。

**当前收录与方法。** 本页仅总结 Main / core 中的论文。当前较常见的子分类：On-Chain Transaction and Account Analysis / 链上交易与账户分析 (20); Smart Contract Analysis / 智能合约分析 (8); Digital Assets and Token Economics / 数字资产及代币经济 (4); DeFi and On-Chain Financial Mechanisms / DeFi 与链上金融机制 (1)。已标注的方法：Language Models & LLM / 语言模型与LLM (10); Uncertainty & Robustness / 不确定性与鲁棒性 (6); Representation Learning / 表征学习 (5); Generative Modeling / 生成建模 (3); Graph Learning / 图学习 (3)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 关注链与协议差异、时间切分、攻击假设及链上成本。 代表论文的摘要、金融关联证据及原文链接见 [1](../finance_notes/aaai-2025-32026.md) · [2](../finance_notes/kdd-2024-c8f737f65bdf.md) · [3](../finance_notes/icml-2026-K5S8N5NgD8.md) · [4](../finance_notes/2025.acl-long.126.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 检验跨链、跨协议和时间变化下的泛化，把链上成本与可观察信息边界纳入评价。

### English

**Problem and subdirections.** Objects include on-chain transactions, accounts, contracts, tokens and DeFi mechanisms. Blockchain context can overlap with a financial task; price forecasting, attack detection and mechanism analysis have distinct primary tasks.

**Current coverage and methods.** This page covers only Main / core. Frequent subcategories: On-Chain Transaction and Account Analysis / 链上交易与账户分析 (20); Smart Contract Analysis / 智能合约分析 (8); Digital Assets and Token Economics / 数字资产及代币经济 (4); DeFi and On-Chain Financial Mechanisms / DeFi 与链上金融机制 (1). Recorded methods: Language Models & LLM / 语言模型与LLM (10); Uncertainty & Robustness / 不确定性与鲁棒性 (6); Representation Learning / 表征学习 (5); Generative Modeling / 生成建模 (3); Graph Learning / 图学习 (3). Counts overlap and are not performance rankings.

**Data and evaluation.** Check chain/protocol differences, chronological splits, attack assumptions and on-chain costs. Representative abstracts, financial evidence and original sources are linked at [1](../finance_notes/aaai-2025-32026.md) · [2](../finance_notes/kdd-2024-c8f737f65bdf.md) · [3](../finance_notes/icml-2026-K5S8N5NgD8.md) · [4](../finance_notes/2025.acl-long.126.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Test transfer across chains, protocols and time, accounting for on-chain costs and limits of observable information.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. SCALM: Detecting Bad Practices in Smart Contracts Through LLMs](../finance_notes/aaai-2025-32026.md) · AAAI 2025 | 用 LLM 与检索检测合约不良实践<br>LLMs and retrieval detect smart-contract bad practices | 不良实践不一定是可利用漏洞<br>Bad practices are not necessarily exploitable vulnerabilities |
| [2. BitLINK: Temporal Linkage of Address Clusters in Bitcoin Blockchain](../finance_notes/kdd-2024-c8f737f65bdf.md) · KDD 2024 | 以自监督时间同步关联地址簇<br>Self-supervised temporal synchrony links address clusters | 地址关联与真实身份确认不同<br>Address linkage differs from verified real-world identity |
| [3. EVMbench: Evaluating AI Agents on Smart Contract Security](../finance_notes/icml-2026-K5S8N5NgD8.md) · ICML 2026 | 用执行测试及链状态评价合约安全 Agent<br>Execution tests and chain state evaluate contract-security agents | 本地任务环境不代表任意线上系统<br>Local task environments do not represent arbitrary live systems |
| [4. INVESTORBENCH: A Benchmark for Financial Decision-Making Tasks with LLM-based Agent](../finance_notes/2025.acl-long.126.md) · ACL 2025 | 跨股票、加密资产及 ETF 的决策基准<br>Decision benchmarks across equities, crypto and ETFs | 收益比较依赖相同环境与信息权限<br>Return comparisons need matched environments and information access |

<!-- task-summary:end -->

## Subtopic statistics / 子方向统计

| Subtopic | Papers |
|---|---:|
| On-Chain Transaction and Account Analysis / 链上交易与账户分析 | 20 |
| Digital Assets and Token Economics / 数字资产及代币经济 | 4 |
| DeFi and On-Chain Financial Mechanisms / DeFi 与链上金融机制 | 1 |
| Smart Contract Analysis / 智能合约分析 | 8 |
| Fees, MEV and On-Chain Markets / 交易费、MEV 与链上市场机制 | 0 |
| Blockchain Financial Infrastructure / 区块链金融基础设施 | 0 |

## Full paper list / 完整论文列表

| Year | Venue | Paper | Scope | Primary topic | Subtopics | Methods | Resources |
|---|---|---|---|---|---|---|---|
| 2026 | AAAI | [BugSweeper: Function-Level Detection of Smart Contract Vulnerabilities Using Graph Neural Networks](../finance_notes/aaai-2026-37021.md) | core | Blockchain / 区块链 | Smart Contract Analysis / 智能合约分析; Privacy and Sensitive Information Protection / 隐私与敏感信息保护; Financial Network and Smart Contract Attacks / 金融网络及智能合约攻击 | Graph Learning / 图学习; Uncertainty & Robustness / 不确定性与鲁棒性 | [PDF](../../pdfs/AAAI/2026/aaai-2026-37021__BugSweeper_Function_Level_Detection_of_Smart_Contract_Vulnerabilities_Using_Graph_Neural_Networks.pdf) |
| 2026 | AAAI | [IGT4ETH: An Isotropic Pre-trained Graph Transformer for Ethereum Account Classification](../finance_notes/aaai-2026-39536.md) | core | Blockchain / 区块链 | On-Chain Transaction and Account Analysis / 链上交易与账户分析; Payment, Transaction and Insurance Fraud / 支付、交易及保险欺诈 | Language Models & LLM / 语言模型与LLM; Transformer / Transformer模型; Representation Learning / 表征学习 | [PDF](../../pdfs/AAAI/2026/aaai-2026-39536__IGT4ETH_An_Isotropic_Pre_trained_Graph_Transformer_for_Ethereum_Account_Classification.pdf) |
| 2026 | ACL | [EVM-QuestBench: An Execution-Grounded Benchmark for Natural-Language Transaction Code Generation](../finance_notes/2026.acl-long.1642.md) | core | Financial Evaluation / 金融评测 | Smart Contract Analysis / 智能合约分析; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Financial Understanding and Multimodal Evaluation / 金融理解及多模态评测; On-Chain Transaction and Account Analysis / 链上交易与账户分析 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/ACL/2026/2026.acl-long.1642__EVM_QuestBench_An_Execution_Grounded_Benchmark_for_Natural_Language_Transaction_Code_Generation.pdf) |
| 2026 | ACL | [Towards Trustworthy Smart Contract Synthesis: A Multi-Agent Framework with Lean-Based Verification](../finance_notes/2026.acl-long.1836.md) | core | Blockchain / 区块链 | Smart Contract Analysis / 智能合约分析 | Language Models & LLM / 语言模型与LLM; Uncertainty & Robustness / 不确定性与鲁棒性 | [PDF](../../pdfs/ACL/2026/2026.acl-long.1836__Towards_Trustworthy_Smart_Contract_Synthesis_A_Multi_Agent_Framework_with_Lean_Based_Verification.pdf) |
| 2026 | ICLR | [CTBench: Cryptocurrency Time Series Generation Benchmark](../finance_notes/iclr-2026-RzT2sombPD.md) | core | Financial Evaluation / 金融评测 | Sequence Generation and Augmentation / 序列生成与数据增强; On-Chain Transaction and Account Analysis / 链上交易与账户分析; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Digital Assets and Token Economics / 数字资产及代币经济 | Generative Modeling / 生成建模 | [PDF](../../pdfs/ICLR/2026/iclr-2026-RzT2sombPD__CTBench_Cryptocurrency_Time_Series_Generation_Benchmark.pdf) |
| 2026 | ICLR | [Trade in Minutes! Rationality-Driven Agentic System for Quantitative Financial Trading](../finance_notes/iclr-2026-ROEwZAxqyS.md) | core | Financial Decision Making / 金融决策 | Trading Strategies and Buy/Sell Decisions / 交易策略与买卖决策; Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策; On-Chain Transaction and Account Analysis / 链上交易与账户分析 | Language Models & LLM / 语言模型与LLM; Optimization & Numerical Methods / 优化与数值方法 | [PDF](../../pdfs/ICLR/2026/iclr-2026-ROEwZAxqyS__Trade_in_Minutes_Rationality_Driven_Agentic_System_for_Quantitative_Financial_Trading.pdf) |
| 2026 | ICML | [EVMbench: Evaluating AI Agents on Smart Contract Security](../finance_notes/icml-2026-K5S8N5NgD8.md) | core | Financial Evaluation / 金融评测 | On-Chain Transaction and Account Analysis / 链上交易与账户分析; Smart Contract Analysis / 智能合约分析; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Financial Decision and Agent Evaluation / 金融决策与智能体评测; Evaluation Protocols and Metrics / 评测协议与指标 |  | [PDF](../../pdfs/ICML/2026/icml-2026-K5S8N5NgD8__EVMbench_Evaluating_AI_Agents_on_Smart_Contract_Security.pdf) |
| 2026 | ICML | [Scam2Prompt: A Scalable Framework for Auditing Malicious Scam Endpoints in Production LLMs](../finance_notes/icml-2026-jEQQBE30m1.md) | core | Financial Safety / 金融安全 | Trading Strategies and Buy/Sell Decisions / 交易策略与买卖决策; Payment, Transaction and Insurance Fraud / 支付、交易及保险欺诈; On-Chain Transaction and Account Analysis / 链上交易与账户分析; Regulatory Compliance and Violation Detection / 监管合规与违规检测 | Language Models & LLM / 语言模型与LLM; Uncertainty & Robustness / 不确定性与鲁棒性; Retrieval & RAG / 检索与RAG | [PDF](../../pdfs/ICML/2026/icml-2026-jEQQBE30m1__Scam2Prompt_A_Scalable_Framework_for_Auditing_Malicious_Scam_Endpoints_in_Production_LLMs.pdf) |
| 2026 | NeurIPS | [Leakage Thresholds for Sandwich Equilibria Under Partial Information](../finance_notes/neurips-2026-yuiJS0iLhX.md) | core | Blockchain / 区块链 | Trading Strategies and Buy/Sell Decisions / 交易策略与买卖决策; Market Making and Quoting / 做市与报价策略; Smart Contract Analysis / 智能合约分析 | Uncertainty & Robustness / 不确定性与鲁棒性 | [Online](https://openreview.net/forum?id=yuiJS0iLhX) |
| 2025 | AAAI | [MTVHunter: Smart Contracts Vulnerability Detection Based on Multi-Teacher Knowledge Translation](../finance_notes/aaai-2025-33664.md) | core | Blockchain / 区块链 | Smart Contract Analysis / 智能合约分析; Privacy and Sensitive Information Protection / 隐私与敏感信息保护; Financial Network and Smart Contract Attacks / 金融网络及智能合约攻击 | Representation Learning / 表征学习 | [PDF](../../pdfs/AAAI/2025/aaai-2025-33664__MTVHunter_Smart_Contracts_Vulnerability_Detection_Based_on_Multi_Teacher_Knowledge_Translation.pdf) |
| 2025 | AAAI | [SCALM: Detecting Bad Practices in Smart Contracts Through LLMs](../finance_notes/aaai-2025-32026.md) | core | Blockchain / 区块链 | Smart Contract Analysis / 智能合约分析; Privacy and Sensitive Information Protection / 隐私与敏感信息保护; Financial Network and Smart Contract Attacks / 金融网络及智能合约攻击 | Language Models & LLM / 语言模型与LLM; Retrieval & RAG / 检索与RAG | [PDF](../../pdfs/AAAI/2025/aaai-2025-32026__SCALM_Detecting_Bad_Practices_in_Smart_Contracts_Through_LLMs.pdf) |
| 2025 | ACL | [INVESTORBENCH: A Benchmark for Financial Decision-Making Tasks with LLM-based Agent](../finance_notes/2025.acl-long.126.md) | core | Financial Evaluation / 金融评测 | Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策; On-Chain Transaction and Account Analysis / 链上交易与账户分析; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Financial Decision and Agent Evaluation / 金融决策与智能体评测 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/ACL/2025/2025.acl-long.126__INVESTORBENCH_A_Benchmark_for_Financial_Decision_Making_Tasks_with_LLM_based_Agent.pdf) |
| 2025 | KDD | [Chainlet Orbits: Topological Address Embedding for Blockchain](../finance_notes/kdd-2025-953d74ec6de0.md) | core | Blockchain / 区块链 | On-Chain Transaction and Account Analysis / 链上交易与账户分析 | Graph Learning / 图学习; Representation Learning / 表征学习 | [Online](https://doi.org/10.1145/3690624.3709322) |
| 2025 | KDD | [CryptoMixer: Fine-grained market information-aware MLP Networks for Individual Cryptocurrency Trading Prediction](../finance_notes/kdd-2025-43e156362af8.md) | core | Financial Decision Making / 金融决策 | Trading Strategies and Buy/Sell Decisions / 交易策略与买卖决策; On-Chain Transaction and Account Analysis / 链上交易与账户分析; Digital Assets and Token Economics / 数字资产及代币经济 |  | [Online](https://doi.org/10.1145/3711896.3736900) |
| 2025 | NeurIPS | [BlockScan: Detecting Anomalies in Blockchain Transactions](../finance_notes/neurips-2025-URB690A5r5.md) | core | Financial Safety / 金融安全 | Payment, Transaction and Insurance Fraud / 支付、交易及保险欺诈; On-Chain Transaction and Account Analysis / 链上交易与账户分析 | Language Models & LLM / 语言模型与LLM; Transformer / Transformer模型; Multimodal Learning / 多模态学习; Representation Learning / 表征学习 | [PDF](../../pdfs/NeurIPS/2025/neurips-2025-URB690A5r5__BlockScan_Detecting_Anomalies_in_Blockchain_Transactions.pdf) |
| 2025 | NeurIPS | [OPHR: Mastering Volatility Trading with Multi-Agent Deep Reinforcement Learning](../finance_notes/neurips-2025-2p4AtivyZz.md) | core | Financial Decision Making / 金融决策 | Dynamic Hedging / 动态对冲; Option and Derivative Pricing / 期权及衍生品定价; Trading Strategies and Buy/Sell Decisions / 交易策略与买卖决策; Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策; On-Chain Transaction and Account Analysis / 链上交易与账户分析 | Reinforcement Learning / 强化学习; Uncertainty & Robustness / 不确定性与鲁棒性 | [Online](https://openreview.net/forum?id=2p4AtivyZz) |
| 2024 | EMNLP | [CryptoTrade: A Reflective LLM-based Agent to Guide Zero-shot Cryptocurrency Trading](../finance_notes/2024.emnlp-main.63.md) | core | Financial Decision Making / 金融决策 | General Sequence Forecasting / 通用序列预测; Trading Strategies and Buy/Sell Decisions / 交易策略与买卖决策; Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策; On-Chain Transaction and Account Analysis / 链上交易与账户分析; Digital Assets and Token Economics / 数字资产及代币经济 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/EMNLP/2024/2024.emnlp-main.63__CryptoTrade_A_Reflective_LLM_based_Agent_to_Guide_Zero_shot_Cryptocurrency_Trading.pdf) |
| 2024 | ICLR | [EX-Graph: A Pioneering Dataset Bridging Ethereum and X](../finance_notes/iclr-2024-juE0rWGCJW.md) | core | Financial Evaluation / 金融评测 | Trading Strategies and Buy/Sell Decisions / 交易策略与买卖决策; On-Chain Transaction and Account Analysis / 链上交易与账户分析; Financial Datasets and Task Benchmarks / 金融数据集与任务基准 |  | [PDF](../../pdfs/ICLR/2024/iclr-2024-juE0rWGCJW__EX_Graph_A_Pioneering_Dataset_Bridging_Ethereum_and_X.pdf) |
| 2024 | KDD | [BitLINK: Temporal Linkage of Address Clusters in Bitcoin Blockchain](../finance_notes/kdd-2024-c8f737f65bdf.md) | core | Blockchain / 区块链 | On-Chain Transaction and Account Analysis / 链上交易与账户分析 |  | [Online](https://doi.org/10.1145/3637528.3672037) |
| 2024 | KDD | [Money Never Sleeps: Maximizing Liquidity Mining Yields in Decentralized Finance](../finance_notes/kdd-2024-ea7cae0393f9.md) | core | Blockchain / 区块链 | On-Chain Transaction and Account Analysis / 链上交易与账户分析; DeFi and On-Chain Financial Mechanisms / DeFi 与链上金融机制 | Generative Modeling / 生成建模 | [Online](https://doi.org/10.1145/3637528.3671942) |
| 2024 | NeurIPS | [Detecting Bugs with Substantial Monetary Consequences by LLM and Rule-based Reasoning](../finance_notes/neurips-2024-94090.md) | core | Blockchain / 区块链 | Smart Contract Analysis / 智能合约分析; Privacy and Sensitive Information Protection / 隐私与敏感信息保护 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/NeurIPS/2024/neurips-2024-94090__Detecting_Bugs_with_Substantial_Monetary_Consequences_by_LLM_and_Rule_based_Reasoning.pdf) |
| 2021 | ICML | [Learning Node Representations Using Stationary Flow Prediction on Large Payment and Cash Transaction Networks](../finance_notes/icml-2021-9941.md) | core | Blockchain / 区块链 | On-Chain Transaction and Account Analysis / 链上交易与账户分析 | Generative Modeling / 生成建模; Uncertainty & Robustness / 不确定性与鲁棒性; Representation Learning / 表征学习 | [PDF](../../pdfs/ICML/2021/icml-2021-9941__Learning_Node_Representations_Using_Stationary_Flow_Prediction_on_Large_Payment_and_Cash_Transaction_Netw.pdf) |
| 2021 | NeurIPS | [Graphical Models in Heavy-Tailed Markets](../finance_notes/neurips-2021-w1FvEPcwTnI.md) | core | Pricing / 定价 | Asset Pricing and Risk Premia / 资产定价与风险溢价; On-Chain Transaction and Account Analysis / 链上交易与账户分析 | Graph Learning / 图学习; Optimization & Numerical Methods / 优化与数值方法 | [PDF](../../pdfs/NeurIPS/2021/neurips-2021-w1FvEPcwTnI__Graphical_Models_in_Heavy_Tailed_Markets.pdf) |
| 2020 | AAAI | [Shoreline: Data-Driven Threshold Estimation of Online Reserves of Cryptocurrency Trading Platforms](../finance_notes/aaai-2020-5472.md) | core | Financial Risk / 金融风险 | Market Risk and Tail Losses / 市场风险与尾部损失; On-Chain Transaction and Account Analysis / 链上交易与账户分析; Digital Assets and Token Economics / 数字资产及代币经济 |  | [PDF](../../pdfs/AAAI/2020/aaai-2020-5472__Shoreline_Data_Driven_Threshold_Estimation_of_Online_Reserves_of_Cryptocurrency_Trading_Platforms.pdf) |
| 2019 | AAAI | [The Pure Price of Anarchy of Pool Block Withholding Attacks in Bitcoin Mining](../finance_notes/aaai-2019-3994.md) | core | Blockchain / 区块链 | On-Chain Transaction and Account Analysis / 链上交易与账户分析 |  | [PDF](../../pdfs/AAAI/2019/aaai-2019-3994__The_Pure_Price_of_Anarchy_of_Pool_Block_Withholding_Attacks_in_Bitcoin_Mining.pdf) |
| 2017 | NeurIPS | [Deanonymization in the Bitcoin P2P Network](../finance_notes/neurips-2017-8928.md) | core | Financial Safety / 金融安全 | On-Chain Transaction and Account Analysis / 链上交易与账户分析; Privacy and Sensitive Information Protection / 隐私与敏感信息保护 | Diffusion & Flow / 扩散与流模型 | [PDF](../../pdfs/NeurIPS/2017/neurips-2017-8928__Deanonymization_in_the_Bitcoin_P2P_Network.pdf) |
