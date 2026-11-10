# TabReD: Analyzing Pitfalls and Filling the Gaps in Tabular Deep Learning Benchmarks

ICLR 2025 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：home-credit。 主题：Credit & Financial Risk / 信贷与金融风险；Insurance & Actuarial / 保险与精算。

- 官方论文页：https://openreview.net/forum?id=L14sqcrUC3
- 摘要来源：https://iclr.cc/virtual/2025/poster/30020
- 本地 PDF：[打开](../../pdfs/ICLR/2025/iclr-2025-L14sqcrUC3__TabReD_Analyzing_Pitfalls_and_Filling_the_Gaps_in_Tabular_Deep_Learning_Benchmarks.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Credit Scoring & Default / 信用评分与违约；Insurance & Claims / 承保与理赔；Lending & Credit Data / 借贷与信贷数据应用
- 技术方法标签：Tabular Learning / 表格学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

96 Kaggle Insurance plan acceptance prediction Ecom Offers 106K 119 Kaggle Predict whether a user will redeem an offers HomeCredit Default 381K (1.5M) 696 Kaggle Loan default prediction Cooking Time 228K (10.6M) 195 New Restaurant order cooking time estimation Delivery ETA 224K (6.9M) 225 New Grocery delivery courier ETA prediction Maps Routing 192K (8.8M) 1026 New Navigation app ETA from live road-graph features Weather 605K (6.0M) 98 New Weather prediction (temperature) 4.1 O N THE ROLE AND LIMITATIONS OF TAB R E D We see our TabReD benchmark as an important addition to the landscape of tabular datasets. TabReD has the properties that are underrepresented in current benchmarks, including the time-based splits and the “feature-

## 原始摘要

Advances in machine learning research drive progress in real-world applications. To ensure this progress, it is important to understand the potential pitfalls on the way from a novel method's success on academic benchmarks to its practical deployment. In this work, we analyze existing tabular deep learning benchmarks and find two common characteristics of tabular data in typical industrial applications that are underrepresented in the datasets usually used for evaluation in the literature.First, in real-world deployment scenarios, distribution of data often changes over time. To account for this distribution drift, time-based train/test splits should be used in evaluation. However, existing academic tabular datasets often lack timestamp metadata to enable such evaluation.Second, a considerable portion of datasets in production settings stem from extensive data acquisition and feature engineering pipelines. This can have an impact on the absolute and relative number of predictive, uninformative, and correlated features compared to academic datasets.In this work, we aim to understand how recent research advances in tabular deep learning transfer to these underrepresented conditions.To this end, we introduce TabReD -- a collection of eight industry-grade tabular datasets. We reassess a large number of tabular ML models and techniques on TabReD. We demonstrate that evaluation on both time-based data splits and richer feature sets leads to different methods ranking, compared to evaluation on random splits and smaller number of features, which are common in academic benchmarks. Furthermore, simple MLP-like architectures and GBDT show the best results on the TabReD datasets, while other methods are less effective in the new setting.
