# Unprocessing Seven Years of Algorithmic Fairness

ICLR 2024 · main · application

正文包含金融领域的数据、模型、任务或独立金融评测。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=jr03SfWsBS
- 摘要来源：https://iclr.cc/virtual/2024/poster/18005
- 本地 PDF：[打开](../../pdfs/ICLR/2024/iclr-2024-jr03SfWsBS__Unprocessing_Seven_Years_of_Algorithmic_Fairness.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_model_or_task
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Credit Scoring & Default / 信用评分与违约
- 技术方法标签：Fairness & Recourse / 公平性与算法追索；Tabular Learning / 表格学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

eedings.neurips.cc/paper_files/paper/2014/ file/5ca3e9b122f61f8f06494c97b1afccf3-Paper.pdf. 11 Published as a conference paper at ICLR 2024 Ulrike Grömping. South german credit data: Correcting a widely used data set. In Reports in Mathematics, Physics and Chemistry, 2019. Moritz Hardt, Eric Price, and Nathan Srebro. Equality of opportunity in supervised learning. In D. Lee, M. Sugiyama, U. Luxburg, I. Guyon, and R. Garnett (eds.), Advances in Neural Information Processing Systems, volume 29. Curran Associates, Inc.,

## 原始摘要

Seven years ago, researchers proposed a postprocessing method to equalize the error rates of a model across different demographic groups. The work launched hundreds of papers purporting to improve over the postprocessing baseline. We empirically evaluate these claims through thousands of model evaluations on several tabular datasets. We find that the fairness-accuracy Pareto frontier achieved by postprocessing contains all other methods we were feasibly able to evaluate. In doing so, we address two common methodological errors that have confounded previous observations. One relates to the comparison of methods with different unconstrained base models. The other concerns methods achieving different levels of constraint relaxation. At the heart of our study is a simple idea we call unprocessing that roughly corresponds to the inverse of postprocessing. Unprocessing allows for a direct comparison of methods using different underlying models and levels of relaxation.
