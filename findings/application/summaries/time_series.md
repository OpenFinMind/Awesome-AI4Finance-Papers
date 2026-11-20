## Research summary / 研究总结

**Time Series / 时间序列 · Findings / Application**

2026-11-20 · 2 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 关注金融序列的时间结构、变量依赖、表示、补全与生成。通用序列方法的金融实验与专门的金融建模分别保存在 Application 和 Core；明确以资产价值为目标的预测另见估值预测。

**当前收录与方法。** 本页仅总结 Findings / application 中的论文。当前较常见的子分类：General Sequence Forecasting / 通用序列预测 (2); Sequence Generation and Augmentation / 序列生成与数据增强 (1)。已标注的方法：Representation Learning / 表征学习 (1); Language Models & LLM / 语言模型与LLM (1)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 使用严格时间切分，分别报告预测误差、概率校准及合成质量。 代表论文的摘要、金融关联证据及原文链接见 [1](../indexes/finance_notes/2024.findings-emnlp.201.md) · [2](../indexes/finance_notes/2024.findings-emnlp.435.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 研究跨频率、缺失和状态变化下的稳定性，避免将单一预测误差改善直接解释为投资收益。

### English

**Problem and subdirections.** This task concerns temporal structure, variable dependence, representation, reconstruction and generation. General sequence methods with financial experiments and finance-specific modeling are separated into Application and Core. Explicit asset-value targets also belong to valuation prediction.

**Current coverage and methods.** This page covers only Findings / application. Frequent subcategories: General Sequence Forecasting / 通用序列预测 (2); Sequence Generation and Augmentation / 序列生成与数据增强 (1). Recorded methods: Representation Learning / 表征学习 (1); Language Models & LLM / 语言模型与LLM (1). Counts overlap and are not performance rankings.

**Data and evaluation.** Use chronological splits and separate forecast error, probabilistic calibration and synthesis quality. Representative abstracts, financial evidence and original sources are linked at [1](../indexes/finance_notes/2024.findings-emnlp.201.md) · [2](../indexes/finance_notes/2024.findings-emnlp.435.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Study stability across frequencies, missingness and regime changes without translating a forecast-error gain directly into investment profit.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. Language Models Still Struggle to Zero-shot Reason about Time Series](../indexes/finance_notes/2024.findings-emnlp.201.md) · EMNLP 2024 | 分任务诊断零样本时间序列推理<br>Task-separated diagnostics of zero-shot sequence reasoning | 通用多领域结果中金融只占部分<br>Finance is one part of a broader multidomain evaluation |
| [2. Demonstration Selection Strategies for Numerical Time Series Data-to-Text](../indexes/finance_notes/2024.findings-emnlp.435.md) · EMNLP 2024 | 按序列相似度和知识选择数值生成示例<br>Select data-to-text demonstrations using sequence similarity and knowledge | 叙述质量和预测效用不同<br>Narrative quality differs from forecasting utility |
