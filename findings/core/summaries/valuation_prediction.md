## Research summary / 研究总结

**Valuation Prediction / 估值预测 · Findings / Core**

2026-11-20 · 18 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 预测目标包括资产价格、收益、波动率、企业价值及经营基本面。新闻、财报、市场序列和关系结构提供不同信息来源，目标与预测窗口必须明确。

**当前收录与方法。** 本页仅总结 Findings / core 中的论文。当前较常见的子分类：Stock Price and Return Prediction / 股票价格与收益预测 (8); Earnings, Revenue and Fundamental Prediction / 盈利、营收与基本面预测 (5); Enterprise and Equity Valuation / 企业价值与股权估值 (2); Volatility Prediction / 波动率预测 (2); FX, Commodity and Digital Asset Forecasting / 汇率、商品及数字资产行情预测 (1)。已标注的方法：Language Models & LLM / 语言模型与LLM (10); Graph Learning / 图学习 (2); Tabular Learning / 表格学习 (2); Causal Learning / 因果学习 (1); Representation Learning / 表征学习 (1)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 同时核对时间泄漏、预测目标、跨市场泛化和经济效用。 代表论文的摘要、金融关联证据及原文链接见 [1](../indexes/finance_notes/2026.findings-acl.1555.md) · [2](../indexes/finance_notes/2025.findings-acl.489.md) · [3](../indexes/finance_notes/2025.findings-acl.946.md) · [4](../indexes/finance_notes/2024.findings-emnlp.486.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 检验时间戳、公司身份和数据修订带来的泄漏，并区分预测准确率、资产排序与扣费后的经济效用。

### English

**Problem and subdirections.** Targets include asset prices, returns, volatility, enterprise value and business fundamentals. News, reports, market sequences and relational structure provide different information; targets and horizons must be explicit.

**Current coverage and methods.** This page covers only Findings / core. Frequent subcategories: Stock Price and Return Prediction / 股票价格与收益预测 (8); Earnings, Revenue and Fundamental Prediction / 盈利、营收与基本面预测 (5); Enterprise and Equity Valuation / 企业价值与股权估值 (2); Volatility Prediction / 波动率预测 (2); FX, Commodity and Digital Asset Forecasting / 汇率、商品及数字资产行情预测 (1). Recorded methods: Language Models & LLM / 语言模型与LLM (10); Graph Learning / 图学习 (2); Tabular Learning / 表格学习 (2); Causal Learning / 因果学习 (1); Representation Learning / 表征学习 (1). Counts overlap and are not performance rankings.

**Data and evaluation.** Check temporal leakage, target definitions, cross-market transfer and economic utility. Representative abstracts, financial evidence and original sources are linked at [1](../indexes/finance_notes/2026.findings-acl.1555.md) · [2](../indexes/finance_notes/2025.findings-acl.489.md) · [3](../indexes/finance_notes/2025.findings-acl.946.md) · [4](../indexes/finance_notes/2024.findings-emnlp.486.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Check leakage from timestamps, company identity and data revisions; separate prediction accuracy, asset ranking and economic value after costs.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. Analyze Like a Venture Capitalist: Information-Gain and Knowledge Enhanced Graph Reasoning for Startup Success Prediction](../indexes/finance_notes/2026.findings-acl.1555.md) · ACL 2026 | 知识与证据子图支持创业成功预测<br>Knowledge and evidence subgraphs support startup-success prediction | 结果标签和真实投资退出收益不同<br>Outcome labels differ from realized investment exits |
| [2. FinRipple: Aligning Large Language Models with Financial Market for Event Ripple Effect Awareness](../indexes/finance_notes/2025.findings-acl.489.md) · ACL 2025 | 时变关系图与 RL 建模事件涟漪效应<br>Dynamic relations and RL model event-ripple effects | 图构建与市场理论假设影响外推<br>Graph construction and market assumptions affect extrapolation |
| [3. Same Company, Same Signal: The Role of Identity in Earnings Call Transcripts](../indexes/finance_notes/2025.findings-acl.946.md) · ACL 2025 | 检验公司身份及历史波动率的强基线<br>Test strong firm-identity and historical-volatility baselines | 特定波动率任务的结论不覆盖所有文本用途<br>Task-specific volatility findings do not cover all uses of text |
| [4. Financial Forecasting from Textual and Tabular Time Series](../indexes/finance_notes/2024.findings-emnlp.486.md) · EMNLP 2024 | 融合数值、宏观及文档预测下季盈利相对预期<br>Fuse numeric, macro and document series to predict next-quarter earnings relative to expectations | 季度任务不能外推为任意频率预测<br>Quarterly evidence does not establish arbitrary-frequency forecasting |
