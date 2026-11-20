# Financial Question Answering / 金融问答

Answer financial questions and perform numerical, table or conversational reasoning. / 金融问题回答及数值、表格、对话推理。

19 Findings long papers. Topic memberships can overlap.

[All topics](../ai_for_finance.md) · [Classification definitions](../finance_taxonomy.md) · [CSV](financial_qa.csv) · [Excel](../../finance_catalog.xlsx)

<!-- task-summary:start -->

## Research summary / 研究总结

**Financial Question Answering / 金融问答 · Findings / Core**

2026-11-20 · 19 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 围绕金融问题寻找证据并生成事实答案、数值答案或可执行推理。文本与表格联合推理、跨文档问答和多轮对话需要不同的证据对齐方式。

**当前收录与方法。** 本页仅总结 Findings / core 中的论文。当前较常见的子分类：Numerical Calculation and Program Reasoning / 数值计算与程序推理 (18); Financial Factual QA / 金融事实问答 (9); Multi-Document and Multi-Hop QA / 多文档与多跳问答 (4); Chart and Multimodal QA / 图表及多模态问答 (2); Table-and-Text QA / 表格与文本联合问答 (1)。已标注的方法：Language Models & LLM / 语言模型与LLM (14); Retrieval & RAG / 检索与RAG (8); Multimodal Learning / 多模态学习 (3); Uncertainty & Robustness / 不确定性与鲁棒性 (3); Tabular Learning / 表格学习 (2)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 分别检查答案、推理程序、证据引用及跨表跨文档一致性。 代表论文的摘要、金融关联证据及原文链接见 [1](../finance_notes/2026.findings-acl.1639.md) · [2](../finance_notes/2026.findings-acl.2151.md) · [3](../finance_notes/2026.findings-acl.1255.md) · [4](../finance_notes/2026.findings-emnlp.2384.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 将答案正确性、数值单位、推理步骤和引用忠实性分别验证，研究拒答与不完整用户信息下的可靠性。

### English

**Problem and subdirections.** Financial QA finds evidence and produces factual answers, numerical answers or executable reasoning. Table-text reasoning, multi-document QA and dialogue require different forms of evidence alignment.

**Current coverage and methods.** This page covers only Findings / core. Frequent subcategories: Numerical Calculation and Program Reasoning / 数值计算与程序推理 (18); Financial Factual QA / 金融事实问答 (9); Multi-Document and Multi-Hop QA / 多文档与多跳问答 (4); Chart and Multimodal QA / 图表及多模态问答 (2); Table-and-Text QA / 表格与文本联合问答 (1). Recorded methods: Language Models & LLM / 语言模型与LLM (14); Retrieval & RAG / 检索与RAG (8); Multimodal Learning / 多模态学习 (3); Uncertainty & Robustness / 不确定性与鲁棒性 (3); Tabular Learning / 表格学习 (2). Counts overlap and are not performance rankings.

**Data and evaluation.** Evaluate answers, reasoning programs, evidence attribution and cross-table/document consistency separately. Representative abstracts, financial evidence and original sources are linked at [1](../finance_notes/2026.findings-acl.1639.md) · [2](../finance_notes/2026.findings-acl.2151.md) · [3](../finance_notes/2026.findings-acl.1255.md) · [4](../finance_notes/2026.findings-emnlp.2384.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Verify answers, numerical units, reasoning steps and citation faithfulness separately, including abstention and underspecified user requests.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. FIND: Toward Multimodal Financial Reasoning and Question Answering for Indic Languages](../finance_notes/2026.findings-acl.1639.md) · ACL 2026 | 印度语言多模态数值推理及约束解码<br>Indic-language multimodal reasoning with constrained decoding | 语言和难度覆盖限定外推范围<br>Language/difficulty coverage bounds extrapolation |
| [2. Fin-STAR: Structure-as-Semantics to Resolve Implicitness in Financial Retrieval](../finance_notes/2026.findings-acl.2151.md) · ACL 2026 | 以结构语义澄清财务片段的隐含范围<br>Structural semantics clarify implicit scope in financial snippets | 结构索引构建质量影响迁移<br>Structural-index quality affects transfer |
| [3. RealFin: How Well Do LLMs Reason About Finance When Users Leave Things Unsaid?](../finance_notes/2026.findings-acl.1255.md) · ACL 2026 | 移除关键前提测试识别缺失与合理拒答<br>Remove premises to test missing-information recognition and abstention | 考试式删条件与自然用户歧义不同<br>Premise-removed exam questions differ from natural user ambiguity |
| [4. FinHopper: A Progressive Multi-Hop Benchmark for Complex Financial Agents with Step-wise Evaluation](../finance_notes/2026.findings-emnlp.2384.md) · EMNLP 2026 | 带中间答案的渐进多跳金融搜索评价<br>Progressive multihop financial search with intermediate answers | 最终答案分数会掩盖中途错误<br>Final-answer scores can conceal intermediate failures |

<!-- task-summary:end -->

## Subtopic statistics / 子方向统计

| Subtopic | Papers |
|---|---:|
| Financial Factual QA / 金融事实问答 | 9 |
| Numerical Calculation and Program Reasoning / 数值计算与程序推理 | 18 |
| Table-and-Text QA / 表格与文本联合问答 | 1 |
| Multi-Document and Multi-Hop QA / 多文档与多跳问答 | 4 |
| Chart and Multimodal QA / 图表及多模态问答 | 2 |
| Conversational Financial QA / 对话式金融问答 | 0 |

## Full paper list / 完整论文列表

| Year | Venue | Paper | Scope | Primary topic | Subtopics | Methods | Resources |
|---|---|---|---|---|---|---|---|
| 2026 | ACL | [Fin-STAR: Structure-as-Semantics to Resolve Implicitness in Financial Retrieval](../finance_notes/2026.findings-acl.2151.md) | core | Financial Retrieval / 金融检索 | Numerical Calculation and Program Reasoning / 数值计算与程序推理; Financial Semantic Matching and Ranking / 金融语义匹配与排序 | Retrieval & RAG / 检索与RAG | [PDF](../../pdfs/ACL/2026/2026.findings-acl.2151.pdf) |
| 2026 | ACL | [FinCARDS: Card-Based Analyst Reranking for Financial Document Question Answering](../finance_notes/2026.findings-acl.1244.md) | core | Financial Retrieval / 金融检索 | Numerical Calculation and Program Reasoning / 数值计算与程序推理; Financial Factual QA / 金融事实问答; Financial Document and Disclosure Retrieval / 金融文档与公告检索; Financial Semantic Matching and Ranking / 金融语义匹配与排序 | Language Models & LLM / 语言模型与LLM; Retrieval & RAG / 检索与RAG | [PDF](../../pdfs/ACL/2026/2026.findings-acl.1244.pdf) |
| 2026 | ACL | [FIND: Toward Multimodal Financial Reasoning and Question Answering for Indic Languages](../finance_notes/2026.findings-acl.1639.md) | core | Financial Question Answering / 金融问答 | Numerical Calculation and Program Reasoning / 数值计算与程序推理; Financial Factual QA / 金融事实问答; Chart and Multimodal QA / 图表及多模态问答 | Uncertainty & Robustness / 不确定性与鲁棒性 | [PDF](../../pdfs/ACL/2026/2026.findings-acl.1639.pdf) |
| 2026 | ACL | [FinMRAGBench: A Realistic and Complex Benchmark for Multi-Modal RAG in Financial Document Analysis](../finance_notes/2026.findings-acl.187.md) | core | Financial Evaluation / 金融评测 | Numerical Calculation and Program Reasoning / 数值计算与程序推理; Financial Semantic Matching and Ranking / 金融语义匹配与排序; Evidence Retrieval and Reranking for Financial RAG / 金融 RAG 的证据检索与重排序; Table, Chart and Document Understanding / 表格、图表及文档理解; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Financial Understanding and Multimodal Evaluation / 金融理解及多模态评测; Financial Document and Disclosure Retrieval / 金融文档与公告检索 | Multimodal Learning / 多模态学习; Retrieval & RAG / 检索与RAG | [PDF](../../pdfs/ACL/2026/2026.findings-acl.187.pdf) |
| 2026 | ACL | [Navigating Large-Scale Document Collections: MuDABench for Multi-Document Analytical QA](../finance_notes/2026.findings-acl.341.md) | core | Financial Evaluation / 金融评测 | Numerical Calculation and Program Reasoning / 数值计算与程序推理; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Financial Understanding and Multimodal Evaluation / 金融理解及多模态评测; Multi-Document and Multi-Hop QA / 多文档与多跳问答 | Retrieval & RAG / 检索与RAG | [PDF](../../pdfs/ACL/2026/2026.findings-acl.341.pdf) |
| 2026 | ACL | [RealFin: How Well Do LLMs Reason About Finance When Users Leave Things Unsaid?](../finance_notes/2026.findings-acl.1255.md) | core | Financial Evaluation / 金融评测 | Numerical Calculation and Program Reasoning / 数值计算与程序推理; Financial Datasets and Task Benchmarks / 金融数据集与任务基准 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/ACL/2026/2026.findings-acl.1255.pdf) |
| 2026 | ACL | [What Factors Affect LLMs and RLLMs in Financial Question Answering?](../finance_notes/2026.findings-acl.752.md) | core | Financial Question Answering / 金融问答 | Financial Factual QA / 金融事实问答 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/ACL/2026/2026.findings-acl.752.pdf) |
| 2026 | EMNLP | [FinAcumen: Financial Multimodal Reasoning via Self-Evolving Experience Memory Harness](../finance_notes/2026.findings-emnlp.2357.md) | core | Financial Question Answering / 金融问答 | Numerical Calculation and Program Reasoning / 数值计算与程序推理; Table, Chart and Document Understanding / 表格、图表及文档理解; Chart and Multimodal QA / 图表及多模态问答 | Language Models & LLM / 语言模型与LLM; Uncertainty & Robustness / 不确定性与鲁棒性; Multimodal Learning / 多模态学习; Retrieval & RAG / 检索与RAG | [PDF](../../pdfs/EMNLP/2026/2026.findings-emnlp.2357.pdf) |
| 2026 | EMNLP | [FinHopper: A Progressive Multi-Hop Benchmark for Complex Financial Agents with Step-wise Evaluation](../finance_notes/2026.findings-emnlp.2384.md) | core | Financial Evaluation / 金融评测 | Numerical Calculation and Program Reasoning / 数值计算与程序推理; Financial Factual QA / 金融事实问答; Financial Semantic Matching and Ranking / 金融语义匹配与排序; Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Financial Decision and Agent Evaluation / 金融决策与智能体评测; Evaluation Protocols and Metrics / 评测协议与指标; Trading Strategies and Buy/Sell Decisions / 交易策略与买卖决策; Multi-Document and Multi-Hop QA / 多文档与多跳问答 | Language Models & LLM / 语言模型与LLM; Retrieval & RAG / 检索与RAG | [PDF](../../pdfs/EMNLP/2026/2026.findings-emnlp.2384.pdf) |
| 2026 | EMNLP | [STQA: A Benchmark for Stock-Focused Tabular Question Answering over Historical and Forecasted Data](../finance_notes/2026.findings-emnlp.869.md) | core | Financial Evaluation / 金融评测 | Stock Price and Return Prediction / 股票价格与收益预测; Numerical Calculation and Program Reasoning / 数值计算与程序推理; Financial Datasets and Task Benchmarks / 金融数据集与任务基准 | Language Models & LLM / 语言模型与LLM; Uncertainty & Robustness / 不确定性与鲁棒性; Tabular Learning / 表格学习; Retrieval & RAG / 检索与RAG | [PDF](../../pdfs/EMNLP/2026/2026.findings-emnlp.869.pdf) |
| 2025 | ACL | [XFinBench: Benchmarking LLMs in Complex Financial Problem Solving and Reasoning](../finance_notes/2025.findings-acl.457.md) | core | Financial Evaluation / 金融评测 | Numerical Calculation and Program Reasoning / 数值计算与程序推理; Financial Factual QA / 金融事实问答; Financial Datasets and Task Benchmarks / 金融数据集与任务基准 | Language Models & LLM / 语言模型与LLM; Multimodal Learning / 多模态学习 | [PDF](../../pdfs/ACL/2025/2025.findings-acl.457.pdf) |
| 2025 | EMNLP | [David vs. Goliath: Cost-Efficient Financial QA via Cascaded Multi-Agent Reasoning](../finance_notes/2025.findings-emnlp.225.md) | core | Financial Question Answering / 金融问答 | Numerical Calculation and Program Reasoning / 数值计算与程序推理; Financial Factual QA / 金融事实问答 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/EMNLP/2025/2025.findings-emnlp.225.pdf) |
| 2025 | EMNLP | [FinLFQA: Evaluating Attributed Text Generation of LLMs in Financial Long-Form Question Answering](../finance_notes/2025.findings-emnlp.908.md) | core | Financial Evaluation / 金融评测 | Numerical Calculation and Program Reasoning / 数值计算与程序推理; Financial Factual QA / 金融事实问答; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Evaluation Protocols and Metrics / 评测协议与指标; Multi-Document and Multi-Hop QA / 多文档与多跳问答 | Language Models & LLM / 语言模型与LLM; Retrieval & RAG / 检索与RAG | [PDF](../../pdfs/EMNLP/2025/2025.findings-emnlp.908.pdf) |
| 2025 | EMNLP | [One More Question is Enough, Expert Question Decomposition (EQD) Model for Domain Quantitative Reasoning](../finance_notes/2025.findings-emnlp.1108.md) | core | Financial Question Answering / 金融问答 | Numerical Calculation and Program Reasoning / 数值计算与程序推理 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/EMNLP/2025/2025.findings-emnlp.1108.pdf) |
| 2024 | ACL | [EconNLI: Evaluating Large Language Models on Economics Reasoning](../finance_notes/2024.findings-acl.58.md) | core | Financial Evaluation / 金融评测 | General Sequence Forecasting / 通用序列预测; Numerical Calculation and Program Reasoning / 数值计算与程序推理; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Financial Understanding and Multimodal Evaluation / 金融理解及多模态评测; Evaluation Protocols and Metrics / 评测协议与指标 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/ACL/2024/2024.findings-acl.58.pdf) |
| 2024 | ACL | [Evaluating LLMs’ Mathematical Reasoning in Financial Document Question Answering](../finance_notes/2024.findings-acl.231.md) | core | Financial Evaluation / 金融评测 | Numerical Calculation and Program Reasoning / 数值计算与程序推理; Financial Factual QA / 金融事实问答; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Numerical Reasoning and Calculation Evaluation / 数值推理与计算评测; Financial Understanding and Multimodal Evaluation / 金融理解及多模态评测; Evaluation Protocols and Metrics / 评测协议与指标 | Language Models & LLM / 语言模型与LLM; Tabular Learning / 表格学习 | [PDF](../../pdfs/ACL/2024/2024.findings-acl.231.pdf) |
| 2024 | EMNLP | [Enhancing Arguments Recognition for Financial Mathematical Reasoning over Hybrid Data](../finance_notes/2024.findings-emnlp.228.md) | core | Financial Question Answering / 金融问答 | Numerical Calculation and Program Reasoning / 数值计算与程序推理; Table-and-Text QA / 表格与文本联合问答 |  | [PDF](../../pdfs/EMNLP/2024/2024.findings-emnlp.228.pdf) |
| 2024 | EMNLP | [Fine-tuning Smaller Language Models for Question Answering over Financial Documents](../finance_notes/2024.findings-emnlp.617.md) | core | Financial Question Answering / 金融问答 | Numerical Calculation and Program Reasoning / 数值计算与程序推理; Financial Factual QA / 金融事实问答 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/EMNLP/2024/2024.findings-emnlp.617.pdf) |
| 2024 | EMNLP | [LLMs Cannot (Yet) Match the Specificity and Simplicity of Online Communities in Long Form Question Answering](../finance_notes/2024.findings-emnlp.111.md) | core | Financial Question Answering / 金融问答 | Numerical Calculation and Program Reasoning / 数值计算与程序推理; Multi-Document and Multi-Hop QA / 多文档与多跳问答 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/EMNLP/2024/2024.findings-emnlp.111.pdf) |
