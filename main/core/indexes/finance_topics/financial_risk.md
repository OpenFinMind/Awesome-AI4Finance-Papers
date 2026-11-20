# Financial Risk / 金融风险

Credit scoring, default, market, liquidity and systemic risk; fraud and attacks belong to financial safety. / 信用评分、违约、市场风险、流动性及系统性风险；欺诈与攻击归金融安全。

18 Main long papers. Topic memberships can overlap.

[All topics](../ai_for_finance.md) · [Classification definitions](../finance_taxonomy.md) · [CSV](financial_risk.csv) · [Excel](../../finance_catalog.xlsx)

<!-- task-summary:start -->

## Research summary / 研究总结

**Financial Risk / 金融风险 · Main / Core**

2026-11-20 · 18 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 研究潜在损失、违约及风险传播。信用解释与反事实补救仍属于信用风险任务；存在故意欺诈或攻击时才转向金融安全。市场、流动性和系统性风险应分别定义事件与损失。

**当前收录与方法。** 本页仅总结 Main / core 中的论文。当前较常见的子分类：Market Risk and Tail Losses / 市场风险与尾部损失 (10); Credit Risk and Default Prediction / 信用风险与违约预测 (9)。已标注的方法：Uncertainty & Robustness / 不确定性与鲁棒性 (4); Graph Learning / 图学习 (3); Language Models & LLM / 语言模型与LLM (3); Multimodal Learning / 多模态学习 (2); Optimization & Numerical Methods / 优化与数值方法 (2)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 关注违约与尾部事件、概率校准、成本敏感性、压力测试及跨期稳定性。 代表论文的摘要、金融关联证据及原文链接见 [1](../finance_notes/aaai-2025-33433.md) · [2](../finance_notes/kdd-2023-84d05f0f7e27.md) · [3](../finance_notes/aaai-2021-16094.md) · [4](../finance_notes/2021.acl-long.526.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 加强尾部事件、跨机构与跨期检验，把概率校准、拒贷成本和压力情景纳入统一决策评价。

### English

**Problem and subdirections.** This task concerns potential losses, default and risk propagation. Credit explanations and recourse remain credit-risk tasks; deliberate fraud or attacks belong to financial safety. Market, liquidity and systemic risks require distinct events and loss definitions.

**Current coverage and methods.** This page covers only Main / core. Frequent subcategories: Market Risk and Tail Losses / 市场风险与尾部损失 (10); Credit Risk and Default Prediction / 信用风险与违约预测 (9). Recorded methods: Uncertainty & Robustness / 不确定性与鲁棒性 (4); Graph Learning / 图学习 (3); Language Models & LLM / 语言模型与LLM (3); Multimodal Learning / 多模态学习 (2); Optimization & Numerical Methods / 优化与数值方法 (2). Counts overlap and are not performance rankings.

**Data and evaluation.** Evaluate default and tail events, calibration, cost sensitivity, stress tests and temporal stability. Representative abstracts, financial evidence and original sources are linked at [1](../finance_notes/aaai-2025-33433.md) · [2](../finance_notes/kdd-2023-84d05f0f7e27.md) · [3](../finance_notes/aaai-2021-16094.md) · [4](../finance_notes/2021.acl-long.526.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Strengthen tail-event, cross-institution and temporal evaluation, integrating calibration, lending costs and stress scenarios into decision assessment.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. Dynamic Graph Learning with Static Relations for Credit Risk Assessment](../finance_notes/aaai-2025-33433.md) · AAAI 2025 | 静态转账增强动态交易图风险表征<br>Static transfers enrich dynamic transaction risk representations | 工业数据结果不直接代表公开基准<br>Industrial-data results do not directly transfer to public benchmarks |
| [2. Financial Default Prediction via Motif-preserving Graph Neural Network with Curriculum Learning](../finance_notes/kdd-2023-84d05f0f7e27.md) · KDD 2023 | 模体图与课程学习处理高阶违约结构<br>Motif graphs and curricula model higher-order default structure | 业务关系可用性影响迁移<br>Transfer depends on available business relationships |
| [3. The Causal Learning of Retail Delinquency](../finance_notes/aaai-2021-16094.md) · AAAI 2021 | 估计授信改变对还款的因果影响<br>Estimate repayment effects of changes in lending decisions | 识别依赖观测数据及混杂假设<br>Identification depends on data and confounding assumptions |
| [4. Multimodal Multi-Speaker Merger & Acquisition Financial Modeling: A New Task, Dataset, and Neural Baselines](../finance_notes/2021.acl-long.526.md) · ACL 2021 | 并购电话会议的多模态风险建模<br>Multimodal risk modeling from M&A calls | 原文报告相对强基线的提升有限<br>The paper reports limited gains over strong baselines |

<!-- task-summary:end -->

## Subtopic statistics / 子方向统计

| Subtopic | Papers |
|---|---:|
| Credit Risk and Default Prediction / 信用风险与违约预测 | 9 |
| Market Risk and Tail Losses / 市场风险与尾部损失 | 10 |
| Liquidity and Funding Risk / 流动性与融资风险 | 0 |
| Counterparty and Contagion Risk / 交易对手与传染风险 | 0 |
| Systemic Risk and Financial Stability / 系统性风险与金融稳定 | 0 |
| Stress Testing and Scenario Analysis / 压力测试与情景分析 | 0 |
| Operational Risk and Loss Prediction / 操作风险与损失预测 | 0 |

## Full paper list / 完整论文列表

| Year | Venue | Paper | Scope | Primary topic | Subtopics | Methods | Resources |
|---|---|---|---|---|---|---|---|
| 2026 | NeurIPS | [A Set-Sequence Model for Time Series](../finance_notes/neurips-2026-y1ZoyGsVuL.md) | core | Time Series / 时间序列 | General Sequence Forecasting / 通用序列预测; Asset Selection and Weight Allocation / 资产选择与权重配置; Stock Price and Return Prediction / 股票价格与收益预测; Credit Risk and Default Prediction / 信用风险与违约预测 | Transformer / Transformer模型; Optimization & Numerical Methods / 优化与数值方法 | [PDF](../../pdfs/NeurIPS/2026/neurips-2026-y1ZoyGsVuL__A_Set_Sequence_Model_for_Time_Series.pdf) |
| 2025 | AAAI | [Dynamic Graph Learning with Static Relations for Credit Risk Assessment](../finance_notes/aaai-2025-33433.md) | core | Financial Risk / 金融风险 | Credit Risk and Default Prediction / 信用风险与违约预测 | Graph Learning / 图学习 | [PDF](../../pdfs/AAAI/2025/aaai-2025-33433__Dynamic_Graph_Learning_with_Static_Relations_for_Credit_Risk_Assessment.pdf) |
| 2025 | EMNLP | [Financial Risk Relation Identification through Dual-view Adaptation](../finance_notes/2025.emnlp-main.1336.md) | core | Financial Risk / 金融风险 | Asset Selection and Weight Allocation / 资产选择与权重配置; Market Risk and Tail Losses / 市场风险与尾部损失; Entity and Relation Extraction / 实体与关系抽取; Evidence Retrieval and Reranking for Financial RAG / 金融 RAG 的证据检索与重排序 |  | [PDF](../../pdfs/EMNLP/2025/2025.emnlp-main.1336__Financial_Risk_Relation_Identification_through_Dual_view_Adaptation.pdf) |
| 2025 | EMNLP | [VisFinEval: A Scenario-Driven Chinese Multimodal Benchmark for Holistic Financial Understanding](../finance_notes/2025.emnlp-main.1229.md) | core | Financial Evaluation / 金融评测 | Market Risk and Tail Losses / 市场风险与尾部损失; Table, Chart and Document Understanding / 表格、图表及文档理解; Report and Disclosure Understanding / 财报与公告理解; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Financial Understanding and Multimodal Evaluation / 金融理解及多模态评测 | Language Models & LLM / 语言模型与LLM; Uncertainty & Robustness / 不确定性与鲁棒性; Multimodal Learning / 多模态学习; Optimization & Numerical Methods / 优化与数值方法 | [PDF](../../pdfs/EMNLP/2025/2025.emnlp-main.1229__VisFinEval_A_Scenario_Driven_Chinese_Multimodal_Benchmark_for_Holistic_Financial_Understanding.pdf) |
| 2025 | ICLR | [Feature Responsiveness Scores: Model-Agnostic Explanations for Recourse](../finance_notes/iclr-2025-wsWCVrH9dv.md) | core | Financial Risk / 金融风险 | Credit Risk and Default Prediction / 信用风险与违约预测 |  | [PDF](../../pdfs/ICLR/2025/iclr-2025-wsWCVrH9dv__Feature_Responsiveness_Scores_Model_Agnostic_Explanations_for_Recourse.pdf) |
| 2025 | ICLR | [MarS: a Financial Market Simulation Engine Powered by Generative Foundation Model](../finance_notes/iclr-2025-Yqk7EyT52H.md) | core | Financial Decision Making / 金融决策 | Market Making and Quoting / 做市与报价策略; Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策; Market Risk and Tail Losses / 市场风险与尾部损失; Financial Foundation Models and Domain Pretraining / 金融基础模型与领域预训练 | Language Models & LLM / 语言模型与LLM; Generative Modeling / 生成建模; Uncertainty & Robustness / 不确定性与鲁棒性 | [PDF](../../pdfs/ICLR/2025/iclr-2025-Yqk7EyT52H__MarS_a_Financial_Market_Simulation_Engine_Powered_by_Generative_Foundation_Model.pdf) |
| 2023 | EMNLP | [STINMatch: Semi-Supervised Semantic-Topological Iteration Network for Financial Risk Detection via News Label Diffusion](../finance_notes/2023.emnlp-main.578.md) | core | Financial Risk / 金融风险 | Market Risk and Tail Losses / 市场风险与尾部损失 | Diffusion & Flow / 扩散与流模型 | [PDF](../../pdfs/EMNLP/2023/2023.emnlp-main.578__STINMatch_Semi_Supervised_Semantic_Topological_Iteration_Network_for_Financial_Risk_Detection_via_News_La.pdf) |
| 2023 | KDD | [Financial Default Prediction via Motif-preserving Graph Neural Network with Curriculum Learning](../finance_notes/kdd-2023-84d05f0f7e27.md) | core | Financial Risk / 金融风险 | Credit Risk and Default Prediction / 信用风险与违约预测 | Graph Learning / 图学习 | [PDF](../../pdfs/KDD/2023/kdd-2023-84d05f0f7e27__Financial_Default_Prediction_via_Motif-preserving_Graph_Neural_Network_with_Curriculum_Learning.pdf) |
| 2022 | AAAI | [An Algorithmic Introduction to Savings Circles](../finance_notes/aaai-2022-20400.md) | core | Financial Risk / 金融风险 | Credit Risk and Default Prediction / 信用风险与违约预测 |  | [PDF](../../pdfs/AAAI/2022/aaai-2022-20400__An_Algorithmic_Introduction_to_Savings_Circles.pdf) |
| 2021 | AAAI | [Self-Supervised Prototype Representation Learning for Event-Based Corporate Profiling](../finance_notes/aaai-2021-16594.md) | core | Valuation Prediction / 估值预测 | Stock Price and Return Prediction / 股票价格与收益预测; Credit Risk and Default Prediction / 信用风险与违约预测; Earnings, Revenue and Fundamental Prediction / 盈利、营收与基本面预测 | Uncertainty & Robustness / 不确定性与鲁棒性; Representation Learning / 表征学习 | [PDF](../../pdfs/AAAI/2021/aaai-2021-16594__Self_Supervised_Prototype_Representation_Learning_for_Event_Based_Corporate_Profiling.pdf) |
| 2021 | AAAI | [The Causal Learning of Retail Delinquency](../finance_notes/aaai-2021-16094.md) | core | Financial Risk / 金融风险 | Credit Risk and Default Prediction / 信用风险与违约预测; Market Risk and Tail Losses / 市场风险与尾部损失 | Causal Learning / 因果学习; Uncertainty & Robustness / 不确定性与鲁棒性 | [PDF](../../pdfs/AAAI/2021/aaai-2021-16094__The_Causal_Learning_of_Retail_Delinquency.pdf) |
| 2021 | ACL | [Multimodal Multi-Speaker Merger & Acquisition Financial Modeling: A New Task, Dataset, and Neural Baselines](../finance_notes/2021.acl-long.526.md) | core | Financial Evaluation / 金融评测 | Market Risk and Tail Losses / 市场风险与尾部损失; Financial Event Detection and Linking / 金融事件识别与关联; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Financial Understanding and Multimodal Evaluation / 金融理解及多模态评测 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/ACL/2021/2021.acl-long.526__Multimodal_Multi_Speaker_Merger_Acquisition_Financial_Modeling_A_New_Task_Dataset_and_Neural_Baselines.pdf) |
| 2021 | NeurIPS | [Neural Pseudo-Label Optimism for the Bank Loan Problem](../finance_notes/neurips-2021-jYzSTzvDP3p.md) | core | Financial Risk / 金融风险 | Credit Risk and Default Prediction / 信用风险与违约预测 |  | [PDF](../../pdfs/NeurIPS/2021/neurips-2021-jYzSTzvDP3p__Neural_Pseudo_Label_Optimism_for_the_Bank_Loan_Problem.pdf) |
| 2020 | AAAI | [Shoreline: Data-Driven Threshold Estimation of Online Reserves of Cryptocurrency Trading Platforms](../finance_notes/aaai-2020-5472.md) | core | Financial Risk / 金融风险 | Market Risk and Tail Losses / 市场风险与尾部损失; On-Chain Transaction and Account Analysis / 链上交易与账户分析; Digital Assets and Token Economics / 数字资产及代币经济 |  | [PDF](../../pdfs/AAAI/2020/aaai-2020-5472__Shoreline_Data_Driven_Threshold_Estimation_of_Online_Reserves_of_Cryptocurrency_Trading_Platforms.pdf) |
| 2020 | EMNLP | [VolTAGE: Volatility Forecasting via Text Audio Fusion with Graph Convolution Networks for Earnings Calls](../finance_notes/2020.emnlp-main.643.md) | core | Valuation Prediction / 估值预测 | Stock Price and Return Prediction / 股票价格与收益预测; Volatility Prediction / 波动率预测; Market Risk and Tail Losses / 市场风险与尾部损失; Entity and Relation Extraction / 实体与关系抽取; Report and Disclosure Understanding / 财报与公告理解; Earnings, Revenue and Fundamental Prediction / 盈利、营收与基本面预测 | Graph Learning / 图学习; Multimodal Learning / 多模态学习 | [PDF](../../pdfs/EMNLP/2020/2020.emnlp-main.643__VolTAGE_Volatility_Forecasting_via_Text_Audio_Fusion_with_Graph_Convolution_Networks_for_Earnings_Calls.pdf) |
| 2019 | AAAI | [Pareto Efficient Auctions with Interest Rates](../finance_notes/aaai-2019-4027.md) | core | Financial Risk / 金融风险 | Credit Risk and Default Prediction / 信用风险与违约预测 |  | [PDF](../../pdfs/AAAI/2019/aaai-2019-4027__Pareto_Efficient_Auctions_with_Interest_Rates.pdf) |
| 2019 | ACL | [What You Say and How You Say It Matters: Predicting Stock Volatility Using Verbal and Vocal Cues](../finance_notes/P19-1038.md) | core | Valuation Prediction / 估值预测 | Trading Strategies and Buy/Sell Decisions / 交易策略与买卖决策; Stock Price and Return Prediction / 股票价格与收益预测; Volatility Prediction / 波动率预测; Market Risk and Tail Losses / 市场风险与尾部损失; Report and Disclosure Understanding / 财报与公告理解 |  | [PDF](../../pdfs/ACL/2019/P19-1038__What_You_Say_and_How_You_Say_It_Matters_Predicting_Stock_Volatility_Using_Verbal_and_Vocal_Cues.pdf) |
| 2018 | NeurIPS | [Parsimonious Quantile Regression of Financial Asset Tail Dynamics via Sequential Learning](../finance_notes/neurips-2018-11172.md) | core | Financial Risk / 金融风险 | General Sequence Forecasting / 通用序列预测; Volatility Prediction / 波动率预测; Market Risk and Tail Losses / 市场风险与尾部损失; Sequence Representation and Pattern Discovery / 序列表示与模式发现; Earnings, Revenue and Fundamental Prediction / 盈利、营收与基本面预测 |  | [PDF](../../pdfs/NeurIPS/2018/neurips-2018-11172__Parsimonious_Quantile_Regression_of_Financial_Asset_Tail_Dynamics_via_Sequential_Learning.pdf) |
