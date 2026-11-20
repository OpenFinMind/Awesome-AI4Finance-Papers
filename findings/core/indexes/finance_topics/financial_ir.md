# Financial Retrieval / 金融检索

Retrieve, embed, rerank and ground financial evidence, including financial RAG. / 金融证据检索、嵌入、重排及 RAG。

8 Findings long papers. Topic memberships can overlap.

[All topics](../ai_for_finance.md) · [Classification definitions](../finance_taxonomy.md) · [CSV](financial_ir.csv) · [Excel](../../finance_catalog.xlsx)

<!-- task-summary:start -->

## Research summary / 研究总结

**Financial Retrieval / 金融检索 · Findings / Core**

2026-11-20 · 8 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 主要贡献是金融证据的表示、搜索、过滤或排序。RAG 的检索模块与最终问答结果分别评价；检索输入可为文本、表格、图表或数值向量。

**当前收录与方法。** 本页仅总结 Findings / core 中的论文。当前较常见的子分类：Financial Semantic Matching and Ranking / 金融语义匹配与排序 (8); Evidence Retrieval and Reranking for Financial RAG / 金融 RAG 的证据检索与重排序 (4); Financial Document and Disclosure Retrieval / 金融文档与公告检索 (3)。已标注的方法：Retrieval & RAG / 检索与RAG (7); Language Models & LLM / 语言模型与LLM (4); Multimodal Learning / 多模态学习 (1); Fairness & Recourse / 公平性与算法追索 (1); Representation Learning / 表征学习 (1)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 分开报告检索召回、重排质量、引用忠实性和最终回答质量。 代表论文的摘要、金融关联证据及原文链接见 [1](../finance_notes/2026.findings-acl.2151.md) · [2](../finance_notes/2025.findings-acl.855.md) · [3](../finance_notes/2026.findings-emnlp.2384.md) · [4](../finance_notes/2026.findings-emnlp.2053.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 研究时间有效性、跨文档覆盖和数值敏感性，分析证据缺失、召回失败与生成错误各自的影响。

### English

**Problem and subdirections.** The main contribution represents, searches, filters or ranks financial evidence. RAG retrieval and final QA need separate evaluation; inputs may be text, tables, charts or numerical vectors.

**Current coverage and methods.** This page covers only Findings / core. Frequent subcategories: Financial Semantic Matching and Ranking / 金融语义匹配与排序 (8); Evidence Retrieval and Reranking for Financial RAG / 金融 RAG 的证据检索与重排序 (4); Financial Document and Disclosure Retrieval / 金融文档与公告检索 (3). Recorded methods: Retrieval & RAG / 检索与RAG (7); Language Models & LLM / 语言模型与LLM (4); Multimodal Learning / 多模态学习 (1); Fairness & Recourse / 公平性与算法追索 (1); Representation Learning / 表征学习 (1). Counts overlap and are not performance rankings.

**Data and evaluation.** Report retrieval recall, reranking, citation faithfulness and answer quality separately. Representative abstracts, financial evidence and original sources are linked at [1](../finance_notes/2026.findings-acl.2151.md) · [2](../finance_notes/2025.findings-acl.855.md) · [3](../finance_notes/2026.findings-emnlp.2384.md) · [4](../finance_notes/2026.findings-emnlp.2053.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Study temporal validity, cross-document coverage and numerical sensitivity, separating missing evidence, retrieval failure and generation errors.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. Fin-STAR: Structure-as-Semantics to Resolve Implicitness in Financial Retrieval](../finance_notes/2026.findings-acl.2151.md) · ACL 2026 | 以结构语义澄清财务片段的隐含范围<br>Structural semantics clarify implicit scope in financial snippets | 结构索引构建质量影响迁移<br>Structural-index quality affects transfer |
| [2. Hierarchical Retrieval with Evidence Curation for Open-Domain Financial Question Answering on Standardized Documents](../finance_notes/2025.findings-acl.855.md) · ACL 2025 | 分层检索与证据整理减少模板混淆<br>Hierarchical retrieval and evidence curation reduce template confusion | 可回答性检查取决于检索证据覆盖<br>Answerability checks depend on retrieved evidence coverage |
| [3. FinHopper: A Progressive Multi-Hop Benchmark for Complex Financial Agents with Step-wise Evaluation](../finance_notes/2026.findings-emnlp.2384.md) · EMNLP 2026 | 带中间答案的渐进多跳金融搜索评价<br>Progressive multihop financial search with intermediate answers | 最终答案分数会掩盖中途错误<br>Final-answer scores can conceal intermediate failures |
| [4. K-FinHallu: A Hallucination Detection Benchmark for Multi-Turn RAG in Korean Finance](../finance_notes/2026.findings-emnlp.2053.md) · EMNLP 2026 | 韩语多轮 RAG 幻觉及合理拒答诊断<br>Korean multi-turn RAG diagnostics of hallucination and justified abstention | 受控注入与自然系统失效需分开验证<br>Controlled injections differ from naturally occurring system failures |

<!-- task-summary:end -->

## Subtopic statistics / 子方向统计

| Subtopic | Papers |
|---|---:|
| Financial Document and Disclosure Retrieval / 金融文档与公告检索 | 3 |
| Financial Semantic Matching and Ranking / 金融语义匹配与排序 | 8 |
| Table and Numerical Retrieval / 表格及数值信息检索 | 0 |
| Chart and Multimodal Retrieval / 图表与多模态检索 | 0 |
| Cross-Lingual Financial Retrieval / 跨语言金融检索 | 0 |
| Evidence Retrieval and Reranking for Financial RAG / 金融 RAG 的证据检索与重排序 | 4 |

## Full paper list / 完整论文列表

| Year | Venue | Paper | Scope | Primary topic | Subtopics | Methods | Resources |
|---|---|---|---|---|---|---|---|
| 2026 | ACL | [Fin-STAR: Structure-as-Semantics to Resolve Implicitness in Financial Retrieval](../finance_notes/2026.findings-acl.2151.md) | core | Financial Retrieval / 金融检索 | Numerical Calculation and Program Reasoning / 数值计算与程序推理; Financial Semantic Matching and Ranking / 金融语义匹配与排序 | Retrieval & RAG / 检索与RAG | [PDF](../../pdfs/ACL/2026/2026.findings-acl.2151.pdf) |
| 2026 | ACL | [FinCARDS: Card-Based Analyst Reranking for Financial Document Question Answering](../finance_notes/2026.findings-acl.1244.md) | core | Financial Retrieval / 金融检索 | Numerical Calculation and Program Reasoning / 数值计算与程序推理; Financial Factual QA / 金融事实问答; Financial Document and Disclosure Retrieval / 金融文档与公告检索; Financial Semantic Matching and Ranking / 金融语义匹配与排序 | Language Models & LLM / 语言模型与LLM; Retrieval & RAG / 检索与RAG | [PDF](../../pdfs/ACL/2026/2026.findings-acl.1244.pdf) |
| 2026 | ACL | [FinMRAGBench: A Realistic and Complex Benchmark for Multi-Modal RAG in Financial Document Analysis](../finance_notes/2026.findings-acl.187.md) | core | Financial Evaluation / 金融评测 | Numerical Calculation and Program Reasoning / 数值计算与程序推理; Financial Semantic Matching and Ranking / 金融语义匹配与排序; Evidence Retrieval and Reranking for Financial RAG / 金融 RAG 的证据检索与重排序; Table, Chart and Document Understanding / 表格、图表及文档理解; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Financial Understanding and Multimodal Evaluation / 金融理解及多模态评测; Financial Document and Disclosure Retrieval / 金融文档与公告检索 | Multimodal Learning / 多模态学习; Retrieval & RAG / 检索与RAG | [PDF](../../pdfs/ACL/2026/2026.findings-acl.187.pdf) |
| 2026 | ACL | [Uncovering Currency Bias and Syntax Gap in Text Embedding Models](../finance_notes/2026.findings-acl.2118.md) | core | Financial Evaluation / 金融评测 | Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Reliability, Safety and Fairness Evaluation / 可靠性、安全与公平性评测; Financial Semantic Matching and Ranking / 金融语义匹配与排序; Financial Model and Agent Safety / 金融模型及智能体安全 | Fairness & Recourse / 公平性与算法追索; Representation Learning / 表征学习 | [PDF](../../pdfs/ACL/2026/2026.findings-acl.2118.pdf) |
| 2026 | EMNLP | [FinHopper: A Progressive Multi-Hop Benchmark for Complex Financial Agents with Step-wise Evaluation](../finance_notes/2026.findings-emnlp.2384.md) | core | Financial Evaluation / 金融评测 | Numerical Calculation and Program Reasoning / 数值计算与程序推理; Financial Factual QA / 金融事实问答; Financial Semantic Matching and Ranking / 金融语义匹配与排序; Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Financial Decision and Agent Evaluation / 金融决策与智能体评测; Evaluation Protocols and Metrics / 评测协议与指标; Trading Strategies and Buy/Sell Decisions / 交易策略与买卖决策; Multi-Document and Multi-Hop QA / 多文档与多跳问答 | Language Models & LLM / 语言模型与LLM; Retrieval & RAG / 检索与RAG | [PDF](../../pdfs/EMNLP/2026/2026.findings-emnlp.2384.pdf) |
| 2026 | EMNLP | [K-FinHallu: A Hallucination Detection Benchmark for Multi-Turn RAG in Korean Finance](../finance_notes/2026.findings-emnlp.2053.md) | core | Financial Evaluation / 金融评测 | Financial Semantic Matching and Ranking / 金融语义匹配与排序; Evidence Retrieval and Reranking for Financial RAG / 金融 RAG 的证据检索与重排序; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Reliability, Safety and Fairness Evaluation / 可靠性、安全与公平性评测 | Language Models & LLM / 语言模型与LLM; Retrieval & RAG / 检索与RAG | [PDF](../../pdfs/EMNLP/2026/2026.findings-emnlp.2053.pdf) |
| 2025 | ACL | [Hierarchical Retrieval with Evidence Curation for Open-Domain Financial Question Answering on Standardized Documents](../finance_notes/2025.findings-acl.855.md) | core | Financial Retrieval / 金融检索 | Financial Semantic Matching and Ranking / 金融语义匹配与排序; Evidence Retrieval and Reranking for Financial RAG / 金融 RAG 的证据检索与重排序; Financial Document and Disclosure Retrieval / 金融文档与公告检索 | Language Models & LLM / 语言模型与LLM; Retrieval & RAG / 检索与RAG | [PDF](../../pdfs/ACL/2025/2025.findings-acl.855.pdf) |
| 2025 | EMNLP | [FinGEAR: Financial Mapping-Guided Enhanced Answer Retrieval](../finance_notes/2025.findings-emnlp.382.md) | core | Financial Retrieval / 金融检索 | Financial Semantic Matching and Ranking / 金融语义匹配与排序; Evidence Retrieval and Reranking for Financial RAG / 金融 RAG 的证据检索与重排序 | Retrieval & RAG / 检索与RAG | [PDF](../../pdfs/EMNLP/2025/2025.findings-emnlp.382.pdf) |
