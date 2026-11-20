## Research summary / 研究总结

**Financial Sentiment / 金融情感 · Findings / Core**

2026-11-20 · 6 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 目标是金融文本中的情感、语调、立场及其对象。公司、事件和方面粒度不同；情感预测与利用情感预测股票收益属于不同任务。

**当前收录与方法。** 本页仅总结 Findings / core 中的论文。当前较常见的子分类：News and Social Media Sentiment / 新闻与社交媒体情感 (2); Report and Earnings-Call Tone / 财报及电话会议语调 (2); Financial Stance and Opinion Detection / 金融立场与观点识别 (1)。已标注的方法：Language Models & LLM / 语言模型与LLM (3); Uncertainty & Robustness / 不确定性与鲁棒性 (3); Fairness & Recourse / 公平性与算法追索 (1); Representation Learning / 表征学习 (1); Optimization & Numerical Methods / 优化与数值方法 (1)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 检查标注口径、时效性、领域与语言迁移，区分情感准确率和收益效果。 代表论文的摘要、金融关联证据及原文链接见 [1](../indexes/finance_notes/2026.findings-acl.32.md) · [2](../indexes/finance_notes/2021.findings-acl.186.md) · [3](../indexes/finance_notes/2026.findings-acl.1106.md) · [4](../indexes/finance_notes/2026.findings-emnlp.137.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 研究标签口径、文化语言差异和跨期漂移，避免以市场收益倒推情感标签正确性。

### English

**Problem and subdirections.** Targets are sentiment, tone, stance and their financial subjects. Company, event and aspect granularity differ; predicting sentiment and using sentiment to predict returns are distinct tasks.

**Current coverage and methods.** This page covers only Findings / core. Frequent subcategories: News and Social Media Sentiment / 新闻与社交媒体情感 (2); Report and Earnings-Call Tone / 财报及电话会议语调 (2); Financial Stance and Opinion Detection / 金融立场与观点识别 (1). Recorded methods: Language Models & LLM / 语言模型与LLM (3); Uncertainty & Robustness / 不确定性与鲁棒性 (3); Fairness & Recourse / 公平性与算法追索 (1); Representation Learning / 表征学习 (1); Optimization & Numerical Methods / 优化与数值方法 (1). Counts overlap and are not performance rankings.

**Data and evaluation.** Check annotation policy, temporal drift and domain/language transfer; separate sentiment accuracy from returns. Representative abstracts, financial evidence and original sources are linked at [1](../indexes/finance_notes/2026.findings-acl.32.md) · [2](../indexes/finance_notes/2021.findings-acl.186.md) · [3](../indexes/finance_notes/2026.findings-acl.1106.md) · [4](../indexes/finance_notes/2026.findings-emnlp.137.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Study annotation policy, cultural and language differences and temporal drift without treating market returns as proof of sentiment-label correctness.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. Op-Fed: Opinion, Stance, and Monetary Policy Annotations on FOMC Transcripts Using Active Learning](../indexes/finance_notes/2026.findings-acl.32.md) · ACL 2026 | 主动学习和上下文标注货币政策立场<br>Active learning and context annotate monetary-policy stance | 意见识别与紧缩/宽松立场不同<br>Opinion detection differs from tightening/easing stance |
| [2. Trade the Event: Corporate Events Detection for News-Based Event-Driven Trading](../indexes/finance_notes/2021.findings-acl.186.md) · ACL 2021 | 从企业新闻事件构建事件驱动交易<br>Corporate-news events support event-driven trading | 收益依赖事件时点和模拟成交假设<br>Returns depend on event timing and simulated execution |
| [3. Cross-Cultural Transfer of Emoji Semantics and Sentiment in Financial Social Media](../indexes/finance_notes/2026.findings-acl.1106.md) · ACL 2026 | 研究主题：Cross-Cultural Transfer of Emoji Semantics and Sentiment in Financial Social Media<br>Research topic: Cross-Cultural Transfer of Emoji Semantics and Sentiment in Financial Social Media | 按原文的任务、数据和实验设置解释结果。<br>Interpret results within the original task, data and experimental setting. |
| [4. DRNash: Efficient and Robust Multi-Task Learning for Financial Sentiment Analysis](../indexes/finance_notes/2026.findings-emnlp.137.md) · EMNLP 2026 | 研究主题：DRNash: Efficient and Robust Multi-Task Learning for Financial Sentiment Analysis<br>Research topic: DRNash: Efficient and Robust Multi-Task Learning for Financial Sentiment Analysis | 按原文的任务、数据和实验设置解释结果。<br>Interpret results within the original task, data and experimental setting. |
