# Financial Question Answering / 金融问答

Answer financial questions and perform numerical, table or conversational reasoning. / 金融问题回答及数值、表格、对话推理。

12 Findings long papers. Topic memberships can overlap.

[All topics](../ai_for_finance.md) · [Classification definitions](../finance_taxonomy.md) · [CSV](financial_qa.csv) · [Excel](../../finance_catalog.xlsx)

<!-- task-summary:start -->

## Research summary / 研究总结

**Financial Question Answering / 金融问答 · Findings / Application**

2026-11-20 · 12 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 围绕金融问题寻找证据并生成事实答案、数值答案或可执行推理。文本与表格联合推理、跨文档问答和多轮对话需要不同的证据对齐方式。

**当前收录与方法。** 本页仅总结 Findings / application 中的论文。当前较常见的子分类：Numerical Calculation and Program Reasoning / 数值计算与程序推理 (9); Financial Factual QA / 金融事实问答 (5); Table-and-Text QA / 表格与文本联合问答 (2); Multi-Document and Multi-Hop QA / 多文档与多跳问答 (2); Conversational Financial QA / 对话式金融问答 (1)。已标注的方法：Language Models & LLM / 语言模型与LLM (9); Retrieval & RAG / 检索与RAG (6); Uncertainty & Robustness / 不确定性与鲁棒性 (2); Tabular Learning / 表格学习 (2); Generative Modeling / 生成建模 (2)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 分别检查答案、推理程序、证据引用及跨表跨文档一致性。 代表论文的摘要、金融关联证据及原文链接见 [1](../finance_notes/2026.findings-emnlp.845.md) · [2](../finance_notes/2026.findings-emnlp.975.md) · [3](../finance_notes/2026.findings-emnlp.1736.md) · [4](../finance_notes/2026.findings-emnlp.438.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 将答案正确性、数值单位、推理步骤和引用忠实性分别验证，研究拒答与不完整用户信息下的可靠性。

### English

**Problem and subdirections.** Financial QA finds evidence and produces factual answers, numerical answers or executable reasoning. Table-text reasoning, multi-document QA and dialogue require different forms of evidence alignment.

**Current coverage and methods.** This page covers only Findings / application. Frequent subcategories: Numerical Calculation and Program Reasoning / 数值计算与程序推理 (9); Financial Factual QA / 金融事实问答 (5); Table-and-Text QA / 表格与文本联合问答 (2); Multi-Document and Multi-Hop QA / 多文档与多跳问答 (2); Conversational Financial QA / 对话式金融问答 (1). Recorded methods: Language Models & LLM / 语言模型与LLM (9); Retrieval & RAG / 检索与RAG (6); Uncertainty & Robustness / 不确定性与鲁棒性 (2); Tabular Learning / 表格学习 (2); Generative Modeling / 生成建模 (2). Counts overlap and are not performance rankings.

**Data and evaluation.** Evaluate answers, reasoning programs, evidence attribution and cross-table/document consistency separately. Representative abstracts, financial evidence and original sources are linked at [1](../finance_notes/2026.findings-emnlp.845.md) · [2](../finance_notes/2026.findings-emnlp.975.md) · [3](../finance_notes/2026.findings-emnlp.1736.md) · [4](../finance_notes/2026.findings-emnlp.438.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Verify answers, numerical units, reasoning steps and citation faithfulness separately, including abstention and underspecified user requests.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. KnowMT-Bench: Benchmarking Knowledge-Intensive Long-Form Question Answering in Multi-Turn Dialogues](../finance_notes/2026.findings-emnlp.845.md) · EMNLP 2026 | 研究主题：KnowMT-Bench: Benchmarking Knowledge-Intensive Long-Form Question Answering in Multi-Turn Dialogues<br>Research topic: KnowMT-Bench: Benchmarking Knowledge-Intensive Long-Form Question Answering in Multi-Turn Dialogues | 按原文的任务、数据和实验设置解释结果。<br>Interpret results within the original task, data and experimental setting. |
| [2. MoE Sparsity Begets Monosemanticity: Insights into Understanding and Fine-Tuning](../finance_notes/2026.findings-emnlp.975.md) · EMNLP 2026 | 研究主题：MoE Sparsity Begets Monosemanticity: Insights into Understanding and Fine-Tuning<br>Research topic: MoE Sparsity Begets Monosemanticity: Insights into Understanding and Fine-Tuning | 按原文的任务、数据和实验设置解释结果。<br>Interpret results within the original task, data and experimental setting. |
| [3. RELOOP: Recursive Retrieval with Multi-Hop Reasoner and Planners for Heterogeneous QA](../finance_notes/2026.findings-emnlp.1736.md) · EMNLP 2026 | 研究主题：RELOOP: Recursive Retrieval with Multi-Hop Reasoner and Planners for Heterogeneous QA<br>Research topic: RELOOP: Recursive Retrieval with Multi-Hop Reasoner and Planners for Heterogeneous QA | 按原文的任务、数据和实验设置解释结果。<br>Interpret results within the original task, data and experimental setting. |
| [4. Synthetic Mixed Training: Scaling Parametric Knowledge Acquisition Beyond RAG](../finance_notes/2026.findings-emnlp.438.md) · EMNLP 2026 | 研究主题：Synthetic Mixed Training: Scaling Parametric Knowledge Acquisition Beyond RAG<br>Research topic: Synthetic Mixed Training: Scaling Parametric Knowledge Acquisition Beyond RAG | 按原文的任务、数据和实验设置解释结果。<br>Interpret results within the original task, data and experimental setting. |

<!-- task-summary:end -->

## Subtopic statistics / 子方向统计

| Subtopic | Papers |
|---|---:|
| Financial Factual QA / 金融事实问答 | 5 |
| Numerical Calculation and Program Reasoning / 数值计算与程序推理 | 9 |
| Table-and-Text QA / 表格与文本联合问答 | 2 |
| Multi-Document and Multi-Hop QA / 多文档与多跳问答 | 2 |
| Chart and Multimodal QA / 图表及多模态问答 | 0 |
| Conversational Financial QA / 对话式金融问答 | 1 |

## Full paper list / 完整论文列表

| Year | Venue | Paper | Scope | Primary topic | Subtopics | Methods | Resources |
|---|---|---|---|---|---|---|---|
| 2026 | EMNLP | [KnowMT-Bench: Benchmarking Knowledge-Intensive Long-Form Question Answering in Multi-Turn Dialogues](../finance_notes/2026.findings-emnlp.845.md) | application | Financial Question Answering / 金融问答 | Financial Factual QA / 金融事实问答; Multi-Document and Multi-Hop QA / 多文档与多跳问答; Conversational Financial QA / 对话式金融问答 | Language Models & LLM / 语言模型与LLM; Retrieval & RAG / 检索与RAG | [PDF](../../pdfs/EMNLP/2026/2026.findings-emnlp.845.pdf) |
| 2026 | EMNLP | [MoE Sparsity Begets Monosemanticity: Insights into Understanding and Fine-Tuning](../finance_notes/2026.findings-emnlp.975.md) | application | Financial Question Answering / 金融问答 | Numerical Calculation and Program Reasoning / 数值计算与程序推理 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/EMNLP/2026/2026.findings-emnlp.975.pdf) |
| 2026 | EMNLP | [RELOOP: Recursive Retrieval with Multi-Hop Reasoner and Planners for Heterogeneous QA](../finance_notes/2026.findings-emnlp.1736.md) | application | Financial Question Answering / 金融问答 | Numerical Calculation and Program Reasoning / 数值计算与程序推理; Multi-Document and Multi-Hop QA / 多文档与多跳问答 | Retrieval & RAG / 检索与RAG | [PDF](../../pdfs/EMNLP/2026/2026.findings-emnlp.1736.pdf) |
| 2026 | EMNLP | [Synthetic Mixed Training: Scaling Parametric Knowledge Acquisition Beyond RAG](../finance_notes/2026.findings-emnlp.438.md) | application | Financial Question Answering / 金融问答 | Financial Factual QA / 金融事实问答 | Language Models & LLM / 语言模型与LLM; Generative Modeling / 生成建模; Retrieval & RAG / 检索与RAG | [PDF](../../pdfs/EMNLP/2026/2026.findings-emnlp.438.pdf) |
| 2026 | EMNLP | [When and How Should an Agent Clarify? CIGAsk: Teaching LLMs to Clarify via Counterfactual Information Gain](../finance_notes/2026.findings-emnlp.314.md) | application | Financial Question Answering / 金融问答 | Financial Factual QA / 金融事实问答; Numerical Calculation and Program Reasoning / 数值计算与程序推理 | Language Models & LLM / 语言模型与LLM; Reinforcement Learning / 强化学习 | [PDF](../../pdfs/EMNLP/2026/2026.findings-emnlp.314.pdf) |
| 2025 | EMNLP | [DaMoC: Efficiently Selecting the Optimal Large Language Model for Fine-tuning Domain Tasks Based on Data and Model Compression](../finance_notes/2025.findings-emnlp.699.md) | application | Financial Question Answering / 金融问答 | Financial Factual QA / 金融事实问答 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/EMNLP/2025/2025.findings-emnlp.699.pdf) |
| 2025 | EMNLP | [MULTITAT: Benchmarking Multilingual Table-and-Text Question Answering](../finance_notes/2025.findings-emnlp.33.md) | application | Financial Question Answering / 金融问答 | Numerical Calculation and Program Reasoning / 数值计算与程序推理; Table-and-Text QA / 表格与文本联合问答 |  | [PDF](../../pdfs/EMNLP/2025/2025.findings-emnlp.33.pdf) |
| 2025 | EMNLP | [OkraLong: A Flexible Retrieval-Augmented Framework for Long-Text Question Answering](../finance_notes/2025.findings-emnlp.890.md) | application | Financial Question Answering / 金融问答 | Numerical Calculation and Program Reasoning / 数值计算与程序推理 | Language Models & LLM / 语言模型与LLM; Retrieval & RAG / 检索与RAG | [PDF](../../pdfs/EMNLP/2025/2025.findings-emnlp.890.pdf) |
| 2025 | EMNLP | [Select to Know: An Internal-External Knowledge Self-Selection Framework for Domain-Specific Question Answering](../finance_notes/2025.findings-emnlp.565.md) | application | Financial Question Answering / 金融问答 | Numerical Calculation and Program Reasoning / 数值计算与程序推理; Financial Factual QA / 金融事实问答 | Language Models & LLM / 语言模型与LLM; Generative Modeling / 生成建模; Retrieval & RAG / 检索与RAG; Representation Learning / 表征学习 | [PDF](../../pdfs/EMNLP/2025/2025.findings-emnlp.565.pdf) |
| 2025 | EMNLP | [TabDSR: Decompose, Sanitize, and Reason for Complex Numerical Reasoning in Tabular Data](../finance_notes/2025.findings-emnlp.169.md) | application | Financial Question Answering / 金融问答 | Numerical Calculation and Program Reasoning / 数值计算与程序推理 | Language Models & LLM / 语言模型与LLM; Uncertainty & Robustness / 不确定性与鲁棒性; Tabular Learning / 表格学习 | [PDF](../../pdfs/EMNLP/2025/2025.findings-emnlp.169.pdf) |
| 2024 | ACL | [DBQR-QA: A Question Answering Dataset on a Hybrid of Database Querying and Reasoning](../finance_notes/2024.findings-acl.900.md) | application | Financial Question Answering / 金融问答 | Numerical Calculation and Program Reasoning / 数值计算与程序推理; Table-and-Text QA / 表格与文本联合问答 | Language Models & LLM / 语言模型与LLM; Retrieval & RAG / 检索与RAG | [PDF](../../pdfs/ACL/2024/2024.findings-acl.900.pdf) |
| 2023 | ACL | [Hypothetical Training for Robust Machine Reading Comprehension of Tabular Context](../finance_notes/2023.findings-acl.79.md) | application | Financial Question Answering / 金融问答 | Numerical Calculation and Program Reasoning / 数值计算与程序推理 | Uncertainty & Robustness / 不确定性与鲁棒性; Tabular Learning / 表格学习 | [PDF](../../pdfs/ACL/2023/2023.findings-acl.79.pdf) |
