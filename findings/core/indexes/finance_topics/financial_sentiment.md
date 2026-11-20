# Financial Sentiment / 金融情感

Financial sentiment, stance, tone and emotion as the prediction target; downstream return prediction stays valuation prediction. / 以金融情感、立场、语气与情绪为目标；下游收益预测仍归估值预测。

6 Findings long papers. Topic memberships can overlap.

[All topics](../ai_for_finance.md) · [Classification definitions](../finance_taxonomy.md) · [CSV](financial_sentiment.csv) · [Excel](../../finance_catalog.xlsx)

<!-- task-summary:start -->

## Research summary / 研究总结

**Financial Sentiment / 金融情感 · Findings / Core**

2026-11-20 · 6 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 目标是金融文本中的情感、语调、立场及其对象。公司、事件和方面粒度不同；情感预测与利用情感预测股票收益属于不同任务。

**当前收录与方法。** 本页仅总结 Findings / core 中的论文。当前较常见的子分类：News and Social Media Sentiment / 新闻与社交媒体情感 (2); Report and Earnings-Call Tone / 财报及电话会议语调 (2); Financial Stance and Opinion Detection / 金融立场与观点识别 (1)。已标注的方法：Language Models & LLM / 语言模型与LLM (3); Uncertainty & Robustness / 不确定性与鲁棒性 (3); Fairness & Recourse / 公平性与算法追索 (1); Representation Learning / 表征学习 (1); Optimization & Numerical Methods / 优化与数值方法 (1)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 检查标注口径、时效性、领域与语言迁移，区分情感准确率和收益效果。 代表论文的摘要、金融关联证据及原文链接见 [1](../finance_notes/2026.findings-acl.32.md) · [2](../finance_notes/2021.findings-acl.186.md) · [3](../finance_notes/2026.findings-acl.1106.md) · [4](../finance_notes/2026.findings-emnlp.137.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 研究标签口径、文化语言差异和跨期漂移，避免以市场收益倒推情感标签正确性。

### English

**Problem and subdirections.** Targets are sentiment, tone, stance and their financial subjects. Company, event and aspect granularity differ; predicting sentiment and using sentiment to predict returns are distinct tasks.

**Current coverage and methods.** This page covers only Findings / core. Frequent subcategories: News and Social Media Sentiment / 新闻与社交媒体情感 (2); Report and Earnings-Call Tone / 财报及电话会议语调 (2); Financial Stance and Opinion Detection / 金融立场与观点识别 (1). Recorded methods: Language Models & LLM / 语言模型与LLM (3); Uncertainty & Robustness / 不确定性与鲁棒性 (3); Fairness & Recourse / 公平性与算法追索 (1); Representation Learning / 表征学习 (1); Optimization & Numerical Methods / 优化与数值方法 (1). Counts overlap and are not performance rankings.

**Data and evaluation.** Check annotation policy, temporal drift and domain/language transfer; separate sentiment accuracy from returns. Representative abstracts, financial evidence and original sources are linked at [1](../finance_notes/2026.findings-acl.32.md) · [2](../finance_notes/2021.findings-acl.186.md) · [3](../finance_notes/2026.findings-acl.1106.md) · [4](../finance_notes/2026.findings-emnlp.137.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Study annotation policy, cultural and language differences and temporal drift without treating market returns as proof of sentiment-label correctness.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. Op-Fed: Opinion, Stance, and Monetary Policy Annotations on FOMC Transcripts Using Active Learning](../finance_notes/2026.findings-acl.32.md) · ACL 2026 | 主动学习和上下文标注货币政策立场<br>Active learning and context annotate monetary-policy stance | 意见识别与紧缩/宽松立场不同<br>Opinion detection differs from tightening/easing stance |
| [2. Trade the Event: Corporate Events Detection for News-Based Event-Driven Trading](../finance_notes/2021.findings-acl.186.md) · ACL 2021 | 从企业新闻事件构建事件驱动交易<br>Corporate-news events support event-driven trading | 收益依赖事件时点和模拟成交假设<br>Returns depend on event timing and simulated execution |
| [3. Cross-Cultural Transfer of Emoji Semantics and Sentiment in Financial Social Media](../finance_notes/2026.findings-acl.1106.md) · ACL 2026 | 研究主题：Cross-Cultural Transfer of Emoji Semantics and Sentiment in Financial Social Media<br>Research topic: Cross-Cultural Transfer of Emoji Semantics and Sentiment in Financial Social Media | 按原文的任务、数据和实验设置解释结果。<br>Interpret results within the original task, data and experimental setting. |
| [4. DRNash: Efficient and Robust Multi-Task Learning for Financial Sentiment Analysis](../finance_notes/2026.findings-emnlp.137.md) · EMNLP 2026 | 研究主题：DRNash: Efficient and Robust Multi-Task Learning for Financial Sentiment Analysis<br>Research topic: DRNash: Efficient and Robust Multi-Task Learning for Financial Sentiment Analysis | 按原文的任务、数据和实验设置解释结果。<br>Interpret results within the original task, data and experimental setting. |

<!-- task-summary:end -->

## Subtopic statistics / 子方向统计

| Subtopic | Papers |
|---|---:|
| News and Social Media Sentiment / 新闻与社交媒体情感 | 2 |
| Investor Sentiment / 投资者情绪 | 0 |
| Report and Earnings-Call Tone / 财报及电话会议语调 | 2 |
| Entity- and Aspect-Based Sentiment / 面向实体与方面的情感 | 0 |
| Financial Stance and Opinion Detection / 金融立场与观点识别 | 1 |
| Sentiment Dynamics and Market Effects / 情绪变化与市场影响 | 0 |

## Full paper list / 完整论文列表

| Year | Venue | Paper | Scope | Primary topic | Subtopics | Methods | Resources |
|---|---|---|---|---|---|---|---|
| 2026 | ACL | [Cross-Cultural Transfer of Emoji Semantics and Sentiment in Financial Social Media](../finance_notes/2026.findings-acl.1106.md) | core | Financial Sentiment / 金融情感 | News and Social Media Sentiment / 新闻与社交媒体情感 |  | [PDF](../../pdfs/ACL/2026/2026.findings-acl.1106.pdf) |
| 2026 | ACL | [Op-Fed: Opinion, Stance, and Monetary Policy Annotations on FOMC Transcripts Using Active Learning](../finance_notes/2026.findings-acl.32.md) | core | Financial Evaluation / 金融评测 | General Sequence Forecasting / 通用序列预测; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Report and Earnings-Call Tone / 财报及电话会议语调; Financial Stance and Opinion Detection / 金融立场与观点识别; Report and Disclosure Understanding / 财报与公告理解 | Language Models & LLM / 语言模型与LLM; Uncertainty & Robustness / 不确定性与鲁棒性 | [PDF](../../pdfs/ACL/2026/2026.findings-acl.32.pdf) |
| 2026 | ACL | [Uncovering Currency Bias and Syntax Gap in Text Embedding Models](../finance_notes/2026.findings-acl.2118.md) | core | Financial Evaluation / 金融评测 | Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Reliability, Safety and Fairness Evaluation / 可靠性、安全与公平性评测; Financial Semantic Matching and Ranking / 金融语义匹配与排序; Financial Model and Agent Safety / 金融模型及智能体安全 | Fairness & Recourse / 公平性与算法追索; Representation Learning / 表征学习 | [PDF](../../pdfs/ACL/2026/2026.findings-acl.2118.pdf) |
| 2026 | EMNLP | [Bias Before the Model: Detecting and Removing Cognitive Bias Triggers in Financial Text](../finance_notes/2026.findings-emnlp.1257.md) | core | Financial Evaluation / 金融评测 | Financial Model and Agent Safety / 金融模型及智能体安全; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Reliability, Safety and Fairness Evaluation / 可靠性、安全与公平性评测 | Language Models & LLM / 语言模型与LLM; Uncertainty & Robustness / 不确定性与鲁棒性 | [PDF](../../pdfs/EMNLP/2026/2026.findings-emnlp.1257.pdf) |
| 2026 | EMNLP | [DRNash: Efficient and Robust Multi-Task Learning for Financial Sentiment Analysis](../finance_notes/2026.findings-emnlp.137.md) | core | Financial Sentiment / 金融情感 | Report and Earnings-Call Tone / 财报及电话会议语调; Report and Disclosure Understanding / 财报与公告理解 | Language Models & LLM / 语言模型与LLM; Uncertainty & Robustness / 不确定性与鲁棒性; Optimization & Numerical Methods / 优化与数值方法 | [PDF](../../pdfs/EMNLP/2026/2026.findings-emnlp.137.pdf) |
| 2021 | ACL | [Trade the Event: Corporate Events Detection for News-Based Event-Driven Trading](../finance_notes/2021.findings-acl.186.md) | core | Financial Decision Making / 金融决策 | Trading Strategies and Buy/Sell Decisions / 交易策略与买卖决策; Stock Price and Return Prediction / 股票价格与收益预测; News and Social Media Sentiment / 新闻与社交媒体情感; Corporate Financing and Cash Management / 企业融资及现金管理决策; Financial Event Detection and Linking / 金融事件识别与关联 |  | [PDF](../../pdfs/ACL/2021/2021.findings-acl.186.pdf) |
