## Research summary / 研究总结

**Financial Retrieval / 金融检索 · Findings / Application**

2026-11-20 · 8 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 主要贡献是金融证据的表示、搜索、过滤或排序。RAG 的检索模块与最终问答结果分别评价；检索输入可为文本、表格、图表或数值向量。

**当前收录与方法。** 本页仅总结 Findings / application 中的论文。当前较常见的子分类：Financial Semantic Matching and Ranking / 金融语义匹配与排序 (8); Evidence Retrieval and Reranking for Financial RAG / 金融 RAG 的证据检索与重排序 (4); Financial Document and Disclosure Retrieval / 金融文档与公告检索 (1); Table and Numerical Retrieval / 表格及数值信息检索 (1)。已标注的方法：Retrieval & RAG / 检索与RAG (5); Language Models & LLM / 语言模型与LLM (4); Representation Learning / 表征学习 (4); Uncertainty & Robustness / 不确定性与鲁棒性 (3); Generative Modeling / 生成建模 (1)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 分开报告检索召回、重排质量、引用忠实性和最终回答质量。 代表论文的摘要、金融关联证据及原文链接见 [1](../indexes/finance_notes/2024.findings-emnlp.707.md) · [2](../indexes/finance_notes/2026.findings-acl.1119.md) · [3](../indexes/finance_notes/2026.findings-emnlp.2230.md) · [4](../indexes/finance_notes/2025.findings-acl.20.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 研究时间有效性、跨文档覆盖和数值敏感性，分析证据缺失、召回失败与生成错误各自的影响。

### English

**Problem and subdirections.** The main contribution represents, searches, filters or ranks financial evidence. RAG retrieval and final QA need separate evaluation; inputs may be text, tables, charts or numerical vectors.

**Current coverage and methods.** This page covers only Findings / application. Frequent subcategories: Financial Semantic Matching and Ranking / 金融语义匹配与排序 (8); Evidence Retrieval and Reranking for Financial RAG / 金融 RAG 的证据检索与重排序 (4); Financial Document and Disclosure Retrieval / 金融文档与公告检索 (1); Table and Numerical Retrieval / 表格及数值信息检索 (1). Recorded methods: Retrieval & RAG / 检索与RAG (5); Language Models & LLM / 语言模型与LLM (4); Representation Learning / 表征学习 (4); Uncertainty & Robustness / 不确定性与鲁棒性 (3); Generative Modeling / 生成建模 (1). Counts overlap and are not performance rankings.

**Data and evaluation.** Report retrieval recall, reranking, citation faithfulness and answer quality separately. Representative abstracts, financial evidence and original sources are linked at [1](../indexes/finance_notes/2024.findings-emnlp.707.md) · [2](../indexes/finance_notes/2026.findings-acl.1119.md) · [3](../indexes/finance_notes/2026.findings-emnlp.2230.md) · [4](../indexes/finance_notes/2025.findings-acl.20.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Study temporal validity, cross-document coverage and numerical sensitivity, separating missing evidence, retrieval failure and generation errors.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. Numbers Matter! Bringing Quantity-awareness to Retrieval Systems](../indexes/finance_notes/2024.findings-emnlp.707.md) · EMNLP 2024 | 把大小与单位条件融入文本排序<br>Add magnitude and unit constraints to ranking | 金融是双领域评价中的一个领域<br>Finance is one domain in a two-domain evaluation |
| [2. NASH: Numerically Aware Scoring Heuristic for Robust Semantic Similarity](../indexes/finance_notes/2026.findings-acl.1119.md) · ACL 2026 | 研究主题：NASH: Numerically Aware Scoring Heuristic for Robust Semantic Similarity<br>Research topic: NASH: Numerically Aware Scoring Heuristic for Robust Semantic Similarity | 按原文的任务、数据和实验设置解释结果。<br>Interpret results within the original task, data and experimental setting. |
| [3. Listwise Explanation of Embedding-Based Rankings via Semantic Chunk Grouping](../indexes/finance_notes/2026.findings-emnlp.2230.md) · EMNLP 2026 | 研究主题：Listwise Explanation of Embedding-Based Rankings via Semantic Chunk Grouping<br>Research topic: Listwise Explanation of Embedding-Based Rankings via Semantic Chunk Grouping | 按原文的任务、数据和实验设置解释结果。<br>Interpret results within the original task, data and experimental setting. |
| [4. TreeRAG: Unleashing the Power of Hierarchical Storage for Enhanced Knowledge Retrieval in Long Documents](../indexes/finance_notes/2025.findings-acl.20.md) · ACL 2025 | 研究主题：TreeRAG: Unleashing the Power of Hierarchical Storage for Enhanced Knowledge Retrieval in Long Documents<br>Research topic: TreeRAG: Unleashing the Power of Hierarchical Storage for Enhanced Knowledge Retrieval in Long Documents | 按原文的任务、数据和实验设置解释结果。<br>Interpret results within the original task, data and experimental setting. |
