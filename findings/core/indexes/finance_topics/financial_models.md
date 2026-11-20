# Financial Models / 金融模型

Financial domain pretraining, adaptation and reusable foundation models; generic time-series pretraining stays time series. / 金融领域预训练、适配与可复用基础模型；通用序列预训练仍归时间序列。

3 Findings long papers. Topic memberships can overlap.

[All topics](../ai_for_finance.md) · [Classification definitions](../finance_taxonomy.md) · [CSV](financial_models.csv) · [Excel](../../finance_catalog.xlsx)

<!-- task-summary:start -->

## Research summary / 研究总结

**Financial Models / 金融模型 · Findings / Core**

2026-11-20 · 3 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 关注可复用的金融领域模型及其预训练、后训练和适配。金融是通用适配方法的实验领域时归 Application；只在单个任务中调用 LLM 不构成金融模型贡献。

**当前收录与方法。** 本页仅总结 Findings / core 中的论文。当前较常见的子分类：Financial Foundation Models and Domain Pretraining / 金融基础模型与领域预训练 (3); Financial Model Adaptation, Compression and Deployment / 金融模型适配、压缩与高效部署 (1); Financial Multimodal Models / 金融多模态模型 (1)。已标注的方法：Language Models & LLM / 语言模型与LLM (3); Representation Learning / 表征学习 (1); Multimodal Learning / 多模态学习 (1)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 检查预训练数据、时间污染、跨任务迁移、模型规模和计算预算。 代表论文的摘要、金融关联证据及原文链接见 [1](../finance_notes/2024.findings-acl.606.md) · [2](../finance_notes/2026.findings-emnlp.2265.md) · [3](../finance_notes/2024.findings-acl.774.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 核对金融语料时间边界、能力保持和跨任务迁移，分离模型规模、数据、训练预算及检索的贡献。

### English

**Problem and subdirections.** This task concerns reusable financial models and their pretraining, post-training and adaptation. Finance as one domain of a general adaptation method belongs to Application; calling an LLM for one task is insufficient.

**Current coverage and methods.** This page covers only Findings / core. Frequent subcategories: Financial Foundation Models and Domain Pretraining / 金融基础模型与领域预训练 (3); Financial Model Adaptation, Compression and Deployment / 金融模型适配、压缩与高效部署 (1); Financial Multimodal Models / 金融多模态模型 (1). Recorded methods: Language Models & LLM / 语言模型与LLM (3); Representation Learning / 表征学习 (1); Multimodal Learning / 多模态学习 (1). Counts overlap and are not performance rankings.

**Data and evaluation.** Audit pretraining data, temporal contamination, cross-task transfer, model size and compute budget. Representative abstracts, financial evidence and original sources are linked at [1](../finance_notes/2024.findings-acl.606.md) · [2](../finance_notes/2026.findings-emnlp.2265.md) · [3](../finance_notes/2024.findings-acl.774.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Audit financial-corpus time boundaries, capability retention and cross-task transfer, separating scale, data, training budget and retrieval effects.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. Efficient Continual Pre-training for Building Domain Specific Large Language Models](../finance_notes/2024.findings-acl.606.md) · ACL 2024 | 通过数据选择降低金融继续预训练成本<br>Selected data reduces financial continual-pretraining cost | 结论依赖底座、语料和目标任务<br>Results depend on backbone, corpus and target tasks |
| [2. FinanceLLM: A Survey of Large Language Models in Finance](../finance_notes/2026.findings-emnlp.2265.md) · EMNLP 2026 | 研究主题：FinanceLLM: A Survey of Large Language Models in Finance<br>Research topic: FinanceLLM: A Survey of Large Language Models in Finance | 按原文的任务、数据和实验设置解释结果。<br>Interpret results within the original task, data and experimental setting. |
| [3. FinTral: A Family of GPT-4 Level Multimodal Financial Large Language Models](../finance_notes/2024.findings-acl.774.md) · ACL 2024 | 研究主题：FinTral: A Family of GPT-4 Level Multimodal Financial Large Language Models<br>Research topic: FinTral: A Family of GPT-4 Level Multimodal Financial Large Language Models | 按原文的任务、数据和实验设置解释结果。<br>Interpret results within the original task, data and experimental setting. |

<!-- task-summary:end -->

## Subtopic statistics / 子方向统计

| Subtopic | Papers |
|---|---:|
| Financial Foundation Models and Domain Pretraining / 金融基础模型与领域预训练 | 3 |
| Financial Instruction Tuning and Post-Training / 金融指令微调与后训练 | 0 |
| Financial Representation Models / 金融专用表示模型 | 0 |
| Financial Multimodal Models / 金融多模态模型 | 1 |
| Financial Time-Series Foundation Models / 金融时序基础模型 | 0 |
| Financial Model Adaptation, Compression and Deployment / 金融模型适配、压缩与高效部署 | 1 |

## Full paper list / 完整论文列表

| Year | Venue | Paper | Scope | Primary topic | Subtopics | Methods | Resources |
|---|---|---|---|---|---|---|---|
| 2026 | EMNLP | [FinanceLLM: A Survey of Large Language Models in Finance](../finance_notes/2026.findings-emnlp.2265.md) | core | Financial Models / 金融模型 | Financial Foundation Models and Domain Pretraining / 金融基础模型与领域预训练 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/EMNLP/2026/2026.findings-emnlp.2265.pdf) |
| 2024 | ACL | [Efficient Continual Pre-training for Building Domain Specific Large Language Models](../finance_notes/2024.findings-acl.606.md) | core | Financial Models / 金融模型 | Financial Foundation Models and Domain Pretraining / 金融基础模型与领域预训练; Financial Model Adaptation, Compression and Deployment / 金融模型适配、压缩与高效部署 | Language Models & LLM / 语言模型与LLM; Representation Learning / 表征学习 | [PDF](../../pdfs/ACL/2024/2024.findings-acl.606.pdf) |
| 2024 | ACL | [FinTral: A Family of GPT-4 Level Multimodal Financial Large Language Models](../finance_notes/2024.findings-acl.774.md) | core | Financial Models / 金融模型 | Financial Foundation Models and Domain Pretraining / 金融基础模型与领域预训练; Financial Multimodal Models / 金融多模态模型 | Language Models & LLM / 语言模型与LLM; Multimodal Learning / 多模态学习 | [PDF](../../pdfs/ACL/2024/2024.findings-acl.774.pdf) |
