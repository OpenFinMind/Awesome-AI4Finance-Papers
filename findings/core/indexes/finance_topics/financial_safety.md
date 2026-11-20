# Financial Safety / 金融安全

Fraud, scams, money laundering, privacy, attacks and regulatory compliance. / 欺诈、诈骗、反洗钱、隐私、攻击与监管合规。

19 Findings long papers. Topic memberships can overlap.

[All topics](../ai_for_finance.md) · [Classification definitions](../finance_taxonomy.md) · [CSV](financial_safety.csv) · [Excel](../../finance_catalog.xlsx)

<!-- task-summary:start -->

## Research summary / 研究总结

**Financial Safety / 金融安全 · Findings / Core**

2026-11-20 · 19 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 关注恶意行为、违规、隐私泄露和攻击造成的损害。欺诈与正常信用违约需要分开；一般公平性或反事实解释若服务于信用评分，主方向仍是金融风险。

**当前收录与方法。** 本页仅总结 Findings / core 中的论文。当前较常见的子分类：Financial Model and Agent Safety / 金融模型及智能体安全 (12); Payment, Transaction and Insurance Fraud / 支付、交易及保险欺诈 (7); Privacy and Sensitive Information Protection / 隐私与敏感信息保护 (4); Regulatory Compliance and Violation Detection / 监管合规与违规检测 (1); Financial Network and Smart Contract Attacks / 金融网络及智能合约攻击 (1)。已标注的方法：Language Models & LLM / 语言模型与LLM (17); Uncertainty & Robustness / 不确定性与鲁棒性 (9); Fairness & Recourse / 公平性与算法追索 (2); Tabular Learning / 表格学习 (1); Representation Learning / 表征学习 (1)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 重视类别不平衡、误报成本、攻击适应性、隐私与合规证据。 代表论文的摘要、金融关联证据及原文链接见 [1](../finance_notes/2026.findings-emnlp.629.md) · [2](../finance_notes/2025.findings-emnlp.270.md) · [3](../finance_notes/2020.findings-emnlp.143.md) · [4](../finance_notes/2026.findings-acl.1481.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 加强误报成本、攻击适应性、延迟标签和真实业务分布检验，明确隐私与安全保障的假设。

### English

**Problem and subdirections.** This task concerns malicious behavior, violations, privacy leakage and attacks. Fraud differs from ordinary credit default; fairness or recourse for credit scoring keeps financial risk as its primary task.

**Current coverage and methods.** This page covers only Findings / core. Frequent subcategories: Financial Model and Agent Safety / 金融模型及智能体安全 (12); Payment, Transaction and Insurance Fraud / 支付、交易及保险欺诈 (7); Privacy and Sensitive Information Protection / 隐私与敏感信息保护 (4); Regulatory Compliance and Violation Detection / 监管合规与违规检测 (1); Financial Network and Smart Contract Attacks / 金融网络及智能合约攻击 (1). Recorded methods: Language Models & LLM / 语言模型与LLM (17); Uncertainty & Robustness / 不确定性与鲁棒性 (9); Fairness & Recourse / 公平性与算法追索 (2); Tabular Learning / 表格学习 (1); Representation Learning / 表征学习 (1). Counts overlap and are not performance rankings.

**Data and evaluation.** Account for imbalance, false-positive costs, adaptive attacks, privacy and compliance evidence. Representative abstracts, financial evidence and original sources are linked at [1](../finance_notes/2026.findings-emnlp.629.md) · [2](../finance_notes/2025.findings-emnlp.270.md) · [3](../finance_notes/2020.findings-emnlp.143.md) · [4](../finance_notes/2026.findings-acl.1481.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Evaluate false-positive costs, adaptive attacks, delayed labels and operational distributions, with explicit assumptions behind privacy and safety guarantees.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. FinGuard: Detecting Financial Regulatory Non-Compliance in LLM Interactions](../finance_notes/2026.findings-emnlp.629.md) · EMNLP 2026 | 规则驱动的查询及回复风险检测模型<br>Rule-grounded query/response risk detection | 规则版本与辖域决定适用范围<br>Rule versions and jurisdictions determine scope |
| [2. Detecting Continuously Evolving Scam Calls under Limited Annotation: A LLM-Augmented Expert Rule Framework](../finance_notes/2025.findings-emnlp.270.md) · EMNLP 2025 | 专家规则和反思支持少标注的演化诈骗检测<br>Expert rules and reflection support evolving-scam detection with few labels | 规则可更新性与跨场景实测需区分<br>Rule adaptability differs from demonstrated cross-setting transfer |
| [3. Inferring about fraudulent collusion risk on Brazilian public works contracts in official texts using a Bi-LSTM approach](../finance_notes/2020.findings-emnlp.143.md) · EMNLP 2020 | 从巴西官方采购文本预测串标风险<br>Predict collusion risk from Brazilian procurement text | 风险标签不等于司法确认欺诈<br>Risk labels differ from legally established fraud |
| [4. Are Large Language Models Reliable Reviewers? A Benchmark for Error Detection in Financial Documents](../finance_notes/2026.findings-acl.1481.md) · ACL 2026 | 分复杂度测试财务文档错误识别<br>Test financial-document errors at different complexities | 文档新颖性依赖被测模型的截止时间<br>Document novelty depends on the evaluated model cutoff |

<!-- task-summary:end -->

## Subtopic statistics / 子方向统计

| Subtopic | Papers |
|---|---:|
| Payment, Transaction and Insurance Fraud / 支付、交易及保险欺诈 | 7 |
| AML and Illicit Fund Tracing / 反洗钱与非法资金追踪 | 0 |
| Identity and Account Abuse / 身份冒用与账户滥用 | 0 |
| Financial Network and Smart Contract Attacks / 金融网络及智能合约攻击 | 1 |
| Privacy and Sensitive Information Protection / 隐私与敏感信息保护 | 4 |
| Regulatory Compliance and Violation Detection / 监管合规与违规检测 | 1 |
| Financial Model and Agent Safety / 金融模型及智能体安全 | 12 |

## Full paper list / 完整论文列表

| Year | Venue | Paper | Scope | Primary topic | Subtopics | Methods | Resources |
|---|---|---|---|---|---|---|---|
| 2026 | ACL | [Are Large Language Models Reliable Reviewers? A Benchmark for Error Detection in Financial Documents](../finance_notes/2026.findings-acl.1481.md) | core | Financial Evaluation / 金融评测 | Financial Model and Agent Safety / 金融模型及智能体安全; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Financial Understanding and Multimodal Evaluation / 金融理解及多模态评测; Reliability, Safety and Fairness Evaluation / 可靠性、安全与公平性评测 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/ACL/2026/2026.findings-acl.1481.pdf) |
| 2026 | ACL | [Fin-Bias: Comprehensive Evaluation for LLM Decision-Making under human bias in Finance Domain](../finance_notes/2026.findings-acl.279.md) | core | Financial Evaluation / 金融评测 | Financial Model and Agent Safety / 金融模型及智能体安全; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Financial Decision and Agent Evaluation / 金融决策与智能体评测; Reliability, Safety and Fairness Evaluation / 可靠性、安全与公平性评测; Evaluation Protocols and Metrics / 评测协议与指标 | Language Models & LLM / 语言模型与LLM; Uncertainty & Robustness / 不确定性与鲁棒性 | [PDF](../../pdfs/ACL/2026/2026.findings-acl.279.pdf) |
| 2026 | ACL | [FinSafetyBench: Evaluating LLM Safety in Real-World Financial Scenarios](../finance_notes/2026.findings-acl.694.md) | core | Financial Evaluation / 金融评测 | Privacy and Sensitive Information Protection / 隐私与敏感信息保护; Financial Model and Agent Safety / 金融模型及智能体安全; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Reliability, Safety and Fairness Evaluation / 可靠性、安全与公平性评测; Evaluation Protocols and Metrics / 评测协议与指标 | Language Models & LLM / 语言模型与LLM; Uncertainty & Robustness / 不确定性与鲁棒性 | [PDF](../../pdfs/ACL/2026/2026.findings-acl.694.pdf) |
| 2026 | ACL | [From Tasks to Teams: A Risk-First Evaluation Framework for Multi-Agent LLM Systems in Finance](../finance_notes/2026.findings-acl.1934.md) | core | Financial Evaluation / 金融评测 | Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策; Privacy and Sensitive Information Protection / 隐私与敏感信息保护; Financial Model and Agent Safety / 金融模型及智能体安全; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Financial Decision and Agent Evaluation / 金融决策与智能体评测; Evaluation Protocols and Metrics / 评测协议与指标 | Language Models & LLM / 语言模型与LLM; Uncertainty & Robustness / 不确定性与鲁棒性 | [PDF](../../pdfs/ACL/2026/2026.findings-acl.1934.pdf) |
| 2026 | ACL | [Same Claim, Different Judgment: Benchmarking Scenario-Induced Bias in Multilingual Financial Misinformation Detection](../finance_notes/2026.findings-acl.479.md) | core | Financial Evaluation / 金融评测 | Financial Model and Agent Safety / 金融模型及智能体安全; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Reliability, Safety and Fairness Evaluation / 可靠性、安全与公平性评测 | Language Models & LLM / 语言模型与LLM; Uncertainty & Robustness / 不确定性与鲁棒性 | [PDF](../../pdfs/ACL/2026/2026.findings-acl.479.pdf) |
| 2026 | ACL | [Targeting the Needle, Ignoring the Haystack: Anchoring Crucial Cues for Evolving Scam Call Detection via an LLM-Assisted Classifier](../finance_notes/2026.findings-acl.1025.md) | core | Financial Safety / 金融安全 | Payment, Transaction and Insurance Fraud / 支付、交易及保险欺诈 | Language Models & LLM / 语言模型与LLM; Uncertainty & Robustness / 不确定性与鲁棒性 | [PDF](../../pdfs/ACL/2026/2026.findings-acl.1025.pdf) |
| 2026 | ACL | [Uncovering Currency Bias and Syntax Gap in Text Embedding Models](../finance_notes/2026.findings-acl.2118.md) | core | Financial Evaluation / 金融评测 | Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Reliability, Safety and Fairness Evaluation / 可靠性、安全与公平性评测; Financial Semantic Matching and Ranking / 金融语义匹配与排序; Financial Model and Agent Safety / 金融模型及智能体安全 | Fairness & Recourse / 公平性与算法追索; Representation Learning / 表征学习 | [PDF](../../pdfs/ACL/2026/2026.findings-acl.2118.pdf) |
| 2026 | EMNLP | [Bias Before the Model: Detecting and Removing Cognitive Bias Triggers in Financial Text](../finance_notes/2026.findings-emnlp.1257.md) | core | Financial Evaluation / 金融评测 | Financial Model and Agent Safety / 金融模型及智能体安全; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Reliability, Safety and Fairness Evaluation / 可靠性、安全与公平性评测 | Language Models & LLM / 语言模型与LLM; Uncertainty & Robustness / 不确定性与鲁棒性 | [PDF](../../pdfs/EMNLP/2026/2026.findings-emnlp.1257.pdf) |
| 2026 | EMNLP | [FinGuard: Detecting Financial Regulatory Non-Compliance in LLM Interactions](../finance_notes/2026.findings-emnlp.629.md) | core | Financial Safety / 金融安全 | Privacy and Sensitive Information Protection / 隐私与敏感信息保护; Financial Model and Agent Safety / 金融模型及智能体安全; Regulatory Compliance and Violation Detection / 监管合规与违规检测 | Language Models & LLM / 语言模型与LLM; Reinforcement Learning / 强化学习 | [PDF](../../pdfs/EMNLP/2026/2026.findings-emnlp.629.pdf) |
| 2026 | EMNLP | [FinRT: Distilling Adaptive Red-Teaming Strategies into Reusable Adversarial Generators in Consumer Finance](../finance_notes/2026.findings-emnlp.2145.md) | core | Financial Safety / 金融安全 | Privacy and Sensitive Information Protection / 隐私与敏感信息保护; Financial Model and Agent Safety / 金融模型及智能体安全 | Language Models & LLM / 语言模型与LLM; Uncertainty & Robustness / 不确定性与鲁棒性 | [PDF](../../pdfs/EMNLP/2026/2026.findings-emnlp.2145.pdf) |
| 2026 | EMNLP | [K-FinHallu: A Hallucination Detection Benchmark for Multi-Turn RAG in Korean Finance](../finance_notes/2026.findings-emnlp.2053.md) | core | Financial Evaluation / 金融评测 | Financial Semantic Matching and Ranking / 金融语义匹配与排序; Evidence Retrieval and Reranking for Financial RAG / 金融 RAG 的证据检索与重排序; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Reliability, Safety and Fairness Evaluation / 可靠性、安全与公平性评测 | Language Models & LLM / 语言模型与LLM; Retrieval & RAG / 检索与RAG | [PDF](../../pdfs/EMNLP/2026/2026.findings-emnlp.2053.pdf) |
| 2026 | EMNLP | [Right Frame, Wrong Rule: Cultural Cues Expose the Financial Knowledge Gap They Were Meant to Close](../finance_notes/2026.findings-emnlp.2110.md) | core | Financial Safety / 金融安全 | Financial Model and Agent Safety / 金融模型及智能体安全 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/EMNLP/2026/2026.findings-emnlp.2110.pdf) |
| 2026 | EMNLP | [SCAMBENCH: A Multi-Dimensional Scam Benchmark through Human-AI Collaborative Data Construction](../finance_notes/2026.findings-emnlp.404.md) | core | Financial Evaluation / 金融评测 | Payment, Transaction and Insurance Fraud / 支付、交易及保险欺诈; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Reliability, Safety and Fairness Evaluation / 可靠性、安全与公平性评测 | Language Models & LLM / 语言模型与LLM; Uncertainty & Robustness / 不确定性与鲁棒性 | [PDF](../../pdfs/EMNLP/2026/2026.findings-emnlp.404.pdf) |
| 2026 | EMNLP | [Vishing-Tactics-Bench: Forecasting Exploitation Trajectories in Voice Phishing Calls](../finance_notes/2026.findings-emnlp.2347.md) | core | Financial Evaluation / 金融评测 | Payment, Transaction and Insurance Fraud / 支付、交易及保险欺诈; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Financial Network and Smart Contract Attacks / 金融网络及智能合约攻击 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/EMNLP/2026/2026.findings-emnlp.2347.pdf) |
| 2025 | ACL | [Fraud-R1 : A Multi-Round Benchmark for Assessing the Robustness of LLM Against Augmented Fraud and Phishing Inducements](../finance_notes/2025.findings-acl.226.md) | core | Financial Evaluation / 金融评测 | Payment, Transaction and Insurance Fraud / 支付、交易及保险欺诈; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Reliability, Safety and Fairness Evaluation / 可靠性、安全与公平性评测; Financial Model and Agent Safety / 金融模型及智能体安全 | Language Models & LLM / 语言模型与LLM; Uncertainty & Robustness / 不确定性与鲁棒性 | [PDF](../../pdfs/ACL/2025/2025.findings-acl.226.pdf) |
| 2025 | EMNLP | [Accept or Deny? Evaluating LLM Fairness and Performance in Loan Approval across Table-to-Text Serialization Approaches](../finance_notes/2025.findings-emnlp.947.md) | core | Financial Evaluation / 金融评测 | Credit Risk and Default Prediction / 信用风险与违约预测; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Financial Understanding and Multimodal Evaluation / 金融理解及多模态评测; Reliability, Safety and Fairness Evaluation / 可靠性、安全与公平性评测; Evaluation Protocols and Metrics / 评测协议与指标; Financial Model and Agent Safety / 金融模型及智能体安全 | Language Models & LLM / 语言模型与LLM; Fairness & Recourse / 公平性与算法追索; Tabular Learning / 表格学习 | [PDF](../../pdfs/EMNLP/2025/2025.findings-emnlp.947.pdf) |
| 2025 | EMNLP | [Detecting Continuously Evolving Scam Calls under Limited Annotation: A LLM-Augmented Expert Rule Framework](../finance_notes/2025.findings-emnlp.270.md) | core | Financial Safety / 金融安全 | Payment, Transaction and Insurance Fraud / 支付、交易及保险欺诈 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/EMNLP/2025/2025.findings-emnlp.270.pdf) |
| 2025 | EMNLP | [PsyScam: A Benchmark for Psychological Techniques in Real-World Scams](../finance_notes/2025.findings-emnlp.675.md) | core | Financial Evaluation / 金融评测 | Payment, Transaction and Insurance Fraud / 支付、交易及保险欺诈; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Reliability, Safety and Fairness Evaluation / 可靠性、安全与公平性评测 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/EMNLP/2025/2025.findings-emnlp.675.pdf) |
| 2020 | EMNLP | [Inferring about fraudulent collusion risk on Brazilian public works contracts in official texts using a Bi-LSTM approach](../finance_notes/2020.findings-emnlp.143.md) | core | Financial Safety / 金融安全 | Payment, Transaction and Insurance Fraud / 支付、交易及保险欺诈 |  | [PDF](../../pdfs/EMNLP/2020/2020.findings-emnlp.143.pdf) |
