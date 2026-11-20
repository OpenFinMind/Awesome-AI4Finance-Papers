## Research summary / 研究总结

**Financial Retrieval / 金融检索 · Findings / Core**

2026-11-20 · 8 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 主要贡献是金融证据的表示、搜索、过滤或排序。RAG 的检索模块与最终问答结果分别评价；检索输入可为文本、表格、图表或数值向量。

**当前收录与方法。** 本页仅总结 Findings / core 中的论文。当前较常见的子分类：Financial Semantic Matching and Ranking / 金融语义匹配与排序 (8); Evidence Retrieval and Reranking for Financial RAG / 金融 RAG 的证据检索与重排序 (4); Financial Document and Disclosure Retrieval / 金融文档与公告检索 (3)。已标注的方法：Retrieval & RAG / 检索与RAG (7); Language Models & LLM / 语言模型与LLM (4); Multimodal Learning / 多模态学习 (1); Fairness & Recourse / 公平性与算法追索 (1); Representation Learning / 表征学习 (1)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 分开报告检索召回、重排质量、引用忠实性和最终回答质量。 代表论文的摘要、金融关联证据及原文链接见 [1](../indexes/finance_notes/2026.findings-acl.2151.md) · [2](../indexes/finance_notes/2025.findings-acl.855.md) · [3](../indexes/finance_notes/2026.findings-emnlp.2384.md) · [4](../indexes/finance_notes/2026.findings-emnlp.2053.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 研究时间有效性、跨文档覆盖和数值敏感性，分析证据缺失、召回失败与生成错误各自的影响。

### English

**Problem and subdirections.** The main contribution represents, searches, filters or ranks financial evidence. RAG retrieval and final QA need separate evaluation; inputs may be text, tables, charts or numerical vectors.

**Current coverage and methods.** This page covers only Findings / core. Frequent subcategories: Financial Semantic Matching and Ranking / 金融语义匹配与排序 (8); Evidence Retrieval and Reranking for Financial RAG / 金融 RAG 的证据检索与重排序 (4); Financial Document and Disclosure Retrieval / 金融文档与公告检索 (3). Recorded methods: Retrieval & RAG / 检索与RAG (7); Language Models & LLM / 语言模型与LLM (4); Multimodal Learning / 多模态学习 (1); Fairness & Recourse / 公平性与算法追索 (1); Representation Learning / 表征学习 (1). Counts overlap and are not performance rankings.

**Data and evaluation.** Report retrieval recall, reranking, citation faithfulness and answer quality separately. Representative abstracts, financial evidence and original sources are linked at [1](../indexes/finance_notes/2026.findings-acl.2151.md) · [2](../indexes/finance_notes/2025.findings-acl.855.md) · [3](../indexes/finance_notes/2026.findings-emnlp.2384.md) · [4](../indexes/finance_notes/2026.findings-emnlp.2053.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Study temporal validity, cross-document coverage and numerical sensitivity, separating missing evidence, retrieval failure and generation errors.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. Fin-STAR: Structure-as-Semantics to Resolve Implicitness in Financial Retrieval](../indexes/finance_notes/2026.findings-acl.2151.md) · ACL 2026 | 以结构语义澄清财务片段的隐含范围<br>Structural semantics clarify implicit scope in financial snippets | 结构索引构建质量影响迁移<br>Structural-index quality affects transfer |
| [2. Hierarchical Retrieval with Evidence Curation for Open-Domain Financial Question Answering on Standardized Documents](../indexes/finance_notes/2025.findings-acl.855.md) · ACL 2025 | 分层检索与证据整理减少模板混淆<br>Hierarchical retrieval and evidence curation reduce template confusion | 可回答性检查取决于检索证据覆盖<br>Answerability checks depend on retrieved evidence coverage |
| [3. FinHopper: A Progressive Multi-Hop Benchmark for Complex Financial Agents with Step-wise Evaluation](../indexes/finance_notes/2026.findings-emnlp.2384.md) · EMNLP 2026 | 带中间答案的渐进多跳金融搜索评价<br>Progressive multihop financial search with intermediate answers | 最终答案分数会掩盖中途错误<br>Final-answer scores can conceal intermediate failures |
| [4. K-FinHallu: A Hallucination Detection Benchmark for Multi-Turn RAG in Korean Finance](../indexes/finance_notes/2026.findings-emnlp.2053.md) · EMNLP 2026 | 韩语多轮 RAG 幻觉及合理拒答诊断<br>Korean multi-turn RAG diagnostics of hallucination and justified abstention | 受控注入与自然系统失效需分开验证<br>Controlled injections differ from naturally occurring system failures |
