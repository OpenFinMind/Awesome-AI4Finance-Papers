# Towards Financial World Modeling

NeurIPS 2026 · main · core

以金融市场为研究对象，或包含明确的金融领域数据和应用评测。 主题：Trading & Microstructure / 交易与市场微观结构；Market Prediction / 股价、收益与波动率预测。

- 官方论文页：https://openreview.net/forum?id=OEokq7iASc
- 摘要来源：https://neurips.cc/Downloads/2026
- PDF 状态：access_blocked
- 金融依据类型：title_abstract_financial_task_or_data
- 主方向：Trading & Microstructure / 交易与市场微观结构
- 细分方向：Market Simulation / 金融市场仿真；Volatility & Tail Forecasts / 波动率与尾部预测
- 技术方法标签：Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Financial markets are complex, noisy environments which present unique challenges for representation learning and world modeling. / In this study, we systematically explore the application of supervised and self-supervised representation learning methods to financial markets data and their ability to learn world models of financial markets. / To support this, we assemble and release $\textbf{Market-1T}$ a dataset of more than one trillion observations spanning all US equities from 2008 through 2025. / Our results highlight that supervised methods are still dominant in this domain when applied directly to core quantitative finance tasks: predicting changes in prices, volatility, and transactions cost.

## 原始摘要

Financial markets are complex, noisy environments which present unique challenges for representation learning and world modeling. In this study, we systematically explore the application of supervised and self-supervised representation learning methods to financial markets data and their ability to learn world models of financial markets. To support this, we assemble and release $\textbf{Market-1T}$ a dataset of more than one trillion observations spanning all US equities from 2008 through 2025. We then develop a domain-specific data augmentation and apply a variety of modern SSL objectives including Joint Embedding Predictive Architecture (JEPA), Masked Autoencoder (MAE), and DINO. Our results highlight that supervised methods are still dominant in this domain when applied directly to core quantitative finance tasks: predicting changes in prices, volatility, and transactions cost. Further, when supervised models are trained across tasks they are able to leverage complementarities which enhance cross-task performance. While performance of SSL-based methods on these core tasks lags behind, we find that they better capture latent structure---such as time and assets effects---which supervised models miss. Our results suggest current SSL objectives capture broad features of markets but further work is needed to close the gap between supervised methods.
