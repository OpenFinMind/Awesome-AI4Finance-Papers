"""Approved financial task subcategories; techniques remain a separate axis.

Patterns only propose refinements within an evidenced financial task. They never
admit a paper or certify a contribution review.
"""
# parent: (stable id, Chinese, English, optional refinement pattern)
GROUPS = {
'alpha_mining': [
('factor_discovery','因子发现与公式生成','Factor Discovery and Formula Generation',r'factor.*(?:discover|generat|mining)|alpha.*(?:discover|generat|mining)'),
('factor_combination','因子组合与交互','Factor Combination and Interaction',r'factor.*(?:combin|interact|synerg)'),
('factor_selection','因子筛选与去冗余','Factor Selection and Deduplication',r'factor.*(?:select|redundan)|alpha.*(?:select|redundan)'),
('factor_evaluation','因子有效性与稳定性','Factor Validity and Stability',r'factor.*(?:evaluat|stabil|robust)|alpha.*(?:evaluat|stabil|robust)'),
('factor_decay','因子衰减与更新','Factor Decay and Updating',r'(?:factor|alpha).*(?:decay|refresh|updat)'),
('factor_interpretation','因子解释与经济含义','Factor Interpretation and Economic Meaning',r'(?:factor|alpha).*(?:interpretab|explain|economic)'),
],
'time_series': [
('ts_forecasting','通用序列预测','General Sequence Forecasting',r'forecast|prediction'),
('ts_representation','序列表示与模式发现','Sequence Representation and Pattern Discovery',r'representation|embedding|pattern|pre.?train|foundation|causal|dynamics|stochastic process'),
('ts_imputation','缺失值填补与序列重建','Imputation and Sequence Reconstruction',r'imput|missing|reconstruct|irregular'),
('ts_generation','序列生成与数据增强','Sequence Generation and Augmentation',r'generat|synthes|augment|simulat'),
('ts_anomaly','异常检测与变点识别','Anomaly and Change-Point Detection',r'anomal|outlier|change.point'),
('ts_multivariate','多变量关联与跨频率建模','Multivariate Relations and Cross-Frequency Modeling',r'multivariate|cross.frequency|mixed.frequency'),
],
'pricing': [
('pricing_models','资产定价与风险溢价','Asset Pricing and Risk Premia',r'asset pricing|risk premi|factor pric|discount factor'),
('option_pricing','期权及衍生品定价','Option and Derivative Pricing',r'option|derivative|Black.Scholes|volatility surface|implied volatility'),
('fixed_income_pricing','利率与固定收益定价','Interest Rates and Fixed Income',r'interest rate|fixed.income|bond|yield curve'),
('credit_pricing','信用工具定价','Credit Instrument Pricing',r'credit.*(?:pric|spread)|credit default swap'),
('pricing_calibration','无套利约束与模型校准','No-Arbitrage Constraints and Calibration',r'no.arbitrage|arbitrage.free|calibrat|numerical|PDE'),
('price_formation','市场微观结构与价格形成','Market Microstructure and Price Formation',r'price formation|market microstructure|price discovery'),
],
'valuation_prediction': [
('stock_prediction','股票价格与收益预测','Stock Price and Return Prediction',r'stock|equity|return predict|return forecast'),
('direction_ranking','涨跌方向与资产排序','Movement Direction and Asset Ranking',r'movement|ranking|direction'),
('volatility_prediction','波动率预测','Volatility Prediction',r'volatility'),
('enterprise_valuation','企业价值与股权估值','Enterprise and Equity Valuation',r'enterprise value|equity valu|valuation|real.estate|house price|housing price'),
('fundamental_prediction','盈利、营收与基本面预测','Earnings, Revenue and Fundamental Prediction',r'earning|revenue|fundamental|sales|survival|crowdfund'),
('fx_crypto','汇率、商品及数字资产行情预测','FX, Commodity and Digital Asset Forecasting',r'exchange.rate|crypto|bitcoin|commodity|commodities|futures'),
],
'portfolio': [
('selection','资产选择与权重配置','Asset Selection and Weight Allocation',r'select|weight|allocat|optimi'),
('portfolio_rebalancing','动态配置与再平衡','Dynamic Allocation and Rebalancing',r'dynamic|rebalanc|online portfolio'),
('multiasset_allocation','多资产与跨市场配置','Multi-Asset and Cross-Market Allocation',r'multi.asset|cross.market'),
('portfolio_objectives','风险收益及多目标优化','Risk-Return and Multi-Objective Optimization',r'mean.variance|risk.return|multi.objective|Sharpe|investment evaluat'),
('portfolio_constraints','交易成本与投资约束','Transaction Costs and Investment Constraints',r'transaction cost|constraint|turnover'),
('financial_planning','长期财富与目标投资','Long-Term Wealth and Goal-Based Investing',r'wealth|retire|financial planning|goal.based|long.term'),
],
'financial_risk': [
('credit_default','信用风险与违约预测','Credit Risk and Default Prediction',r'credit|default|loan|lending|HELOC|FICO|recourse'),
('market_risk','市场风险与尾部损失','Market Risk and Tail Losses',r'market risk|tail|value.at.risk|expected shortfall|VaR|CVaR'),
('liquidity_risk','流动性与融资风险','Liquidity and Funding Risk',r'liquidity|funding risk'),
('counterparty_risk','交易对手与传染风险','Counterparty and Contagion Risk',r'counterparty|contagion|exposure network'),
('systemic_risk','系统性风险与金融稳定','Systemic Risk and Financial Stability',r'systemic|financial stability|financial crisis'),
('stress_testing','压力测试与情景分析','Stress Testing and Scenario Analysis',r'stress test|scenario analys'),
('operational_risk','操作风险与损失预测','Operational Risk and Loss Prediction',r'operational risk|loss predict'),
],
'insurance': [
('insurance_pricing','保险定价与保费厘定','Insurance Pricing and Premium Setting',r'premium|insurance pric|ratemaking|underwrit'),
('insurance_claims','索赔频率与损失严重度','Claim Frequency and Loss Severity',r'claim|severity|insurance loss'),
('insurance_reserves','准备金与赔付预测','Reserves and Payout Prediction',r'reserv|payout|loss develop'),
('mortality_longevity','死亡率、长寿与生存分析','Mortality, Longevity and Survival',r'mortal|longev|survival|life insurance'),
('reinsurance','再保险与风险分担','Reinsurance and Risk Sharing',r'reinsur|risk shar'),
('insurance_solvency','巨灾风险与偿付能力','Catastrophe Risk and Solvency',r'catastroph|solvency|long.term risk|risk.based allocat'),
],
'financial_sentiment': [
('news_sentiment','新闻与社交媒体情感','News and Social Media Sentiment',r'news|social|tweet|microblog'),
('investor_sentiment','投资者情绪','Investor Sentiment',r'investor.*(?:sentiment|emotion)|market sentiment'),
('disclosure_tone','财报及电话会议语调','Report and Earnings-Call Tone',r'earning|report|disclosure|call transcript'),
('aspect_sentiment','面向实体与方面的情感','Entity- and Aspect-Based Sentiment',r'aspect|entity|targeted'),
('financial_stance','金融立场与观点识别','Financial Stance and Opinion Detection',r'stance|opinion|hawkish|dovish'),
('sentiment_market_effect','情绪变化与市场影响','Sentiment Dynamics and Market Effects',r'sentiment.*(?:market|return|dynamic)|emotion.*market'),
],
'financial_qa': [
('knowledge_qa','金融事实问答','Financial Factual QA',r'knowledge|factual|professional'),
('numerical_reasoning','数值计算与程序推理','Numerical Calculation and Program Reasoning',r'numerical|program|calculat|arithmet|math|reasoning'),
('table_text_qa','表格与文本联合问答','Table-and-Text QA',r'tabl|spreadsheet|hybrid'),
('multihop_qa','多文档与多跳问答','Multi-Document and Multi-Hop QA',r'multi.hop|multi.document|long.form'),
('multimodal_qa','图表及多模态问答','Chart and Multimodal QA',r'multimodal|chart|visual|image'),
('conversational_qa','对话式金融问答','Conversational Financial QA',r'convers|dialog|multi.turn'),
],
'financial_understanding': [
('information_extraction','实体与关系抽取','Entity and Relation Extraction',r'entity|relation|extract|named.entity'),
('financial_events','金融事件识别与关联','Financial Event Detection and Linking',r'event|merger|acquisition'),
('financial_text_classification','金融文本分类','Financial Text Classification',r'classif|translation|language task'),
('report_understanding','财报与公告理解','Report and Disclosure Understanding',r'report|disclosure|earning|account|tax|claim verif'),
('document_understanding','表格、图表及文档理解','Table, Chart and Document Understanding',r'tabl|chart|document|receipt|invoice|OCR|spreadsheet|layout'),
('text_generation','金融摘要与报告生成','Financial Summarization and Report Generation',r'summar|generat|narrat'),
],
'financial_decision': [
('trading_strategy','交易策略与买卖决策','Trading Strategies and Buy/Sell Decisions',r'trad|investment agent|financial agent|prediction market'),
('trading_execution','订单执行','Order Execution',r'execution|order execut'),
('market_making','做市与报价策略','Market Making and Quoting',r'market mak|quot|order book|market impact'),
('hedging','动态对冲','Dynamic Hedging',r'hedg'),
('corporate_decisions','企业融资及现金管理决策','Corporate Financing and Cash Management',r'corporate|cash manage|financing|business decision'),
('agent_decisions','金融智能体与多主体决策','Financial Agents and Multi-Agent Decisions',r'agent|simulat|economic behavior|prediction market'),
],
'sustainable_finance': [
('esg_evaluation','ESG 信息抽取与评价','ESG Extraction and Evaluation',r'ESG|sustainab'),
('esg_disclosure','可持续披露与漂绿识别','Sustainability Disclosure and Greenwashing',r'disclos|greenwash|report'),
('climate_risk','气候风险与转型风险','Climate and Transition Risk',r'climate|transition risk'),
('green_financing','绿色信贷与绿色融资','Green Credit and Financing',r'green.*(?:credit|financ|bond)'),
('carbon_finance','碳市场与碳金融','Carbon Markets and Finance',r'carbon|emission trad'),
('sustainable_investment','责任投资与社会影响','Responsible Investment and Social Impact',r'invest|social impact|responsib'),
],
'financial_services': [
('customer_intents','智能客服与业务咨询','Customer Support and Business Consultation',r'customer service|intent|banking dialog|consult|assistant'),
('product_recommendation','金融产品推荐与匹配','Financial Product Recommendation and Matching',r'recommend|product match'),
('personal_finance','个人财务规划与服务','Personal Financial Planning and Services',r'personal financ|financial advice|financial plan|household'),
('banking_workflows','贷款、支付及银行业务流程','Lending, Payment and Banking Workflows',r'bank|payment|lending|loan|business data'),
('bank_marketing','客户行为与关系管理','Customer Behavior and Relationship Management',r'market|churn|customer behav|subscription'),
('financial_inclusion','金融服务可及性与普惠金融','Financial Access and Inclusion',r'inclusion|accessib|unbanked|microfinance'),
],
'blockchain': [
('crypto_transactions','链上交易与账户分析','On-Chain Transaction and Account Analysis',r'transaction|account|address|blockchain'),
('token_economics','数字资产及代币经济','Digital Assets and Token Economics',r'token|digital asset|cryptocurrenc'),
('defi','DeFi 与链上金融机制','DeFi and On-Chain Financial Mechanisms',r'DeFi|decentrali.ed finance|liquidity pool|automated market'),
('smart_contracts','智能合约分析','Smart Contract Analysis',r'smart contract|Solidity'),
('onchain_markets','交易费、MEV 与链上市场机制','Fees, MEV and On-Chain Markets',r'MEV|transaction fee|miner.extract|maximum.extract|front.running'),
('blockchain_infrastructure','区块链金融基础设施','Blockchain Financial Infrastructure',r'infrastructure|consensus|settlement|ledger'),
],
'financial_safety': [
('financial_fraud','支付、交易及保险欺诈','Payment, Transaction and Insurance Fraud',r'fraud|scam|banknote|phishing'),
('aml','反洗钱与非法资金追踪','AML and Illicit Fund Tracing',r'money launder|illicit|AML'),
('identity_abuse','身份冒用与账户滥用','Identity and Account Abuse',r'identity|account.*(?:abuse|takeover)|impersonat'),
('financial_attacks','金融网络及智能合约攻击','Financial Network and Smart Contract Attacks',r'attack|vulnerab|exploit|smart contract'),
('privacy_security','隐私与敏感信息保护','Privacy and Sensitive Information Protection',r'privacy|sensitive|federated|confidential'),
('financial_regulation','监管合规与违规检测','Regulatory Compliance and Violation Detection',r'regulat|complian|audit'),
('model_safety','金融模型及智能体安全','Financial Model and Agent Safety',r'adversarial|robustness|bias|fairness|jailbreak|LLM.*safety|model.*safety'),
],
'financial_ir': [
('document_retrieval','金融文档与公告检索','Financial Document and Disclosure Retrieval',r'document|report|filing'),
('retrieval','金融语义匹配与排序','Financial Semantic Matching and Ranking',r'retriev|embed|rerank|semantic|match'),
('table_retrieval','表格及数值信息检索','Table and Numerical Retrieval',r'tabl|numeric|spreadsheet'),
('multimodal_retrieval','图表与多模态检索','Chart and Multimodal Retrieval',r'multimodal|chart|visual|image'),
('crosslingual_retrieval','跨语言金融检索','Cross-Lingual Financial Retrieval',r'cross.ling|multiling'),
('rag','金融 RAG 的证据检索与重排序','Evidence Retrieval and Reranking for Financial RAG',r'RAG|retrieval.augment|evidence'),
],
'financial_evaluation': [
('task_benchmarks','金融数据集与任务基准','Financial Datasets and Task Benchmarks',r'dataset|benchmark|corpus|corpora|bench'),
('financial_reasoning_eval','金融知识与专业能力评测','Financial Knowledge and Professional Evaluation',r'knowledge|professional|exam|business|accounting'),
('numerical_evaluation','数值推理与计算评测','Numerical Reasoning and Calculation Evaluation',r'numeric|math|quantitative reason|calculat'),
('understanding_evaluation','金融理解及多模态评测','Financial Understanding and Multimodal Evaluation',r'understanding|multimodal|document|chart|table|summar|language'),
('agent_evaluation','金融决策与智能体评测','Financial Decision and Agent Evaluation',r'agent|decision|gym|environment|trading'),
('trust_evaluation','可靠性、安全与公平性评测','Reliability, Safety and Fairness Evaluation',r'reliab|safe|fair|bias|robust|hallu|fraud|scam'),
('evaluation_protocols','评测协议与指标','Evaluation Protocols and Metrics',r'protocol|metric|contamin|leakage|evaluat'),
],
'financial_models': [
('domain_models','金融基础模型与领域预训练','Financial Foundation Models and Domain Pretraining',r'pre.?train|foundation|world model|financial.*model'),
('financial_posttraining','金融指令微调与后训练','Financial Instruction Tuning and Post-Training',r'instruct|fine.tun|post.train|adapt|preference'),
('financial_representations','金融专用表示模型','Financial Representation Models',r'representation|embed|FinBERT'),
('financial_multimodal_models','金融多模态模型','Financial Multimodal Models',r'multimodal|FinTral|vision|image'),
('financial_ts_models','金融时序基础模型','Financial Time-Series Foundation Models',r'time.series|candlestick|K.line|market data|time series'),
('financial_efficient_models','金融模型适配、压缩与高效部署','Financial Model Adaptation, Compression and Deployment',r'compress|efficient|deploy|distill|quantiz'),
],
}

# Every former subcategory is either mapped or deliberately replaced by a more
# specific evidenced refinement. Historical schema and assignments remain frozen.
OLD_SUB = {
'factor_discovery':'factor_discovery','factor_evaluation':'factor_evaluation','ts_forecasting':'ts_forecasting','ts_foundation':'ts_representation','ts_generation':'ts_generation','ts_anomaly':'ts_anomaly','ts_imputation':'ts_imputation','ts_dynamics':'ts_representation','ts_uncertainty':'ts_forecasting','ts_general':'ts_forecasting','financial_processes':'ts_representation',
'pricing_models':'pricing_models','risk_factors':'pricing_models','option_pricing':'option_pricing','volatility_surface':'option_pricing','numerical_finance':'pricing_calibration','hedging':'hedging',
'allocation':'selection','selection':'selection','investment_evaluation':'portfolio_objectives','financial_planning':'financial_planning','trading_execution':'trading_strategy','microstructure':'market_making','market_simulation':'agent_decisions','prediction_markets':'agent_decisions',
'stock_prediction':'stock_prediction','volatility_prediction':'volatility_prediction','fx_crypto':'fx_crypto','credit_default':'credit_default','credit_data':'credit_default','financial_risk':'market_risk','risk_recourse':'credit_default','market_risk':'market_risk','liquidity_risk':'liquidity_risk','systemic_risk':'systemic_risk',
'insurance_business':'insurance_claims','financial_fraud':'financial_fraud','aml':'aml','scam':'financial_fraud','banknote_authentication':'financial_fraud','sentiment_stance':'news_sentiment','information_extraction':'information_extraction','text_generation':'text_generation','nlp_datasets':'financial_text_classification','claim_verification':'report_understanding','financial_translation':'financial_text_classification',
'numerical_reasoning':'numerical_reasoning','knowledge_qa':'knowledge_qa','qa_tasks':'numerical_reasoning','retrieval':'retrieval','rag':'rag','receipts_invoices':'document_understanding','financial_charts':'document_understanding','reports_tables':'document_understanding','financial_tables':'document_understanding','agent_decisions':'agent_decisions','tools_research':'agent_decisions','macro_forecasting':'ts_forecasting','economic_simulation':'agent_decisions','earnings_disclosure':'report_understanding','ma':'financial_events','accounting_tax':'report_understanding','real_estate':'enterprise_valuation',
'esg_disclosure':'esg_disclosure','sustainable_investment':'sustainable_investment','customer_intents':'customer_intents','bank_marketing':'bank_marketing','bank_data':'banking_workflows','personal_finance':'personal_finance','business_data':'banking_workflows','crypto_transactions':'crypto_transactions','smart_contracts':'smart_contracts','privacy_security':'privacy_security','trust_compliance':'model_safety','financial_regulation':'financial_regulation','robustness_attacks':'financial_attacks','domain_models':'domain_models','financial_benchmarks':'task_benchmarks','financial_reasoning_eval':'financial_reasoning_eval','task_benchmarks':'task_benchmarks','agent_evaluation':'agent_evaluation',
}

def definitions():
    return [dict(parent_id=parent,id=sid,label=en+' / '+zh,pattern=pattern)
            for parent,subs in GROUPS.items() for sid,zh,en,pattern in subs]
