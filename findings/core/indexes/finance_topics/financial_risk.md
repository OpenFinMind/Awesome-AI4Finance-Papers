# Financial Risk / 金融风险

Credit scoring, default, market, liquidity and systemic risk; fraud and attacks belong to financial safety. / 信用评分、违约、市场风险、流动性及系统性风险；欺诈与攻击归金融安全。

2 Findings long papers. Topic memberships can overlap.

[All topics](../ai_for_finance.md) · [Classification definitions](../finance_taxonomy.md) · [CSV](financial_risk.csv) · [Excel](../../finance_catalog.xlsx)

<!-- task-summary:start -->

## Research summary / 研究总结

**Financial Risk / 金融风险 · Findings / Core**

2026-11-20 · 2 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 研究潜在损失、违约及风险传播。信用解释与反事实补救仍属于信用风险任务；存在故意欺诈或攻击时才转向金融安全。市场、流动性和系统性风险应分别定义事件与损失。

**当前收录与方法。** 本页仅总结 Findings / core 中的论文。当前较常见的子分类：Credit Risk and Default Prediction / 信用风险与违约预测 (1)。已标注的方法：Fairness & Recourse / 公平性与算法追索 (2); Language Models & LLM / 语言模型与LLM (1); Tabular Learning / 表格学习 (1); Representation Learning / 表征学习 (1)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 关注违约与尾部事件、概率校准、成本敏感性、压力测试及跨期稳定性。 代表论文的摘要、金融关联证据及原文链接见 [1](../finance_notes/2025.findings-emnlp.947.md) · [2](../finance_notes/2026.findings-acl.2118.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 加强尾部事件、跨机构与跨期检验，把概率校准、拒贷成本和压力情景纳入统一决策评价。

### English

**Problem and subdirections.** This task concerns potential losses, default and risk propagation. Credit explanations and recourse remain credit-risk tasks; deliberate fraud or attacks belong to financial safety. Market, liquidity and systemic risks require distinct events and loss definitions.

**Current coverage and methods.** This page covers only Findings / core. Frequent subcategories: Credit Risk and Default Prediction / 信用风险与违约预测 (1). Recorded methods: Fairness & Recourse / 公平性与算法追索 (2); Language Models & LLM / 语言模型与LLM (1); Tabular Learning / 表格学习 (1); Representation Learning / 表征学习 (1). Counts overlap and are not performance rankings.

**Data and evaluation.** Evaluate default and tail events, calibration, cost sensitivity, stress tests and temporal stability. Representative abstracts, financial evidence and original sources are linked at [1](../finance_notes/2025.findings-emnlp.947.md) · [2](../finance_notes/2026.findings-acl.2118.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Strengthen tail-event, cross-institution and temporal evaluation, integrating calibration, lending costs and stress scenarios into decision assessment.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. Accept or Deny? Evaluating LLM Fairness and Performance in Loan Approval across Table-to-Text Serialization Approaches](../finance_notes/2025.findings-emnlp.947.md) · EMNLP 2025 | 比较贷款表格序列化的预测与公平影响<br>Compare predictive and fairness effects of loan-data serialization | 不同地区及格式可能改变公平—准确权衡<br>Regions and formats may change accuracy–fairness tradeoffs |
| [2. Uncovering Currency Bias and Syntax Gap in Text Embedding Models](../finance_notes/2026.findings-acl.2118.md) · ACL 2026 | 研究主题：Uncovering Currency Bias and Syntax Gap in Text Embedding Models<br>Research topic: Uncovering Currency Bias and Syntax Gap in Text Embedding Models | 按原文的任务、数据和实验设置解释结果。<br>Interpret results within the original task, data and experimental setting. |

<!-- task-summary:end -->

## Subtopic statistics / 子方向统计

| Subtopic | Papers |
|---|---:|
| Credit Risk and Default Prediction / 信用风险与违约预测 | 1 |
| Market Risk and Tail Losses / 市场风险与尾部损失 | 0 |
| Liquidity and Funding Risk / 流动性与融资风险 | 0 |
| Counterparty and Contagion Risk / 交易对手与传染风险 | 0 |
| Systemic Risk and Financial Stability / 系统性风险与金融稳定 | 0 |
| Stress Testing and Scenario Analysis / 压力测试与情景分析 | 0 |
| Operational Risk and Loss Prediction / 操作风险与损失预测 | 0 |

## Full paper list / 完整论文列表

| Year | Venue | Paper | Scope | Primary topic | Subtopics | Methods | Resources |
|---|---|---|---|---|---|---|---|
| 2026 | ACL | [Uncovering Currency Bias and Syntax Gap in Text Embedding Models](../finance_notes/2026.findings-acl.2118.md) | core | Financial Evaluation / 金融评测 | Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Reliability, Safety and Fairness Evaluation / 可靠性、安全与公平性评测; Financial Semantic Matching and Ranking / 金融语义匹配与排序; Financial Model and Agent Safety / 金融模型及智能体安全 | Fairness & Recourse / 公平性与算法追索; Representation Learning / 表征学习 | [PDF](../../pdfs/ACL/2026/2026.findings-acl.2118.pdf) |
| 2025 | EMNLP | [Accept or Deny? Evaluating LLM Fairness and Performance in Loan Approval across Table-to-Text Serialization Approaches](../finance_notes/2025.findings-emnlp.947.md) | core | Financial Evaluation / 金融评测 | Credit Risk and Default Prediction / 信用风险与违约预测; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Financial Understanding and Multimodal Evaluation / 金融理解及多模态评测; Reliability, Safety and Fairness Evaluation / 可靠性、安全与公平性评测; Evaluation Protocols and Metrics / 评测协议与指标; Financial Model and Agent Safety / 金融模型及智能体安全 | Language Models & LLM / 语言模型与LLM; Fairness & Recourse / 公平性与算法追索; Tabular Learning / 表格学习 | [PDF](../../pdfs/EMNLP/2025/2025.findings-emnlp.947.pdf) |
