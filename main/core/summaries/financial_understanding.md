## Research summary / 研究总结

**Financial Understanding / 金融理解 · Main / Core**

2026-11-20 · 62 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 关注事实、实体、关系、事件与文档结构的提取和解释，也包括有证据支持的摘要及报告生成。文档版面理解与金融语义理解需要分别识别。

**当前收录与方法。** 本页仅总结 Main / core 中的论文。当前较常见的子分类：Report and Disclosure Understanding / 财报与公告理解 (30); Table, Chart and Document Understanding / 表格、图表及文档理解 (20); Entity and Relation Extraction / 实体与关系抽取 (14); Financial Text Classification / 金融文本分类 (8); Financial Event Detection and Linking / 金融事件识别与关联 (7)。已标注的方法：Language Models & LLM / 语言模型与LLM (35); Retrieval & RAG / 检索与RAG (12); Multimodal Learning / 多模态学习 (10); Uncertainty & Robustness / 不确定性与鲁棒性 (9); Representation Learning / 表征学习 (5)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 关注结构提取、数值忠实性、证据覆盖及版面变化。 代表论文的摘要、金融关联证据及原文链接见 [1](../indexes/finance_notes/2022.acl-long.303.md) · [2](../indexes/finance_notes/P19-1047.md) · [3](../indexes/finance_notes/D19-1032.md) · [4](../indexes/finance_notes/P17-1126.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 连接结构提取、数值一致性和跨文档事实核验，检验版式、语言和报告规则变化带来的影响。

### English

**Problem and subdirections.** This task extracts and interprets facts, entities, relations, events and document structure, including evidence-grounded summaries and reports. Layout understanding and financial semantics need separate treatment.

**Current coverage and methods.** This page covers only Main / core. Frequent subcategories: Report and Disclosure Understanding / 财报与公告理解 (30); Table, Chart and Document Understanding / 表格、图表及文档理解 (20); Entity and Relation Extraction / 实体与关系抽取 (14); Financial Text Classification / 金融文本分类 (8); Financial Event Detection and Linking / 金融事件识别与关联 (7). Recorded methods: Language Models & LLM / 语言模型与LLM (35); Retrieval & RAG / 检索与RAG (12); Multimodal Learning / 多模态学习 (10); Uncertainty & Robustness / 不确定性与鲁棒性 (9); Representation Learning / 表征学习 (5). Counts overlap and are not performance rankings.

**Data and evaluation.** Measure structural extraction, numerical faithfulness, evidence coverage and layout shift. Representative abstracts, financial evidence and original sources are linked at [1](../indexes/finance_notes/2022.acl-long.303.md) · [2](../indexes/finance_notes/P19-1047.md) · [3](../indexes/finance_notes/D19-1032.md) · [4](../indexes/finance_notes/P17-1126.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Connect structural extraction, numerical consistency and cross-document verification, testing shifts in layouts, languages and reporting rules.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. FiNER: Financial Numeric Entity Recognition for XBRL Tagging](../indexes/finance_notes/2022.acl-long.303.md) · ACL 2022 | 金融报告数值的上下文相关 XBRL 标注<br>Context-sensitive XBRL tagging of report numbers | 数值形态处理与完整会计推理应区分<br>Numeric representation differs from full accounting reasoning |
| [2. Modeling Financial Analysts’ Decision Making via the Pragmatics and Semantics of Earnings Calls](../indexes/finance_notes/P19-1047.md) · ACL 2019 | 语用及语义特征预测分析师目标价调整<br>Pragmatic and semantic features predict analyst target revisions | 分析师行为受未观察信息影响<br>Analyst behavior also depends on unobserved information |
| [3. Doc2EDAG: An End-to-End Document-level Framework for Chinese Financial Event Extraction](../indexes/finance_notes/D19-1032.md) · EMNLP 2019 | 用实体有向无环图抽取文档级金融事件<br>An entity DAG supports document-level financial event extraction | 依赖事件模式及公告标注范围<br>Results depend on event schemas and disclosure annotations |
| [4. Learning to Generate Market Comments from Stock Prices](../indexes/finance_notes/P17-1126.md) · ACL 2017 | 以价格编码与算术操作生成市场评论<br>Generate market commentary using prices and arithmetic operations | 流畅度与数字事实正确性不同<br>Fluency differs from numerical factual correctness |
