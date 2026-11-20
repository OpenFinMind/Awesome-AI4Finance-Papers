# Financial Services / 金融服务

Banking, payments, customer service, marketing and personal/business financial services. / 银行、支付、客户服务、营销及个人与企业金融服务。

3 Findings long papers. Topic memberships can overlap.

[All topics](../ai_for_finance.md) · [Classification definitions](../finance_taxonomy.md) · [CSV](financial_services.csv) · [Excel](../../finance_catalog.xlsx)

<!-- task-summary:start -->

## Research summary / 研究总结

**Financial Services / 金融服务 · Findings / Core**

2026-11-20 · 3 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 关注客户交互、产品匹配、个人财务服务及银行支付流程。服务质量、业务效率与金融结果需要分别评价；违约预测和欺诈检测按风险或安全任务归类。

**当前收录与方法。** 本页仅总结 Findings / core 中的论文。当前较常见的子分类：Lending, Payment and Banking Workflows / 贷款、支付及银行业务流程 (1); Personal Financial Planning and Services / 个人财务规划与服务 (1); Customer Support and Business Consultation / 智能客服与业务咨询 (1)。已标注的方法：Language Models & LLM / 语言模型与LLM (3); Uncertainty & Robustness / 不确定性与鲁棒性 (2); Causal Learning / 因果学习 (1); Reinforcement Learning / 强化学习 (1)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 区分公开业务数据与真实部署，检查客户、时间和机构间迁移。 代表论文的摘要、金融关联证据及原文链接见 [1](../finance_notes/2026.findings-emnlp.1982.md) · [2](../finance_notes/2026.findings-emnlp.1170.md) · [3](../finance_notes/2026.findings-emnlp.1340.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 研究服务可及性、长期客户利益与跨机构迁移，区分公开数据实验和真实业务部署。

### English

**Problem and subdirections.** This task concerns customer interaction, product matching, personal finance and banking/payment workflows. Service quality, efficiency and financial outcomes require separate evaluation; default and fraud prediction belong to risk or safety.

**Current coverage and methods.** This page covers only Findings / core. Frequent subcategories: Lending, Payment and Banking Workflows / 贷款、支付及银行业务流程 (1); Personal Financial Planning and Services / 个人财务规划与服务 (1); Customer Support and Business Consultation / 智能客服与业务咨询 (1). Recorded methods: Language Models & LLM / 语言模型与LLM (3); Uncertainty & Robustness / 不确定性与鲁棒性 (2); Causal Learning / 因果学习 (1); Reinforcement Learning / 强化学习 (1). Counts overlap and are not performance rankings.

**Data and evaluation.** Distinguish public business data from deployment; check transfer across customers, time and institutions. Representative abstracts, financial evidence and original sources are linked at [1](../finance_notes/2026.findings-emnlp.1982.md) · [2](../finance_notes/2026.findings-emnlp.1170.md) · [3](../finance_notes/2026.findings-emnlp.1340.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Study access, long-term customer interests and transfer across institutions, distinguishing public-data experiments from deployment.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. PersuaRL: Reinforcement Learning-Driven Multi-Expert Selection for Persuasive Dialogue Generation in Insurance](../finance_notes/2026.findings-emnlp.1982.md) · EMNLP 2026 | 用 RL 选择多专家策略生成保险对话<br>RL selects expert strategies for insurance dialogue | 说服质量并不自动证明客户决策质量<br>Persuasion quality does not establish customer decision quality |
| [2. BenchCompass: From Scores to Signals for Training and Harness Decisions in Payment-Domain LLMs](../finance_notes/2026.findings-emnlp.1170.md) · EMNLP 2026 | 支付知识、规则使用和输入鲁棒性诊断<br>Diagnose payment knowledge, rule use and input robustness | 不同审查级别的数据池不能混用<br>Do not conflate pools with different review assurance |
| [3. FairFund-Bench: Evaluating Distributive Bias in LLM Resource Allocation](../finance_notes/2026.findings-emnlp.1340.md) · EMNLP 2026 | 研究主题：FairFund-Bench: Evaluating Distributive Bias in LLM Resource Allocation<br>Research topic: FairFund-Bench: Evaluating Distributive Bias in LLM Resource Allocation | 按原文的任务、数据和实验设置解释结果。<br>Interpret results within the original task, data and experimental setting. |

<!-- task-summary:end -->

## Subtopic statistics / 子方向统计

| Subtopic | Papers |
|---|---:|
| Customer Support and Business Consultation / 智能客服与业务咨询 | 1 |
| Financial Product Recommendation and Matching / 金融产品推荐与匹配 | 0 |
| Personal Financial Planning and Services / 个人财务规划与服务 | 1 |
| Lending, Payment and Banking Workflows / 贷款、支付及银行业务流程 | 1 |
| Customer Behavior and Relationship Management / 客户行为与关系管理 | 0 |
| Financial Access and Inclusion / 金融服务可及性与普惠金融 | 0 |

## Full paper list / 完整论文列表

| Year | Venue | Paper | Scope | Primary topic | Subtopics | Methods | Resources |
|---|---|---|---|---|---|---|---|
| 2026 | EMNLP | [BenchCompass: From Scores to Signals for Training and Harness Decisions in Payment-Domain LLMs](../finance_notes/2026.findings-emnlp.1170.md) | core | Financial Evaluation / 金融评测 | Lending, Payment and Banking Workflows / 贷款、支付及银行业务流程; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Financial Decision and Agent Evaluation / 金融决策与智能体评测 | Language Models & LLM / 语言模型与LLM; Uncertainty & Robustness / 不确定性与鲁棒性 | [PDF](../../pdfs/EMNLP/2026/2026.findings-emnlp.1170.pdf) |
| 2026 | EMNLP | [FairFund-Bench: Evaluating Distributive Bias in LLM Resource Allocation](../finance_notes/2026.findings-emnlp.1340.md) | core | Financial Evaluation / 金融评测 | Personal Financial Planning and Services / 个人财务规划与服务; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Reliability, Safety and Fairness Evaluation / 可靠性、安全与公平性评测; Evaluation Protocols and Metrics / 评测协议与指标 | Language Models & LLM / 语言模型与LLM; Causal Learning / 因果学习; Uncertainty & Robustness / 不确定性与鲁棒性 | [PDF](../../pdfs/EMNLP/2026/2026.findings-emnlp.1340.pdf) |
| 2026 | EMNLP | [PersuaRL: Reinforcement Learning-Driven Multi-Expert Selection for Persuasive Dialogue Generation in Insurance](../finance_notes/2026.findings-emnlp.1982.md) | core | Financial Services / 金融服务 | Customer Support and Business Consultation / 智能客服与业务咨询 | Language Models & LLM / 语言模型与LLM; Reinforcement Learning / 强化学习 | [PDF](../../pdfs/EMNLP/2026/2026.findings-emnlp.1982.pdf) |
