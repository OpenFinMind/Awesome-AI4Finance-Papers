# Well-tuned Simple Nets Excel on Tabular Datasets

NeurIPS 2021 · main · application

实验使用汇率、宏观金融、信用评估或财务文档等金融相关基准。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=d3k38LTDCyO
- 摘要来源：https://neurips.cc/virtual/2021/poster/28356
- 本地 PDF：[打开](../../pdfs/NeurIPS/2021/neurips-2021-d3k38LTDCyO__Well_tuned_Simple_Nets_Excel_on_Tabular_Datasets.pdf)；版本：publisher_version
- 金融依据类型：fulltext_financial_benchmark
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Credit Scoring & Default / 信用评分与违约
- 技术方法标签：Tabular Learning / 表格学习；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：optimization
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

37.991 38.704 48.779 46.850 43.562 N/A 48.934 61.461 mfeat. 2000 / 217 97.750 98.000 98.000 97.500 97.250 97.250 98.000 98.000 credit-g 1000 / 21 69.405 68.095 68.929 71.191 61.190 73.095 69.643 74.643 vehicle 846 / 19 83.766 82.603 74.973 80.165 79.654 75.541 83.793 82.576 kc1 2109 / 22 70.274 72.980 66.846 63.353 52.517 55.803 67.270 74.381 adult 48842 / 15 76.893 78.520 79.824 79.830 77

## 原始摘要

Tabular datasets are the last "unconquered castle" for deep learning, with traditional ML methods like Gradient-Boosted Decision Trees still performing strongly even against recent specialized neural architectures. In this paper, we hypothesize that the key to boosting the performance of neural networks lies in rethinking the joint and simultaneous application of a large set of modern regularization techniques. As a result, we propose regularizing plain Multilayer Perceptron (MLP) networks by searching for the optimal combination/cocktail of 13 regularization techniques for each dataset using a joint optimization over the decision on which regularizers to apply and their subsidiary hyperparameters. We empirically assess the impact of these regularization cocktails for MLPs in a large-scale empirical study comprising 40 tabular datasets and demonstrate that (i) well-regularized plain MLPs significantly outperform recent state-of-the-art specialized neural network architectures, and (ii) they even outperform strong traditional ML methods, such as XGBoost.
