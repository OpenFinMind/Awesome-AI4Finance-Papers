# Equilibrium Pricing in Oligopolistic Data Markets

ICML 2026 · main · application

正文包含金融领域数据、模型、实验或分领域评测。 主题：Market Prediction / 股价、收益与波动率预测。

- 官方论文页：https://openreview.net/forum?id=TAqejOfEAJ
- 摘要来源：https://icml.cc/virtual/2026/oral/71184
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-TAqejOfEAJ__Equilibrium_Pricing_in_Oligopolistic_Data_Markets.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_domain_data_or_experiment
- 主方向：Market Prediction / 股价、收益与波动率预测
- 细分方向：Stock Movement & Returns / 股价方向与收益预测
- 技术方法标签：Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

ding the relaxation in both theory and practice. 4. Finally, we run some empirics to show the robustness of our results. We simulate a news data marketplace where n firms purchase data from m news agencies to predict stock price movements, from a real-world dataset [1]. Each firm evaluates the informativeness of a dataset by training a logistic regression model on historical news and measuring prediction error. Sellers update their pricing strategies via an inertial approximate best-response dynamics (defined in Section 6). Empirically, the dynamics converge e

## 原始摘要

We study equilibrium pricing in oligopolistic data markets with budget-constrained buyers (e.g., ML companies purchasing data to improve model accuracy) and strategic data sellers. Sellers compete by setting prices for their datasets, giving rise to a pricing game whose pure Nash equilibria correspond to equilibrium prices. While equilibrium prices are guaranteed for rivalrous goods via competitive equilibrium, we show that the non-rivalry of data fundamentally alters this picture: an exact Nash equilibrium need not exist, and in fact no 1.364-approximate equilibrium exists under uniform pricing. We therefore investigate relaxed equilibrium notions. Allowing sellers to use beyond-uniform pricing—specifically, piecewise-linear convex pricing functions—guarantees approximate stability within a constant factor: there exists a pricing profile in which no seller can improve revenue by a factor of two by deviating to any uniform price (a 2-approximate Nash equilibrium). Finally, our simulations demonstrate fast convergence and empirical approximation guarantees that outperform the worst-case bound of 2.
