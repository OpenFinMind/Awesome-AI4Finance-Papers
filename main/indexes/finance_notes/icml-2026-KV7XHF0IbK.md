# Decision-focused Sparse Tangent Portfolio Optimization

ICML 2026 · main · core

以金融任务或金融数据为核心研究对象。 主题：Portfolio & Investment / 投资组合与投资管理。

- 官方论文页：https://openreview.net/forum?id=KV7XHF0IbK
- 摘要来源：https://icml.cc/virtual/2026/poster/64722
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-KV7XHF0IbK__Decision_focused_Sparse_Tangent_Portfolio_Optimization.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_review
- 主方向：Portfolio & Investment / 投资组合与投资管理
- 细分方向：Portfolio Selection & Optimization / 组合选择与优化
- 技术方法标签：Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：optimization
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Sparse tangent portfolio optimization aims to learn an interpretable, low-cardinality portfolio in the tangency direction of the mean-variance frontier. / However, the associated cardinality-constrained formulation is NP-hard, and standard predict-then-optimize pipelines often misalign forecasting accuracy with downstream portfolio quality. / This enables gradient flow through prediction, asset selection, and re-optimization, allowing the predictive model to directly optimize portfolio performance.

## 原始摘要

Sparse tangent portfolio optimization aims to learn an interpretable, low-cardinality portfolio in the tangency direction of the mean-variance frontier. However, the associated cardinality-constrained formulation is NP-hard, and standard predict-then-optimize pipelines often misalign forecasting accuracy with downstream portfolio quality. We propose an end-to-end decision-focused learning framework that reformulates Sharpe ratio maximization as a Disciplined Parametrized Programming (DPP)-compliant convex programming layer and replaces discrete selection with a smooth top-$k$ operator enforcing an exact cardinality $k$. This enables gradient flow through prediction, asset selection, and re-optimization, allowing the predictive model to directly optimize portfolio performance. Across four major equity markets, our method achieves competitive and often superior out-of-sample Sharpe ratios compared with historical and prediction-focused baselines, with particularly strong gains in larger asset universes. Our code is publicly available.
