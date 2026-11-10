# Graphical Models in Heavy-Tailed Markets

NeurIPS 2021 · main · core

以金融任务或金融数据为核心研究对象。 主题：Asset Pricing / 资产定价；Blockchain & Digital Assets / 区块链与数字资产。

- 官方论文页：https://openreview.net/forum?id=w1FvEPcwTnI
- 摘要来源：https://neurips.cc/virtual/2021/poster/27885
- 本地 PDF：[打开](../../pdfs/NeurIPS/2021/neurips-2021-w1FvEPcwTnI__Graphical_Models_in_Heavy_Tailed_Markets.pdf)；版本：publisher_version
- 金融依据类型：title_abstract_review
- 主方向：Asset Pricing / 资产定价
- 细分方向：Risk Factor Models / 市场风险因子建模；Crypto & Blockchain Transactions / 加密资产与链上交易
- 技术方法标签：Graph Learning / 图学习；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Heavy-tailed statistical distributions have long been considered a more realistic statistical model for the data generating process in financial markets in comparison to their Gaussian counterpart.

## 原始摘要

Heavy-tailed statistical distributions have long been considered a more realistic statistical model for the data generating process in financial markets in comparison to their Gaussian counterpart. Nonetheless, mathematical nuisances, including nonconvexities, involved in estimating graphs in heavy-tailed settings pose a significant challenge to the practical design of algorithms for graph learning. In this work, we present graph learning estimators based on the Markov random field framework that assume a Student-$t$ data generating process. We design scalable numerical algorithms, via the alternating direction method of multipliers, to learn both connected and $k$-component graphs along with their theoretical convergence guarantees. The proposed methods outperform state-of-the-art benchmarks in an extensive series of practical experiments with publicly available data from the S\&P500 index, foreign exchanges, and cryptocurrencies.
