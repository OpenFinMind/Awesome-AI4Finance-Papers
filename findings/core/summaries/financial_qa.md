## Research summary / 研究总结

**Financial Question Answering / 金融问答 · Findings / Core**

2026-11-20 · 19 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 围绕金融问题寻找证据并生成事实答案、数值答案或可执行推理。文本与表格联合推理、跨文档问答和多轮对话需要不同的证据对齐方式。

**当前收录与方法。** 本页仅总结 Findings / core 中的论文。当前较常见的子分类：Numerical Calculation and Program Reasoning / 数值计算与程序推理 (18); Financial Factual QA / 金融事实问答 (9); Multi-Document and Multi-Hop QA / 多文档与多跳问答 (4); Chart and Multimodal QA / 图表及多模态问答 (2); Table-and-Text QA / 表格与文本联合问答 (1)。已标注的方法：Language Models & LLM / 语言模型与LLM (14); Retrieval & RAG / 检索与RAG (8); Multimodal Learning / 多模态学习 (3); Uncertainty & Robustness / 不确定性与鲁棒性 (3); Tabular Learning / 表格学习 (2)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 分别检查答案、推理程序、证据引用及跨表跨文档一致性。 代表论文的摘要、金融关联证据及原文链接见 [1](../indexes/finance_notes/2026.findings-acl.1639.md) · [2](../indexes/finance_notes/2026.findings-acl.2151.md) · [3](../indexes/finance_notes/2026.findings-acl.1255.md) · [4](../indexes/finance_notes/2026.findings-emnlp.2384.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 将答案正确性、数值单位、推理步骤和引用忠实性分别验证，研究拒答与不完整用户信息下的可靠性。

### English

**Problem and subdirections.** Financial QA finds evidence and produces factual answers, numerical answers or executable reasoning. Table-text reasoning, multi-document QA and dialogue require different forms of evidence alignment.

**Current coverage and methods.** This page covers only Findings / core. Frequent subcategories: Numerical Calculation and Program Reasoning / 数值计算与程序推理 (18); Financial Factual QA / 金融事实问答 (9); Multi-Document and Multi-Hop QA / 多文档与多跳问答 (4); Chart and Multimodal QA / 图表及多模态问答 (2); Table-and-Text QA / 表格与文本联合问答 (1). Recorded methods: Language Models & LLM / 语言模型与LLM (14); Retrieval & RAG / 检索与RAG (8); Multimodal Learning / 多模态学习 (3); Uncertainty & Robustness / 不确定性与鲁棒性 (3); Tabular Learning / 表格学习 (2). Counts overlap and are not performance rankings.

**Data and evaluation.** Evaluate answers, reasoning programs, evidence attribution and cross-table/document consistency separately. Representative abstracts, financial evidence and original sources are linked at [1](../indexes/finance_notes/2026.findings-acl.1639.md) · [2](../indexes/finance_notes/2026.findings-acl.2151.md) · [3](../indexes/finance_notes/2026.findings-acl.1255.md) · [4](../indexes/finance_notes/2026.findings-emnlp.2384.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Verify answers, numerical units, reasoning steps and citation faithfulness separately, including abstention and underspecified user requests.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. FIND: Toward Multimodal Financial Reasoning and Question Answering for Indic Languages](../indexes/finance_notes/2026.findings-acl.1639.md) · ACL 2026 | 印度语言多模态数值推理及约束解码<br>Indic-language multimodal reasoning with constrained decoding | 语言和难度覆盖限定外推范围<br>Language/difficulty coverage bounds extrapolation |
| [2. Fin-STAR: Structure-as-Semantics to Resolve Implicitness in Financial Retrieval](../indexes/finance_notes/2026.findings-acl.2151.md) · ACL 2026 | 以结构语义澄清财务片段的隐含范围<br>Structural semantics clarify implicit scope in financial snippets | 结构索引构建质量影响迁移<br>Structural-index quality affects transfer |
| [3. RealFin: How Well Do LLMs Reason About Finance When Users Leave Things Unsaid?](../indexes/finance_notes/2026.findings-acl.1255.md) · ACL 2026 | 移除关键前提测试识别缺失与合理拒答<br>Remove premises to test missing-information recognition and abstention | 考试式删条件与自然用户歧义不同<br>Premise-removed exam questions differ from natural user ambiguity |
| [4. FinHopper: A Progressive Multi-Hop Benchmark for Complex Financial Agents with Step-wise Evaluation](../indexes/finance_notes/2026.findings-emnlp.2384.md) · EMNLP 2026 | 带中间答案的渐进多跳金融搜索评价<br>Progressive multihop financial search with intermediate answers | 最终答案分数会掩盖中途错误<br>Final-answer scores can conceal intermediate failures |
