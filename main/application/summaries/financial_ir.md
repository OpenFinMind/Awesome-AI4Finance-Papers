## Research summary / 研究总结

**Financial Retrieval / 金融检索 · Main / Application**

2026-11-20 · 95 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 主要贡献是金融证据的表示、搜索、过滤或排序。RAG 的检索模块与最终问答结果分别评价；检索输入可为文本、表格、图表或数值向量。

**当前收录与方法。** 本页仅总结 Main / application 中的论文。当前较常见的子分类：Financial Semantic Matching and Ranking / 金融语义匹配与排序 (89); Evidence Retrieval and Reranking for Financial RAG / 金融 RAG 的证据检索与重排序 (24); Chart and Multimodal Retrieval / 图表与多模态检索 (9); Financial Document and Disclosure Retrieval / 金融文档与公告检索 (8); Table and Numerical Retrieval / 表格及数值信息检索 (2)。已标注的方法：Retrieval & RAG / 检索与RAG (74); Language Models & LLM / 语言模型与LLM (60); Representation Learning / 表征学习 (36); Uncertainty & Robustness / 不确定性与鲁棒性 (23); Optimization & Numerical Methods / 优化与数值方法 (9)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 分开报告检索召回、重排质量、引用忠实性和最终回答质量。 代表论文的摘要、金融关联证据及原文链接见 [1](../indexes/finance_notes/2022.emnlp-main.95.md) · [2](../indexes/finance_notes/aaai-2026-39015.md) · [3](../indexes/finance_notes/2026.acl-long.371.md) · [4](../indexes/finance_notes/2026.acl-long.1397.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 研究时间有效性、跨文档覆盖和数值敏感性，分析证据缺失、召回失败与生成错误各自的影响。

### English

**Problem and subdirections.** The main contribution represents, searches, filters or ranks financial evidence. RAG retrieval and final QA need separate evaluation; inputs may be text, tables, charts or numerical vectors.

**Current coverage and methods.** This page covers only Main / application. Frequent subcategories: Financial Semantic Matching and Ranking / 金融语义匹配与排序 (89); Evidence Retrieval and Reranking for Financial RAG / 金融 RAG 的证据检索与重排序 (24); Chart and Multimodal Retrieval / 图表与多模态检索 (9); Financial Document and Disclosure Retrieval / 金融文档与公告检索 (8); Table and Numerical Retrieval / 表格及数值信息检索 (2). Recorded methods: Retrieval & RAG / 检索与RAG (74); Language Models & LLM / 语言模型与LLM (60); Representation Learning / 表征学习 (36); Uncertainty & Robustness / 不确定性与鲁棒性 (23); Optimization & Numerical Methods / 优化与数值方法 (9). Counts overlap and are not performance rankings.

**Data and evaluation.** Report retrieval recall, reranking, citation faithfulness and answer quality separately. Representative abstracts, financial evidence and original sources are linked at [1](../indexes/finance_notes/2022.emnlp-main.95.md) · [2](../indexes/finance_notes/aaai-2026-39015.md) · [3](../indexes/finance_notes/2026.acl-long.371.md) · [4](../indexes/finance_notes/2026.acl-long.1397.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Study temporal validity, cross-document coverage and numerical sensitivity, separating missing evidence, retrieval failure and generation errors.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. COCO-DR: Combating the Distribution Shift in Zero-Shot Dense Retrieval with Contrastive and Distributionally Robust Learning](../indexes/finance_notes/2022.emnlp-main.95.md) · EMNLP 2022 | 对比预训练与鲁棒重加权改善零样本检索<br>Contrastive adaptation and robust reweighting for zero-shot retrieval | 通用方法在金融子集的证据有范围限制<br>General-method evidence is bounded by the financial subset |
| [2. HierSearch: A Hierarchical Enterprise Deep Search Framework Integrating Local and Web Searches](../indexes/finance_notes/aaai-2026-39015.md) · AAAI 2026 | 研究主题：HierSearch: A Hierarchical Enterprise Deep Search Framework Integrating Local and Web Searches<br>Research topic: HierSearch: A Hierarchical Enterprise Deep Search Framework Integrating Local and Web Searches | 按原文的任务、数据和实验设置解释结果。<br>Interpret results within the original task, data and experimental setting. |
| [3. ARK: Answer-Centric Retriever Tuning via KG-augmented Curriculum Learning](../indexes/finance_notes/2026.acl-long.371.md) · ACL 2026 | 研究主题：ARK: Answer-Centric Retriever Tuning via KG-augmented Curriculum Learning<br>Research topic: ARK: Answer-Centric Retriever Tuning via KG-augmented Curriculum Learning | 按原文的任务、数据和实验设置解释结果。<br>Interpret results within the original task, data and experimental setting. |
| [4. Beyond Explicit Refusals: Soft-Failure Attacks on Retrieval-Augmented Generation](../indexes/finance_notes/2026.acl-long.1397.md) · ACL 2026 | 研究主题：Beyond Explicit Refusals: Soft-Failure Attacks on Retrieval-Augmented Generation<br>Research topic: Beyond Explicit Refusals: Soft-Failure Attacks on Retrieval-Augmented Generation | 按原文的任务、数据和实验设置解释结果。<br>Interpret results within the original task, data and experimental setting. |
