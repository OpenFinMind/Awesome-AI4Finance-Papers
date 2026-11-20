# Financial Services / 金融服务

Banking, payments, customer service, marketing and personal/business financial services. / 银行、支付、客户服务、营销及个人与企业金融服务。

10 Findings long papers. Topic memberships can overlap.

[All topics](../ai_for_finance.md) · [Classification definitions](../finance_taxonomy.md) · [CSV](financial_services.csv) · [Excel](../../finance_catalog.xlsx)

<!-- task-summary:start -->

## Research summary / 研究总结

**Financial Services / 金融服务 · Findings / Application**

2026-11-20 · 10 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 关注客户交互、产品匹配、个人财务服务及银行支付流程。服务质量、业务效率与金融结果需要分别评价；违约预测和欺诈检测按风险或安全任务归类。

**当前收录与方法。** 本页仅总结 Findings / application 中的论文。当前较常见的子分类：Customer Support and Business Consultation / 智能客服与业务咨询 (8); Lending, Payment and Banking Workflows / 贷款、支付及银行业务流程 (2)。已标注的方法：Language Models & LLM / 语言模型与LLM (6); Uncertainty & Robustness / 不确定性与鲁棒性 (2); Representation Learning / 表征学习 (2); Reinforcement Learning / 强化学习 (2); Optimization & Numerical Methods / 优化与数值方法 (1)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 区分公开业务数据与真实部署，检查客户、时间和机构间迁移。 代表论文的摘要、金融关联证据及原文链接见 [1](../finance_notes/2026.findings-acl.931.md) · [2](../finance_notes/2023.findings-acl.230.md) · [3](../finance_notes/2021.findings-acl.252.md) · [4](../finance_notes/2026.findings-emnlp.342.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 研究服务可及性、长期客户利益与跨机构迁移，区分公开数据实验和真实业务部署。

### English

**Problem and subdirections.** This task concerns customer interaction, product matching, personal finance and banking/payment workflows. Service quality, efficiency and financial outcomes require separate evaluation; default and fraud prediction belong to risk or safety.

**Current coverage and methods.** This page covers only Findings / application. Frequent subcategories: Customer Support and Business Consultation / 智能客服与业务咨询 (8); Lending, Payment and Banking Workflows / 贷款、支付及银行业务流程 (2). Recorded methods: Language Models & LLM / 语言模型与LLM (6); Uncertainty & Robustness / 不确定性与鲁棒性 (2); Representation Learning / 表征学习 (2); Reinforcement Learning / 强化学习 (2); Optimization & Numerical Methods / 优化与数值方法 (1). Counts overlap and are not performance rankings.

**Data and evaluation.** Distinguish public business data from deployment; check transfer across customers, time and institutions. Representative abstracts, financial evidence and original sources are linked at [1](../finance_notes/2026.findings-acl.931.md) · [2](../finance_notes/2023.findings-acl.230.md) · [3](../finance_notes/2021.findings-acl.252.md) · [4](../finance_notes/2026.findings-emnlp.342.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Study access, long-term customer interests and transfer across institutions, distinguishing public-data experiments from deployment.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. ToolDNA: Autonomous Evolution of Tool Metadata for Robust Dialogue Agents](../finance_notes/2026.findings-acl.931.md) · ACL 2026 | 通过 RL 协同改进策略及工具元数据<br>RL coevolves policies and tool metadata | 贷款计算案例不代表完整银行部署<br>Loan-calculation cases do not establish full banking deployment |
| [2. Multi3NLU++: A Multilingual, Multi-Intent, Multi-Domain Dataset for Natural Language Understanding in Task-Oriented Dialogue](../finance_notes/2023.findings-acl.230.md) · ACL 2023 | 银行及酒店的多语言多意图/槽位基准<br>Multilingual multi-intent/slot benchmarks for banking and hotels | 翻译语料的文化和对话覆盖有限<br>Translated corpora have bounded cultural/dialogue coverage |
| [3. Energy-based Unknown Intent Detection with Data Manipulation](../finance_notes/2021.findings-acl.252.md) · ACL 2021 | 能量分数与生成 OOD 样本识别未知意图<br>Energy scores and generated OOD examples identify unknown intents | 合成未知意图未必覆盖真实新需求<br>Synthetic OOD intents may not cover real new requests |
| [4. PIVOT: Perplexity-Informed KD-to-RL Transition Scheduling for Vertical-Domain Few-Shot Distillation](../finance_notes/2026.findings-emnlp.342.md) · EMNLP 2026 | 研究主题：PIVOT: Perplexity-Informed KD-to-RL Transition Scheduling for Vertical-Domain Few-Shot Distillation<br>Research topic: PIVOT: Perplexity-Informed KD-to-RL Transition Scheduling for Vertical-Domain Few-Shot Distillation | 按原文的任务、数据和实验设置解释结果。<br>Interpret results within the original task, data and experimental setting. |

<!-- task-summary:end -->

## Subtopic statistics / 子方向统计

| Subtopic | Papers |
|---|---:|
| Customer Support and Business Consultation / 智能客服与业务咨询 | 8 |
| Financial Product Recommendation and Matching / 金融产品推荐与匹配 | 0 |
| Personal Financial Planning and Services / 个人财务规划与服务 | 0 |
| Lending, Payment and Banking Workflows / 贷款、支付及银行业务流程 | 2 |
| Customer Behavior and Relationship Management / 客户行为与关系管理 | 0 |
| Financial Access and Inclusion / 金融服务可及性与普惠金融 | 0 |

## Full paper list / 完整论文列表

| Year | Venue | Paper | Scope | Primary topic | Subtopics | Methods | Resources |
|---|---|---|---|---|---|---|---|
| 2026 | ACL | [ToolDNA: Autonomous Evolution of Tool Metadata for Robust Dialogue Agents](../finance_notes/2026.findings-acl.931.md) | application | Financial Services / 金融服务 | Lending, Payment and Banking Workflows / 贷款、支付及银行业务流程; Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策 | Language Models & LLM / 语言模型与LLM; Reinforcement Learning / 强化学习; Uncertainty & Robustness / 不确定性与鲁棒性 | [PDF](../../pdfs/ACL/2026/2026.findings-acl.931.pdf) |
| 2026 | EMNLP | [PIVOT: Perplexity-Informed KD-to-RL Transition Scheduling for Vertical-Domain Few-Shot Distillation](../finance_notes/2026.findings-emnlp.342.md) | application | Financial Services / 金融服务 | Customer Support and Business Consultation / 智能客服与业务咨询 | Language Models & LLM / 语言模型与LLM; Reinforcement Learning / 强化学习; Optimization & Numerical Methods / 优化与数值方法 | [PDF](../../pdfs/EMNLP/2026/2026.findings-emnlp.342.pdf) |
| 2025 | EMNLP | [TS-SQL: Test-driven Self-refinement for Text-to-SQL](../finance_notes/2025.findings-emnlp.156.md) | application | Financial Services / 金融服务 | Lending, Payment and Banking Workflows / 贷款、支付及银行业务流程 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/EMNLP/2025/2025.findings-emnlp.156.pdf) |
| 2024 | ACL | [Mitigating Boundary Ambiguity and Inherent Bias for Text Classification in the Era of Large Language Models](../finance_notes/2024.findings-acl.467.md) | application | Financial Services / 金融服务 | Customer Support and Business Consultation / 智能客服与业务咨询 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/ACL/2024/2024.findings-acl.467.pdf) |
| 2024 | ACL | [SELP: A Semantically-Driven Approach for Separated and Accurate Class Prototypes in Few-Shot Text Classification](../finance_notes/2024.findings-acl.579.md) | application | Financial Services / 金融服务 | Customer Support and Business Consultation / 智能客服与业务咨询 |  | [PDF](../../pdfs/ACL/2024/2024.findings-acl.579.pdf) |
| 2024 | EMNLP | [Selection-p: Self-Supervised Task-Agnostic Prompt Compression for Faithfulness and Transferability](../finance_notes/2024.findings-emnlp.646.md) | application | Financial Services / 金融服务 | Customer Support and Business Consultation / 智能客服与业务咨询 | Language Models & LLM / 语言模型与LLM; Representation Learning / 表征学习 | [PDF](../../pdfs/EMNLP/2024/2024.findings-emnlp.646.pdf) |
| 2023 | ACL | [Multi3NLU++: A Multilingual, Multi-Intent, Multi-Domain Dataset for Natural Language Understanding in Task-Oriented Dialogue](../finance_notes/2023.findings-acl.230.md) | application | Financial Services / 金融服务 | Customer Support and Business Consultation / 智能客服与业务咨询 |  | [PDF](../../pdfs/ACL/2023/2023.findings-acl.230.pdf) |
| 2023 | EMNLP | [TK-KNN: A Balanced Distance-Based Pseudo Labeling Approach for Semi-Supervised Intent Classification](../finance_notes/2023.findings-emnlp.429.md) | application | Financial Services / 金融服务 | Customer Support and Business Consultation / 智能客服与业务咨询 | Uncertainty & Robustness / 不确定性与鲁棒性; Representation Learning / 表征学习 | [PDF](../../pdfs/EMNLP/2023/2023.findings-emnlp.429.pdf) |
| 2021 | ACL | [Don’t Miss the Labels: Label-semantic Augmented Meta-Learner for Few-Shot Text Classification](../finance_notes/2021.findings-acl.245.md) | application | Financial Services / 金融服务 | Customer Support and Business Consultation / 智能客服与业务咨询 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/ACL/2021/2021.findings-acl.245.pdf) |
| 2021 | ACL | [Energy-based Unknown Intent Detection with Data Manipulation](../finance_notes/2021.findings-acl.252.md) | application | Financial Services / 金融服务 | Customer Support and Business Consultation / 智能客服与业务咨询 |  | [PDF](../../pdfs/ACL/2021/2021.findings-acl.252.pdf) |
