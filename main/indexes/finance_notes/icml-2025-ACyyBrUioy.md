# Near-Optimal Decision Trees in a SPLIT Second

ICML 2025 · main · application

正文包含金融领域的数据、模型、任务或独立金融评测。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=ACyyBrUioy
- 摘要来源：https://icml.cc/virtual/2025/oral/47254
- 本地 PDF：[打开](../../pdfs/ICML/2025/icml-2025-ACyyBrUioy__Near_Optimal_Decision_Trees_in_a_SPLIT_Second.pdf)；版本：publisher_version
- 金融依据类型：fulltext_financial_data_model_or_task
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Credit Scoring & Default / 信用评分与违约
- 技术方法标签：Tabular Learning / 表格学习；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：optimization
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

930 takes merely a second in most cases. This is the regime Netherlands 4255 216 0.932 most relevant to our algorithms. HELOC 5564 337 0.979 • When the optimal objective is high and the tree is super- HIV 9273 388 0.959 sparse (right side of each plot), SPLIT and Lickety- Bike 14330 194 0.999 SPLIT have small overhead costs and can be slower, Table 1. Table summarizing the advantages of RESPLIT. The because we need to train a greedy tree for each sub- first 2 columns show the time taken to compute all bootstrapped problem encountered at the loo

## 原始摘要

Decision tree optimization is fundamental to interpretable machine learning. The most popular approach is to greedily search for the best feature at every decision point, which is fast but provably suboptimal. Recent approaches find the global optimum using branch and bound with dynamic programming, showing substantial improvements in accuracy and sparsity at great cost to scalability. An ideal solution would have the accuracy of an optimal method and the scalability of a greedy method. We introduce a family of algorithms called SPLIT (SParse Lookahead for Interpretable Trees) that moves us significantly forward in achieving this ideal balance. We demonstrate that not all sub-problems need to be solved to optimality to find high quality trees; greediness suffices near the leaves. Since each depth adds an exponential number of possible trees, this change makes our algorithms orders of magnitude faster than existing optimal methods, with negligible loss in performance. We extend this algorithm to allow scalable computation of sets of near-optimal trees (i.e., the Rashomon set).
