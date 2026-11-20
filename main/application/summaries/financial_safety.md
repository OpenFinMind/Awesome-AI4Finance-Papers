## Research summary / 研究总结

**Financial Safety / 金融安全 · Main / Application**

2026-11-20 · 162 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 关注恶意行为、违规、隐私泄露和攻击造成的损害。欺诈与正常信用违约需要分开；一般公平性或反事实解释若服务于信用评分，主方向仍是金融风险。

**当前收录与方法。** 本页仅总结 Main / application 中的论文。当前较常见的子分类：Financial Model and Agent Safety / 金融模型及智能体安全 (58); Payment, Transaction and Insurance Fraud / 支付、交易及保险欺诈 (55); Privacy and Sensitive Information Protection / 隐私与敏感信息保护 (48); Financial Network and Smart Contract Attacks / 金融网络及智能合约攻击 (8); Regulatory Compliance and Violation Detection / 监管合规与违规检测 (6)。已标注的方法：Language Models & LLM / 语言模型与LLM (55); Fairness & Recourse / 公平性与算法追索 (46); Uncertainty & Robustness / 不确定性与鲁棒性 (43); Optimization & Numerical Methods / 优化与数值方法 (22); Generative Modeling / 生成建模 (21)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 重视类别不平衡、误报成本、攻击适应性、隐私与合规证据。 代表论文的摘要、金融关联证据及原文链接见 [1](../indexes/finance_notes/iclr-2023-x-mXzBgCX3a.md) · [2](../indexes/finance_notes/kdd-2020-226b55e1393a.md) · [3](../indexes/finance_notes/aaai-2026-40456.md) · [4](../indexes/finance_notes/2026.acl-long.1625.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 加强误报成本、攻击适应性、延迟标签和真实业务分布检验，明确隐私与安全保障的假设。

### English

**Problem and subdirections.** This task concerns malicious behavior, violations, privacy leakage and attacks. Fraud differs from ordinary credit default; fairness or recourse for credit scoring keeps financial risk as its primary task.

**Current coverage and methods.** This page covers only Main / application. Frequent subcategories: Financial Model and Agent Safety / 金融模型及智能体安全 (58); Payment, Transaction and Insurance Fraud / 支付、交易及保险欺诈 (55); Privacy and Sensitive Information Protection / 隐私与敏感信息保护 (48); Financial Network and Smart Contract Attacks / 金融网络及智能合约攻击 (8); Regulatory Compliance and Violation Detection / 监管合规与违规检测 (6). Recorded methods: Language Models & LLM / 语言模型与LLM (55); Fairness & Recourse / 公平性与算法追索 (46); Uncertainty & Robustness / 不确定性与鲁棒性 (43); Optimization & Numerical Methods / 优化与数值方法 (22); Generative Modeling / 生成建模 (21). Counts overlap and are not performance rankings.

**Data and evaluation.** Account for imbalance, false-positive costs, adaptive attacks, privacy and compliance evidence. Representative abstracts, financial evidence and original sources are linked at [1](../indexes/finance_notes/iclr-2023-x-mXzBgCX3a.md) · [2](../indexes/finance_notes/kdd-2020-226b55e1393a.md) · [3](../indexes/finance_notes/aaai-2026-40456.md) · [4](../indexes/finance_notes/2026.acl-long.1625.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Evaluate false-positive costs, adaptive attacks, delayed labels and operational distributions, with explicit assumptions behind privacy and safety guarantees.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. FairGBM: Gradient Boosting with Fairness Constraints](../indexes/finance_notes/iclr-2023-x-mXzBgCX3a.md) · ICLR 2023 | 支持公平约束的梯度提升树训练<br>Gradient-boosted trees trained with fairness constraints | 公平标准及数据人口决定解释范围<br>Fairness criteria and population determine interpretation |
| [2. Algorithmic Decision Making with Conditional Fairness](../indexes/finance_notes/kdd-2020-226b55e1393a.md) · KDD 2020 | 在条件变量下定义并优化公平约束<br>Define and optimize fairness conditional on chosen covariates | 选择哪些变量公平本身是建模假设<br>The choice of fair covariates is itself an assumption |
| [3. Query-Efficient Domain Knowledge Stealing Against Large Language Models](../indexes/finance_notes/aaai-2026-40456.md) · AAAI 2026 | 研究主题：Query-Efficient Domain Knowledge Stealing Against Large Language Models<br>Research topic: Query-Efficient Domain Knowledge Stealing Against Large Language Models | 按原文的任务、数据和实验设置解释结果。<br>Interpret results within the original task, data and experimental setting. |
| [4. Business as Rulesual: A Benchmark and Framework for Business Rule Flow Modeling with LLMs](../indexes/finance_notes/2026.acl-long.1625.md) · ACL 2026 | 研究主题：Business as Rulesual: A Benchmark and Framework for Business Rule Flow Modeling with LLMs<br>Research topic: Business as Rulesual: A Benchmark and Framework for Business Rule Flow Modeling with LLMs | 按原文的任务、数据和实验设置解释结果。<br>Interpret results within the original task, data and experimental setting. |
