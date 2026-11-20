## Research summary / 研究总结

**Financial Risk / 金融风险 · Main / Core**

2026-11-20 · 18 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 研究潜在损失、违约及风险传播。信用解释与反事实补救仍属于信用风险任务；存在故意欺诈或攻击时才转向金融安全。市场、流动性和系统性风险应分别定义事件与损失。

**当前收录与方法。** 本页仅总结 Main / core 中的论文。当前较常见的子分类：Market Risk and Tail Losses / 市场风险与尾部损失 (10); Credit Risk and Default Prediction / 信用风险与违约预测 (9)。已标注的方法：Uncertainty & Robustness / 不确定性与鲁棒性 (4); Graph Learning / 图学习 (3); Language Models & LLM / 语言模型与LLM (3); Multimodal Learning / 多模态学习 (2); Optimization & Numerical Methods / 优化与数值方法 (2)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 关注违约与尾部事件、概率校准、成本敏感性、压力测试及跨期稳定性。 代表论文的摘要、金融关联证据及原文链接见 [1](../indexes/finance_notes/aaai-2025-33433.md) · [2](../indexes/finance_notes/kdd-2023-84d05f0f7e27.md) · [3](../indexes/finance_notes/aaai-2021-16094.md) · [4](../indexes/finance_notes/2021.acl-long.526.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 加强尾部事件、跨机构与跨期检验，把概率校准、拒贷成本和压力情景纳入统一决策评价。

### English

**Problem and subdirections.** This task concerns potential losses, default and risk propagation. Credit explanations and recourse remain credit-risk tasks; deliberate fraud or attacks belong to financial safety. Market, liquidity and systemic risks require distinct events and loss definitions.

**Current coverage and methods.** This page covers only Main / core. Frequent subcategories: Market Risk and Tail Losses / 市场风险与尾部损失 (10); Credit Risk and Default Prediction / 信用风险与违约预测 (9). Recorded methods: Uncertainty & Robustness / 不确定性与鲁棒性 (4); Graph Learning / 图学习 (3); Language Models & LLM / 语言模型与LLM (3); Multimodal Learning / 多模态学习 (2); Optimization & Numerical Methods / 优化与数值方法 (2). Counts overlap and are not performance rankings.

**Data and evaluation.** Evaluate default and tail events, calibration, cost sensitivity, stress tests and temporal stability. Representative abstracts, financial evidence and original sources are linked at [1](../indexes/finance_notes/aaai-2025-33433.md) · [2](../indexes/finance_notes/kdd-2023-84d05f0f7e27.md) · [3](../indexes/finance_notes/aaai-2021-16094.md) · [4](../indexes/finance_notes/2021.acl-long.526.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Strengthen tail-event, cross-institution and temporal evaluation, integrating calibration, lending costs and stress scenarios into decision assessment.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. Dynamic Graph Learning with Static Relations for Credit Risk Assessment](../indexes/finance_notes/aaai-2025-33433.md) · AAAI 2025 | 静态转账增强动态交易图风险表征<br>Static transfers enrich dynamic transaction risk representations | 工业数据结果不直接代表公开基准<br>Industrial-data results do not directly transfer to public benchmarks |
| [2. Financial Default Prediction via Motif-preserving Graph Neural Network with Curriculum Learning](../indexes/finance_notes/kdd-2023-84d05f0f7e27.md) · KDD 2023 | 模体图与课程学习处理高阶违约结构<br>Motif graphs and curricula model higher-order default structure | 业务关系可用性影响迁移<br>Transfer depends on available business relationships |
| [3. The Causal Learning of Retail Delinquency](../indexes/finance_notes/aaai-2021-16094.md) · AAAI 2021 | 估计授信改变对还款的因果影响<br>Estimate repayment effects of changes in lending decisions | 识别依赖观测数据及混杂假设<br>Identification depends on data and confounding assumptions |
| [4. Multimodal Multi-Speaker Merger & Acquisition Financial Modeling: A New Task, Dataset, and Neural Baselines](../indexes/finance_notes/2021.acl-long.526.md) · ACL 2021 | 并购电话会议的多模态风险建模<br>Multimodal risk modeling from M&A calls | 原文报告相对强基线的提升有限<br>The paper reports limited gains over strong baselines |
