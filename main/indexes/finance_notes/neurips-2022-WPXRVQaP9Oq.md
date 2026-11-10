# On the Safety of Interpretable Machine Learning: A Maximum Deviation Approach

NeurIPS 2022 · main · application

包含明确的金融任务、金融领域数据或金融案例验证。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=WPXRVQaP9Oq
- 摘要来源：https://neurips.cc/virtual/2022/poster/53918
- 本地 PDF：[打开](../../pdfs/NeurIPS/2022/neurips-2022-WPXRVQaP9Oq__On_the_Safety_of_Interpretable_Machine_Learning_A_Maximum_Deviation_Approach.pdf)；版本：publisher_version
- 金融依据类型：title_abstract_financial_task_or_data
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Lending & Credit Data / 借贷与信贷数据应用
- 技术方法标签：Reinforcement Learning / 强化学习；Tabular Learning / 表格学习；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：optimization
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

We present case studies, including one on mortgage approval, to illustrate our methods and the insights about models that may be obtained from deviation maximization.

## 原始摘要

Interpretable and explainable machine learning has seen a recent surge of interest. We focus on safety as a key motivation behind the surge and make the relationship between interpretability and safety more quantitative. Toward assessing safety, we introduce the concept of *maximum deviation* via an optimization problem to find the largest deviation of a supervised learning model from a reference model regarded as safe. We then show how interpretability facilitates this safety assessment. For models including decision trees, generalized linear and additive models, the maximum deviation can be computed exactly and efficiently. For tree ensembles, which are not regarded as interpretable, discrete optimization techniques can still provide informative bounds. For a broader class of piecewise Lipschitz functions, we leverage the multi-armed bandit literature to show that interpretability produces tighter (regret) bounds on the maximum deviation. We present case studies, including one on mortgage approval, to illustrate our methods and the insights about models that may be obtained from deviation maximization.
