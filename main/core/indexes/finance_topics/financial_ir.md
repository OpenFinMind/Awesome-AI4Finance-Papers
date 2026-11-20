# Financial Retrieval / 金融检索

Retrieve, embed, rerank and ground financial evidence, including financial RAG. / 金融证据检索、嵌入、重排及 RAG。

17 Main long papers. Topic memberships can overlap.

[All topics](../ai_for_finance.md) · [Classification definitions](../finance_taxonomy.md) · [CSV](financial_ir.csv) · [Excel](../../finance_catalog.xlsx)

<!-- task-summary:start -->

## Research summary / 研究总结

**Financial Retrieval / 金融检索 · Main / Core**

2026-11-20 · 17 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 主要贡献是金融证据的表示、搜索、过滤或排序。RAG 的检索模块与最终问答结果分别评价；检索输入可为文本、表格、图表或数值向量。

**当前收录与方法。** 本页仅总结 Main / core 中的论文。当前较常见的子分类：Financial Semantic Matching and Ranking / 金融语义匹配与排序 (12); Evidence Retrieval and Reranking for Financial RAG / 金融 RAG 的证据检索与重排序 (10); Chart and Multimodal Retrieval / 图表与多模态检索 (1); Financial Document and Disclosure Retrieval / 金融文档与公告检索 (1)。已标注的方法：Language Models & LLM / 语言模型与LLM (11); Retrieval & RAG / 检索与RAG (10); Generative Modeling / 生成建模 (4); Optimization & Numerical Methods / 优化与数值方法 (3); Representation Learning / 表征学习 (2)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 分开报告检索召回、重排质量、引用忠实性和最终回答质量。 代表论文的摘要、金融关联证据及原文链接见 [1](../finance_notes/2023.emnlp-main.234.md) · [2](../finance_notes/2026.acl-long.492.md) · [3](../finance_notes/2026.acl-long.265.md) · [4](../finance_notes/iclr-2026-8AJbbbe2ni.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 研究时间有效性、跨文档覆盖和数值敏感性，分析证据缺失、召回失败与生成错误各自的影响。

### English

**Problem and subdirections.** The main contribution represents, searches, filters or ranks financial evidence. RAG retrieval and final QA need separate evaluation; inputs may be text, tables, charts or numerical vectors.

**Current coverage and methods.** This page covers only Main / core. Frequent subcategories: Financial Semantic Matching and Ranking / 金融语义匹配与排序 (12); Evidence Retrieval and Reranking for Financial RAG / 金融 RAG 的证据检索与重排序 (10); Chart and Multimodal Retrieval / 图表与多模态检索 (1); Financial Document and Disclosure Retrieval / 金融文档与公告检索 (1). Recorded methods: Language Models & LLM / 语言模型与LLM (11); Retrieval & RAG / 检索与RAG (10); Generative Modeling / 生成建模 (4); Optimization & Numerical Methods / 优化与数值方法 (3); Representation Learning / 表征学习 (2). Counts overlap and are not performance rankings.

**Data and evaluation.** Report retrieval recall, reranking, citation faithfulness and answer quality separately. Representative abstracts, financial evidence and original sources are linked at [1](../finance_notes/2023.emnlp-main.234.md) · [2](../finance_notes/2026.acl-long.492.md) · [3](../finance_notes/2026.acl-long.265.md) · [4](../finance_notes/iclr-2026-8AJbbbe2ni.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Study temporal validity, cross-document coverage and numerical sensitivity, separating missing evidence, retrieval failure and generation errors.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. TRAVEL: Tag-Aware Conversational FAQ Retrieval via Reinforcement Learning](../finance_notes/2023.emnlp-main.234.md) · EMNLP 2023 | 标签与 RL 减少 FAQ 对话中的噪声<br>Tags and RL reduce noise in conversational FAQ retrieval | 检索成功不代表完成银行业务操作<br>Retrieval success does not establish workflow completion |
| [2. All That Glisters Is Not Gold: A Benchmark for Reference-Free Counterfactual Financial Misinformation Detection](../finance_notes/2026.acl-long.492.md) · ACL 2026 | 测试无外部参照时的金融虚假信息识别<br>Test financial misinformation without external references | 有配对参照的成功不代表无参照能力<br>Paired-reference success does not establish reference-free ability |
| [3. FinSight: Towards Real-World Financial Deep Research](../finance_notes/2026.acl-long.265.md) · ACL 2026 | 可执行分析、来源引用与视觉反馈的投研报告<br>Research reports with executable analysis, citations and visual feedback | 报告质量不直接验证投资预测能力<br>Report quality does not directly establish predictive investment skill |
| [4. FinSearchComp: Towards a Realistic, Expert-Level Evaluation of Financial Search and Reasoning](../finance_notes/iclr-2026-8AJbbbe2ni.md) · ICLR 2026 | 专家设计的时效搜索及复杂金融调查<br>Expert-designed timely search and complex financial investigations | 结果依赖工具、地域覆盖及检索时间<br>Results depend on tools, geographic coverage and retrieval time |

<!-- task-summary:end -->

## Subtopic statistics / 子方向统计

| Subtopic | Papers |
|---|---:|
| Financial Document and Disclosure Retrieval / 金融文档与公告检索 | 1 |
| Financial Semantic Matching and Ranking / 金融语义匹配与排序 | 12 |
| Table and Numerical Retrieval / 表格及数值信息检索 | 0 |
| Chart and Multimodal Retrieval / 图表与多模态检索 | 1 |
| Cross-Lingual Financial Retrieval / 跨语言金融检索 | 0 |
| Evidence Retrieval and Reranking for Financial RAG / 金融 RAG 的证据检索与重排序 | 10 |

## Full paper list / 完整论文列表

| Year | Venue | Paper | Scope | Primary topic | Subtopics | Methods | Resources |
|---|---|---|---|---|---|---|---|
| 2026 | ACL | [All That Glisters Is Not Gold: A Benchmark for Reference-Free Counterfactual Financial Misinformation Detection](../finance_notes/2026.acl-long.492.md) | core | Financial Evaluation / 金融评测 | Payment, Transaction and Insurance Fraud / 支付、交易及保险欺诈; Evidence Retrieval and Reranking for Financial RAG / 金融 RAG 的证据检索与重排序; Financial Datasets and Task Benchmarks / 金融数据集与任务基准 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/ACL/2026/2026.acl-long.492__All_That_Glisters_Is_Not_Gold_A_Benchmark_for_Reference_Free_Counterfactual_Financial_Misinformation_Dete.pdf) |
| 2026 | ACL | [FinKario: Event-Enhanced Automated Construction of Financial Knowledge Graph](../finance_notes/2026.acl-long.446.md) | core | Financial Evaluation / 金融评测 | Stock Price and Return Prediction / 股票价格与收益预测; Entity and Relation Extraction / 实体与关系抽取; Financial Semantic Matching and Ranking / 金融语义匹配与排序; Evidence Retrieval and Reranking for Financial RAG / 金融 RAG 的证据检索与重排序; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Financial Knowledge and Professional Evaluation / 金融知识与专业能力评测; Financial Event Detection and Linking / 金融事件识别与关联 | Language Models & LLM / 语言模型与LLM; Retrieval & RAG / 检索与RAG | [PDF](../../pdfs/ACL/2026/2026.acl-long.446__FinKario_Event_Enhanced_Automated_Construction_of_Financial_Knowledge_Graph.pdf) |
| 2026 | ACL | [FinSight: Towards Real-World Financial Deep Research](../finance_notes/2026.acl-long.265.md) | core | Financial Decision Making / 金融决策 | Financial Semantic Matching and Ranking / 金融语义匹配与排序; Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策; Risk-Return and Multi-Objective Optimization / 风险收益及多目标优化 | Generative Modeling / 生成建模; Retrieval & RAG / 检索与RAG | [PDF](../../pdfs/ACL/2026/2026.acl-long.265__FinSight_Towards_Real_World_Financial_Deep_Research.pdf) |
| 2026 | EMNLP | [The Analyst in the Prompt: Role, Retrieval, and Memory Biases in LLM Financial Analysis](../finance_notes/2026.emnlp-main.2268.md) | core | Financial Retrieval / 金融检索 | Financial Semantic Matching and Ranking / 金融语义匹配与排序; Report and Disclosure Understanding / 财报与公告理解; Financial Model and Agent Safety / 金融模型及智能体安全 | Language Models & LLM / 语言模型与LLM; Retrieval & RAG / 检索与RAG | [PDF](../../pdfs/EMNLP/2026/2026.emnlp-main.2268__The_Analyst_in_the_Prompt_Role_Retrieval_and_Memory_Biases_in_LLM_Financial_Analysis.pdf) |
| 2026 | ICLR | [FinSearchComp: Towards a Realistic, Expert-Level Evaluation of Financial Search and Reasoning](../finance_notes/iclr-2026-8AJbbbe2ni.md) | core | Financial Evaluation / 金融评测 | Financial Semantic Matching and Ranking / 金融语义匹配与排序; Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Evaluation Protocols and Metrics / 评测协议与指标 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/ICLR/2026/iclr-2026-8AJbbbe2ni__FinSearchComp_Towards_a_Realistic_Expert_Level_Evaluation_of_Financial_Search_and_Reasoning.pdf) |
| 2026 | ICML | [Global Merger-Arbitrage Forecasting with Language Models](../finance_notes/icml-2026-wDaX9bFufS.md) | core | Financial Decision Making / 金融决策 | Trading Strategies and Buy/Sell Decisions / 交易策略与买卖决策; Evidence Retrieval and Reranking for Financial RAG / 金融 RAG 的证据检索与重排序; Financial Event Detection and Linking / 金融事件识别与关联 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/ICML/2026/icml-2026-wDaX9bFufS__Global_Merger_Arbitrage_Forecasting_with_Language_Models.pdf) |
| 2026 | KDD | [NumCache: KV Cache Compression and Retrieval for Financial Document QA](../finance_notes/kdd-2026-73c0c179c05e.md) | core | Financial Question Answering / 金融问答 | Numerical Calculation and Program Reasoning / 数值计算与程序推理; Financial Semantic Matching and Ranking / 金融语义匹配与排序; Financial Document and Disclosure Retrieval / 金融文档与公告检索 | Language Models & LLM / 语言模型与LLM; Retrieval & RAG / 检索与RAG | [Online](https://doi.org/10.1145/3770855.3818131) |
| 2026 | NeurIPS | [Retrieval-Augmented Diffusion Modeling for Stochastic Discount Factor Portfolios](../finance_notes/neurips-2026-Dk8yYYJtw0.md) | core | Pricing / 定价 | Asset Pricing and Risk Premia / 资产定价与风险溢价; Asset Selection and Weight Allocation / 资产选择与权重配置; Financial Semantic Matching and Ranking / 金融语义匹配与排序; Evidence Retrieval and Reranking for Financial RAG / 金融 RAG 的证据检索与重排序 | Diffusion & Flow / 扩散与流模型; Uncertainty & Robustness / 不确定性与鲁棒性; Retrieval & RAG / 检索与RAG; Optimization & Numerical Methods / 优化与数值方法 | [PDF](../../pdfs/NeurIPS/2026/neurips-2026-Dk8yYYJtw0__Retrieval_Augmented_Diffusion_Modeling_for_Stochastic_Discount_Factor_Portfolios.pdf) |
| 2025 | EMNLP | [Financial Risk Relation Identification through Dual-view Adaptation](../finance_notes/2025.emnlp-main.1336.md) | core | Financial Risk / 金融风险 | Asset Selection and Weight Allocation / 资产选择与权重配置; Market Risk and Tail Losses / 市场风险与尾部损失; Entity and Relation Extraction / 实体与关系抽取; Evidence Retrieval and Reranking for Financial RAG / 金融 RAG 的证据检索与重排序 |  | [PDF](../../pdfs/EMNLP/2025/2025.emnlp-main.1336__Financial_Risk_Relation_Identification_through_Dual_view_Adaptation.pdf) |
| 2025 | EMNLP | [FinMTEB: Finance Massive Text Embedding Benchmark](../finance_notes/2025.emnlp-main.179.md) | core | Financial Evaluation / 金融评测 | Financial Semantic Matching and Ranking / 金融语义匹配与排序; Financial Text Classification / 金融文本分类; Financial Datasets and Task Benchmarks / 金融数据集与任务基准 | Language Models & LLM / 语言模型与LLM; Generative Modeling / 生成建模; Uncertainty & Robustness / 不确定性与鲁棒性; Retrieval & RAG / 检索与RAG; Representation Learning / 表征学习 | [PDF](../../pdfs/EMNLP/2025/2025.emnlp-main.179__FinMTEB_Finance_Massive_Text_Embedding_Benchmark.pdf) |
| 2025 | EMNLP | [FinRAGBench-V: A Benchmark for Multimodal RAG with Visual Citation in the Financial Domain](../finance_notes/2025.emnlp-main.211.md) | core | Financial Evaluation / 金融评测 | Financial Semantic Matching and Ranking / 金融语义匹配与排序; Evidence Retrieval and Reranking for Financial RAG / 金融 RAG 的证据检索与重排序; Table, Chart and Document Understanding / 表格、图表及文档理解; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Financial Understanding and Multimodal Evaluation / 金融理解及多模态评测; Chart and Multimodal Retrieval / 图表与多模态检索 | Language Models & LLM / 语言模型与LLM; Retrieval & RAG / 检索与RAG | [PDF](../../pdfs/EMNLP/2025/2025.emnlp-main.211__FinRAGBench_V_A_Benchmark_for_Multimodal_RAG_with_Visual_Citation_in_the_Financial_Domain.pdf) |
| 2025 | EMNLP | [OmniEval: An Omnidirectional and Automatic RAG Evaluation Benchmark in Financial Domain](../finance_notes/2025.emnlp-main.292.md) | core | Financial Evaluation / 金融评测 | Evidence Retrieval and Reranking for Financial RAG / 金融 RAG 的证据检索与重排序; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Evaluation Protocols and Metrics / 评测协议与指标 | Language Models & LLM / 语言模型与LLM; Generative Modeling / 生成建模; Retrieval & RAG / 检索与RAG | [PDF](../../pdfs/EMNLP/2025/2025.emnlp-main.292__OmniEval_An_Omnidirectional_and_Automatic_RAG_Evaluation_Benchmark_in_Financial_Domain.pdf) |
| 2025 | EMNLP | [Program of Thoughts for Financial Reasoning: Leveraging Dynamic In-Context Examples and Generative Retrieval](../finance_notes/2025.emnlp-main.1577.md) | core | Financial Question Answering / 金融问答 | Numerical Calculation and Program Reasoning / 数值计算与程序推理; Financial Semantic Matching and Ranking / 金融语义匹配与排序; Evidence Retrieval and Reranking for Financial RAG / 金融 RAG 的证据检索与重排序 | Language Models & LLM / 语言模型与LLM; Generative Modeling / 生成建模; Retrieval & RAG / 检索与RAG | [PDF](../../pdfs/EMNLP/2025/2025.emnlp-main.1577__Program_of_Thoughts_for_Financial_Reasoning_Leveraging_Dynamic_In_Context_Examples_and_Generative_Retriev.pdf) |
| 2024 | ICLR | [SocioDojo: Building Lifelong Analytical Agents with Real-world Text and Time Series](../finance_notes/iclr-2024-s9z0HzWJJp.md) | core | Financial Decision Making / 金融决策 | General Sequence Forecasting / 通用序列预测; Asset Selection and Weight Allocation / 资产选择与权重配置; Financial Semantic Matching and Ranking / 金融语义匹配与排序; Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策 | Optimization & Numerical Methods / 优化与数值方法 | [Online](https://openreview.net/forum?id=s9z0HzWJJp) |
| 2023 | EMNLP | [TRAVEL: Tag-Aware Conversational FAQ Retrieval via Reinforcement Learning](../finance_notes/2023.emnlp-main.234.md) | core | Financial Retrieval / 金融检索 | Financial Semantic Matching and Ranking / 金融语义匹配与排序; Customer Support and Business Consultation / 智能客服与业务咨询 | Reinforcement Learning / 强化学习; Retrieval & RAG / 检索与RAG | [PDF](../../pdfs/EMNLP/2023/2023.emnlp-main.234__TRAVEL_Tag_Aware_Conversational_FAQ_Retrieval_via_Reinforcement_Learning.pdf) |
| 2022 | EMNLP | [When FLUE Meets FLANG: Benchmarks and Large Pretrained Language Model for Financial Domain](../finance_notes/2022.emnlp-main.148.md) | core | Financial Models / 金融模型 | Evidence Retrieval and Reranking for Financial RAG / 金融 RAG 的证据检索与重排序; Financial Foundation Models and Domain Pretraining / 金融基础模型与领域预训练; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Financial Understanding and Multimodal Evaluation / 金融理解及多模态评测 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/EMNLP/2022/2022.emnlp-main.148__When_FLUE_Meets_FLANG_Benchmarks_and_Large_Pretrained_Language_Model_for_Financial_Domain.pdf) |
| 2020 | ACL | [Stock Embeddings Acquired from News Articles and Price History, and an Application to Portfolio Optimization](../finance_notes/2020.acl-main.307.md) | core | Portfolio / 投资组合 | Asset Selection and Weight Allocation / 资产选择与权重配置; Stock Price and Return Prediction / 股票价格与收益预测; Evidence Retrieval and Reranking for Financial RAG / 金融 RAG 的证据检索与重排序; Financial Semantic Matching and Ranking / 金融语义匹配与排序 | Optimization & Numerical Methods / 优化与数值方法; Representation Learning / 表征学习 | [PDF](../../pdfs/ACL/2020/2020.acl-main.307__Stock_Embeddings_Acquired_from_News_Articles_and_Price_History_and_an_Application_to_Portfolio_Optimizati.pdf) |
