## Research summary / 研究总结

**Financial Safety / 金融安全 · Main / Core**

2026-11-20 · 41 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 关注恶意行为、违规、隐私泄露和攻击造成的损害。欺诈与正常信用违约需要分开；一般公平性或反事实解释若服务于信用评分，主方向仍是金融风险。

**当前收录与方法。** 本页仅总结 Main / core 中的论文。当前较常见的子分类：Payment, Transaction and Insurance Fraud / 支付、交易及保险欺诈 (23); Financial Model and Agent Safety / 金融模型及智能体安全 (10); Privacy and Sensitive Information Protection / 隐私与敏感信息保护 (8); AML and Illicit Fund Tracing / 反洗钱与非法资金追踪 (4); Regulatory Compliance and Violation Detection / 监管合规与违规检测 (4)。已标注的方法：Language Models & LLM / 语言模型与LLM (22); Representation Learning / 表征学习 (9); Graph Learning / 图学习 (8); Retrieval & RAG / 检索与RAG (6); Transformer / Transformer模型 (5)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 重视类别不平衡、误报成本、攻击适应性、隐私与合规证据。 代表论文的摘要、金融关联证据及原文链接见 [1](../indexes/finance_notes/aaai-2026-38499.md) · [2](../indexes/finance_notes/2026.acl-long.1903.md) · [3](../indexes/finance_notes/2026.acl-long.1071.md) · [4](../indexes/finance_notes/kdd-2024-6d7b4399644b.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 加强误报成本、攻击适应性、延迟标签和真实业务分布检验，明确隐私与安全保障的假设。

### English

**Problem and subdirections.** This task concerns malicious behavior, violations, privacy leakage and attacks. Fraud differs from ordinary credit default; fairness or recourse for credit scoring keeps financial risk as its primary task.

**Current coverage and methods.** This page covers only Main / core. Frequent subcategories: Payment, Transaction and Insurance Fraud / 支付、交易及保险欺诈 (23); Financial Model and Agent Safety / 金融模型及智能体安全 (10); Privacy and Sensitive Information Protection / 隐私与敏感信息保护 (8); AML and Illicit Fund Tracing / 反洗钱与非法资金追踪 (4); Regulatory Compliance and Violation Detection / 监管合规与违规检测 (4). Recorded methods: Language Models & LLM / 语言模型与LLM (22); Representation Learning / 表征学习 (9); Graph Learning / 图学习 (8); Retrieval & RAG / 检索与RAG (6); Transformer / Transformer模型 (5). Counts overlap and are not performance rankings.

**Data and evaluation.** Account for imbalance, false-positive costs, adaptive attacks, privacy and compliance evidence. Representative abstracts, financial evidence and original sources are linked at [1](../indexes/finance_notes/aaai-2026-38499.md) · [2](../indexes/finance_notes/2026.acl-long.1903.md) · [3](../indexes/finance_notes/2026.acl-long.1071.md) · [4](../indexes/finance_notes/kdd-2024-6d7b4399644b.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Evaluate false-positive costs, adaptive attacks, delayed labels and operational distributions, with explicit assumptions behind privacy and safety guarantees.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. Beyond Single Transactions: D-EMAML---Dual-Edge Motif Neural Networks for Enhanced Anti-Money Laundering Detection](../indexes/finance_notes/aaai-2026-38499.md) · AAAI 2026 | 双边模体建模交易链路的边异常<br>Dual-edge motifs model transaction-edge anomalies | 节点与边预测的结果口径不同<br>Node and edge prediction use different evaluation units |
| [2. Learning to Conceal Risk: Controllable Multi-turn Red Teaming for LLMs in the Financial Domain](../indexes/finance_notes/2026.acl-long.1903.md) · ACL 2026 | 评价隐藏风险的多轮金融红队交互<br>Evaluate financial safeguards under concealed-risk multi-turn interactions | 攻击成功率取决于任务和判分口径<br>Attack success depends on task and grading definitions |
| [3. Understanding Structured Financial Data with LLMs: A Case Study on Fraud Detection](../indexes/finance_notes/2026.acl-long.1071.md) · ACL 2026 | 特征压缩加检索增强表格欺诈判断<br>Feature reduction and retrieval support tabular fraud detection | 可解释辅助价值与专用分类性能分开<br>Separate assistive explanations from specialist classification quality |
| [4. Cost-Efficient Fraud Risk Optimization with Submodularity in Insurance Claim](../indexes/finance_notes/kdd-2024-6d7b4399644b.md) · KDD 2024 | 用次模优化平衡调查信息成本与风险识别<br>Submodular optimization balances investigation cost and fraud risk | 预算与信息来源决定业务适用性<br>Budgets and information sources determine applicability |
