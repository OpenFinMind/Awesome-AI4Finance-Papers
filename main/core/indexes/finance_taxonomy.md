# Classification / 分类说明

Taxonomy 3.0 / 分类版本 3.0。Main/Findings and Core/Application are independent partitions. / 发表轨道与金融范围独立分区。

- **Core / 金融核心研究**: the main research problem or contribution concerns finance. / 主要研究问题或贡献直接面向金融。
- **Application / 金融应用**: finance is a substantive application of a general method. / 通用方法含有实质性的金融应用。
- One primary task and one primary subcategory; related tasks, subcategories and methods may overlap. / 一个主方向和一个主要子分类；关联方向、子分类与方法允许多标签。
- Insufficiently supported subcategories remain pending, visible in the catalog and paper note. / 证据不足的子分类保留待核对状态，在清单与逐篇笔记中显示。

**Boundaries / 分类边界**

Predictive signal discovery → factor mining; economic pricing relationships → pricing. Sequence structure/reconstruction → time series; explicit prices/returns/volatility/fundamentals → valuation prediction. Portfolio weights → portfolio; trading/execution/hedging actions → financial decision. Loss/default/uncertainty → financial risk; fraud/attacks/privacy/compliance → financial safety. Insurance pricing/claims/reserves/longevity → actuarial science; insurance sales/service → financial services. / 预测信号发现归因子挖掘，经济定价关系归定价；序列结构与重建归时间序列，明确的价格、收益、波动率与基本面预测归估值预测；组合权重归投资组合，交易执行对冲行动归金融决策；损失与违约归金融风险，欺诈攻击隐私合规归金融安全；保险精算任务与保险销售服务分开。

A dataset, benchmark or capability audit as the main contribution → financial evaluation. Reusable financial-domain pretraining/post-training/adaptation → financial models. Merely reporting experiments or using an LLM is insufficient. / 数据集、基准或能力诊断为主要贡献时归金融评测；可复用金融领域模型的训练适配归金融模型；仅做实验或调用 LLM 不自动归入这两类。

[Task index / 任务目录](ai_for_finance.md) · [Per-paper evidence / 逐篇依据](../checks/finance_taxonomy/assignments.json) · [Schema / 分类定义](../checks/finance_taxonomy/schema.json)

## [Factor Mining / 因子挖掘](finance_topics/alpha_mining.md)

Discover and select reusable alpha signals or formulas; distinguish predictive alpha from economic pricing factors. / 发现与筛选可复用的收益信号或公式，区别于经济定价因子。

- [Factor Discovery and Formula Generation / 因子发现与公式生成](subtopics/factor_discovery.md)
- [Factor Combination and Interaction / 因子组合与交互](subtopics/factor_combination.md)
- [Factor Selection and Deduplication / 因子筛选与去冗余](subtopics/factor_selection.md)
- [Factor Validity and Stability / 因子有效性与稳定性](subtopics/factor_evaluation.md)
- [Factor Decay and Updating / 因子衰减与更新](subtopics/factor_decay.md)
- [Factor Interpretation and Economic Meaning / 因子解释与经济含义](subtopics/factor_interpretation.md)

## [Time Series / 时间序列](finance_topics/time_series.md)

Forecast, represent, generate or reconstruct financial sequences; a specific asset-value target belongs to valuation prediction. / 金融序列预测、表征、生成与重建；明确的资产价值目标归估值预测。

- [General Sequence Forecasting / 通用序列预测](subtopics/ts_forecasting.md)
- [Sequence Representation and Pattern Discovery / 序列表示与模式发现](subtopics/ts_representation.md)
- [Imputation and Sequence Reconstruction / 缺失值填补与序列重建](subtopics/ts_imputation.md)
- [Sequence Generation and Augmentation / 序列生成与数据增强](subtopics/ts_generation.md)
- [Anomaly and Change-Point Detection / 异常检测与变点识别](subtopics/ts_anomaly.md)
- [Multivariate Relations and Cross-Frequency Modeling / 多变量关联与跨频率建模](subtopics/ts_multivariate.md)

## [Pricing / 定价](finance_topics/pricing.md)

Asset pricing mechanisms, risk premia, derivative valuation and calibration; distinguish pricing relationships from predictive price targets. / 资产定价机制、风险溢价、衍生品估价与校准，区别于价格预测。

- [Asset Pricing and Risk Premia / 资产定价与风险溢价](subtopics/pricing_models.md)
- [Option and Derivative Pricing / 期权及衍生品定价](subtopics/option_pricing.md)
- [Interest Rates and Fixed Income / 利率与固定收益定价](subtopics/fixed_income_pricing.md)
- [Credit Instrument Pricing / 信用工具定价](subtopics/credit_pricing.md)
- [No-Arbitrage Constraints and Calibration / 无套利约束与模型校准](subtopics/pricing_calibration.md)
- [Market Microstructure and Price Formation / 市场微观结构与价格形成](subtopics/price_formation.md)

## [Valuation Prediction / 估值预测](finance_topics/valuation_prediction.md)

Predict asset prices, returns, volatility, enterprise value, earnings or revenue. / 预测资产价格、收益、波动率、企业价值、盈利与营收。

- [Stock Price and Return Prediction / 股票价格与收益预测](subtopics/stock_prediction.md)
- [Movement Direction and Asset Ranking / 涨跌方向与资产排序](subtopics/direction_ranking.md)
- [Volatility Prediction / 波动率预测](subtopics/volatility_prediction.md)
- [Enterprise and Equity Valuation / 企业价值与股权估值](subtopics/enterprise_valuation.md)
- [Earnings, Revenue and Fundamental Prediction / 盈利、营收与基本面预测](subtopics/fundamental_prediction.md)
- [FX, Commodity and Digital Asset Forecasting / 汇率、商品及数字资产行情预测](subtopics/fx_crypto.md)

## [Portfolio / 投资组合](finance_topics/portfolio.md)

Select, allocate, rebalance and evaluate portfolios across assets. / 跨资产组合选择、配置、再平衡与评价。

- [Asset Selection and Weight Allocation / 资产选择与权重配置](subtopics/selection.md)
- [Dynamic Allocation and Rebalancing / 动态配置与再平衡](subtopics/portfolio_rebalancing.md)
- [Multi-Asset and Cross-Market Allocation / 多资产与跨市场配置](subtopics/multiasset_allocation.md)
- [Risk-Return and Multi-Objective Optimization / 风险收益及多目标优化](subtopics/portfolio_objectives.md)
- [Transaction Costs and Investment Constraints / 交易成本与投资约束](subtopics/portfolio_constraints.md)
- [Long-Term Wealth and Goal-Based Investing / 长期财富与目标投资](subtopics/financial_planning.md)

## [Insurance and Actuarial Science / 保险精算](finance_topics/insurance.md)

Insurance underwriting, claims, reserves, actuarial prediction and insurance business decisions. / 承保、理赔、准备金、精算预测及保险业务决策。

- [Insurance Pricing and Premium Setting / 保险定价与保费厘定](subtopics/insurance_pricing.md)
- [Claim Frequency and Loss Severity / 索赔频率与损失严重度](subtopics/insurance_claims.md)
- [Reserves and Payout Prediction / 准备金与赔付预测](subtopics/insurance_reserves.md)
- [Mortality, Longevity and Survival / 死亡率、长寿与生存分析](subtopics/mortality_longevity.md)
- [Reinsurance and Risk Sharing / 再保险与风险分担](subtopics/reinsurance.md)
- [Catastrophe Risk and Solvency / 巨灾风险与偿付能力](subtopics/insurance_solvency.md)

## [Financial Sentiment / 金融情感](finance_topics/financial_sentiment.md)

Financial sentiment, stance, tone and emotion as the prediction target; downstream return prediction stays valuation prediction. / 以金融情感、立场、语气与情绪为目标；下游收益预测仍归估值预测。

- [News and Social Media Sentiment / 新闻与社交媒体情感](subtopics/news_sentiment.md)
- [Investor Sentiment / 投资者情绪](subtopics/investor_sentiment.md)
- [Report and Earnings-Call Tone / 财报及电话会议语调](subtopics/disclosure_tone.md)
- [Entity- and Aspect-Based Sentiment / 面向实体与方面的情感](subtopics/aspect_sentiment.md)
- [Financial Stance and Opinion Detection / 金融立场与观点识别](subtopics/financial_stance.md)
- [Sentiment Dynamics and Market Effects / 情绪变化与市场影响](subtopics/sentiment_market_effect.md)

## [Financial Question Answering / 金融问答](finance_topics/financial_qa.md)

Answer financial questions and perform numerical, table or conversational reasoning. / 金融问题回答及数值、表格、对话推理。

- [Financial Factual QA / 金融事实问答](subtopics/knowledge_qa.md)
- [Numerical Calculation and Program Reasoning / 数值计算与程序推理](subtopics/numerical_reasoning.md)
- [Table-and-Text QA / 表格与文本联合问答](subtopics/table_text_qa.md)
- [Multi-Document and Multi-Hop QA / 多文档与多跳问答](subtopics/multihop_qa.md)
- [Chart and Multimodal QA / 图表及多模态问答](subtopics/multimodal_qa.md)
- [Conversational Financial QA / 对话式金融问答](subtopics/conversational_qa.md)

## [Financial Understanding / 金融理解](finance_topics/financial_understanding.md)

Extract, interpret, summarize and verify financial language, reports, charts, invoices and accounting records. / 金融文本、财报、图表、票据及会计记录的抽取、解释、摘要与核验。

- [Entity and Relation Extraction / 实体与关系抽取](subtopics/information_extraction.md)
- [Financial Event Detection and Linking / 金融事件识别与关联](subtopics/financial_events.md)
- [Financial Text Classification / 金融文本分类](subtopics/financial_text_classification.md)
- [Report and Disclosure Understanding / 财报与公告理解](subtopics/report_understanding.md)
- [Table, Chart and Document Understanding / 表格、图表及文档理解](subtopics/document_understanding.md)
- [Financial Summarization and Report Generation / 金融摘要与报告生成](subtopics/text_generation.md)

## [Financial Decision Making / 金融决策](finance_topics/financial_decision.md)

Trading, execution, market simulation and financial agent decisions; portfolio allocation has its own task. / 交易、执行、市场仿真与金融 Agent 决策；组合配置单列。

- [Trading Strategies and Buy/Sell Decisions / 交易策略与买卖决策](subtopics/trading_strategy.md)
- [Order Execution / 订单执行](subtopics/trading_execution.md)
- [Market Making and Quoting / 做市与报价策略](subtopics/market_making.md)
- [Dynamic Hedging / 动态对冲](subtopics/hedging.md)
- [Corporate Financing and Cash Management / 企业融资及现金管理决策](subtopics/corporate_decisions.md)
- [Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策](subtopics/agent_decisions.md)

## [Sustainable Finance / 可持续金融](finance_topics/sustainable_finance.md)

ESG disclosure, greenwashing, climate-related financial analysis and sustainable investment. / ESG 披露、漂绿、气候金融分析与可持续投资。

- [ESG Extraction and Evaluation / ESG 信息抽取与评价](subtopics/esg_evaluation.md)
- [Sustainability Disclosure and Greenwashing / 可持续披露与漂绿识别](subtopics/esg_disclosure.md)
- [Climate and Transition Risk / 气候风险与转型风险](subtopics/climate_risk.md)
- [Green Credit and Financing / 绿色信贷与绿色融资](subtopics/green_financing.md)
- [Carbon Markets and Finance / 碳市场与碳金融](subtopics/carbon_finance.md)
- [Responsible Investment and Social Impact / 责任投资与社会影响](subtopics/sustainable_investment.md)

## [Financial Services / 金融服务](finance_topics/financial_services.md)

Banking, payments, customer service, marketing and personal/business financial services. / 银行、支付、客户服务、营销及个人与企业金融服务。

- [Customer Support and Business Consultation / 智能客服与业务咨询](subtopics/customer_intents.md)
- [Financial Product Recommendation and Matching / 金融产品推荐与匹配](subtopics/product_recommendation.md)
- [Personal Financial Planning and Services / 个人财务规划与服务](subtopics/personal_finance.md)
- [Lending, Payment and Banking Workflows / 贷款、支付及银行业务流程](subtopics/banking_workflows.md)
- [Customer Behavior and Relationship Management / 客户行为与关系管理](subtopics/bank_marketing.md)
- [Financial Access and Inclusion / 金融服务可及性与普惠金融](subtopics/financial_inclusion.md)

## [Blockchain / 区块链](finance_topics/blockchain.md)

Blockchain transactions, digital assets, smart contracts and DeFi mechanisms. / 链上交易、数字资产、智能合约与 DeFi 机制。

- [On-Chain Transaction and Account Analysis / 链上交易与账户分析](subtopics/crypto_transactions.md)
- [Digital Assets and Token Economics / 数字资产及代币经济](subtopics/token_economics.md)
- [DeFi and On-Chain Financial Mechanisms / DeFi 与链上金融机制](subtopics/defi.md)
- [Smart Contract Analysis / 智能合约分析](subtopics/smart_contracts.md)
- [Fees, MEV and On-Chain Markets / 交易费、MEV 与链上市场机制](subtopics/onchain_markets.md)
- [Blockchain Financial Infrastructure / 区块链金融基础设施](subtopics/blockchain_infrastructure.md)

## [Financial Safety / 金融安全](finance_topics/financial_safety.md)

Fraud, scams, money laundering, privacy, attacks and regulatory compliance. / 欺诈、诈骗、反洗钱、隐私、攻击与监管合规。

- [Payment, Transaction and Insurance Fraud / 支付、交易及保险欺诈](subtopics/financial_fraud.md)
- [AML and Illicit Fund Tracing / 反洗钱与非法资金追踪](subtopics/aml.md)
- [Identity and Account Abuse / 身份冒用与账户滥用](subtopics/identity_abuse.md)
- [Financial Network and Smart Contract Attacks / 金融网络及智能合约攻击](subtopics/financial_attacks.md)
- [Privacy and Sensitive Information Protection / 隐私与敏感信息保护](subtopics/privacy_security.md)
- [Regulatory Compliance and Violation Detection / 监管合规与违规检测](subtopics/financial_regulation.md)
- [Financial Model and Agent Safety / 金融模型及智能体安全](subtopics/model_safety.md)

## [Financial Retrieval / 金融检索](finance_topics/financial_ir.md)

Retrieve, embed, rerank and ground financial evidence, including financial RAG. / 金融证据检索、嵌入、重排及 RAG。

- [Financial Document and Disclosure Retrieval / 金融文档与公告检索](subtopics/document_retrieval.md)
- [Financial Semantic Matching and Ranking / 金融语义匹配与排序](subtopics/retrieval.md)
- [Table and Numerical Retrieval / 表格及数值信息检索](subtopics/table_retrieval.md)
- [Chart and Multimodal Retrieval / 图表与多模态检索](subtopics/multimodal_retrieval.md)
- [Cross-Lingual Financial Retrieval / 跨语言金融检索](subtopics/crosslingual_retrieval.md)
- [Evidence Retrieval and Reranking for Financial RAG / 金融 RAG 的证据检索与重排序](subtopics/rag.md)

## [Financial Evaluation / 金融评测](finance_topics/financial_evaluation.md)

The main contribution is a financial dataset, benchmark, evaluation environment or capability audit. / 主要贡献为金融数据集、基准、评测环境或能力诊断。

- [Financial Datasets and Task Benchmarks / 金融数据集与任务基准](subtopics/task_benchmarks.md)
- [Financial Knowledge and Professional Evaluation / 金融知识与专业能力评测](subtopics/financial_reasoning_eval.md)
- [Numerical Reasoning and Calculation Evaluation / 数值推理与计算评测](subtopics/numerical_evaluation.md)
- [Financial Understanding and Multimodal Evaluation / 金融理解及多模态评测](subtopics/understanding_evaluation.md)
- [Financial Decision and Agent Evaluation / 金融决策与智能体评测](subtopics/agent_evaluation.md)
- [Reliability, Safety and Fairness Evaluation / 可靠性、安全与公平性评测](subtopics/trust_evaluation.md)
- [Evaluation Protocols and Metrics / 评测协议与指标](subtopics/evaluation_protocols.md)

## [Financial Models / 金融模型](finance_topics/financial_models.md)

Financial domain pretraining, adaptation and reusable foundation models; generic time-series pretraining stays time series. / 金融领域预训练、适配与可复用基础模型；通用序列预训练仍归时间序列。

- [Financial Foundation Models and Domain Pretraining / 金融基础模型与领域预训练](subtopics/domain_models.md)
- [Financial Instruction Tuning and Post-Training / 金融指令微调与后训练](subtopics/financial_posttraining.md)
- [Financial Representation Models / 金融专用表示模型](subtopics/financial_representations.md)
- [Financial Multimodal Models / 金融多模态模型](subtopics/financial_multimodal_models.md)
- [Financial Time-Series Foundation Models / 金融时序基础模型](subtopics/financial_ts_models.md)
- [Financial Model Adaptation, Compression and Deployment / 金融模型适配、压缩与高效部署](subtopics/financial_efficient_models.md)

## [Financial Risk / 金融风险](finance_topics/financial_risk.md)

Credit scoring, default, market, liquidity and systemic risk; fraud and attacks belong to financial safety. / 信用评分、违约、市场风险、流动性及系统性风险；欺诈与攻击归金融安全。

- [Credit Risk and Default Prediction / 信用风险与违约预测](subtopics/credit_default.md)
- [Market Risk and Tail Losses / 市场风险与尾部损失](subtopics/market_risk.md)
- [Liquidity and Funding Risk / 流动性与融资风险](subtopics/liquidity_risk.md)
- [Counterparty and Contagion Risk / 交易对手与传染风险](subtopics/counterparty_risk.md)
- [Systemic Risk and Financial Stability / 系统性风险与金融稳定](subtopics/systemic_risk.md)
- [Stress Testing and Scenario Analysis / 压力测试与情景分析](subtopics/stress_testing.md)
- [Operational Risk and Loss Prediction / 操作风险与损失预测](subtopics/operational_risk.md)

## Methods / 技术方法

- [Language Models & LLM / 语言模型与LLM](methods/llm.md)
- [Reinforcement Learning / 强化学习](methods/reinforcement_learning.md)
- [Graph Learning / 图学习](methods/graph_learning.md)
- [Diffusion & Flow / 扩散与流模型](methods/diffusion_flow.md)
- [Generative Modeling / 生成建模](methods/generative.md)
- [Transformer / Transformer模型](methods/transformer.md)
- [Causal Learning / 因果学习](methods/causal.md)
- [Fairness & Recourse / 公平性与算法追索](methods/fairness_recourse.md)
- [Uncertainty & Robustness / 不确定性与鲁棒性](methods/uncertainty_robustness.md)
- [Privacy & Federated Learning / 隐私与联邦学习](methods/privacy.md)
- [Tabular Learning / 表格学习](methods/tabular.md)
- [Multimodal Learning / 多模态学习](methods/multimodal.md)
- [Retrieval & RAG / 检索与RAG](methods/retrieval.md)
- [Optimization & Numerical Methods / 优化与数值方法](methods/optimization.md)
- [Representation Learning / 表征学习](methods/representation.md)
