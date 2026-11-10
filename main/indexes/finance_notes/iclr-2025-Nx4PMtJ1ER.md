# Signature Kernel Conditional Independence Tests in Causal Discovery for Stochastic Processes

ICLR 2025 · main · application

正文包含金融数据、金融训练数据、金融任务评测或具体金融场景案例。 主题：Time Series / 时间序列；Trading & Microstructure / 交易与市场微观结构；Corporate Finance & Accounting / 公司金融与会计。

- 官方论文页：https://openreview.net/forum?id=Nx4PMtJ1ER
- 摘要来源：https://iclr.cc/virtual/2025/poster/29848
- 本地 PDF：[打开](../../pdfs/ICLR/2025/iclr-2025-Nx4PMtJ1ER__Signature_Kernel_Conditional_Independence_Tests_in_Causal_Discovery_for_Stochastic_Processes.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Causality & Dynamics / 序列因果与动力学；Trading & Execution / 交易策略与执行；Real Estate & Business Finance / 房地产与企业财务应用
- 技术方法标签：Causal Learning / 因果学习；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：causal
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

8 ± 293 7799 ± 250 SCOTCH 558 ± 14 1861 ± 43 8567 ± 63 35467 ± 833 105165 ± 10934 B.7 R EAL -W ORLD PAIRS T RADING E XAMPLE In the pairs trading experiment, stock price data is downloaded from Yahoo Finance for a predefined list of stocks over a specific period, divided into training (1st January 2010 to 31st December 2011) and trading intervals (1st January 2012 to 31st December 2012). The chose stocks are Trinity Industries (TRN), Brandywine Realty Trust (BDN), Commercial Metals Company (CMC), The New York Times Company (NYT), New York Community Bancorp (NYCB), The Wendy’s Company (WEN), CNX Resources Corporation (CNX). Logarithms of the stock prices are computed to stabilize variance and normalize the prices. During the t

## 原始摘要

Inferring the causal structure underlying stochastic dynamical systems from observational data holds great promise in domains ranging from science and health to finance. Such processes can often be accurately modeled via stochastic differential equations (SDEs), which naturally imply causal relationships via `which variables enter the differential of which other variables'. In this paper, we develop conditional independence (CI) constraints on coordinate processes over selected intervals that are Markov with respect to the acyclic dependence graph (allowing self-loops) induced by a general SDE model. We then provide a sound and complete causal discovery algorithm, capable of handling both fully and partially observed data, and uniquely recovering the underlying or induced ancestral graph by exploiting time directionality assuming a CI oracle. Finally, to make our algorithm practically usable, we also propose a flexible, consistent signature kernel-based CI test to infer these constraints from data. We extensively benchmark the CI test in isolation and as part of our causal discovery algorithms, outperforming existing approaches in SDE models and beyond.
