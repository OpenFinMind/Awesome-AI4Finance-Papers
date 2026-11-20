# Financial Understanding / 金融理解

Extract, interpret, summarize and verify financial language, reports, charts, invoices and accounting records. / 金融文本、财报、图表、票据及会计记录的抽取、解释、摘要与核验。

21 Findings long papers. Topic memberships can overlap.

[All topics](../ai_for_finance.md) · [Classification definitions](../finance_taxonomy.md) · [CSV](financial_understanding.csv) · [Excel](../../finance_catalog.xlsx)

<!-- task-summary:start -->

## Research summary / 研究总结

**Financial Understanding / 金融理解 · Findings / Application**

2026-11-20 · 21 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 关注事实、实体、关系、事件与文档结构的提取和解释，也包括有证据支持的摘要及报告生成。文档版面理解与金融语义理解需要分别识别。

**当前收录与方法。** 本页仅总结 Findings / application 中的论文。当前较常见的子分类：Report and Disclosure Understanding / 财报与公告理解 (8); Entity and Relation Extraction / 实体与关系抽取 (7); Financial Text Classification / 金融文本分类 (6); Table, Chart and Document Understanding / 表格、图表及文档理解 (6); Financial Event Detection and Linking / 金融事件识别与关联 (3)。已标注的方法：Language Models & LLM / 语言模型与LLM (10); Representation Learning / 表征学习 (3); Retrieval & RAG / 检索与RAG (3); Reinforcement Learning / 强化学习 (2); Uncertainty & Robustness / 不确定性与鲁棒性 (2)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 关注结构提取、数值忠实性、证据覆盖及版面变化。 代表论文的摘要、金融关联证据及原文链接见 [1](../finance_notes/2024.findings-emnlp.435.md) · [2](../finance_notes/2021.findings-acl.28.md) · [3](../finance_notes/2021.findings-acl.308.md) · [4](../finance_notes/2026.findings-acl.82.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 连接结构提取、数值一致性和跨文档事实核验，检验版式、语言和报告规则变化带来的影响。

### English

**Problem and subdirections.** This task extracts and interprets facts, entities, relations, events and document structure, including evidence-grounded summaries and reports. Layout understanding and financial semantics need separate treatment.

**Current coverage and methods.** This page covers only Findings / application. Frequent subcategories: Report and Disclosure Understanding / 财报与公告理解 (8); Entity and Relation Extraction / 实体与关系抽取 (7); Financial Text Classification / 金融文本分类 (6); Table, Chart and Document Understanding / 表格、图表及文档理解 (6); Financial Event Detection and Linking / 金融事件识别与关联 (3). Recorded methods: Language Models & LLM / 语言模型与LLM (10); Representation Learning / 表征学习 (3); Retrieval & RAG / 检索与RAG (3); Reinforcement Learning / 强化学习 (2); Uncertainty & Robustness / 不确定性与鲁棒性 (2). Counts overlap and are not performance rankings.

**Data and evaluation.** Measure structural extraction, numerical faithfulness, evidence coverage and layout shift. Representative abstracts, financial evidence and original sources are linked at [1](../finance_notes/2024.findings-emnlp.435.md) · [2](../finance_notes/2021.findings-acl.28.md) · [3](../finance_notes/2021.findings-acl.308.md) · [4](../finance_notes/2026.findings-acl.82.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Connect structural extraction, numerical consistency and cross-document verification, testing shifts in layouts, languages and reporting rules.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. Demonstration Selection Strategies for Numerical Time Series Data-to-Text](../finance_notes/2024.findings-emnlp.435.md) · EMNLP 2024 | 按序列相似度和知识选择数值生成示例<br>Select data-to-text demonstrations using sequence similarity and knowledge | 叙述质量和预测效用不同<br>Narrative quality differs from forecasting utility |
| [2. Spatial Dependency Parsing for Semi-Structured Document Information Extraction](../finance_notes/2021.findings-acl.28.md) · ACL 2021 | 空间依存结构支持票据和发票信息抽取<br>Spatial dependencies support receipt/invoice extraction | 通用抽取方法，非完整财务审核<br>General extraction rather than complete financial auditing |
| [3. Towards Protecting Vital Healthcare Programs by Extracting Actionable Knowledge from Policy](../finance_notes/2021.findings-acl.308.md) · ACL 2021 | 把政策文本转为本体引导的规则图<br>Convert policy text into ontology-guided rule graphs | 抽取规则仍需专业人员监督<br>Extracted rules still require professional oversight |
| [4. Infinity-Parser: Layout-Aware Reinforcement Learning with High-quality Document Parsing Dataset](../finance_notes/2026.findings-acl.82.md) · ACL 2026 | 研究主题：Infinity-Parser: Layout-Aware Reinforcement Learning with High-quality Document Parsing Dataset<br>Research topic: Infinity-Parser: Layout-Aware Reinforcement Learning with High-quality Document Parsing Dataset | 按原文的任务、数据和实验设置解释结果。<br>Interpret results within the original task, data and experimental setting. |

<!-- task-summary:end -->

## Subtopic statistics / 子方向统计

| Subtopic | Papers |
|---|---:|
| Entity and Relation Extraction / 实体与关系抽取 | 7 |
| Financial Event Detection and Linking / 金融事件识别与关联 | 3 |
| Financial Text Classification / 金融文本分类 | 6 |
| Report and Disclosure Understanding / 财报与公告理解 | 8 |
| Table, Chart and Document Understanding / 表格、图表及文档理解 | 6 |
| Financial Summarization and Report Generation / 金融摘要与报告生成 | 2 |

## Full paper list / 完整论文列表

| Year | Venue | Paper | Scope | Primary topic | Subtopics | Methods | Resources |
|---|---|---|---|---|---|---|---|
| 2026 | ACL | [Infinity-Parser: Layout-Aware Reinforcement Learning with High-quality Document Parsing Dataset](../finance_notes/2026.findings-acl.82.md) | application | Financial Understanding / 金融理解 | Table, Chart and Document Understanding / 表格、图表及文档理解; Report and Disclosure Understanding / 财报与公告理解 | Language Models & LLM / 语言模型与LLM; Reinforcement Learning / 强化学习; Uncertainty & Robustness / 不确定性与鲁棒性; Multimodal Learning / 多模态学习 | [PDF](../../pdfs/ACL/2026/2026.findings-acl.82.pdf) |
| 2026 | ACL | [On Finding Inconsistencies in Documents](../finance_notes/2026.findings-acl.1675.md) | application | Financial Evaluation / 金融评测 | Report and Disclosure Understanding / 财报与公告理解; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Financial Understanding and Multimodal Evaluation / 金融理解及多模态评测; Table, Chart and Document Understanding / 表格、图表及文档理解 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/ACL/2026/2026.findings-acl.1675.pdf) |
| 2026 | EMNLP | [DataCross: A Unified Benchmark and Agent Framework for Cross-Modal Heterogeneous Data Analysis](../finance_notes/2026.findings-emnlp.1229.md) | application | Financial Understanding / 金融理解 | Table, Chart and Document Understanding / 表格、图表及文档理解 | Language Models & LLM / 语言模型与LLM; Multimodal Learning / 多模态学习 | [PDF](../../pdfs/EMNLP/2026/2026.findings-emnlp.1229.pdf) |
| 2026 | EMNLP | [HardMTBench: Stress-Testing Chinese-English Translation on Knowledge-Intensive Domains](../finance_notes/2026.findings-emnlp.235.md) | application | Financial Understanding / 金融理解 | Financial Text Classification / 金融文本分类 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/EMNLP/2026/2026.findings-emnlp.235.pdf) |
| 2025 | ACL | [Task-Oriented Automatic Fact-Checking with Frame-Semantics](../finance_notes/2025.findings-acl.711.md) | application | Financial Understanding / 金融理解 | Report and Disclosure Understanding / 财报与公告理解 | Retrieval & RAG / 检索与RAG | [PDF](../../pdfs/ACL/2025/2025.findings-acl.711.pdf) |
| 2024 | ACL | [Can Large Language Models Follow Concept Annotation Guidelines? A Case Study on Scientific and Financial Domains](../finance_notes/2024.findings-acl.478.md) | application | Financial Understanding / 金融理解 | Financial Text Classification / 金融文本分类; Financial Understanding and Multimodal Evaluation / 金融理解及多模态评测 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/ACL/2024/2024.findings-acl.478.pdf) |
| 2024 | ACL | [Leveraging Collection-Wide Similarities for Unsupervised Document Structure Extraction](../finance_notes/2024.findings-acl.568.md) | application | Financial Understanding / 金融理解 | Table, Chart and Document Understanding / 表格、图表及文档理解; Entity and Relation Extraction / 实体与关系抽取 |  | [PDF](../../pdfs/ACL/2024/2024.findings-acl.568.pdf) |
| 2024 | ACL | [ZeroStance: Leveraging ChatGPT for Open-Domain Stance Detection via Dataset Generation](../finance_notes/2024.findings-acl.794.md) | application | Financial Understanding / 金融理解 | Financial Event Detection and Linking / 金融事件识别与关联; Financial Summarization and Report Generation / 金融摘要与报告生成 | Generative Modeling / 生成建模 | [PDF](../../pdfs/ACL/2024/2024.findings-acl.794.pdf) |
| 2024 | EMNLP | [Demonstration Selection Strategies for Numerical Time Series Data-to-Text](../finance_notes/2024.findings-emnlp.435.md) | application | Financial Understanding / 金融理解 | Financial Summarization and Report Generation / 金融摘要与报告生成; General Sequence Forecasting / 通用序列预测 | Representation Learning / 表征学习 | [PDF](../../pdfs/EMNLP/2024/2024.findings-emnlp.435.pdf) |
| 2024 | EMNLP | [DictDis: Dictionary Constrained Disambiguation for Improved NMT](../finance_notes/2024.findings-emnlp.643.md) | application | Financial Understanding / 金融理解 | Financial Text Classification / 金融文本分类 |  | [PDF](../../pdfs/EMNLP/2024/2024.findings-emnlp.643.pdf) |
| 2024 | EMNLP | [ValueScope: Unveiling Implicit Norms and Values via Return Potential Model of Social Interactions](../finance_notes/2024.findings-emnlp.972.md) | application | Financial Understanding / 金融理解 | Financial Text Classification / 金融文本分类 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/EMNLP/2024/2024.findings-emnlp.972.pdf) |
| 2023 | EMNLP | [Causal Inference from Text: Unveiling Interactions between Variables](../finance_notes/2023.findings-emnlp.709.md) | application | Financial Understanding / 金融理解 | Report and Disclosure Understanding / 财报与公告理解 | Causal Learning / 因果学习 | [PDF](../../pdfs/EMNLP/2023/2023.findings-emnlp.709.pdf) |
| 2023 | EMNLP | [On Task-personalized Multimodal Few-shot Learning for Visually-rich Document Entity Retrieval](../finance_notes/2023.findings-emnlp.604.md) | application | Financial Understanding / 金融理解 | Table, Chart and Document Understanding / 表格、图表及文档理解; Entity and Relation Extraction / 实体与关系抽取; Report and Disclosure Understanding / 财报与公告理解 | Uncertainty & Robustness / 不确定性与鲁棒性; Retrieval & RAG / 检索与RAG; Representation Learning / 表征学习 | [PDF](../../pdfs/EMNLP/2023/2023.findings-emnlp.604.pdf) |
| 2023 | EMNLP | [PersonaLM: Language Model Personalization via Domain-distributed Span Aggregated K-Nearest N-gram Retrieval Augmentation](../finance_notes/2023.findings-emnlp.757.md) | application | Financial Understanding / 金融理解 | Report and Disclosure Understanding / 财报与公告理解 | Language Models & LLM / 语言模型与LLM; Retrieval & RAG / 检索与RAG | [PDF](../../pdfs/EMNLP/2023/2023.findings-emnlp.757.pdf) |
| 2022 | ACL | [DaLC: Domain Adaptation Learning Curve Prediction for Neural Machine Translation](../finance_notes/2022.findings-acl.141.md) | application | Financial Understanding / 金融理解 | Financial Text Classification / 金融文本分类; Report and Disclosure Understanding / 财报与公告理解 |  | [PDF](../../pdfs/ACL/2022/2022.findings-acl.141.pdf) |
| 2021 | ACL | [CasEE: A Joint Learning Framework with Cascade Decoding for Overlapping Event Extraction](../finance_notes/2021.findings-acl.14.md) | application | Financial Understanding / 金融理解 | Entity and Relation Extraction / 实体与关系抽取; Financial Event Detection and Linking / 金融事件识别与关联; Report and Disclosure Understanding / 财报与公告理解 |  | [PDF](../../pdfs/ACL/2021/2021.findings-acl.14.pdf) |
| 2021 | ACL | [Fingerprinting Fine-tuned Language Models in the Wild](../finance_notes/2021.findings-acl.409.md) | application | Financial Understanding / 金融理解 | Financial Text Classification / 金融文本分类; Financial Understanding and Multimodal Evaluation / 金融理解及多模态评测 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/ACL/2021/2021.findings-acl.409.pdf) |
| 2021 | ACL | [Revisiting the Evaluation of End-to-end Event Extraction](../finance_notes/2021.findings-acl.405.md) | application | Financial Understanding / 金融理解 | Entity and Relation Extraction / 实体与关系抽取; Financial Event Detection and Linking / 金融事件识别与关联 | Reinforcement Learning / 强化学习 | [PDF](../../pdfs/ACL/2021/2021.findings-acl.405.pdf) |
| 2021 | ACL | [Spatial Dependency Parsing for Semi-Structured Document Information Extraction](../finance_notes/2021.findings-acl.28.md) | application | Financial Understanding / 金融理解 | Table, Chart and Document Understanding / 表格、图表及文档理解; Entity and Relation Extraction / 实体与关系抽取 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/ACL/2021/2021.findings-acl.28.pdf) |
| 2021 | ACL | [Towards Protecting Vital Healthcare Programs by Extracting Actionable Knowledge from Policy](../finance_notes/2021.findings-acl.308.md) | application | Financial Safety / 金融安全 | Regulatory Compliance and Violation Detection / 监管合规与违规检测; Entity and Relation Extraction / 实体与关系抽取 |  | [PDF](../../pdfs/ACL/2021/2021.findings-acl.308.pdf) |
| 2021 | EMNLP | [mDAPT: Multilingual Domain Adaptive Pretraining in a Single Model](../finance_notes/2021.findings-emnlp.290.md) | application | Financial Understanding / 金融理解 | Entity and Relation Extraction / 实体与关系抽取 | Language Models & LLM / 语言模型与LLM; Representation Learning / 表征学习 | [PDF](../../pdfs/EMNLP/2021/2021.findings-emnlp.290.pdf) |
