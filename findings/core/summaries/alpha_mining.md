## Research summary / 研究总结

**Factor Mining / 因子挖掘 · Findings / Core**

2026-11-20 · 7 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 研究对象是可以复用、组合和检验的收益信号。公式生成、筛选与组合是不同环节，搜索到低相关信号并不自动证明它具有稳定的样本外预测能力。

**当前收录与方法。** 本页仅总结 Findings / core 中的论文。当前较常见的子分类：Factor Discovery and Formula Generation / 因子发现与公式生成 (5); Factor Interpretation and Economic Meaning / 因子解释与经济含义 (1); Factor Validity and Stability / 因子有效性与稳定性 (1)。已标注的方法：Language Models & LLM / 语言模型与LLM (7); Uncertainty & Robustness / 不确定性与鲁棒性 (2); Optimization & Numerical Methods / 优化与数值方法 (2); Causal Learning / 因果学习 (1)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 检查样本外 IC、因子冗余、搜索预算、换手与成本。 代表论文的摘要、金融关联证据及原文链接见 [1](../indexes/finance_notes/2026.findings-emnlp.1514.md) · [2](../indexes/finance_notes/2024.findings-acl.233.md) · [3](../indexes/finance_notes/2024.findings-acl.185.md) · [4](../indexes/finance_notes/2026.findings-acl.138.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 将新颖性、经济含义与样本外有效性分开检验，并研究不同市场状态下的因子更新机制。

### English

**Problem and subdirections.** The object is a reusable return signal. Formula discovery, selection and combination are distinct stages; finding a low-correlation signal does not establish stable out-of-sample predictability.

**Current coverage and methods.** This page covers only Findings / core. Frequent subcategories: Factor Discovery and Formula Generation / 因子发现与公式生成 (5); Factor Interpretation and Economic Meaning / 因子解释与经济含义 (1); Factor Validity and Stability / 因子有效性与稳定性 (1). Recorded methods: Language Models & LLM / 语言模型与LLM (7); Uncertainty & Robustness / 不确定性与鲁棒性 (2); Optimization & Numerical Methods / 优化与数值方法 (2); Causal Learning / 因果学习 (1). Counts overlap and are not performance rankings.

**Data and evaluation.** Check out-of-sample IC, signal redundancy, search budget, turnover and costs. Representative abstracts, financial evidence and original sources are linked at [1](../indexes/finance_notes/2026.findings-emnlp.1514.md) · [2](../indexes/finance_notes/2024.findings-acl.233.md) · [3](../indexes/finance_notes/2024.findings-acl.185.md) · [4](../indexes/finance_notes/2026.findings-acl.138.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Test novelty, economic interpretation and out-of-sample validity separately, and study signal updating across market regimes.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. FaVOR: LLM-Based Agentic Framework for Factor Mining via Empirical Validation](../indexes/finance_notes/2026.findings-emnlp.1514.md) · EMNLP 2026 | 拆解、验证并整合经济假设对应因子<br>Decompose, validate and integrate hypothesis-grounded factors | 假设一致性仍需长期样本外验证<br>Hypothesis consistency still needs long-horizon out-of-sample testing |
| [2. Can Large Language Models Mine Interpretable Financial Factors More Effectively? A Neural-Symbolic Factor Mining Agent Model](../indexes/finance_notes/2024.findings-acl.233.md) · ACL 2024 | 多样样例选择与经验链辅助可解释因子挖掘<br>Diverse examples and experience chains support interpretable factor mining | 模拟收益取决于组合及回测设定<br>Simulated returns depend on portfolio and backtest settings |
| [3. LLMFactor: Extracting Profitable Factors through Prompts for Explainable Stock Movement Prediction](../indexes/finance_notes/2024.findings-acl.185.md) · ACL 2024 | 知识引导提示生成可解释市场影响因素<br>Knowledge-guided prompts produce explanatory market factors | 自然语言因素与可执行公式因子不同<br>Narrative factors differ from executable formulaic alphas |
| [4. AlphaQT-Bench: Diagnosing the Gap between Financial Code Generation and Quantitative Reasoning in LLMs](../indexes/finance_notes/2026.findings-acl.138.md) · ACL 2026 | 分层诊断金融代码的执行与时间正确性<br>Layered diagnosis of financial-code execution and temporal correctness | 过程可靠性不直接代表因子盈利<br>Process reliability does not directly establish profitable factors |
