## Research summary / 研究总结

**Financial Models / 金融模型 · Main / Core**

2026-11-20 · 5 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 关注可复用的金融领域模型及其预训练、后训练和适配。金融是通用适配方法的实验领域时归 Application；只在单个任务中调用 LLM 不构成金融模型贡献。

**当前收录与方法。** 本页仅总结 Main / core 中的论文。当前较常见的子分类：Financial Foundation Models and Domain Pretraining / 金融基础模型与领域预训练 (5); Financial Instruction Tuning and Post-Training / 金融指令微调与后训练 (1); Financial Time-Series Foundation Models / 金融时序基础模型 (1)。已标注的方法：Language Models & LLM / 语言模型与LLM (4); Generative Modeling / 生成建模 (3); Representation Learning / 表征学习 (3); Uncertainty & Robustness / 不确定性与鲁棒性 (2)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 检查预训练数据、时间污染、跨任务迁移、模型规模和计算预算。 代表论文的摘要、金融关联证据及原文链接见 [1](../indexes/finance_notes/aaai-2026-39730.md) · [2](../indexes/finance_notes/2025.emnlp-main.1579.md) · [3](../indexes/finance_notes/2022.emnlp-main.148.md) · [4](../indexes/finance_notes/neurips-2026-OEokq7iASc.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 核对金融语料时间边界、能力保持和跨任务迁移，分离模型规模、数据、训练预算及检索的贡献。

### English

**Problem and subdirections.** This task concerns reusable financial models and their pretraining, post-training and adaptation. Finance as one domain of a general adaptation method belongs to Application; calling an LLM for one task is insufficient.

**Current coverage and methods.** This page covers only Main / core. Frequent subcategories: Financial Foundation Models and Domain Pretraining / 金融基础模型与领域预训练 (5); Financial Instruction Tuning and Post-Training / 金融指令微调与后训练 (1); Financial Time-Series Foundation Models / 金融时序基础模型 (1). Recorded methods: Language Models & LLM / 语言模型与LLM (4); Generative Modeling / 生成建模 (3); Representation Learning / 表征学习 (3); Uncertainty & Robustness / 不确定性与鲁棒性 (2). Counts overlap and are not performance rankings.

**Data and evaluation.** Audit pretraining data, temporal contamination, cross-task transfer, model size and compute budget. Representative abstracts, financial evidence and original sources are linked at [1](../indexes/finance_notes/aaai-2026-39730.md) · [2](../indexes/finance_notes/2025.emnlp-main.1579.md) · [3](../indexes/finance_notes/2022.emnlp-main.148.md) · [4](../indexes/finance_notes/neurips-2026-OEokq7iASc.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Audit financial-corpus time boundaries, capability retention and cross-task transfer, separating scale, data, training budget and retrieval effects.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. Kronos: A Foundation Model for the Language of Financial Markets](../indexes/finance_notes/aaai-2026-39730.md) · AAAI 2026 | K 线离散化与跨市场自回归预训练<br>Candlestick tokenization and cross-market autoregressive pretraining | 下游任务间的收益口径不同<br>Downstream tasks use different success criteria |
| [2. Demystifying Domain-adaptive Post-training for Financial LLMs](../indexes/finance_notes/2025.emnlp-main.1579.md) · EMNLP 2025 | 系统拆解领域后训练数据、配方和能力<br>Systematically examine adaptation data, recipes and capabilities | 比较要控制底座、数据量与训练预算<br>Control backbone, data volume and training budget |
| [3. When FLUE Meets FLANG: Benchmarks and Large Pretrained Language Model for Financial Domain](../indexes/finance_notes/2022.emnlp-main.148.md) · EMNLP 2022 | 金融预训练目标及 FLUE 多任务套件<br>Finance-specific pretraining objectives and the FLUE suite | 任务覆盖与整体金融能力不是同义词<br>Task coverage is not equivalent to comprehensive financial capability |
| [4. Towards Financial World Modeling](../indexes/finance_notes/neurips-2026-OEokq7iASc.md) · NeurIPS 2026 | 研究主题：Towards Financial World Modeling<br>Research topic: Towards Financial World Modeling | 按原文的任务、数据和实验设置解释结果。<br>Interpret results within the original task, data and experimental setting. |
