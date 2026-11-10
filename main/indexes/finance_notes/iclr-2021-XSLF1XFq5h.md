# Getting a CLUE: A  Method for Explaining Uncertainty Estimates

ICLR 2021 · main · application

正文包含金融领域的数据、模型、任务或独立金融评测。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=XSLF1XFq5h
- 摘要来源：https://iclr.cc/virtual/2021/poster/3505
- 本地 PDF：[打开](../../pdfs/ICLR/2021/iclr-2021-XSLF1XFq5h__Getting_a_CLUE_A_Method_for_Explaining_Uncertainty_Estimates.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_model_or_task
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Credit Scoring & Default / 信用评分与违约；Lending & Credit Data / 借贷与信贷数据应用
- 技术方法标签：Fairness & Recourse / 公平性与算法追索；Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Bayesian
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

mpas-analysis/blob/master/ compas-scores-two-years.csv). The red wine quality prediction dataset can be obtained from and is described in detail at (https: //archive.ics.uci.edu/ml/datasets/wine+quality). The default of credit card clients dataset, which we refer to as “Credit” in this work, can be ob- tained from and is described in detail at (https://archive.ics.uci.edu/ml/datasets/ default+of+credit+card+clients). Note that this dataset is different from the also com- monly used German credit dataset. The MNIST handwritten digit image dataset can be obtained from (http://

## 原始摘要

Both uncertainty estimation and interpretability are important factors for trustworthy machine learning systems. However, there is little work at the intersection of these two areas. We address this gap by proposing a novel method for interpreting uncertainty estimates from differentiable probabilistic models, like Bayesian Neural Networks (BNNs). Our method, Counterfactual Latent Uncertainty Explanations (CLUE), indicates how to change an input, while keeping it on the data manifold, such that a BNN becomes more confident about the input's prediction. We validate CLUE through 1) a novel framework for evaluating counterfactual explanations of uncertainty, 2) a series of ablation experiments, and 3) a user study. Our experiments show that CLUE outperforms baselines and enables practitioners to better understand which input patterns are responsible for predictive uncertainty.
