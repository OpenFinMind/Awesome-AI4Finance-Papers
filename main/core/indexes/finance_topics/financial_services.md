# Financial Services / 金融服务

Banking, payments, customer service, marketing and personal/business financial services. / 银行、支付、客户服务、营销及个人与企业金融服务。

5 Main long papers. Topic memberships can overlap.

[All topics](../ai_for_finance.md) · [Classification definitions](../finance_taxonomy.md) · [CSV](financial_services.csv) · [Excel](../../finance_catalog.xlsx)

<!-- task-summary:start -->

## Research summary / 研究总结

**Financial Services / 金融服务 · Main / Core**

2026-11-20 · 5 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 关注客户交互、产品匹配、个人财务服务及银行支付流程。服务质量、业务效率与金融结果需要分别评价；违约预测和欺诈检测按风险或安全任务归类。

**当前收录与方法。** 本页仅总结 Main / core 中的论文。当前较常见的子分类：Customer Support and Business Consultation / 智能客服与业务咨询 (4); Financial Product Recommendation and Matching / 金融产品推荐与匹配 (1)。已标注的方法：Retrieval & RAG / 检索与RAG (2); Language Models & LLM / 语言模型与LLM (2); Reinforcement Learning / 强化学习 (1); Representation Learning / 表征学习 (1)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 区分公开业务数据与真实部署，检查客户、时间和机构间迁移。 代表论文的摘要、金融关联证据及原文链接见 [1](../finance_notes/aaai-2021-16105.md) · [2](../finance_notes/2026.acl-long.232.md) · [3](../finance_notes/icml-2026-XHZK5abtw2.md) · [4](../finance_notes/2023.emnlp-main.234.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 研究服务可及性、长期客户利益与跨机构迁移，区分公开数据实验和真实业务部署。

### English

**Problem and subdirections.** This task concerns customer interaction, product matching, personal finance and banking/payment workflows. Service quality, efficiency and financial outcomes require separate evaluation; default and fraud prediction belong to risk or safety.

**Current coverage and methods.** This page covers only Main / core. Frequent subcategories: Customer Support and Business Consultation / 智能客服与业务咨询 (4); Financial Product Recommendation and Matching / 金融产品推荐与匹配 (1). Recorded methods: Retrieval & RAG / 检索与RAG (2); Language Models & LLM / 语言模型与LLM (2); Reinforcement Learning / 强化学习 (1); Representation Learning / 表征学习 (1). Counts overlap and are not performance rankings.

**Data and evaluation.** Distinguish public business data from deployment; check transfer across customers, time and institutions. Representative abstracts, financial evidence and original sources are linked at [1](../finance_notes/aaai-2021-16105.md) · [2](../finance_notes/2026.acl-long.232.md) · [3](../finance_notes/icml-2026-XHZK5abtw2.md) · [4](../finance_notes/2023.emnlp-main.234.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Study access, long-term customer interests and transfer across institutions, distinguishing public-data experiments from deployment.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. RevMan: Revenue-aware Multi-task Online Insurance Recommendation](../finance_notes/aaai-2021-16105.md) · AAAI 2021 | 跨产品和场景的收入导向推荐<br>Revenue-aware recommendation across products and scenarios | 收入提升不是理赔准确性证据<br>Revenue gains do not establish adjudication accuracy |
| [2. Everyone is unique: Towards Behaviorally Heterogeneous Negotiation Dialogue Systems for Debt Collection](../finance_notes/2026.acl-long.232.md) · ACL 2026 | 异质人物设定下优化催收协商与体验<br>Optimize debt negotiation and experience across heterogeneous personas | 用户模拟与实际客户行为需要区分<br>Simulated personas differ from actual customers |
| [3. $\tau$-Knowledge: Evaluating Conversational Agents over Unstructured Knowledge](../finance_notes/icml-2026-XHZK5abtw2.md) · ICML 2026 | 在非结构化知识和工具间完成可验证账户任务<br>Complete verifiable account tasks using unstructured knowledge and tools | 规则执行及多次运行稳定性同样重要<br>Rule execution and repeated-run reliability both matter |
| [4. TRAVEL: Tag-Aware Conversational FAQ Retrieval via Reinforcement Learning](../finance_notes/2023.emnlp-main.234.md) · EMNLP 2023 | 标签与 RL 减少 FAQ 对话中的噪声<br>Tags and RL reduce noise in conversational FAQ retrieval | 检索成功不代表完成银行业务操作<br>Retrieval success does not establish workflow completion |

<!-- task-summary:end -->

## Subtopic statistics / 子方向统计

| Subtopic | Papers |
|---|---:|
| Customer Support and Business Consultation / 智能客服与业务咨询 | 4 |
| Financial Product Recommendation and Matching / 金融产品推荐与匹配 | 1 |
| Personal Financial Planning and Services / 个人财务规划与服务 | 0 |
| Lending, Payment and Banking Workflows / 贷款、支付及银行业务流程 | 0 |
| Customer Behavior and Relationship Management / 客户行为与关系管理 | 0 |
| Financial Access and Inclusion / 金融服务可及性与普惠金融 | 0 |

## Full paper list / 完整论文列表

| Year | Venue | Paper | Scope | Primary topic | Subtopics | Methods | Resources |
|---|---|---|---|---|---|---|---|
| 2026 | ACL | [Everyone is unique: Towards Behaviorally Heterogeneous Negotiation Dialogue Systems for Debt Collection](../finance_notes/2026.acl-long.232.md) | core | Financial Evaluation / 金融评测 | Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策; Customer Support and Business Consultation / 智能客服与业务咨询; Financial Datasets and Task Benchmarks / 金融数据集与任务基准 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/ACL/2026/2026.acl-long.232__Everyone_is_unique_Towards_Behaviorally_Heterogeneous_Negotiation_Dialogue_Systems_for_Debt_Collection.pdf) |
| 2026 | EMNLP | [Risk-Adjusted Harm Scoring for Automated Red Teaming of LLMs in Financial Services](../finance_notes/2026.emnlp-main.1730.md) | core | Financial Safety / 金融安全 | Customer Support and Business Consultation / 智能客服与业务咨询; Privacy and Sensitive Information Protection / 隐私与敏感信息保护; Financial Model and Agent Safety / 金融模型及智能体安全 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/EMNLP/2026/2026.emnlp-main.1730__Risk_Adjusted_Harm_Scoring_for_Automated_Red_Teaming_of_LLMs_in_Financial_Services.pdf) |
| 2026 | ICML | [$\tau$-Knowledge: Evaluating Conversational Agents over Unstructured Knowledge](../finance_notes/icml-2026-XHZK5abtw2.md) | core | Financial Evaluation / 金融评测 | Customer Support and Business Consultation / 智能客服与业务咨询; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Financial Knowledge and Professional Evaluation / 金融知识与专业能力评测; Financial Decision and Agent Evaluation / 金融决策与智能体评测; Evaluation Protocols and Metrics / 评测协议与指标 | Retrieval & RAG / 检索与RAG; Representation Learning / 表征学习 | [PDF](../../pdfs/ICML/2026/icml-2026-XHZK5abtw2__tau_Knowledge_Evaluating_Conversational_Agents_over_Unstructured_Knowledge.pdf) |
| 2023 | EMNLP | [TRAVEL: Tag-Aware Conversational FAQ Retrieval via Reinforcement Learning](../finance_notes/2023.emnlp-main.234.md) | core | Financial Retrieval / 金融检索 | Financial Semantic Matching and Ranking / 金融语义匹配与排序; Customer Support and Business Consultation / 智能客服与业务咨询 | Reinforcement Learning / 强化学习; Retrieval & RAG / 检索与RAG | [PDF](../../pdfs/EMNLP/2023/2023.emnlp-main.234__TRAVEL_Tag_Aware_Conversational_FAQ_Retrieval_via_Reinforcement_Learning.pdf) |
| 2021 | AAAI | [RevMan: Revenue-aware Multi-task Online Insurance Recommendation](../finance_notes/aaai-2021-16105.md) | core | Financial Services / 金融服务 | Financial Product Recommendation and Matching / 金融产品推荐与匹配 |  | [PDF](../../pdfs/AAAI/2021/aaai-2021-16105__RevMan_Revenue_aware_Multi_task_Online_Insurance_Recommendation.pdf) |
