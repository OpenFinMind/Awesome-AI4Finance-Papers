# Insurance and Actuarial Science / 保险精算

Insurance underwriting, claims, reserves, actuarial prediction and insurance business decisions. / 承保、理赔、准备金、精算预测及保险业务决策。

3 Main long papers. Topic memberships can overlap.

[All topics](../ai_for_finance.md) · [Classification definitions](../finance_taxonomy.md) · [CSV](insurance.csv) · [Excel](../../finance_catalog.xlsx)

<!-- task-summary:start -->

## Research summary / 研究总结

**Insurance and Actuarial Science / 保险精算 · Main / Core**

2026-11-20 · 3 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 以保险合同、保费、索赔、准备金及寿命风险为对象。客户营销、保险销售对话与欺诈检测分别与金融服务或金融安全关联，不因使用保险数据就视为精算贡献。

**当前收录与方法。** 本页仅总结 Main / core 中的论文。当前较常见的子分类：Claim Frequency and Loss Severity / 索赔频率与损失严重度 (2); Catastrophe Risk and Solvency / 巨灾风险与偿付能力 (1)。已标注的方法：Language Models & LLM / 语言模型与LLM (2); Retrieval & RAG / 检索与RAG (1)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 关注索赔分布、校准、选择偏差、长期风险及业务约束。 代表论文的摘要、金融关联证据及原文链接见 [1](../finance_notes/2026.acl-long.1035.md) · [2](../finance_notes/neurips-2026-1LHT6frSus.md) · [3](../finance_notes/2026.emnlp-main.2165.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 联合考察长尾赔付、风险选择和长期校准，检验模型在保单结构与人群变化下的适用性。

### English

**Problem and subdirections.** This task concerns insurance contracts, premiums, claims, reserves and longevity risk. Marketing, sales dialogue and fraud detection connect to services or safety; using insurance data alone does not establish an actuarial contribution.

**Current coverage and methods.** This page covers only Main / core. Frequent subcategories: Claim Frequency and Loss Severity / 索赔频率与损失严重度 (2); Catastrophe Risk and Solvency / 巨灾风险与偿付能力 (1). Recorded methods: Language Models & LLM / 语言模型与LLM (2); Retrieval & RAG / 检索与RAG (1). Counts overlap and are not performance rankings.

**Data and evaluation.** Inspect claim distributions, calibration, selection bias, long-term risk and business constraints. Representative abstracts, financial evidence and original sources are linked at [1](../finance_notes/2026.acl-long.1035.md) · [2](../finance_notes/neurips-2026-1LHT6frSus.md) · [3](../finance_notes/2026.emnlp-main.2165.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Examine heavy-tailed claims, risk selection and long-term calibration, including changes in contract structure and insured populations.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. InsLogicBench: An Argumentation Logic Grounded Benchmark for Complex Insurance Claims Adjudication](../finance_notes/2026.acl-long.1035.md) · ACL 2026 | 为复杂理赔构建可检查的条款推理链<br>Checkable clause-grounded reasoning for complex claims | 合成逻辑可靠性与真实案件迁移需区分<br>Synthetic logical validity differs from real-case transfer |
| [2. Long-Term Risks of Risk-Based Allocation](../finance_notes/neurips-2026-1LHT6frSus.md) · NeurIPS 2026 | 研究主题：Long-Term Risks of Risk-Based Allocation<br>Research topic: Long-Term Risks of Risk-Based Allocation | 按原文的任务、数据和实验设置解释结果。<br>Interpret results within the original task, data and experimental setting. |
| [3. T2ER: A Chinese Benchmark for Text-to-Executable-Rule Generation in Medical Insurance](../finance_notes/2026.emnlp-main.2165.md) · EMNLP 2026 | 研究主题：T2ER: A Chinese Benchmark for Text-to-Executable-Rule Generation in Medical Insurance<br>Research topic: T2ER: A Chinese Benchmark for Text-to-Executable-Rule Generation in Medical Insurance | 按原文的任务、数据和实验设置解释结果。<br>Interpret results within the original task, data and experimental setting. |

<!-- task-summary:end -->

## Subtopic statistics / 子方向统计

| Subtopic | Papers |
|---|---:|
| Insurance Pricing and Premium Setting / 保险定价与保费厘定 | 0 |
| Claim Frequency and Loss Severity / 索赔频率与损失严重度 | 2 |
| Reserves and Payout Prediction / 准备金与赔付预测 | 0 |
| Mortality, Longevity and Survival / 死亡率、长寿与生存分析 | 0 |
| Reinsurance and Risk Sharing / 再保险与风险分担 | 0 |
| Catastrophe Risk and Solvency / 巨灾风险与偿付能力 | 1 |

## Full paper list / 完整论文列表

| Year | Venue | Paper | Scope | Primary topic | Subtopics | Methods | Resources |
|---|---|---|---|---|---|---|---|
| 2026 | ACL | [InsLogicBench: An Argumentation Logic Grounded Benchmark for Complex Insurance Claims Adjudication](../finance_notes/2026.acl-long.1035.md) | core | Financial Evaluation / 金融评测 | Claim Frequency and Loss Severity / 索赔频率与损失严重度; Financial Datasets and Task Benchmarks / 金融数据集与任务基准 | Language Models & LLM / 语言模型与LLM; Retrieval & RAG / 检索与RAG | [PDF](../../pdfs/ACL/2026/2026.acl-long.1035__InsLogicBench_An_Argumentation_Logic_Grounded_Benchmark_for_Complex_Insurance_Claims_Adjudication.pdf) |
| 2026 | EMNLP | [T2ER: A Chinese Benchmark for Text-to-Executable-Rule Generation in Medical Insurance](../finance_notes/2026.emnlp-main.2165.md) | core | Financial Evaluation / 金融评测 | Claim Frequency and Loss Severity / 索赔频率与损失严重度; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Financial Understanding and Multimodal Evaluation / 金融理解及多模态评测 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/EMNLP/2026/2026.emnlp-main.2165__T2ER_A_Chinese_Benchmark_for_Text_to_Executable_Rule_Generation_in_Medical_Insurance.pdf) |
| 2026 | NeurIPS | [Long-Term Risks of Risk-Based Allocation](../finance_notes/neurips-2026-1LHT6frSus.md) | core | Insurance and Actuarial Science / 保险精算 | Catastrophe Risk and Solvency / 巨灾风险与偿付能力 |  | [Online](https://openreview.net/forum?id=1LHT6frSus) |
