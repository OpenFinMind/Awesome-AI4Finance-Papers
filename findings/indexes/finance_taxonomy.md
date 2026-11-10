# AI for Finance 分类说明

分类版本 2.0。仅整理本目录中已核验的长文；金融收录与 core / application 属性独立于任务、子方向和技术方法。Main 与 Findings 分开维护。

- `finance_primary_topic`：一个归档主方向，便于按单一目录查看，主方向篇数合计为全部金融篇数。

- `finance_topics`：可重叠的金融研究主题。例如金融序列生成可同时属于 Time Series 和 Blockchain。

- `finance_subtopics`：具体任务，如 Alpha Discovery、Forecasting、Anomaly Detection、Credit Scoring、Numerical Reasoning。

- `finance_methods`：独立的技术方法维度，如 LLM、强化学习、图学习、扩散、因果、公平性与追索、联邦学习。技术标签不能替代金融任务。

- 标签依据题名、官方摘要及已复核的金融证据；具体匹配片段保存在 [逐篇分类记录](../checks/finance_taxonomy/assignments.json)。不确定细分方向时保留在 Other Financial Applications，不强行猜测。规则辅助分类并保留按论文 ID 的人工修订，后续可继续纠正。

- Alpha Mining 聚焦公式化因子和 alpha 发现；Asset Pricing 聚焦收益定价与风险溢价。普通 alpha 超参数不属于 Alpha Mining。Time Series 只覆盖当前金融清单中的序列方法。

- 借贷、银行营销和钞票真伪数据上的通用模型按具体金融任务归类；例如 German Credit 的反事实解释论文可以是 Credit & Financial Risk + Fairness & Recourse，并不表示它提出了金融专用模型。

- 子方向和技术方法允许多个标签，篇数不能直接相加；标签不会把 application 升格为 core。

[主题总览](ai_for_finance.md) · [金融 Excel](../finance_catalog.xlsx) · [分类规则与定义](../checks/finance_taxonomy/schema.json) · [人工修订](../checks/finance_taxonomy/manual_overrides.json)

## 主题与子方向

### [Alpha Mining / 量化因子挖掘](finance_topics/alpha_mining.md)

因子表达式搜索、自动化 alpha 发现与因子评价；不把一般 alpha 超参数或资产定价混入。

- Alpha Discovery / Alpha与因子发现

- Factor Evaluation / 因子评价与回测

### [Time Series / 时间序列](finance_topics/time_series.md)

有金融应用证据的序列预测、生成、表征、异常、缺失及动态建模。

- Forecasting / 序列预测

- Representation & Foundation Models / 表征与基础模型

- Generation & Simulation / 序列生成与仿真

- Anomaly Detection / 序列异常检测

- Imputation & Irregular Series / 缺失与不规则序列

- Causality & Dynamics / 序列因果与动力学

- Probabilistic Forecasting & Calibration / 概率预测与校准

- General Time-Series Methods / 综合序列方法

- Financial Stochastic Processes / 金融随机过程

### [Asset Pricing / 资产定价](finance_topics/asset_pricing.md)

收益横截面、风险溢价、随机折现因子与资产定价模型。

- Pricing Models & Risk Premia / 定价模型与风险溢价

- Risk Factor Models / 市场风险因子建模

### [Derivatives & Hedging / 衍生品定价与对冲](finance_topics/derivatives.md)

期权、隐含波动率曲面、衍生品定价与对冲。

- Option Pricing & PDEs / 期权定价与PDE

- Hedging / 对冲

- Implied Volatility / 隐含波动率曲面

### [Portfolio & Investment / 投资组合与投资管理](finance_topics/portfolio.md)

资产配置、组合选择、投资评价与有效前沿；通用模型组合不据此归类。

- Asset Allocation / 资产配置

- Portfolio Selection & Optimization / 组合选择与优化

- Investment Evaluation & Decisions / 投资评价与决策

- Financial Planning / 财务规划

### [Trading & Microstructure / 交易与市场微观结构](finance_topics/trading.md)

交易策略、执行、做市、订单簿、市场仿真与预测市场。

- Trading & Execution / 交易策略与执行

- Order Books & Market Impact / 订单簿与市场冲击

- Market Simulation / 金融市场仿真

- Prediction Markets / 预测市场

### [Market Prediction / 股价、收益与波动率预测](finance_topics/market_prediction.md)

股票方向与收益、波动率、汇率或加密资产市场预测。

- Stock Movement & Returns / 股价方向与收益预测

- Volatility & Tail Forecasts / 波动率与尾部预测

- FX & Crypto Forecasts / 汇率与加密资产预测

### [Credit & Financial Risk / 信贷与金融风险](finance_topics/credit_risk.md)

授信、违约、信用风险、运营风险和尾部风险。

- Credit Scoring & Default / 信用评分与违约

- Financial Risk / 金融风险管理

- Lending & Credit Data / 借贷与信贷数据应用

### [Insurance & Actuarial / 保险与精算](finance_topics/insurance.md)

承保、保费、理赔、保险业务数据与精算应用。

- Insurance & Claims / 承保与理赔

### [Fraud & AML / 欺诈检测与反洗钱](finance_topics/fraud_aml.md)

支付和金融交易欺诈、反洗钱、金融诈骗。

- Payment & Transaction Fraud / 支付与交易欺诈

- Anti-Money Laundering / 反洗钱

- Scams & Financial Misinformation / 诈骗与金融虚假信息

- Banknote Authentication / 钞票真伪识别

### [Financial NLP / 金融文本、情感与事件](finance_topics/financial_nlp.md)

金融文本情感、立场、信息抽取、生成和摘要。

- Sentiment & Stance / 情感与立场

- Entities, Events & Causality / 实体、事件与关系抽取

- Generation & Summarization / 金融文本生成与摘要

- Financial Language Tasks & Corpora / 金融语言任务与语料

- Financial Claim Verification / 金融声明核验

- Financial Translation / 金融翻译

### [Financial QA & Reasoning / 金融问答与数值推理](finance_topics/financial_qa.md)

金融知识问答、财报表格计算、数学和多跳推理。

- Numerical & Table Reasoning / 数值与表格推理

- Knowledge & Conversational QA / 知识与对话问答

- Financial Reasoning Tasks / 金融推理任务

### [Financial IR & RAG / 金融检索与RAG](finance_topics/financial_ir.md)

金融信息检索、FiQA 检索评测、嵌入、重排与金融 RAG。

- Retrieval, Embedding & Reranking / 检索、嵌入与重排

- Financial RAG & Long Documents / 金融RAG与长文档

### [Document AI / 票据、财报与图表理解](finance_topics/document_ai.md)

票据发票、OCR、文档版面、财务表格与金融图表；普通表格分类另标技术方法。

- Receipts, Invoices & OCR / 票据发票与OCR

- Charts & Visual Understanding / 金融图表与视觉理解

- Report Layout & Structured Extraction / 财报版面与结构提取

- Financial Tables & Spreadsheets / 财务表格与电子表格

### [Financial Agents / 金融Agent与决策](finance_topics/financial_agents.md)

金融研究、投资分析、金融工具使用和金融决策 Agent。

- Investment & Financial Research Agents / 投研与金融决策Agent

- Financial Tools & Deep Research / 金融工具与深度研究

### [Macro & Economic Forecasting / 宏观经济与预测](finance_topics/macro_economics.md)

宏观指标、货币政策、经济预测、经济活动仿真。

- Macro Indicators & Policy / 宏观指标与政策

- Economic Behavior & Simulation / 经济行为与仿真

### [Corporate Finance & Accounting / 公司金融与会计](finance_topics/corporate_finance.md)

盈利、披露、并购、财务报告、会计审计与税务。

- Earnings & Corporate Disclosures / 盈利与公司披露

- Mergers & Acquisitions / 并购与公司事件

- Accounting, Audit & Tax / 会计、审计与税务

- Real Estate & Business Finance / 房地产与企业财务应用

### [ESG & Sustainable Finance / ESG与可持续金融](finance_topics/esg.md)

企业可持续披露、绿色投资、ESG 分析和合规审计。

- ESG Disclosure & Greenwashing / ESG披露与漂绿

- Sustainable Investment / 可持续投资

### [Banking & Customer Service / 银行业务与客户服务](finance_topics/banking.md)

银行营销、客户意图、客服对话、债务催收及金融服务。

- Banking Dialogue & Intent / 银行对话与意图

- Bank Marketing & Churn / 银行营销与客户流失

- Banking Data Applications / 银行业务数据应用

- Personal Finance Interaction / 个人理财交互

### [Blockchain & Digital Assets / 区块链与数字资产](finance_topics/blockchain.md)

比特币、以太坊、链上交易、智能合约及加密资产数据。

- Crypto & Blockchain Transactions / 加密资产与链上交易

- Smart Contracts & DeFi / 智能合约与DeFi

### [Financial Safety & Compliance / 金融安全与合规](finance_topics/financial_safety.md)

金融隐私、金融 LLM 安全、投资建议风险、监管及可信评测。

- Financial Privacy & Security / 金融隐私与信息安全

- Trust, Compliance & Bias / 可信、合规与偏差审计

- Financial Regulation / 金融监管与业务规则

- Adversarial Robustness in Finance / 金融应用中的攻击与防御

### [Financial Models & Benchmarks / 金融模型与评测资源](finance_topics/financial_models.md)

金融领域预训练、领域适配、跨任务金融评测与综合金融资源。

- Financial Pretraining & Adaptation / 金融预训练与领域适配

- Cross-Task Financial Evaluation / 跨任务金融综合评测

- Numerical Finance / 计算金融与数值方法

- Professional Financial Evaluation / 金融专业能力评测

### [Other Financial Applications / 其他金融应用](finance_topics/other_finance.md)

金融相关性已确认，但当前证据未支持更具体的上述任务分类。


## 技术方法标签

- Language Models & LLM / 语言模型与LLM

- Reinforcement Learning / 强化学习

- Graph Learning / 图学习

- Diffusion & Flow / 扩散与流模型

- Generative Modeling / 生成建模

- Transformer / Transformer模型

- Causal Learning / 因果学习

- Fairness & Recourse / 公平性与算法追索

- Uncertainty & Robustness / 不确定性与鲁棒性

- Privacy & Federated Learning / 隐私与联邦学习

- Tabular Learning / 表格学习

- Multimodal Learning / 多模态学习

- Retrieval & RAG / 检索与RAG

- Optimization & Numerical Methods / 优化与数值方法

- Representation Learning / 表征学习
