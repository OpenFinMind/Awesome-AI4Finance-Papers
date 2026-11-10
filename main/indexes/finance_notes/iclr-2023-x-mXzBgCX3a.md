# FairGBM: Gradient Boosting with Fairness Constraints

ICLR 2023 · main · application

包含明确的金融任务、金融领域数据或金融案例验证。 主题：Other Financial Applications / 其他金融应用。

- 官方论文页：https://openreview.net/forum?id=x-mXzBgCX3a
- 摘要来源：https://iclr.cc/virtual/2023/poster/10702
- 本地 PDF：[打开](../../pdfs/ICLR/2023/iclr-2023-x-mXzBgCX3a__FairGBM_Gradient_Boosting_with_Fairness_Constraints.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_financial_task_or_data
- 主方向：Other Financial Applications / 其他金融应用
- 细分方向：尚未细分
- 技术方法标签：Fairness & Recourse / 公平性与算法追索；Tabular Learning / 表格学习；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：optimization
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Tabular data is prevalent in many high-stakes domains, such as financial services or public policy.

## 原始摘要

Tabular data is prevalent in many high-stakes domains, such as financial services or public policy. Gradient Boosted Decision Trees (GBDT) are popular in these settings due to their scalability, performance, and low training cost. While fairness in these domains is a foremost concern, existing in-processing Fair ML methods are either incompatible with GBDT, or incur in significant performance losses while taking considerably longer to train. We present FairGBM, a dual ascent learning framework for training GBDT under fairness constraints, with little to no impact on predictive performance when compared to unconstrained GBDT. Since observational fairness metrics are non-differentiable, we propose smooth convex error rate proxies for common fairness criteria, enabling gradient-based optimization using a ``proxy-Lagrangian'' formulation. Our implementation shows an order of magnitude speedup in training time relative to related work, a pivotal aspect to foster the widespread adoption of FairGBM by real-world practitioners.
