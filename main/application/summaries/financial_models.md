## Research summary / 研究总结

**Financial Models / 金融模型 · Main / Application**

2026-11-20 · 22 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 关注可复用的金融领域模型及其预训练、后训练和适配。金融是通用适配方法的实验领域时归 Application；只在单个任务中调用 LLM 不构成金融模型贡献。

**当前收录与方法。** 本页仅总结 Main / application 中的论文。当前较常见的子分类：Financial Foundation Models and Domain Pretraining / 金融基础模型与领域预训练 (17); Financial Instruction Tuning and Post-Training / 金融指令微调与后训练 (8); Financial Model Adaptation, Compression and Deployment / 金融模型适配、压缩与高效部署 (5); Financial Representation Models / 金融专用表示模型 (2); Financial Multimodal Models / 金融多模态模型 (1)。已标注的方法：Language Models & LLM / 语言模型与LLM (20); Representation Learning / 表征学习 (6); Optimization & Numerical Methods / 优化与数值方法 (4); Uncertainty & Robustness / 不确定性与鲁棒性 (4); Retrieval & RAG / 检索与RAG (3)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 检查预训练数据、时间污染、跨任务迁移、模型规模和计算预算。 代表论文的摘要、金融关联证据及原文链接见 [1](../indexes/finance_notes/aaai-2026-40722.md) · [2](../indexes/finance_notes/2026.acl-long.645.md) · [3](../indexes/finance_notes/2026.acl-long.996.md) · [4](../indexes/finance_notes/2026.acl-long.2201.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 核对金融语料时间边界、能力保持和跨任务迁移，分离模型规模、数据、训练预算及检索的贡献。

### English

**Problem and subdirections.** This task concerns reusable financial models and their pretraining, post-training and adaptation. Finance as one domain of a general adaptation method belongs to Application; calling an LLM for one task is insufficient.

**Current coverage and methods.** This page covers only Main / application. Frequent subcategories: Financial Foundation Models and Domain Pretraining / 金融基础模型与领域预训练 (17); Financial Instruction Tuning and Post-Training / 金融指令微调与后训练 (8); Financial Model Adaptation, Compression and Deployment / 金融模型适配、压缩与高效部署 (5); Financial Representation Models / 金融专用表示模型 (2); Financial Multimodal Models / 金融多模态模型 (1). Recorded methods: Language Models & LLM / 语言模型与LLM (20); Representation Learning / 表征学习 (6); Optimization & Numerical Methods / 优化与数值方法 (4); Uncertainty & Robustness / 不确定性与鲁棒性 (4); Retrieval & RAG / 检索与RAG (3). Counts overlap and are not performance rankings.

**Data and evaluation.** Audit pretraining data, temporal contamination, cross-task transfer, model size and compute budget. Representative abstracts, financial evidence and original sources are linked at [1](../indexes/finance_notes/aaai-2026-40722.md) · [2](../indexes/finance_notes/2026.acl-long.645.md) · [3](../indexes/finance_notes/2026.acl-long.996.md) · [4](../indexes/finance_notes/2026.acl-long.2201.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Audit financial-corpus time boundaries, capability retention and cross-task transfer, separating scale, data, training budget and retrieval effects.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. RCP-Merging: Merging Long Chain-of-Thought Models with Domain-Specific Models by Considering Reasoning Capability as Prior](../indexes/finance_notes/aaai-2026-40722.md) · AAAI 2026 | 研究主题：RCP-Merging: Merging Long Chain-of-Thought Models with Domain-Specific Models by Considering Reasoning Capability as Prior<br>Research topic: RCP-Merging: Merging Long Chain-of-Thought Models with Domain-Specific Models by Considering Reasoning Capability as Prior | 按原文的任务、数据和实验设置解释结果。<br>Interpret results within the original task, data and experimental setting. |
| [2. Map of Encoders – Mapping Sentence Encoders using Quantum Relative Entropy](../indexes/finance_notes/2026.acl-long.645.md) · ACL 2026 | 研究主题：Map of Encoders – Mapping Sentence Encoders using Quantum Relative Entropy<br>Research topic: Map of Encoders – Mapping Sentence Encoders using Quantum Relative Entropy | 按原文的任务、数据和实验设置解释结果。<br>Interpret results within the original task, data and experimental setting. |
| [3. Nirvana: A Specialized Generalist Model With Task-Aware Memory Mechanism](../indexes/finance_notes/2026.acl-long.996.md) · ACL 2026 | 研究主题：Nirvana: A Specialized Generalist Model With Task-Aware Memory Mechanism<br>Research topic: Nirvana: A Specialized Generalist Model With Task-Aware Memory Mechanism | 按原文的任务、数据和实验设置解释结果。<br>Interpret results within the original task, data and experimental setting. |
| [4. ReasonAny: Incorporating Reasoning Capability to Any Model via Simple and Effective Model Merging](../indexes/finance_notes/2026.acl-long.2201.md) · ACL 2026 | 研究主题：ReasonAny: Incorporating Reasoning Capability to Any Model via Simple and Effective Model Merging<br>Research topic: ReasonAny: Incorporating Reasoning Capability to Any Model via Simple and Effective Model Merging | 按原文的任务、数据和实验设置解释结果。<br>Interpret results within the original task, data and experimental setting. |
