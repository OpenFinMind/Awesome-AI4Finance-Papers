## Research summary / 研究总结

**Financial Understanding / 金融理解 · Main / Application**

2026-11-20 · 110 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 关注事实、实体、关系、事件与文档结构的提取和解释，也包括有证据支持的摘要及报告生成。文档版面理解与金融语义理解需要分别识别。

**当前收录与方法。** 本页仅总结 Main / application 中的论文。当前较常见的子分类：Table, Chart and Document Understanding / 表格、图表及文档理解 (50); Entity and Relation Extraction / 实体与关系抽取 (28); Financial Summarization and Report Generation / 金融摘要与报告生成 (26); Financial Text Classification / 金融文本分类 (21); Report and Disclosure Understanding / 财报与公告理解 (20)。已标注的方法：Language Models & LLM / 语言模型与LLM (57); Representation Learning / 表征学习 (24); Uncertainty & Robustness / 不确定性与鲁棒性 (19); Multimodal Learning / 多模态学习 (12); Retrieval & RAG / 检索与RAG (11)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 关注结构提取、数值忠实性、证据覆盖及版面变化。 代表论文的摘要、金融关联证据及原文链接见 [1](../indexes/finance_notes/2021.acl-long.201.md) · [2](../indexes/finance_notes/D18-1476.md) · [3](../indexes/finance_notes/aaai-2026-37075.md) · [4](../indexes/finance_notes/2026.acl-long.262.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 连接结构提取、数值一致性和跨文档事实核验，检验版式、语言和报告规则变化带来的影响。

### English

**Problem and subdirections.** This task extracts and interprets facts, entities, relations, events and document structure, including evidence-grounded summaries and reports. Layout understanding and financial semantics need separate treatment.

**Current coverage and methods.** This page covers only Main / application. Frequent subcategories: Table, Chart and Document Understanding / 表格、图表及文档理解 (50); Entity and Relation Extraction / 实体与关系抽取 (28); Financial Summarization and Report Generation / 金融摘要与报告生成 (26); Financial Text Classification / 金融文本分类 (21); Report and Disclosure Understanding / 财报与公告理解 (20). Recorded methods: Language Models & LLM / 语言模型与LLM (57); Representation Learning / 表征学习 (24); Uncertainty & Robustness / 不确定性与鲁棒性 (19); Multimodal Learning / 多模态学习 (12); Retrieval & RAG / 检索与RAG (11). Counts overlap and are not performance rankings.

**Data and evaluation.** Measure structural extraction, numerical faithfulness, evidence coverage and layout shift. Representative abstracts, financial evidence and original sources are linked at [1](../indexes/finance_notes/2021.acl-long.201.md) · [2](../indexes/finance_notes/D18-1476.md) · [3](../indexes/finance_notes/aaai-2026-37075.md) · [4](../indexes/finance_notes/2026.acl-long.262.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Connect structural extraction, numerical consistency and cross-document verification, testing shifts in layouts, languages and reporting rules.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. LayoutLMv2: Multi-modal Pre-training for Visually-rich Document Understanding](../indexes/finance_notes/2021.acl-long.201.md) · ACL 2021 | 联合文字、图像及空间关系的预训练<br>Joint text, image and spatial pretraining | 通用文档基准与金融语义任务不同<br>General document benchmarks differ from financial semantic tasks |
| [2. Chargrid: Towards Understanding 2D Documents](../indexes/finance_notes/D18-1476.md) · EMNLP 2018 | 二维字符网格支持发票字段抽取<br>Two-dimensional character grids support invoice extraction | 发票布局实验不是所有金融文档的证明<br>Invoice-layout results do not establish universal document coverage |
| [3. TermGPT: Multi-Level Contrastive Fine-Tuning for Terminology Adaptation in Legal and Financial Domains](../indexes/finance_notes/aaai-2026-37075.md) · AAAI 2026 | 研究主题：TermGPT: Multi-Level Contrastive Fine-Tuning for Terminology Adaptation in Legal and Financial Domains<br>Research topic: TermGPT: Multi-Level Contrastive Fine-Tuning for Terminology Adaptation in Legal and Financial Domains | 按原文的任务、数据和实验设置解释结果。<br>Interpret results within the original task, data and experimental setting. |
| [4. Revisit What You See: Revealing Visual Semantics in Vision Tokens to Guide LVLM Decoding](../indexes/finance_notes/2026.acl-long.262.md) · ACL 2026 | 研究主题：Revisit What You See: Revealing Visual Semantics in Vision Tokens to Guide LVLM Decoding<br>Research topic: Revisit What You See: Revealing Visual Semantics in Vision Tokens to Guide LVLM Decoding | 按原文的任务、数据和实验设置解释结果。<br>Interpret results within the original task, data and experimental setting. |
