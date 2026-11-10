# xRFM: Accurate, scalable, and interpretable feature learning models for tabular data

ICLR 2026 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：Allstate。 主题：Insurance & Actuarial / 保险与精算。

- 官方论文页：https://openreview.net/forum?id=wHuVdpnUFp
- 摘要来源：https://iclr.cc/virtual/2026/poster/10006744
- 本地 PDF：[打开](../../pdfs/ICLR/2026/iclr-2026-wHuVdpnUFp__xRFM_Accurate_scalable_and_interpretable_feature_learning_models_for_tabular_data.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Insurance & Actuarial / 保险与精算
- 细分方向：Insurance & Claims / 承保与理赔
- 技术方法标签：Tabular Learning / 表格学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Splitting method Dataset AGOP AGOP + TT PCA + TT RF + TT Airlines DepDelay 10M 0.9792 0.9782 0.9785 0.9785 Allstate Claims Severity 0.6480 0.6509 0.6526 0.6521 black friday 0.6879 0.6879 0.6891 0.6877 Buzzinsocialmedia Twitter 0.2300 0.2290 0.2137 0.2138 nyc-taxi-green-dec-2016 0.5268 0.5250 0.6283 0.5256 wave

## 原始摘要

Inference from tabular data, collections of continuous and categorical variables organized into matrices, is a foundation for modern technology and science. Yet, in contrast to the explosive changes in the rest of AI, the best practice for these predictive tasks has been relatively unchanged and is still primarily based on variations of Gradient Boosted Decision Trees (GBDTs). Very recently, there has been renewed interest in developing state-of-the-art methods for tabular data based on recent developments in neural networks and feature learning methods.  In this work, we introduce xRFM, an algorithm that combines feature learning kernel machines with a tree structure to both adapt to the local structure of the data and scale to essentially unlimited amounts of training data. We show that compared to $31$ other methods, including recently introduced tabular foundation models (TabPFN-v2) and GBDTs,  xRFM achieves best performance across $100$ regression datasets and is competitive to the best methods across $200$ classification datasets outperforming GBDTs. Additionally, xRFM provides  interpretability natively through the Average Gradient Outer Product.
