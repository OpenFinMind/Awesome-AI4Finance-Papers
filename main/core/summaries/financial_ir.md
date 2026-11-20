## Research summary / 研究总结

**Financial Retrieval / 金融检索 · Main / Core**

2026-11-20 · 17 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 主要贡献是金融证据的表示、搜索、过滤或排序。RAG 的检索模块与最终问答结果分别评价；检索输入可为文本、表格、图表或数值向量。

**当前收录与方法。** 本页仅总结 Main / core 中的论文。当前较常见的子分类：Financial Semantic Matching and Ranking / 金融语义匹配与排序 (12); Evidence Retrieval and Reranking for Financial RAG / 金融 RAG 的证据检索与重排序 (10); Chart and Multimodal Retrieval / 图表与多模态检索 (1); Financial Document and Disclosure Retrieval / 金融文档与公告检索 (1)。已标注的方法：Language Models & LLM / 语言模型与LLM (11); Retrieval & RAG / 检索与RAG (10); Generative Modeling / 生成建模 (4); Optimization & Numerical Methods / 优化与数值方法 (3); Representation Learning / 表征学习 (2)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 分开报告检索召回、重排质量、引用忠实性和最终回答质量。 代表论文的摘要、金融关联证据及原文链接见 [1](../indexes/finance_notes/2023.emnlp-main.234.md) · [2](../indexes/finance_notes/2026.acl-long.492.md) · [3](../indexes/finance_notes/2026.acl-long.265.md) · [4](../indexes/finance_notes/iclr-2026-8AJbbbe2ni.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 研究时间有效性、跨文档覆盖和数值敏感性，分析证据缺失、召回失败与生成错误各自的影响。

### English

**Problem and subdirections.** The main contribution represents, searches, filters or ranks financial evidence. RAG retrieval and final QA need separate evaluation; inputs may be text, tables, charts or numerical vectors.

**Current coverage and methods.** This page covers only Main / core. Frequent subcategories: Financial Semantic Matching and Ranking / 金融语义匹配与排序 (12); Evidence Retrieval and Reranking for Financial RAG / 金融 RAG 的证据检索与重排序 (10); Chart and Multimodal Retrieval / 图表与多模态检索 (1); Financial Document and Disclosure Retrieval / 金融文档与公告检索 (1). Recorded methods: Language Models & LLM / 语言模型与LLM (11); Retrieval & RAG / 检索与RAG (10); Generative Modeling / 生成建模 (4); Optimization & Numerical Methods / 优化与数值方法 (3); Representation Learning / 表征学习 (2). Counts overlap and are not performance rankings.

**Data and evaluation.** Report retrieval recall, reranking, citation faithfulness and answer quality separately. Representative abstracts, financial evidence and original sources are linked at [1](../indexes/finance_notes/2023.emnlp-main.234.md) · [2](../indexes/finance_notes/2026.acl-long.492.md) · [3](../indexes/finance_notes/2026.acl-long.265.md) · [4](../indexes/finance_notes/iclr-2026-8AJbbbe2ni.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Study temporal validity, cross-document coverage and numerical sensitivity, separating missing evidence, retrieval failure and generation errors.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. TRAVEL: Tag-Aware Conversational FAQ Retrieval via Reinforcement Learning](../indexes/finance_notes/2023.emnlp-main.234.md) · EMNLP 2023 | 标签与 RL 减少 FAQ 对话中的噪声<br>Tags and RL reduce noise in conversational FAQ retrieval | 检索成功不代表完成银行业务操作<br>Retrieval success does not establish workflow completion |
| [2. All That Glisters Is Not Gold: A Benchmark for Reference-Free Counterfactual Financial Misinformation Detection](../indexes/finance_notes/2026.acl-long.492.md) · ACL 2026 | 测试无外部参照时的金融虚假信息识别<br>Test financial misinformation without external references | 有配对参照的成功不代表无参照能力<br>Paired-reference success does not establish reference-free ability |
| [3. FinSight: Towards Real-World Financial Deep Research](../indexes/finance_notes/2026.acl-long.265.md) · ACL 2026 | 可执行分析、来源引用与视觉反馈的投研报告<br>Research reports with executable analysis, citations and visual feedback | 报告质量不直接验证投资预测能力<br>Report quality does not directly establish predictive investment skill |
| [4. FinSearchComp: Towards a Realistic, Expert-Level Evaluation of Financial Search and Reasoning](../indexes/finance_notes/iclr-2026-8AJbbbe2ni.md) · ICLR 2026 | 专家设计的时效搜索及复杂金融调查<br>Expert-designed timely search and complex financial investigations | 结果依赖工具、地域覆盖及检索时间<br>Results depend on tools, geographic coverage and retrieval time |
