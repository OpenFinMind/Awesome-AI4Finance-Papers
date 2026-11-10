# Fair and Optimal Decision Trees: A Dynamic Programming Approach

NeurIPS 2022 · main · application

正文包含明确金融数据、金融任务或金融案例；金融应用可属于通用方法的一个实验。 主题：Banking & Customer Service / 银行业务与客户服务。

- 官方论文页：https://openreview.net/forum?id=LCIZmSw1DuE
- 摘要来源：https://neurips.cc/virtual/2022/poster/55259
- 本地 PDF：[打开](../../pdfs/NeurIPS/2022/neurips-2022-LCIZmSw1DuE__Fair_and_Optimal_Decision_Trees_A_Dynamic_Programming_Approach.pdf)；版本：publisher_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Banking & Customer Service / 银行业务与客户服务
- 细分方向：Bank Marketing & Churn / 银行营销与客户流失
- 技术方法标签：Fairness & Recourse / 公平性与算法追索；Tabular Learning / 表格学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

DPF Dataset a |D| |F| d=2 d=2 d=3 d=4 Adult Gender 45222 17 > 1h <1 <1 1012 Bank Marketing Married 45211 46 > 1h <1 2 > 1h Communities & Crime Race 1994 97 > 1h <1 4 1261 COMPAS recid. Race 6172 9 > 1h <1 <1 9 COMPAS viol. recid. Race 4020 9

## 原始摘要

Interpretable and fair machine learning models are required for many applications, such as credit assessment and in criminal justice. Decision trees offer this interpretability, especially when they are small. Optimal decision trees are of particular interest because they offer the best performance possible for a given size. However, state-of-the-art algorithms for fair and optimal decision trees have scalability issues, often requiring several hours to find such trees even for small datasets. Previous research has shown that dynamic programming (DP) performs well for optimizing decision trees because it can exploit the tree structure. However, adding a global fairness constraint to a DP approach is not straightforward, because the global constraint violates the condition that subproblems should be independent. We show how such a constraint can be incorporated by introducing upper and lower bounds on final fairness values for partial solutions of subproblems, which enables early comparison and pruning. Our results show that our model can find fair and optimal trees several orders of magnitude faster than previous methods, and now also for larger datasets that were previously beyond reach. Moreover, we show that with this substantial improvement our method can find the full Pareto front in the trade-off between accuracy and fairness.
