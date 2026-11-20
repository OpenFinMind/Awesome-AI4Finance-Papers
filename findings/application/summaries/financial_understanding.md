## Research summary / 研究总结

**Financial Understanding / 金融理解 · Findings / Application**

2026-11-20 · 21 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 关注事实、实体、关系、事件与文档结构的提取和解释，也包括有证据支持的摘要及报告生成。文档版面理解与金融语义理解需要分别识别。

**当前收录与方法。** 本页仅总结 Findings / application 中的论文。当前较常见的子分类：Report and Disclosure Understanding / 财报与公告理解 (8); Entity and Relation Extraction / 实体与关系抽取 (7); Financial Text Classification / 金融文本分类 (6); Table, Chart and Document Understanding / 表格、图表及文档理解 (6); Financial Event Detection and Linking / 金融事件识别与关联 (3)。已标注的方法：Language Models & LLM / 语言模型与LLM (10); Representation Learning / 表征学习 (3); Retrieval & RAG / 检索与RAG (3); Reinforcement Learning / 强化学习 (2); Uncertainty & Robustness / 不确定性与鲁棒性 (2)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 关注结构提取、数值忠实性、证据覆盖及版面变化。 代表论文的摘要、金融关联证据及原文链接见 [1](../indexes/finance_notes/2024.findings-emnlp.435.md) · [2](../indexes/finance_notes/2021.findings-acl.28.md) · [3](../indexes/finance_notes/2021.findings-acl.308.md) · [4](../indexes/finance_notes/2026.findings-acl.82.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 连接结构提取、数值一致性和跨文档事实核验，检验版式、语言和报告规则变化带来的影响。

### English

**Problem and subdirections.** This task extracts and interprets facts, entities, relations, events and document structure, including evidence-grounded summaries and reports. Layout understanding and financial semantics need separate treatment.

**Current coverage and methods.** This page covers only Findings / application. Frequent subcategories: Report and Disclosure Understanding / 财报与公告理解 (8); Entity and Relation Extraction / 实体与关系抽取 (7); Financial Text Classification / 金融文本分类 (6); Table, Chart and Document Understanding / 表格、图表及文档理解 (6); Financial Event Detection and Linking / 金融事件识别与关联 (3). Recorded methods: Language Models & LLM / 语言模型与LLM (10); Representation Learning / 表征学习 (3); Retrieval & RAG / 检索与RAG (3); Reinforcement Learning / 强化学习 (2); Uncertainty & Robustness / 不确定性与鲁棒性 (2). Counts overlap and are not performance rankings.

**Data and evaluation.** Measure structural extraction, numerical faithfulness, evidence coverage and layout shift. Representative abstracts, financial evidence and original sources are linked at [1](../indexes/finance_notes/2024.findings-emnlp.435.md) · [2](../indexes/finance_notes/2021.findings-acl.28.md) · [3](../indexes/finance_notes/2021.findings-acl.308.md) · [4](../indexes/finance_notes/2026.findings-acl.82.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Connect structural extraction, numerical consistency and cross-document verification, testing shifts in layouts, languages and reporting rules.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. Demonstration Selection Strategies for Numerical Time Series Data-to-Text](../indexes/finance_notes/2024.findings-emnlp.435.md) · EMNLP 2024 | 按序列相似度和知识选择数值生成示例<br>Select data-to-text demonstrations using sequence similarity and knowledge | 叙述质量和预测效用不同<br>Narrative quality differs from forecasting utility |
| [2. Spatial Dependency Parsing for Semi-Structured Document Information Extraction](../indexes/finance_notes/2021.findings-acl.28.md) · ACL 2021 | 空间依存结构支持票据和发票信息抽取<br>Spatial dependencies support receipt/invoice extraction | 通用抽取方法，非完整财务审核<br>General extraction rather than complete financial auditing |
| [3. Towards Protecting Vital Healthcare Programs by Extracting Actionable Knowledge from Policy](../indexes/finance_notes/2021.findings-acl.308.md) · ACL 2021 | 把政策文本转为本体引导的规则图<br>Convert policy text into ontology-guided rule graphs | 抽取规则仍需专业人员监督<br>Extracted rules still require professional oversight |
| [4. Infinity-Parser: Layout-Aware Reinforcement Learning with High-quality Document Parsing Dataset](../indexes/finance_notes/2026.findings-acl.82.md) · ACL 2026 | 研究主题：Infinity-Parser: Layout-Aware Reinforcement Learning with High-quality Document Parsing Dataset<br>Research topic: Infinity-Parser: Layout-Aware Reinforcement Learning with High-quality Document Parsing Dataset | 按原文的任务、数据和实验设置解释结果。<br>Interpret results within the original task, data and experimental setting. |
