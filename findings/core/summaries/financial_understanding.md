## Research summary / 研究总结

**Financial Understanding / 金融理解 · Findings / Core**

2026-11-20 · 26 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 关注事实、实体、关系、事件与文档结构的提取和解释，也包括有证据支持的摘要及报告生成。文档版面理解与金融语义理解需要分别识别。

**当前收录与方法。** 本页仅总结 Findings / core 中的论文。当前较常见的子分类：Report and Disclosure Understanding / 财报与公告理解 (12); Table, Chart and Document Understanding / 表格、图表及文档理解 (6); Entity and Relation Extraction / 实体与关系抽取 (5); Financial Event Detection and Linking / 金融事件识别与关联 (2); Financial Text Classification / 金融文本分类 (2)。已标注的方法：Language Models & LLM / 语言模型与LLM (18); Uncertainty & Robustness / 不确定性与鲁棒性 (5); Multimodal Learning / 多模态学习 (4); Retrieval & RAG / 检索与RAG (3); Causal Learning / 因果学习 (2)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 关注结构提取、数值忠实性、证据覆盖及版面变化。 代表论文的摘要、金融关联证据及原文链接见 [1](../indexes/finance_notes/2025.findings-emnlp.1405.md) · [2](../indexes/finance_notes/2023.findings-emnlp.26.md) · [3](../indexes/finance_notes/2023.findings-emnlp.774.md) · [4](../indexes/finance_notes/2021.findings-acl.58.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 连接结构提取、数值一致性和跨文档事实核验，检验版式、语言和报告规则变化带来的影响。

### English

**Problem and subdirections.** This task extracts and interprets facts, entities, relations, events and document structure, including evidence-grounded summaries and reports. Layout understanding and financial semantics need separate treatment.

**Current coverage and methods.** This page covers only Findings / core. Frequent subcategories: Report and Disclosure Understanding / 财报与公告理解 (12); Table, Chart and Document Understanding / 表格、图表及文档理解 (6); Entity and Relation Extraction / 实体与关系抽取 (5); Financial Event Detection and Linking / 金融事件识别与关联 (2); Financial Text Classification / 金融文本分类 (2). Recorded methods: Language Models & LLM / 语言模型与LLM (18); Uncertainty & Robustness / 不确定性与鲁棒性 (5); Multimodal Learning / 多模态学习 (4); Retrieval & RAG / 检索与RAG (3); Causal Learning / 因果学习 (2). Counts overlap and are not performance rankings.

**Data and evaluation.** Measure structural extraction, numerical faithfulness, evidence coverage and layout shift. Representative abstracts, financial evidence and original sources are linked at [1](../indexes/finance_notes/2025.findings-emnlp.1405.md) · [2](../indexes/finance_notes/2023.findings-emnlp.26.md) · [3](../indexes/finance_notes/2023.findings-emnlp.774.md) · [4](../indexes/finance_notes/2021.findings-acl.58.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Connect structural extraction, numerical consistency and cross-document verification, testing shifts in layouts, languages and reporting rules.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. KAHAN: Knowledge-Augmented Hierarchical Analysis and Narration for Financial Data Narration](../indexes/finance_notes/2025.findings-emnlp.1405.md) · EMNLP 2025 | 知识增强的层级表格分析及叙述<br>Knowledge-augmented hierarchical tabular analysis and narration | 事实性和叙述质量应分别衡量<br>Measure factuality separately from narrative quality |
| [2. CR-COPEC: Causal Rationale of Corporate Performance Changes to learn from Financial Reports](../indexes/finance_notes/2023.findings-emnlp.26.md) · EMNLP 2023 | 标注财报中业绩变化的原因句<br>Annotate performance-change rationale sentences in filings | 原因表述抽取不等于因果效应识别<br>Extracting causal narratives is not causal-effect identification |
| [3. EconBERTa: Towards Robust Extraction of Named Entities in Economics](../indexes/finance_notes/2023.findings-emnlp.774.md) · EMNLP 2023 | 经济文献预训练与专家实体识别数据<br>Economics pretraining and expert entity annotations | 长实体和未见词性组合影响迁移<br>Long entities and unseen syntactic patterns affect transfer |
| [4. A Dialogue-based Information Extraction System for Medical Insurance Assessment](../indexes/finance_notes/2021.findings-acl.58.md) · ACL 2021 | 对话抽取辅助医疗保险评估及报告<br>Dialogue extraction assists medical-insurance assessment and reports | 效率证据依赖原业务流程和人工协作<br>Efficiency evidence depends on workflow and human collaboration |
