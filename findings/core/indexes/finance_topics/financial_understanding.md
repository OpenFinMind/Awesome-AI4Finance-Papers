# Financial Understanding / 金融理解

Extract, interpret, summarize and verify financial language, reports, charts, invoices and accounting records. / 金融文本、财报、图表、票据及会计记录的抽取、解释、摘要与核验。

26 Findings long papers. Topic memberships can overlap.

[All topics](../ai_for_finance.md) · [Classification definitions](../finance_taxonomy.md) · [CSV](financial_understanding.csv) · [Excel](../../finance_catalog.xlsx)

<!-- task-summary:start -->

## Research summary / 研究总结

**Financial Understanding / 金融理解 · Findings / Core**

2026-11-20 · 26 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 关注事实、实体、关系、事件与文档结构的提取和解释，也包括有证据支持的摘要及报告生成。文档版面理解与金融语义理解需要分别识别。

**当前收录与方法。** 本页仅总结 Findings / core 中的论文。当前较常见的子分类：Report and Disclosure Understanding / 财报与公告理解 (12); Table, Chart and Document Understanding / 表格、图表及文档理解 (6); Entity and Relation Extraction / 实体与关系抽取 (5); Financial Event Detection and Linking / 金融事件识别与关联 (2); Financial Text Classification / 金融文本分类 (2)。已标注的方法：Language Models & LLM / 语言模型与LLM (18); Uncertainty & Robustness / 不确定性与鲁棒性 (5); Multimodal Learning / 多模态学习 (4); Retrieval & RAG / 检索与RAG (3); Causal Learning / 因果学习 (2)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 关注结构提取、数值忠实性、证据覆盖及版面变化。 代表论文的摘要、金融关联证据及原文链接见 [1](../finance_notes/2025.findings-emnlp.1405.md) · [2](../finance_notes/2023.findings-emnlp.26.md) · [3](../finance_notes/2023.findings-emnlp.774.md) · [4](../finance_notes/2021.findings-acl.58.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 连接结构提取、数值一致性和跨文档事实核验，检验版式、语言和报告规则变化带来的影响。

### English

**Problem and subdirections.** This task extracts and interprets facts, entities, relations, events and document structure, including evidence-grounded summaries and reports. Layout understanding and financial semantics need separate treatment.

**Current coverage and methods.** This page covers only Findings / core. Frequent subcategories: Report and Disclosure Understanding / 财报与公告理解 (12); Table, Chart and Document Understanding / 表格、图表及文档理解 (6); Entity and Relation Extraction / 实体与关系抽取 (5); Financial Event Detection and Linking / 金融事件识别与关联 (2); Financial Text Classification / 金融文本分类 (2). Recorded methods: Language Models & LLM / 语言模型与LLM (18); Uncertainty & Robustness / 不确定性与鲁棒性 (5); Multimodal Learning / 多模态学习 (4); Retrieval & RAG / 检索与RAG (3); Causal Learning / 因果学习 (2). Counts overlap and are not performance rankings.

**Data and evaluation.** Measure structural extraction, numerical faithfulness, evidence coverage and layout shift. Representative abstracts, financial evidence and original sources are linked at [1](../finance_notes/2025.findings-emnlp.1405.md) · [2](../finance_notes/2023.findings-emnlp.26.md) · [3](../finance_notes/2023.findings-emnlp.774.md) · [4](../finance_notes/2021.findings-acl.58.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Connect structural extraction, numerical consistency and cross-document verification, testing shifts in layouts, languages and reporting rules.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. KAHAN: Knowledge-Augmented Hierarchical Analysis and Narration for Financial Data Narration](../finance_notes/2025.findings-emnlp.1405.md) · EMNLP 2025 | 知识增强的层级表格分析及叙述<br>Knowledge-augmented hierarchical tabular analysis and narration | 事实性和叙述质量应分别衡量<br>Measure factuality separately from narrative quality |
| [2. CR-COPEC: Causal Rationale of Corporate Performance Changes to learn from Financial Reports](../finance_notes/2023.findings-emnlp.26.md) · EMNLP 2023 | 标注财报中业绩变化的原因句<br>Annotate performance-change rationale sentences in filings | 原因表述抽取不等于因果效应识别<br>Extracting causal narratives is not causal-effect identification |
| [3. EconBERTa: Towards Robust Extraction of Named Entities in Economics](../finance_notes/2023.findings-emnlp.774.md) · EMNLP 2023 | 经济文献预训练与专家实体识别数据<br>Economics pretraining and expert entity annotations | 长实体和未见词性组合影响迁移<br>Long entities and unseen syntactic patterns affect transfer |
| [4. A Dialogue-based Information Extraction System for Medical Insurance Assessment](../finance_notes/2021.findings-acl.58.md) · ACL 2021 | 对话抽取辅助医疗保险评估及报告<br>Dialogue extraction assists medical-insurance assessment and reports | 效率证据依赖原业务流程和人工协作<br>Efficiency evidence depends on workflow and human collaboration |

<!-- task-summary:end -->

## Subtopic statistics / 子方向统计

| Subtopic | Papers |
|---|---:|
| Entity and Relation Extraction / 实体与关系抽取 | 5 |
| Financial Event Detection and Linking / 金融事件识别与关联 | 2 |
| Financial Text Classification / 金融文本分类 | 2 |
| Report and Disclosure Understanding / 财报与公告理解 | 12 |
| Table, Chart and Document Understanding / 表格、图表及文档理解 | 6 |
| Financial Summarization and Report Generation / 金融摘要与报告生成 | 2 |

## Full paper list / 完整论文列表

| Year | Venue | Paper | Scope | Primary topic | Subtopics | Methods | Resources |
|---|---|---|---|---|---|---|---|
| 2026 | ACL | [Analyze Like a Venture Capitalist: Information-Gain and Knowledge Enhanced Graph Reasoning for Startup Success Prediction](../finance_notes/2026.findings-acl.1555.md) | core | Valuation Prediction / 估值预测 | Stock Price and Return Prediction / 股票价格与收益预测; Risk-Return and Multi-Objective Optimization / 风险收益及多目标优化 | Language Models & LLM / 语言模型与LLM; Graph Learning / 图学习 | [PDF](../../pdfs/ACL/2026/2026.findings-acl.1555.pdf) |
| 2026 | ACL | [Cogito: A Cognitive Agentic Framework Driven by Dynamic Graph of Thoughts for Financial Report Generation](../finance_notes/2026.findings-acl.430.md) | core | Financial Decision Making / 金融决策 | Financial Summarization and Report Generation / 金融摘要与报告生成; Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策; Report and Disclosure Understanding / 财报与公告理解 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/ACL/2026/2026.findings-acl.430.pdf) |
| 2026 | ACL | [Cross-Cultural Transfer of Emoji Semantics and Sentiment in Financial Social Media](../finance_notes/2026.findings-acl.1106.md) | core | Financial Sentiment / 金融情感 | News and Social Media Sentiment / 新闻与社交媒体情感 |  | [PDF](../../pdfs/ACL/2026/2026.findings-acl.1106.pdf) |
| 2026 | ACL | [Finch: Benchmarking Finance & Accounting across Spreadsheet-Centric Enterprise Workflows](../finance_notes/2026.findings-acl.523.md) | core | Financial Evaluation / 金融评测 | Report and Disclosure Understanding / 财报与公告理解; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Financial Knowledge and Professional Evaluation / 金融知识与专业能力评测; Table, Chart and Document Understanding / 表格、图表及文档理解 | Language Models & LLM / 语言模型与LLM; Retrieval & RAG / 检索与RAG | [PDF](../../pdfs/ACL/2026/2026.findings-acl.523.pdf) |
| 2026 | ACL | [FinMRAGBench: A Realistic and Complex Benchmark for Multi-Modal RAG in Financial Document Analysis](../finance_notes/2026.findings-acl.187.md) | core | Financial Evaluation / 金融评测 | Numerical Calculation and Program Reasoning / 数值计算与程序推理; Financial Semantic Matching and Ranking / 金融语义匹配与排序; Evidence Retrieval and Reranking for Financial RAG / 金融 RAG 的证据检索与重排序; Table, Chart and Document Understanding / 表格、图表及文档理解; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Financial Understanding and Multimodal Evaluation / 金融理解及多模态评测; Financial Document and Disclosure Retrieval / 金融文档与公告检索 | Multimodal Learning / 多模态学习; Retrieval & RAG / 检索与RAG | [PDF](../../pdfs/ACL/2026/2026.findings-acl.187.pdf) |
| 2026 | ACL | [Op-Fed: Opinion, Stance, and Monetary Policy Annotations on FOMC Transcripts Using Active Learning](../finance_notes/2026.findings-acl.32.md) | core | Financial Evaluation / 金融评测 | General Sequence Forecasting / 通用序列预测; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Report and Earnings-Call Tone / 财报及电话会议语调; Financial Stance and Opinion Detection / 金融立场与观点识别; Report and Disclosure Understanding / 财报与公告理解 | Language Models & LLM / 语言模型与LLM; Uncertainty & Robustness / 不确定性与鲁棒性 | [PDF](../../pdfs/ACL/2026/2026.findings-acl.32.pdf) |
| 2026 | ACL | [SAE-FiRE: Enhancing Earnings Surprise Predictions Through Sparse Autoencoder Feature Selection](../finance_notes/2026.findings-acl.265.md) | core | Valuation Prediction / 估值预测 | Report and Disclosure Understanding / 财报与公告理解; Earnings, Revenue and Fundamental Prediction / 盈利、营收与基本面预测 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/ACL/2026/2026.findings-acl.265.pdf) |
| 2026 | ACL | [SEC-FinTables: Evaluating Large Language Models for Detecting Logical Inconsistencies on Tabular Data](../finance_notes/2026.findings-acl.764.md) | core | Financial Evaluation / 金融评测 | Table, Chart and Document Understanding / 表格、图表及文档理解; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Financial Understanding and Multimodal Evaluation / 金融理解及多模态评测; Evaluation Protocols and Metrics / 评测协议与指标 | Language Models & LLM / 语言模型与LLM; Tabular Learning / 表格学习 | [PDF](../../pdfs/ACL/2026/2026.findings-acl.764.pdf) |
| 2026 | EMNLP | [CrossAlpha: An Annual-Report Benchmark for Cross-Market Factor Research with LLM Agents](../finance_notes/2026.findings-emnlp.914.md) | core | Financial Evaluation / 金融评测 | Report and Disclosure Understanding / 财报与公告理解; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Financial Decision and Agent Evaluation / 金融决策与智能体评测; Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/EMNLP/2026/2026.findings-emnlp.914.pdf) |
| 2026 | EMNLP | [DRNash: Efficient and Robust Multi-Task Learning for Financial Sentiment Analysis](../finance_notes/2026.findings-emnlp.137.md) | core | Financial Sentiment / 金融情感 | Report and Earnings-Call Tone / 财报及电话会议语调; Report and Disclosure Understanding / 财报与公告理解 | Language Models & LLM / 语言模型与LLM; Uncertainty & Robustness / 不确定性与鲁棒性; Optimization & Numerical Methods / 优化与数值方法 | [PDF](../../pdfs/EMNLP/2026/2026.findings-emnlp.137.pdf) |
| 2026 | EMNLP | [E2A-Bench: Benchmarking Evidence-to-Action Reliability in Financial Chart Reasoning](../finance_notes/2026.findings-emnlp.450.md) | core | Financial Evaluation / 金融评测 | Table, Chart and Document Understanding / 表格、图表及文档理解; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Financial Understanding and Multimodal Evaluation / 金融理解及多模态评测; Reliability, Safety and Fairness Evaluation / 可靠性、安全与公平性评测 | Language Models & LLM / 语言模型与LLM; Uncertainty & Robustness / 不确定性与鲁棒性; Multimodal Learning / 多模态学习 | [PDF](../../pdfs/EMNLP/2026/2026.findings-emnlp.450.pdf) |
| 2026 | EMNLP | [FinAcumen: Financial Multimodal Reasoning via Self-Evolving Experience Memory Harness](../finance_notes/2026.findings-emnlp.2357.md) | core | Financial Question Answering / 金融问答 | Numerical Calculation and Program Reasoning / 数值计算与程序推理; Table, Chart and Document Understanding / 表格、图表及文档理解; Chart and Multimodal QA / 图表及多模态问答 | Language Models & LLM / 语言模型与LLM; Uncertainty & Robustness / 不确定性与鲁棒性; Multimodal Learning / 多模态学习; Retrieval & RAG / 检索与RAG | [PDF](../../pdfs/EMNLP/2026/2026.findings-emnlp.2357.pdf) |
| 2026 | EMNLP | [FinBalance: A Multi-Document Accounting Reconciliation Benchmark](../finance_notes/2026.findings-emnlp.675.md) | core | Financial Evaluation / 金融评测 | Report and Disclosure Understanding / 财报与公告理解; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Financial Knowledge and Professional Evaluation / 金融知识与专业能力评测; Financial Understanding and Multimodal Evaluation / 金融理解及多模态评测; Table, Chart and Document Understanding / 表格、图表及文档理解 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/EMNLP/2026/2026.findings-emnlp.675.pdf) |
| 2026 | EMNLP | [ReimburseBench: Benchmarking LMMs as Full-Workflow Auditors for Financial Internal Control](../finance_notes/2026.findings-emnlp.821.md) | core | Financial Evaluation / 金融评测 | Report and Disclosure Understanding / 财报与公告理解; Financial Datasets and Task Benchmarks / 金融数据集与任务基准 |  | [PDF](../../pdfs/EMNLP/2026/2026.findings-emnlp.821.pdf) |
| 2026 | EMNLP | [Scope3Trace: Evidence-Based Identification and Extraction of Scope 3 GHG Emissions from Sustainability Reports](../finance_notes/2026.findings-emnlp.1167.md) | core | Sustainable Finance / 可持续金融 | Report and Disclosure Understanding / 财报与公告理解; Sustainability Disclosure and Greenwashing / 可持续披露与漂绿识别; ESG Extraction and Evaluation / ESG 信息抽取与评价; Entity and Relation Extraction / 实体与关系抽取 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/EMNLP/2026/2026.findings-emnlp.1167.pdf) |
| 2026 | EMNLP | [UniFinEval: Towards Unified Evaluation of Financial Multimodal Models across Text, Images and Videos](../finance_notes/2026.findings-emnlp.2075.md) | core | Financial Evaluation / 金融评测 | Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Financial Understanding and Multimodal Evaluation / 金融理解及多模态评测; Evaluation Protocols and Metrics / 评测协议与指标 | Language Models & LLM / 语言模型与LLM; Multimodal Learning / 多模态学习 | [PDF](../../pdfs/EMNLP/2026/2026.findings-emnlp.2075.pdf) |
| 2025 | ACL | [MFinMeeting: A Multilingual, Multi-Sector, and Multi-Task Financial Meeting Understanding Evaluation Dataset](../finance_notes/2025.findings-acl.14.md) | core | Financial Evaluation / 金融评测 | Financial Text Classification / 金融文本分类; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Financial Understanding and Multimodal Evaluation / 金融理解及多模态评测; Evaluation Protocols and Metrics / 评测协议与指标 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/ACL/2025/2025.findings-acl.14.pdf) |
| 2025 | ACL | [Same Company, Same Signal: The Role of Identity in Earnings Call Transcripts](../finance_notes/2025.findings-acl.946.md) | core | Valuation Prediction / 估值预测 | Report and Disclosure Understanding / 财报与公告理解; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Earnings, Revenue and Fundamental Prediction / 盈利、营收与基本面预测; Entity and Relation Extraction / 实体与关系抽取 |  | [PDF](../../pdfs/ACL/2025/2025.findings-acl.946.pdf) |
| 2025 | EMNLP | [KAHAN: Knowledge-Augmented Hierarchical Analysis and Narration for Financial Data Narration](../finance_notes/2025.findings-emnlp.1405.md) | core | Financial Understanding / 金融理解 | Financial Summarization and Report Generation / 金融摘要与报告生成 | Language Models & LLM / 语言模型与LLM; Tabular Learning / 表格学习 | [PDF](../../pdfs/EMNLP/2025/2025.findings-emnlp.1405.pdf) |
| 2024 | EMNLP | [OEE-CFC: A Dataset for Open Event Extraction from Chinese Financial Commentary](../finance_notes/2024.findings-emnlp.256.md) | core | Financial Evaluation / 金融评测 | Entity and Relation Extraction / 实体与关系抽取; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Financial Event Detection and Linking / 金融事件识别与关联 |  | [PDF](../../pdfs/EMNLP/2024/2024.findings-emnlp.256.pdf) |
| 2023 | ACL | [Forecasting Earnings Surprises from Conference Call Transcripts](../finance_notes/2023.findings-acl.520.md) | core | Valuation Prediction / 估值预测 | Report and Disclosure Understanding / 财报与公告理解; Earnings, Revenue and Fundamental Prediction / 盈利、营收与基本面预测 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/ACL/2023/2023.findings-acl.520.pdf) |
| 2023 | EMNLP | [CR-COPEC: Causal Rationale of Corporate Performance Changes to learn from Financial Reports](../finance_notes/2023.findings-emnlp.26.md) | core | Financial Understanding / 金融理解 | Report and Disclosure Understanding / 财报与公告理解 | Causal Learning / 因果学习 | [PDF](../../pdfs/EMNLP/2023/2023.findings-emnlp.26.pdf) |
| 2023 | EMNLP | [EconBERTa: Towards Robust Extraction of Named Entities in Economics](../finance_notes/2023.findings-emnlp.774.md) | core | Financial Understanding / 金融理解 | Entity and Relation Extraction / 实体与关系抽取 | Language Models & LLM / 语言模型与LLM; Causal Learning / 因果学习; Uncertainty & Robustness / 不确定性与鲁棒性 | [PDF](../../pdfs/EMNLP/2023/2023.findings-emnlp.774.pdf) |
| 2021 | ACL | [A Dialogue-based Information Extraction System for Medical Insurance Assessment](../finance_notes/2021.findings-acl.58.md) | core | Financial Understanding / 金融理解 | Entity and Relation Extraction / 实体与关系抽取 |  | [PDF](../../pdfs/ACL/2021/2021.findings-acl.58.pdf) |
| 2021 | ACL | [Trade the Event: Corporate Events Detection for News-Based Event-Driven Trading](../finance_notes/2021.findings-acl.186.md) | core | Financial Decision Making / 金融决策 | Trading Strategies and Buy/Sell Decisions / 交易策略与买卖决策; Stock Price and Return Prediction / 股票价格与收益预测; News and Social Media Sentiment / 新闻与社交媒体情感; Corporate Financing and Cash Management / 企业融资及现金管理决策; Financial Event Detection and Linking / 金融事件识别与关联 |  | [PDF](../../pdfs/ACL/2021/2021.findings-acl.186.pdf) |
| 2021 | EMNLP | [Classification and Geotemporal Analysis of Quality-of-Life Issues in Tenant Reviews](../finance_notes/2021.findings-emnlp.217.md) | core | Financial Understanding / 金融理解 | Enterprise and Equity Valuation / 企业价值与股权估值; Financial Text Classification / 金融文本分类 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/EMNLP/2021/2021.findings-emnlp.217.pdf) |
