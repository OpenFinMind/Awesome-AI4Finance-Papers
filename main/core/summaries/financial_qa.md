## Research summary / 研究总结

**Financial Question Answering / 金融问答 · Main / Core**

2026-11-20 · 32 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 围绕金融问题寻找证据并生成事实答案、数值答案或可执行推理。文本与表格联合推理、跨文档问答和多轮对话需要不同的证据对齐方式。

**当前收录与方法。** 本页仅总结 Main / core 中的论文。当前较常见的子分类：Numerical Calculation and Program Reasoning / 数值计算与程序推理 (29); Financial Factual QA / 金融事实问答 (9); Chart and Multimodal QA / 图表及多模态问答 (4); Multi-Document and Multi-Hop QA / 多文档与多跳问答 (3); Conversational Financial QA / 对话式金融问答 (2)。已标注的方法：Language Models & LLM / 语言模型与LLM (27); Retrieval & RAG / 检索与RAG (12); Uncertainty & Robustness / 不确定性与鲁棒性 (6); Tabular Learning / 表格学习 (5); Multimodal Learning / 多模态学习 (4)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 分别检查答案、推理程序、证据引用及跨表跨文档一致性。 代表论文的摘要、金融关联证据及原文链接见 [1](../indexes/finance_notes/2026.acl-long.662.md) · [2](../indexes/finance_notes/2026.acl-long.770.md) · [3](../indexes/finance_notes/2022.emnlp-main.421.md) · [4](../indexes/finance_notes/2021.acl-long.254.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 将答案正确性、数值单位、推理步骤和引用忠实性分别验证，研究拒答与不完整用户信息下的可靠性。

### English

**Problem and subdirections.** Financial QA finds evidence and produces factual answers, numerical answers or executable reasoning. Table-text reasoning, multi-document QA and dialogue require different forms of evidence alignment.

**Current coverage and methods.** This page covers only Main / core. Frequent subcategories: Numerical Calculation and Program Reasoning / 数值计算与程序推理 (29); Financial Factual QA / 金融事实问答 (9); Chart and Multimodal QA / 图表及多模态问答 (4); Multi-Document and Multi-Hop QA / 多文档与多跳问答 (3); Conversational Financial QA / 对话式金融问答 (2). Recorded methods: Language Models & LLM / 语言模型与LLM (27); Retrieval & RAG / 检索与RAG (12); Uncertainty & Robustness / 不确定性与鲁棒性 (6); Tabular Learning / 表格学习 (5); Multimodal Learning / 多模态学习 (4). Counts overlap and are not performance rankings.

**Data and evaluation.** Evaluate answers, reasoning programs, evidence attribution and cross-table/document consistency separately. Representative abstracts, financial evidence and original sources are linked at [1](../indexes/finance_notes/2026.acl-long.662.md) · [2](../indexes/finance_notes/2026.acl-long.770.md) · [3](../indexes/finance_notes/2022.emnlp-main.421.md) · [4](../indexes/finance_notes/2021.acl-long.254.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Verify answers, numerical units, reasoning steps and citation faithfulness separately, including abstention and underspecified user requests.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. FinChain: A Symbolic Benchmark for Verifiable Chain-of-Thought Financial Reasoning](../indexes/finance_notes/2026.acl-long.662.md) · ACL 2026 | 可执行模板及答案—步骤联合验证<br>Executable templates jointly verify answers and reasoning steps | 符号模板范围与真实文件难度不同<br>Symbolic-template scope differs from real-document difficulty |
| [2. MultiFinBen: Benchmarking Large Language Models for Multilingual and Multimodal Financial Application](../indexes/finance_notes/2026.acl-long.770.md) · ACL 2026 | 多语言、多模态与专家难度的金融评价<br>Multilingual, multimodal, expert-oriented financial evaluation | 任务选择和语言覆盖影响总分<br>Task selection and language coverage affect aggregate scores |
| [3. ConvFinQA: Exploring the Chain of Numerical Reasoning in Conversational Finance Question Answering](../indexes/finance_notes/2022.emnlp-main.421.md) · EMNLP 2022 | 对话中的长程多步数值推理<br>Long-range numerical reasoning in conversations | 跨轮上下文与单轮能力须分别评价<br>Evaluate conversational context separately from single-turn reasoning |
| [4. TAT-QA: A Question Answering Benchmark on a Hybrid of Tabular and Textual Content in Finance](../indexes/finance_notes/2021.acl-long.254.md) · ACL 2021 | 表格—文本联合抽取后执行聚合运算<br>Extract hybrid evidence and apply aggregation operations | 需要区分证据错误与运算错误<br>Separate evidence-selection errors from arithmetic errors |
