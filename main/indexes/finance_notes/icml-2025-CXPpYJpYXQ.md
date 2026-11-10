# LOB-Bench: Benchmarking Generative AI for Finance - an Application to Limit Order Book Data

ICML 2025 · main · core

以金融任务或金融数据为核心研究对象。 主题：Trading & Microstructure / 交易与市场微观结构。

- 官方论文页：https://openreview.net/forum?id=CXPpYJpYXQ
- 摘要来源：https://icml.cc/virtual/2025/poster/46058
- 本地 PDF：[打开](../../pdfs/ICML/2025/icml-2025-CXPpYJpYXQ__LOB_Bench_Benchmarking_Generative_AI_for_Finance_an_Application_to_Limit_Order_Book_Data.pdf)；版本：publisher_version
- 金融依据类型：title_abstract_review
- 主方向：Trading & Microstructure / 交易与市场微观结构
- 细分方向：Order Books & Market Impact / 订单簿与市场冲击
- 技术方法标签：Generative Modeling / 生成建模
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：LOB-Bench
- 代码链接：摘要未提供可确认链接

## 纳入依据

While financial data presents one of the most challenging and interesting sequence modelling tasks due to high noise, heavy tails, and strategic interactions, progress in this area has been hindered by the lack of consensus on quantitative evaluation paradigms.

## 原始摘要

While financial data presents one of the most challenging and interesting sequence modelling tasks due to high noise, heavy tails, and strategic interactions, progress in this area has been hindered by the lack of consensus on quantitative evaluation paradigms. To address this, we present **LOB-Bench**, a benchmark, implemented in python, designed to evaluate the quality and realism of generative message-by-order data for limit order books (LOB) in the LOBSTER format. Our framework  measures distributional differences in conditional and unconditional statistics between generated and real LOB data, supporting flexible multivariate statistical evaluation. The benchmark also includes features commonly used LOB statistics such as spread, order book volumes, order imbalance, and message inter-arrival times, along with scores from a trained discriminator network. Lastly, LOB-Bench contains "market impact metrics", i.e. the cross-correlations and price response functions for specific events in the data. We benchmark generative autoregressive state-space models, a (C)GAN, as well as a parametric LOB model and find that the autoregressive GenAI approach beats traditional model classes.
