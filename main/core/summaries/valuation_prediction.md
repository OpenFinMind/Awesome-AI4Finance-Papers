## Research summary / 研究总结

**Valuation Prediction / 估值预测 · Main / Core**

2026-11-20 · 82 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 预测目标包括资产价格、收益、波动率、企业价值及经营基本面。新闻、财报、市场序列和关系结构提供不同信息来源，目标与预测窗口必须明确。

**当前收录与方法。** 本页仅总结 Main / core 中的论文。当前较常见的子分类：Stock Price and Return Prediction / 股票价格与收益预测 (57); Earnings, Revenue and Fundamental Prediction / 盈利、营收与基本面预测 (23); Volatility Prediction / 波动率预测 (11); Movement Direction and Asset Ranking / 涨跌方向与资产排序 (9); Enterprise and Equity Valuation / 企业价值与股权估值 (3)。已标注的方法：Uncertainty & Robustness / 不确定性与鲁棒性 (20); Language Models & LLM / 语言模型与LLM (20); Representation Learning / 表征学习 (14); Transformer / Transformer模型 (13); Graph Learning / 图学习 (11)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 同时核对时间泄漏、预测目标、跨市场泛化和经济效用。 代表论文的摘要、金融关联证据及原文链接见 [1](../indexes/finance_notes/2026.emnlp-main.1329.md) · [2](../indexes/finance_notes/kdd-2025-c2b0e7b0df67.md) · [3](../indexes/finance_notes/kdd-2023-f7332a9c061f.md) · [4](../indexes/finance_notes/kdd-2021-7b279452953c.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 检验时间戳、公司身份和数据修订带来的泄漏，并区分预测准确率、资产排序与扣费后的经济效用。

### English

**Problem and subdirections.** Targets include asset prices, returns, volatility, enterprise value and business fundamentals. News, reports, market sequences and relational structure provide different information; targets and horizons must be explicit.

**Current coverage and methods.** This page covers only Main / core. Frequent subcategories: Stock Price and Return Prediction / 股票价格与收益预测 (57); Earnings, Revenue and Fundamental Prediction / 盈利、营收与基本面预测 (23); Volatility Prediction / 波动率预测 (11); Movement Direction and Asset Ranking / 涨跌方向与资产排序 (9); Enterprise and Equity Valuation / 企业价值与股权估值 (3). Recorded methods: Uncertainty & Robustness / 不确定性与鲁棒性 (20); Language Models & LLM / 语言模型与LLM (20); Representation Learning / 表征学习 (14); Transformer / Transformer模型 (13); Graph Learning / 图学习 (11). Counts overlap and are not performance rankings.

**Data and evaluation.** Check temporal leakage, target definitions, cross-market transfer and economic utility. Representative abstracts, financial evidence and original sources are linked at [1](../indexes/finance_notes/2026.emnlp-main.1329.md) · [2](../indexes/finance_notes/kdd-2025-c2b0e7b0df67.md) · [3](../indexes/finance_notes/kdd-2023-f7332a9c061f.md) · [4](../indexes/finance_notes/kdd-2021-7b279452953c.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Check leakage from timestamps, company identity and data revisions; separate prediction accuracy, asset ranking and economic value after costs.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. CAME: Company-Aware Evidence-Memory Experts for Interpretable Quarter-Ahead Revenue Forecasting](../indexes/finance_notes/2026.emnlp-main.1329.md) · EMNLP 2026 | 公司证据与误差记忆修正收入预测锚点<br>Company evidence and error memory adjust revenue forecast anchors | 含开发样本且公司数有限，需外部验证<br>Development-inclusive and limited-firm evidence needs external validation |
| [2. CAMEF: Causal-Augmented Multi-Modality Event-Driven Financial Forecasting by Integrating Time Series Patterns and Salient Macroeconomic Announcements](../indexes/finance_notes/kdd-2025-c2b0e7b0df67.md) · KDD 2025 | 宏观事件、价格及反事实增强的多模态预测<br>Multimodal forecasting with macro events, prices and counterfactual augmentation | 事件时点与因果假设限定解释范围<br>Event timing and causal assumptions bound interpretation |
| [3. DoubleAdapt: A Meta-learning Approach to Incremental Learning for Stock Trend Forecasting](../indexes/finance_notes/kdd-2023-f7332a9c061f.md) · KDD 2023 | 双适配器元学习处理增量分布变化<br>Dual-adapter meta-learning handles incremental shifts | 更新效率与长期效果应分别报告<br>Report update efficiency and long-term quality separately |
| [4. Learning Multiple Stock Trading Patterns with Temporal Routing Adaptor and Optimal Transport](../indexes/finance_notes/kdd-2021-7b279452953c.md) · KDD 2021 | 最优传输辅助多模式预测器路由<br>Optimal transport supports routing among trading-pattern predictors | 路由训练和测试信息必须分离<br>Routing must separate training and test information |
