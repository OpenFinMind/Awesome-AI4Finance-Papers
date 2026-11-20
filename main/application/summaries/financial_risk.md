## Research summary / 研究总结

**Financial Risk / 金融风险 · Main / Application**

2026-11-20 · 251 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 研究潜在损失、违约及风险传播。信用解释与反事实补救仍属于信用风险任务；存在故意欺诈或攻击时才转向金融安全。市场、流动性和系统性风险应分别定义事件与损失。

**当前收录与方法。** 本页仅总结 Main / application 中的论文。当前较常见的子分类：Credit Risk and Default Prediction / 信用风险与违约预测 (242); Market Risk and Tail Losses / 市场风险与尾部损失 (20); Systemic Risk and Financial Stability / 系统性风险与金融稳定 (1)。已标注的方法：Fairness & Recourse / 公平性与算法追索 (114); Uncertainty & Robustness / 不确定性与鲁棒性 (72); Tabular Learning / 表格学习 (65); Optimization & Numerical Methods / 优化与数值方法 (57); Language Models & LLM / 语言模型与LLM (41)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 关注违约与尾部事件、概率校准、成本敏感性、压力测试及跨期稳定性。 代表论文的摘要、金融关联证据及原文链接见 [1](../indexes/finance_notes/kdd-2024-9859013a6cee.md) · [2](../indexes/finance_notes/neurips-2017-8820.md) · [3](../indexes/finance_notes/aaai-2026-39414.md) · [4](../indexes/finance_notes/2026.acl-long.151.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 加强尾部事件、跨机构与跨期检验，把概率校准、拒贷成本和压力情景纳入统一决策评价。

### English

**Problem and subdirections.** This task concerns potential losses, default and risk propagation. Credit explanations and recourse remain credit-risk tasks; deliberate fraud or attacks belong to financial safety. Market, liquidity and systemic risks require distinct events and loss definitions.

**Current coverage and methods.** This page covers only Main / application. Frequent subcategories: Credit Risk and Default Prediction / 信用风险与违约预测 (242); Market Risk and Tail Losses / 市场风险与尾部损失 (20); Systemic Risk and Financial Stability / 系统性风险与金融稳定 (1). Recorded methods: Fairness & Recourse / 公平性与算法追索 (114); Uncertainty & Robustness / 不确定性与鲁棒性 (72); Tabular Learning / 表格学习 (65); Optimization & Numerical Methods / 优化与数值方法 (57); Language Models & LLM / 语言模型与LLM (41). Counts overlap and are not performance rankings.

**Data and evaluation.** Evaluate default and tail events, calibration, cost sensitivity, stress tests and temporal stability. Representative abstracts, financial evidence and original sources are linked at [1](../indexes/finance_notes/kdd-2024-9859013a6cee.md) · [2](../indexes/finance_notes/neurips-2017-8820.md) · [3](../indexes/finance_notes/aaai-2026-39414.md) · [4](../indexes/finance_notes/2026.acl-long.151.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Strengthen tail-event, cross-institution and temporal evaluation, integrating calibration, lending costs and stress scenarios into decision assessment.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. Team up GBDTs and DNNs: Advancing Efficient and Effective Tabular Prediction with Tree-hybrid MLPs](../indexes/finance_notes/kdd-2024-9859013a6cee.md) · KDD 2024 | 树结构与 MLP 结合改善表格预测效率<br>Tree structure and MLPs improve tabular prediction efficiency | 包含收入数据不代表金融专用设计<br>Income-data experiments do not imply finance-specific design |
| [2. From Parity to Preference-based Notions of Fairness in Classification](../indexes/finance_notes/neurips-2017-8820.md) · NeurIPS 2017 | 用偏好公平替代单纯群体平等约束<br>Preference-based fairness complements parity constraints | 公平定义改变会改变可比较的目标<br>Changing fairness definitions changes the objective |
| [3. GLANCE: Global Actions in a Nutshell for Counterfactual Explainability](../indexes/finance_notes/aaai-2026-39414.md) · AAAI 2026 | 研究主题：GLANCE: Global Actions in a Nutshell for Counterfactual Explainability<br>Research topic: GLANCE: Global Actions in a Nutshell for Counterfactual Explainability | 按原文的任务、数据和实验设置解释结果。<br>Interpret results within the original task, data and experimental setting. |
| [4. KG-MuLQA: A Framework for KG-based Multi-Level QA Extraction and Long-Context LLM Evaluation](../indexes/finance_notes/2026.acl-long.151.md) · ACL 2026 | 研究主题：KG-MuLQA: A Framework for KG-based Multi-Level QA Extraction and Long-Context LLM Evaluation<br>Research topic: KG-MuLQA: A Framework for KG-based Multi-Level QA Extraction and Long-Context LLM Evaluation | 按原文的任务、数据和实验设置解释结果。<br>Interpret results within the original task, data and experimental setting. |
