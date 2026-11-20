## Research summary / 研究总结

**Time Series / 时间序列 · Main / Core**

2026-11-20 · 41 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 关注金融序列的时间结构、变量依赖、表示、补全与生成。通用序列方法的金融实验与专门的金融建模分别保存在 Application 和 Core；明确以资产价值为目标的预测另见估值预测。

**当前收录与方法。** 本页仅总结 Main / core 中的论文。当前较常见的子分类：General Sequence Forecasting / 通用序列预测 (25); Sequence Representation and Pattern Discovery / 序列表示与模式发现 (19); Sequence Generation and Augmentation / 序列生成与数据增强 (9); Multivariate Relations and Cross-Frequency Modeling / 多变量关联与跨频率建模 (1); Imputation and Sequence Reconstruction / 缺失值填补与序列重建 (1)。已标注的方法：Uncertainty & Robustness / 不确定性与鲁棒性 (12); Language Models & LLM / 语言模型与LLM (12); Generative Modeling / 生成建模 (10); Optimization & Numerical Methods / 优化与数值方法 (8); Diffusion & Flow / 扩散与流模型 (5)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 使用严格时间切分，分别报告预测误差、概率校准及合成质量。 代表论文的摘要、金融关联证据及原文链接见 [1](../indexes/finance_notes/aaai-2024-29531.md) · [2](../indexes/finance_notes/aaai-2026-39730.md) · [3](../indexes/finance_notes/2026.acl-long.1071.md) · [4](../indexes/finance_notes/2026.emnlp-main.1329.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 研究跨频率、缺失和状态变化下的稳定性，避免将单一预测误差改善直接解释为投资收益。

### English

**Problem and subdirections.** This task concerns temporal structure, variable dependence, representation, reconstruction and generation. General sequence methods with financial experiments and finance-specific modeling are separated into Application and Core. Explicit asset-value targets also belong to valuation prediction.

**Current coverage and methods.** This page covers only Main / core. Frequent subcategories: General Sequence Forecasting / 通用序列预测 (25); Sequence Representation and Pattern Discovery / 序列表示与模式发现 (19); Sequence Generation and Augmentation / 序列生成与数据增强 (9); Multivariate Relations and Cross-Frequency Modeling / 多变量关联与跨频率建模 (1); Imputation and Sequence Reconstruction / 缺失值填补与序列重建 (1). Recorded methods: Uncertainty & Robustness / 不确定性与鲁棒性 (12); Language Models & LLM / 语言模型与LLM (12); Generative Modeling / 生成建模 (10); Optimization & Numerical Methods / 优化与数值方法 (8); Diffusion & Flow / 扩散与流模型 (5). Counts overlap and are not performance rankings.

**Data and evaluation.** Use chronological splits and separate forecast error, probabilistic calibration and synthesis quality. Representative abstracts, financial evidence and original sources are linked at [1](../indexes/finance_notes/aaai-2024-29531.md) · [2](../indexes/finance_notes/aaai-2026-39730.md) · [3](../indexes/finance_notes/2026.acl-long.1071.md) · [4](../indexes/finance_notes/2026.emnlp-main.1329.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Study stability across frequencies, missingness and regime changes without translating a forecast-error gain directly into investment profit.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. Market-GAN: Adding Control to Financial Market Data Generation with Semantic Context](../indexes/finance_notes/aaai-2024-29531.md) · AAAI 2024 | 利用语义上下文控制市场序列生成<br>Semantic context controls market-sequence generation | 分布保真与策略有效性需分别核验<br>Distributional fidelity and strategy utility need separate tests |
| [2. Kronos: A Foundation Model for the Language of Financial Markets](../indexes/finance_notes/aaai-2026-39730.md) · AAAI 2026 | K 线离散化与跨市场自回归预训练<br>Candlestick tokenization and cross-market autoregressive pretraining | 下游任务间的收益口径不同<br>Downstream tasks use different success criteria |
| [3. Understanding Structured Financial Data with LLMs: A Case Study on Fraud Detection](../indexes/finance_notes/2026.acl-long.1071.md) · ACL 2026 | 特征压缩加检索增强表格欺诈判断<br>Feature reduction and retrieval support tabular fraud detection | 可解释辅助价值与专用分类性能分开<br>Separate assistive explanations from specialist classification quality |
| [4. CAME: Company-Aware Evidence-Memory Experts for Interpretable Quarter-Ahead Revenue Forecasting](../indexes/finance_notes/2026.emnlp-main.1329.md) · EMNLP 2026 | 公司证据与误差记忆修正收入预测锚点<br>Company evidence and error memory adjust revenue forecast anchors | 含开发样本且公司数有限，需外部验证<br>Development-inclusive and limited-firm evidence needs external validation |
