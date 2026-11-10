# Smooth Quadratic Prediction Markets

NeurIPS 2025 · main · core

以金融任务或金融数据为核心研究对象。 主题：Trading & Microstructure / 交易与市场微观结构；Financial Agents / 金融Agent与决策。

- 官方论文页：https://openreview.net/forum?id=d3FjdOwLEd
- 摘要来源：https://neurips.cc/virtual/2025/poster/117036
- 本地 PDF：[打开](../../pdfs/NeurIPS/2025/neurips-2025-d3FjdOwLEd__Smooth_Quadratic_Prediction_Markets.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_review
- 主方向：Trading & Microstructure / 交易与市场微观结构
- 细分方向：Trading & Execution / 交易策略与执行；Order Books & Market Impact / 订单簿与市场冲击；Prediction Markets / 预测市场；Investment & Financial Research Agents / 投研与金融决策Agent
- 技术方法标签：Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

To motivate the application of the Smooth Quadratic Prediction Market, we independently examine agents' trading behavior under two realistic constraints: bounded budgets and buy-only securities.

## 原始摘要

When agents trade in a Duality-based Cost Function prediction market, they collectively implement the learning algorithm Follow-The-Regularized-Leader [Abernethy et al., 2013]. We ask whether other learning algorithms could be used to inspire the design of prediction markets. By decomposing and modifying the Duality-based Cost Function Market Maker's (DCFMM) pricing mechanism, we propose a new prediction market, called the Smooth Quadratic Prediction Market, the incentivizes agents to collectively implement general steepest gradient descent. Relative to the DCFMM, the Smooth Quadratic Prediction Market has a better worst-case monetary loss for AD securities while preserving axiom guarantees such as the existence of instantaneous price, information incorporation, expressiveness, no arbitrage, and a form of incentive compatibility.  To motivate the application of the Smooth Quadratic Prediction Market, we independently examine agents' trading behavior under two realistic constraints: bounded budgets and buy-only securities.  Finally, we provide an introductory analysis of an approach to facilitate adaptive liquidity using the Smooth Quadratic Prediction Market. Our results suggest future designs where the price update rule is separate from the fee structure, yet guarantees are preserved.
