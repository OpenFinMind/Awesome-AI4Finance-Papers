## Research summary / 研究总结

**Financial Safety / 金融安全 · Findings / Core**

2026-11-20 · 19 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 关注恶意行为、违规、隐私泄露和攻击造成的损害。欺诈与正常信用违约需要分开；一般公平性或反事实解释若服务于信用评分，主方向仍是金融风险。

**当前收录与方法。** 本页仅总结 Findings / core 中的论文。当前较常见的子分类：Financial Model and Agent Safety / 金融模型及智能体安全 (12); Payment, Transaction and Insurance Fraud / 支付、交易及保险欺诈 (7); Privacy and Sensitive Information Protection / 隐私与敏感信息保护 (4); Regulatory Compliance and Violation Detection / 监管合规与违规检测 (1); Financial Network and Smart Contract Attacks / 金融网络及智能合约攻击 (1)。已标注的方法：Language Models & LLM / 语言模型与LLM (17); Uncertainty & Robustness / 不确定性与鲁棒性 (9); Fairness & Recourse / 公平性与算法追索 (2); Tabular Learning / 表格学习 (1); Representation Learning / 表征学习 (1)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 重视类别不平衡、误报成本、攻击适应性、隐私与合规证据。 代表论文的摘要、金融关联证据及原文链接见 [1](../indexes/finance_notes/2026.findings-emnlp.629.md) · [2](../indexes/finance_notes/2025.findings-emnlp.270.md) · [3](../indexes/finance_notes/2020.findings-emnlp.143.md) · [4](../indexes/finance_notes/2026.findings-acl.1481.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 加强误报成本、攻击适应性、延迟标签和真实业务分布检验，明确隐私与安全保障的假设。

### English

**Problem and subdirections.** This task concerns malicious behavior, violations, privacy leakage and attacks. Fraud differs from ordinary credit default; fairness or recourse for credit scoring keeps financial risk as its primary task.

**Current coverage and methods.** This page covers only Findings / core. Frequent subcategories: Financial Model and Agent Safety / 金融模型及智能体安全 (12); Payment, Transaction and Insurance Fraud / 支付、交易及保险欺诈 (7); Privacy and Sensitive Information Protection / 隐私与敏感信息保护 (4); Regulatory Compliance and Violation Detection / 监管合规与违规检测 (1); Financial Network and Smart Contract Attacks / 金融网络及智能合约攻击 (1). Recorded methods: Language Models & LLM / 语言模型与LLM (17); Uncertainty & Robustness / 不确定性与鲁棒性 (9); Fairness & Recourse / 公平性与算法追索 (2); Tabular Learning / 表格学习 (1); Representation Learning / 表征学习 (1). Counts overlap and are not performance rankings.

**Data and evaluation.** Account for imbalance, false-positive costs, adaptive attacks, privacy and compliance evidence. Representative abstracts, financial evidence and original sources are linked at [1](../indexes/finance_notes/2026.findings-emnlp.629.md) · [2](../indexes/finance_notes/2025.findings-emnlp.270.md) · [3](../indexes/finance_notes/2020.findings-emnlp.143.md) · [4](../indexes/finance_notes/2026.findings-acl.1481.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Evaluate false-positive costs, adaptive attacks, delayed labels and operational distributions, with explicit assumptions behind privacy and safety guarantees.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. FinGuard: Detecting Financial Regulatory Non-Compliance in LLM Interactions](../indexes/finance_notes/2026.findings-emnlp.629.md) · EMNLP 2026 | 规则驱动的查询及回复风险检测模型<br>Rule-grounded query/response risk detection | 规则版本与辖域决定适用范围<br>Rule versions and jurisdictions determine scope |
| [2. Detecting Continuously Evolving Scam Calls under Limited Annotation: A LLM-Augmented Expert Rule Framework](../indexes/finance_notes/2025.findings-emnlp.270.md) · EMNLP 2025 | 专家规则和反思支持少标注的演化诈骗检测<br>Expert rules and reflection support evolving-scam detection with few labels | 规则可更新性与跨场景实测需区分<br>Rule adaptability differs from demonstrated cross-setting transfer |
| [3. Inferring about fraudulent collusion risk on Brazilian public works contracts in official texts using a Bi-LSTM approach](../indexes/finance_notes/2020.findings-emnlp.143.md) · EMNLP 2020 | 从巴西官方采购文本预测串标风险<br>Predict collusion risk from Brazilian procurement text | 风险标签不等于司法确认欺诈<br>Risk labels differ from legally established fraud |
| [4. Are Large Language Models Reliable Reviewers? A Benchmark for Error Detection in Financial Documents](../indexes/finance_notes/2026.findings-acl.1481.md) · ACL 2026 | 分复杂度测试财务文档错误识别<br>Test financial-document errors at different complexities | 文档新颖性依赖被测模型的截止时间<br>Document novelty depends on the evaluated model cutoff |
