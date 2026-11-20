## Research summary / 研究总结

**Time Series / 时间序列 · Main / Application**

2026-11-20 · 338 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 关注金融序列的时间结构、变量依赖、表示、补全与生成。通用序列方法的金融实验与专门的金融建模分别保存在 Application 和 Core；明确以资产价值为目标的预测另见估值预测。

**当前收录与方法。** 本页仅总结 Main / application 中的论文。当前较常见的子分类：General Sequence Forecasting / 通用序列预测 (260); Sequence Representation and Pattern Discovery / 序列表示与模式发现 (136); Sequence Generation and Augmentation / 序列生成与数据增强 (64); Multivariate Relations and Cross-Frequency Modeling / 多变量关联与跨频率建模 (25); Anomaly and Change-Point Detection / 异常检测与变点识别 (19)。已标注的方法：Uncertainty & Robustness / 不确定性与鲁棒性 (96); Transformer / Transformer模型 (68); Generative Modeling / 生成建模 (66); Representation Learning / 表征学习 (59); Language Models & LLM / 语言模型与LLM (54)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 使用严格时间切分，分别报告预测误差、概率校准及合成质量。 代表论文的摘要、金融关联证据及原文链接见 [1](../indexes/finance_notes/iclr-2024-JePfAI8fah.md) · [2](../indexes/finance_notes/aaai-2026-39330.md) · [3](../indexes/finance_notes/aaai-2026-38542.md) · [4](../indexes/finance_notes/aaai-2026-39855.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 研究跨频率、缺失和状态变化下的稳定性，避免将单一预测误差改善直接解释为投资收益。

### English

**Problem and subdirections.** This task concerns temporal structure, variable dependence, representation, reconstruction and generation. General sequence methods with financial experiments and finance-specific modeling are separated into Application and Core. Explicit asset-value targets also belong to valuation prediction.

**Current coverage and methods.** This page covers only Main / application. Frequent subcategories: General Sequence Forecasting / 通用序列预测 (260); Sequence Representation and Pattern Discovery / 序列表示与模式发现 (136); Sequence Generation and Augmentation / 序列生成与数据增强 (64); Multivariate Relations and Cross-Frequency Modeling / 多变量关联与跨频率建模 (25); Anomaly and Change-Point Detection / 异常检测与变点识别 (19). Recorded methods: Uncertainty & Robustness / 不确定性与鲁棒性 (96); Transformer / Transformer模型 (68); Generative Modeling / 生成建模 (66); Representation Learning / 表征学习 (59); Language Models & LLM / 语言模型与LLM (54). Counts overlap and are not performance rankings.

**Data and evaluation.** Use chronological splits and separate forecast error, probabilistic calibration and synthesis quality. Representative abstracts, financial evidence and original sources are linked at [1](../indexes/finance_notes/iclr-2024-JePfAI8fah.md) · [2](../indexes/finance_notes/aaai-2026-39330.md) · [3](../indexes/finance_notes/aaai-2026-38542.md) · [4](../indexes/finance_notes/aaai-2026-39855.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Study stability across frequencies, missingness and regime changes without translating a forecast-error gain directly into investment profit.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. iTransformer: Inverted Transformers Are Effective for Time Series Forecasting](../indexes/finance_notes/iclr-2024-JePfAI8fah.md) · ICLR 2024 | 将变量作为 token 学习多变量关系<br>Variate tokens learn multivariate dependence | 属于通用方法，金融适用性取决于具体实验<br>A general method whose financial scope depends on experiments |
| [2. A Theoretical Analysis of Detecting Large Model-Generated Time Series](../indexes/finance_notes/aaai-2026-39330.md) · AAAI 2026 | 研究主题：A Theoretical Analysis of Detecting Large Model-Generated Time Series<br>Research topic: A Theoretical Analysis of Detecting Large Model-Generated Time Series | 按原文的任务、数据和实验设置解释结果。<br>Interpret results within the original task, data and experimental setting. |
| [3. APT: Affine Prototype-Timestamp for Time Series Forecasting Under Distribution Shift](../indexes/finance_notes/aaai-2026-38542.md) · AAAI 2026 | 研究主题：APT: Affine Prototype-Timestamp for Time Series Forecasting Under Distribution Shift<br>Research topic: APT: Affine Prototype-Timestamp for Time Series Forecasting Under Distribution Shift | 按原文的任务、数据和实验设置解释结果。<br>Interpret results within the original task, data and experimental setting. |
| [4. CometNet: Contextual Motif-guided Long-term Time Series Forecasting](../indexes/finance_notes/aaai-2026-39855.md) · AAAI 2026 | 研究主题：CometNet: Contextual Motif-guided Long-term Time Series Forecasting<br>Research topic: CometNet: Contextual Motif-guided Long-term Time Series Forecasting | 按原文的任务、数据和实验设置解释结果。<br>Interpret results within the original task, data and experimental setting. |
