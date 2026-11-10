# FeDaL: Federated Dataset Learning for General Time Series Foundation Models

ICLR 2026 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：FRED-MD。 主题：Time Series / 时间序列；Macro & Economic Forecasting / 宏观经济与预测；Blockchain & Digital Assets / 区块链与数字资产。

- 官方论文页：https://openreview.net/forum?id=HK6t5x5gJq
- 摘要来源：https://iclr.cc/virtual/2026/poster/10010401
- 本地 PDF：[打开](../../pdfs/ICLR/2026/iclr-2026-HK6t5x5gJq__FeDaL_Federated_Dataset_Learning_for_General_Time_Series_Foundation_Models.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；Representation & Foundation Models / 表征与基础模型；Macro Indicators & Policy / 宏观指标与政策；Crypto & Blockchain Transactions / 加密资产与链上交易
- 技术方法标签：Privacy & Federated Learning / 隐私与联邦学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Time Series；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/shengchaochen82/FeDaL.

## 纳入依据

Dataset # Channels Frequency Length Bitcoin 18 Daily Min: 2659 Max: 4581 Economic FRED-MD 107 Monthly Fixed: 728 NN5 111 Daily Fixed: 791 Pedestrain Counts 66 Hourly Min: 576 Max: 96424 Transport Rideshare 2304 Daily Fixed: 541 San Francisco Traffic 862

## 原始摘要

Dataset-level heterogeneity introduces significant domain biases that fundamentally degrade generalization on general Time Series Foundation Models (TSFMs), yet this challenge remains underexplored. This paper rethinks the from-scratch training of TSFMs using the paradigm of federated learning. We propose a novel Federated Dataset Learning (**FeDaL**) approach to tackle heterogeneous time series by learning dataset-agnostic temporal representations. Specifically, the distributed architecture of federated learning is a nature solution to decompose heterogeneous TS datasets into shared generalized knowledge and preserved personalized knowledge. Moreover, based on the TSFM architecture, FeDaL explicitly mitigates both local and global biases by adding two complementary mechanisms: Domain Bias Elimination (DBE) and Global Bias Elimination (GBE). FeDaL`s cross-dataset generalization has been extensively evaluated in real-world datasets spanning eight tasks (including various regression and classification), against 54 baselines. We further analyze federated scaling behavior, showing how data volume, client count, and join rate affect model performance under decentralization. Our code is publicly available at https://github.com/shengchaochen82/FeDaL.
