# Financial Sentiment / 金融情感

Financial sentiment, stance, tone and emotion as the prediction target; downstream return prediction stays valuation prediction. / 以金融情感、立场、语气与情绪为目标；下游收益预测仍归估值预测。

10 Main long papers. Topic memberships can overlap.

[All topics](../ai_for_finance.md) · [Classification definitions](../finance_taxonomy.md) · [CSV](financial_sentiment.csv) · [Excel](../../finance_catalog.xlsx)

<!-- task-summary:start -->

## Research summary / 研究总结

**Financial Sentiment / 金融情感 · Main / Core**

2026-11-20 · 10 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 目标是金融文本中的情感、语调、立场及其对象。公司、事件和方面粒度不同；情感预测与利用情感预测股票收益属于不同任务。

**当前收录与方法。** 本页仅总结 Main / core 中的论文。当前较常见的子分类：News and Social Media Sentiment / 新闻与社交媒体情感 (7); Report and Earnings-Call Tone / 财报及电话会议语调 (4); Financial Stance and Opinion Detection / 金融立场与观点识别 (2); Entity- and Aspect-Based Sentiment / 面向实体与方面的情感 (1)。已标注的方法：Language Models & LLM / 语言模型与LLM (4); Uncertainty & Robustness / 不确定性与鲁棒性 (3); Representation Learning / 表征学习 (2); Retrieval & RAG / 检索与RAG (1); Causal Learning / 因果学习 (1)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 检查标注口径、时效性、领域与语言迁移，区分情感准确率和收益效果。 代表论文的摘要、金融关联证据及原文链接见 [1](../finance_notes/2024.acl-long.402.md) · [2](../finance_notes/2023.emnlp-main.65.md) · [3](../finance_notes/2023.acl-long.412.md) · [4](../finance_notes/2022.acl-long.281.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 研究标签口径、文化语言差异和跨期漂移，避免以市场收益倒推情感标签正确性。

### English

**Problem and subdirections.** Targets are sentiment, tone, stance and their financial subjects. Company, event and aspect granularity differ; predicting sentiment and using sentiment to predict returns are distinct tasks.

**Current coverage and methods.** This page covers only Main / core. Frequent subcategories: News and Social Media Sentiment / 新闻与社交媒体情感 (7); Report and Earnings-Call Tone / 财报及电话会议语调 (4); Financial Stance and Opinion Detection / 金融立场与观点识别 (2); Entity- and Aspect-Based Sentiment / 面向实体与方面的情感 (1). Recorded methods: Language Models & LLM / 语言模型与LLM (4); Uncertainty & Robustness / 不确定性与鲁棒性 (3); Representation Learning / 表征学习 (2); Retrieval & RAG / 检索与RAG (1); Causal Learning / 因果学习 (1). Counts overlap and are not performance rankings.

**Data and evaluation.** Check annotation policy, temporal drift and domain/language transfer; separate sentiment accuracy from returns. Representative abstracts, financial evidence and original sources are linked at [1](../finance_notes/2024.acl-long.402.md) · [2](../finance_notes/2023.emnlp-main.65.md) · [3](../finance_notes/2023.acl-long.412.md) · [4](../finance_notes/2022.acl-long.281.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Study annotation policy, cultural and language differences and temporal drift without treating market returns as proof of sentiment-label correctness.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. EFSA: Towards Event-Level Financial Sentiment Analysis](../finance_notes/2024.acl-long.402.md) · ACL 2024 | 联合输出公司、行业、事件及情绪五元组<br>Jointly output company, industry, event and sentiment quintuples | 事件粒度和语言范围限定泛化结论<br>Event granularity and language scope bound generalization |
| [2. Predict the Future from the Past? On the Temporal Data Distribution Shift in Financial Sentiment Classifications](../finance_notes/2023.emnlp-main.65.md) · EMNLP 2023 | 研究金融情绪的时间分布变化及适应<br>Study temporal sentiment shifts and adaptation | 随机切分难以反映时间漂移<br>Random splits do not adequately reflect temporal drift |
| [3. When Does Aggregating Multiple Skills with Multi-Task Learning Work? A Case Study in Financial NLP](../finance_notes/2023.acl-long.412.md) · ACL 2023 | 研究主题：When Does Aggregating Multiple Skills with Multi-Task Learning Work? A Case Study in Financial NLP<br>Research topic: When Does Aggregating Multiple Skills with Multi-Task Learning Work? A Case Study in Financial NLP | 按原文的任务、数据和实验设置解释结果。<br>Interpret results within the original task, data and experimental setting. |
| [4. Incorporating Stock Market Signals for Twitter Stance Detection](../finance_notes/2022.acl-long.281.md) · ACL 2022 | 研究主题：Incorporating Stock Market Signals for Twitter Stance Detection<br>Research topic: Incorporating Stock Market Signals for Twitter Stance Detection | 按原文的任务、数据和实验设置解释结果。<br>Interpret results within the original task, data and experimental setting. |

<!-- task-summary:end -->

## Subtopic statistics / 子方向统计

| Subtopic | Papers |
|---|---:|
| News and Social Media Sentiment / 新闻与社交媒体情感 | 7 |
| Investor Sentiment / 投资者情绪 | 0 |
| Report and Earnings-Call Tone / 财报及电话会议语调 | 4 |
| Entity- and Aspect-Based Sentiment / 面向实体与方面的情感 | 1 |
| Financial Stance and Opinion Detection / 金融立场与观点识别 | 2 |
| Sentiment Dynamics and Market Effects / 情绪变化与市场影响 | 0 |

## Full paper list / 完整论文列表

| Year | Venue | Paper | Scope | Primary topic | Subtopics | Methods | Resources |
|---|---|---|---|---|---|---|---|
| 2026 | AAAI | [Interpreting Fedspeak with Confidence: A LLM-Based Uncertainty-Aware Framework Guided by Monetary Policy Transmission Paths](../finance_notes/aaai-2026-40739.md) | core | Time Series / 时间序列 | General Sequence Forecasting / 通用序列预测; News and Social Media Sentiment / 新闻与社交媒体情感 | Language Models & LLM / 语言模型与LLM; Uncertainty & Robustness / 不确定性与鲁棒性 | [PDF](../../pdfs/AAAI/2026/aaai-2026-40739__Interpreting_Fedspeak_with_Confidence_A_LLM_Based_Uncertainty_Aware_Framework_Guided_by_Monetary_Policy_Transmission_Paths.pdf) |
| 2026 | ACL | [SAHM: A Benchmark for Arabic Financial and Shari’ah-Compliant Reasoning](../finance_notes/2026.acl-long.1593.md) | core | Financial Evaluation / 金融评测 | News and Social Media Sentiment / 新闻与社交媒体情感; Numerical Calculation and Program Reasoning / 数值计算与程序推理; Financial Factual QA / 金融事实问答; Table, Chart and Document Understanding / 表格、图表及文档理解; Financial Model and Agent Safety / 金融模型及智能体安全; Financial Text Classification / 金融文本分类; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Regulatory Compliance and Violation Detection / 监管合规与违规检测 | Language Models & LLM / 语言模型与LLM; Causal Learning / 因果学习 | [PDF](../../pdfs/ACL/2026/2026.acl-long.1593__SAHM_A_Benchmark_for_Arabic_Financial_and_Shari_ah_Compliant_Reasoning.pdf) |
| 2026 | ICML | [Learning the ESG Geometry with Domain Aware Language Models](../finance_notes/icml-2026-CydNEMsNM6.md) | core | Sustainable Finance / 可持续金融 | Sequence Representation and Pattern Discovery / 序列表示与模式发现; News and Social Media Sentiment / 新闻与社交媒体情感; Sustainability Disclosure and Greenwashing / 可持续披露与漂绿识别; ESG Extraction and Evaluation / ESG 信息抽取与评价; Report and Disclosure Understanding / 财报与公告理解; Report and Earnings-Call Tone / 财报及电话会议语调 | Language Models & LLM / 语言模型与LLM; Multimodal Learning / 多模态学习; Representation Learning / 表征学习 | [Online](https://openreview.net/forum?id=CydNEMsNM6) |
| 2024 | ACL | [EFSA: Towards Event-Level Financial Sentiment Analysis](../finance_notes/2024.acl-long.402.md) | core | Financial Sentiment / 金融情感 | Entity- and Aspect-Based Sentiment / 面向实体与方面的情感; Entity and Relation Extraction / 实体与关系抽取; Financial Event Detection and Linking / 金融事件识别与关联 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/ACL/2024/2024.acl-long.402__EFSA_Towards_Event_Level_Financial_Sentiment_Analysis.pdf) |
| 2023 | ACL | [When Does Aggregating Multiple Skills with Multi-Task Learning Work? A Case Study in Financial NLP](../finance_notes/2023.acl-long.412.md) | core | Financial Sentiment / 金融情感 | Report and Earnings-Call Tone / 财报及电话会议语调; Report and Disclosure Understanding / 财报与公告理解 |  | [PDF](../../pdfs/ACL/2023/2023.acl-long.412__When_Does_Aggregating_Multiple_Skills_with_Multi_Task_Learning_Work_A_Case_Study_in_Financial_NLP.pdf) |
| 2023 | EMNLP | [Predict the Future from the Past? On the Temporal Data Distribution Shift in Financial Sentiment Classifications](../finance_notes/2023.emnlp-main.65.md) | core | Financial Sentiment / 金融情感 | News and Social Media Sentiment / 新闻与社交媒体情感; General Sequence Forecasting / 通用序列预测; Financial Text Classification / 金融文本分类 | Uncertainty & Robustness / 不确定性与鲁棒性 | [PDF](../../pdfs/EMNLP/2023/2023.emnlp-main.65__Predict_the_Future_from_the_Past_On_the_Temporal_Data_Distribution_Shift_in_Financial_Sentiment_Classific.pdf) |
| 2022 | ACL | [Incorporating Stock Market Signals for Twitter Stance Detection](../finance_notes/2022.acl-long.281.md) | core | Financial Sentiment / 金融情感 | General Sequence Forecasting / 通用序列预测; Financial Event Detection and Linking / 金融事件识别与关联; Financial Stance and Opinion Detection / 金融立场与观点识别 | Uncertainty & Robustness / 不确定性与鲁棒性 | [PDF](../../pdfs/ACL/2022/2022.acl-long.281__Incorporating_Stock_Market_Signals_for_Twitter_Stance_Detection.pdf) |
| 2020 | AAAI | [Incorporating Expert-Based Investment Opinion Signals in Stock Prediction: A Deep Learning Framework](../finance_notes/aaai-2020-5445.md) | core | Valuation Prediction / 估值预测 | Stock Price and Return Prediction / 股票价格与收益预测; News and Social Media Sentiment / 新闻与社交媒体情感; Earnings, Revenue and Fundamental Prediction / 盈利、营收与基本面预测; Report and Disclosure Understanding / 财报与公告理解; Report and Earnings-Call Tone / 财报及电话会议语调; Financial Stance and Opinion Detection / 金融立场与观点识别 |  | [PDF](../../pdfs/AAAI/2020/aaai-2020-5445__Incorporating_Expert_Based_Investment_Opinion_Signals_in_Stock_Prediction_A_Deep_Learning_Framework.pdf) |
| 2019 | ACL | [Automatic Domain Adaptation Outperforms Manual Domain Adaptation for Predicting Financial Outcomes](../finance_notes/P19-1034.md) | core | Valuation Prediction / 估值预测 | Stock Price and Return Prediction / 股票价格与收益预测; Volatility Prediction / 波动率预测; News and Social Media Sentiment / 新闻与社交媒体情感 |  | [PDF](../../pdfs/ACL/2019/P19-1034__Automatic_Domain_Adaptation_Outperforms_Manual_Domain_Adaptation_for_Predicting_Financial_Outcomes.pdf) |
| 2017 | ACL | [Volatility Prediction using Financial Disclosures Sentiments with Word Embedding-based IR Models](../finance_notes/P17-1157.md) | core | Valuation Prediction / 估值预测 | Stock Price and Return Prediction / 股票价格与收益预测; Volatility Prediction / 波动率预测; News and Social Media Sentiment / 新闻与社交媒体情感; Report and Disclosure Understanding / 财报与公告理解; Report and Earnings-Call Tone / 财报及电话会议语调 | Retrieval & RAG / 检索与RAG; Representation Learning / 表征学习 | [PDF](../../pdfs/ACL/2017/P17-1157__Volatility_Prediction_using_Financial_Disclosures_Sentiments_with_Word_Embedding_based_IR_Models.pdf) |
