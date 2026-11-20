# Financial Sentiment / 金融情感

Financial sentiment, stance, tone and emotion as the prediction target; downstream return prediction stays valuation prediction. / 以金融情感、立场、语气与情绪为目标；下游收益预测仍归估值预测。

10 Main long papers. Topic memberships can overlap.

[All topics](../ai_for_finance.md) · [Classification definitions](../finance_taxonomy.md) · [CSV](financial_sentiment.csv) · [Excel](../../finance_catalog.xlsx)

<!-- task-summary:start -->

## Research summary / 研究总结

**Financial Sentiment / 金融情感 · Main / Application**

2026-11-20 · 10 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 目标是金融文本中的情感、语调、立场及其对象。公司、事件和方面粒度不同；情感预测与利用情感预测股票收益属于不同任务。

**当前收录与方法。** 本页仅总结 Main / application 中的论文。当前较常见的子分类：News and Social Media Sentiment / 新闻与社交媒体情感 (9); Financial Stance and Opinion Detection / 金融立场与观点识别 (2); Report and Earnings-Call Tone / 财报及电话会议语调 (1)。已标注的方法：Language Models & LLM / 语言模型与LLM (5); Representation Learning / 表征学习 (4); Uncertainty & Robustness / 不确定性与鲁棒性 (2); Fairness & Recourse / 公平性与算法追索 (1); Retrieval & RAG / 检索与RAG (1)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 检查标注口径、时效性、领域与语言迁移，区分情感准确率和收益效果。 代表论文的摘要、金融关联证据及原文链接见 [1](../finance_notes/2025.emnlp-main.486.md) · [2](../finance_notes/2023.acl-long.747.md) · [3](../finance_notes/2023.emnlp-main.848.md) · [4](../finance_notes/aaai-2022-21305.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 研究标签口径、文化语言差异和跨期漂移，避免以市场收益倒推情感标签正确性。

### English

**Problem and subdirections.** Targets are sentiment, tone, stance and their financial subjects. Company, event and aspect granularity differ; predicting sentiment and using sentiment to predict returns are distinct tasks.

**Current coverage and methods.** This page covers only Main / application. Frequent subcategories: News and Social Media Sentiment / 新闻与社交媒体情感 (9); Financial Stance and Opinion Detection / 金融立场与观点识别 (2); Report and Earnings-Call Tone / 财报及电话会议语调 (1). Recorded methods: Language Models & LLM / 语言模型与LLM (5); Representation Learning / 表征学习 (4); Uncertainty & Robustness / 不确定性与鲁棒性 (2); Fairness & Recourse / 公平性与算法追索 (1); Retrieval & RAG / 检索与RAG (1). Counts overlap and are not performance rankings.

**Data and evaluation.** Check annotation policy, temporal drift and domain/language transfer; separate sentiment accuracy from returns. Representative abstracts, financial evidence and original sources are linked at [1](../finance_notes/2025.emnlp-main.486.md) · [2](../finance_notes/2023.acl-long.747.md) · [3](../finance_notes/2023.emnlp-main.848.md) · [4](../finance_notes/aaai-2022-21305.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Study annotation policy, cultural and language differences and temporal drift without treating market returns as proof of sentiment-label correctness.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. Generative or Discriminative? Revisiting Text Classification in the Era of Transformers](../finance_notes/2025.emnlp-main.486.md) · EMNLP 2025 | 研究主题：Generative or Discriminative? Revisiting Text Classification in the Era of Transformers<br>Research topic: Generative or Discriminative? Revisiting Text Classification in the Era of Transformers | 按原文的任务、数据和实验设置解释结果。<br>Interpret results within the original task, data and experimental setting. |
| [2. C-STANCE: A Large Dataset for Chinese Zero-Shot Stance Detection](../finance_notes/2023.acl-long.747.md) · ACL 2023 | 研究主题：C-STANCE: A Large Dataset for Chinese Zero-Shot Stance Detection<br>Research topic: C-STANCE: A Large Dataset for Chinese Zero-Shot Stance Detection | 按原文的任务、数据和实验设置解释结果。<br>Interpret results within the original task, data and experimental setting. |
| [3. The Sentiment Problem: A Critical Survey towards Deconstructing Sentiment Analysis](../finance_notes/2023.emnlp-main.848.md) · EMNLP 2023 | 研究主题：The Sentiment Problem: A Critical Survey towards Deconstructing Sentiment Analysis<br>Research topic: The Sentiment Problem: A Critical Survey towards Deconstructing Sentiment Analysis | 按原文的任务、数据和实验设置解释结果。<br>Interpret results within the original task, data and experimental setting. |
| [4. Fortunately, Discourse Markers Can Enhance Language Models for Sentiment Analysis](../finance_notes/aaai-2022-21305.md) · AAAI 2022 | 研究主题：Fortunately, Discourse Markers Can Enhance Language Models for Sentiment Analysis<br>Research topic: Fortunately, Discourse Markers Can Enhance Language Models for Sentiment Analysis | 按原文的任务、数据和实验设置解释结果。<br>Interpret results within the original task, data and experimental setting. |

<!-- task-summary:end -->

## Subtopic statistics / 子方向统计

| Subtopic | Papers |
|---|---:|
| News and Social Media Sentiment / 新闻与社交媒体情感 | 9 |
| Investor Sentiment / 投资者情绪 | 0 |
| Report and Earnings-Call Tone / 财报及电话会议语调 | 1 |
| Entity- and Aspect-Based Sentiment / 面向实体与方面的情感 | 0 |
| Financial Stance and Opinion Detection / 金融立场与观点识别 | 2 |
| Sentiment Dynamics and Market Effects / 情绪变化与市场影响 | 0 |

## Full paper list / 完整论文列表

| Year | Venue | Paper | Scope | Primary topic | Subtopics | Methods | Resources |
|---|---|---|---|---|---|---|---|
| 2025 | EMNLP | [Generative or Discriminative? Revisiting Text Classification in the Era of Transformers](../finance_notes/2025.emnlp-main.486.md) | application | Financial Sentiment / 金融情感 | News and Social Media Sentiment / 新闻与社交媒体情感; Financial Text Classification / 金融文本分类; Financial Summarization and Report Generation / 金融摘要与报告生成 | Language Models & LLM / 语言模型与LLM; Diffusion & Flow / 扩散与流模型; Generative Modeling / 生成建模; Transformer / Transformer模型; Uncertainty & Robustness / 不确定性与鲁棒性 | [PDF](../../pdfs/EMNLP/2025/2025.emnlp-main.486__Generative_or_Discriminative_Revisiting_Text_Classification_in_the_Era_of_Transformers.pdf) |
| 2024 | ICLR | [SetCSE: Set Operations using Contrastive Learning of Sentence Embeddings](../finance_notes/iclr-2024-zEHGSN8Hy8.md) | application | Financial Services / 金融服务 | News and Social Media Sentiment / 新闻与社交媒体情感; Customer Support and Business Consultation / 智能客服与业务咨询; Report and Disclosure Understanding / 财报与公告理解; Report and Earnings-Call Tone / 财报及电话会议语调 | Retrieval & RAG / 检索与RAG; Representation Learning / 表征学习 | [PDF](../../pdfs/ICLR/2024/iclr-2024-zEHGSN8Hy8__SetCSE_Set_Operations_using_Contrastive_Learning_of_Sentence_Embeddings.pdf) |
| 2023 | ACL | [C-STANCE: A Large Dataset for Chinese Zero-Shot Stance Detection](../finance_notes/2023.acl-long.747.md) | application | Financial Sentiment / 金融情感 | Financial Stance and Opinion Detection / 金融立场与观点识别 |  | [PDF](../../pdfs/ACL/2023/2023.acl-long.747__C_STANCE_A_Large_Dataset_for_Chinese_Zero_Shot_Stance_Detection.pdf) |
| 2023 | ACL | [Document-Level Multi-Event Extraction with Event Proxy Nodes and Hausdorff Distance Minimization](../finance_notes/2023.acl-long.563.md) | application | Financial Understanding / 金融理解 | Financial Event Detection and Linking / 金融事件识别与关联; Entity and Relation Extraction / 实体与关系抽取; News and Social Media Sentiment / 新闻与社交媒体情感; Table, Chart and Document Understanding / 表格、图表及文档理解; Financial Stance and Opinion Detection / 金融立场与观点识别 |  | [PDF](../../pdfs/ACL/2023/2023.acl-long.563__Document_Level_Multi_Event_Extraction_with_Event_Proxy_Nodes_and_Hausdorff_Distance_Minimization.pdf) |
| 2023 | EMNLP | [AdaSent: Efficient Domain-Adapted Sentence Embeddings for Few-Shot Classification](../finance_notes/2023.emnlp-main.208.md) | application | Financial Understanding / 金融理解 | News and Social Media Sentiment / 新闻与社交媒体情感; Financial Text Classification / 金融文本分类 | Language Models & LLM / 语言模型与LLM; Uncertainty & Robustness / 不确定性与鲁棒性; Representation Learning / 表征学习 | [PDF](../../pdfs/EMNLP/2023/2023.emnlp-main.208__AdaSent_Efficient_Domain_Adapted_Sentence_Embeddings_for_Few_Shot_Classification.pdf) |
| 2023 | EMNLP | [The Sentiment Problem: A Critical Survey towards Deconstructing Sentiment Analysis](../finance_notes/2023.emnlp-main.848.md) | application | Financial Sentiment / 金融情感 | News and Social Media Sentiment / 新闻与社交媒体情感 |  | [PDF](../../pdfs/EMNLP/2023/2023.emnlp-main.848__The_Sentiment_Problem_A_Critical_Survey_towards_Deconstructing_Sentiment_Analysis.pdf) |
| 2022 | AAAI | [Fortunately, Discourse Markers Can Enhance Language Models for Sentiment Analysis](../finance_notes/aaai-2022-21305.md) | application | Financial Sentiment / 金融情感 | News and Social Media Sentiment / 新闻与社交媒体情感 | Language Models & LLM / 语言模型与LLM; Representation Learning / 表征学习 | [PDF](../../pdfs/AAAI/2022/aaai-2022-21305__Fortunately_Discourse_Markers_Can_Enhance_Language_Models_for_Sentiment_Analysis.pdf) |
| 2022 | EMNLP | [Ground-Truth Labels Matter: A Deeper Look into Input-Label Demonstrations](../finance_notes/2022.emnlp-main.155.md) | application | Financial Sentiment / 金融情感 | News and Social Media Sentiment / 新闻与社交媒体情感 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/EMNLP/2022/2022.emnlp-main.155__Ground_Truth_Labels_Matter_A_Deeper_Look_into_Input_Label_Demonstrations.pdf) |
| 2022 | ICML | [Active fairness auditing](../finance_notes/icml-2022-17204.md) | application | Financial Risk / 金融风险 | News and Social Media Sentiment / 新闻与社交媒体情感; Credit Risk and Default Prediction / 信用风险与违约预测 | Fairness & Recourse / 公平性与算法追索 | [PDF](../../pdfs/ICML/2022/icml-2022-17204__Active_fairness_auditing.pdf) |
| 2021 | ACL | [ChineseBERT: Chinese Pretraining Enhanced by Glyph and Pinyin Information](../finance_notes/2021.acl-long.161.md) | application | Financial Understanding / 金融理解 | Financial Text Classification / 金融文本分类; News and Social Media Sentiment / 新闻与社交媒体情感 | Language Models & LLM / 语言模型与LLM; Representation Learning / 表征学习 | [PDF](../../pdfs/ACL/2021/2021.acl-long.161__ChineseBERT_Chinese_Pretraining_Enhanced_by_Glyph_and_Pinyin_Information.pdf) |
