# Algorithmic Recourse for Long-Term Improvement

ICML 2025 · main · application

通用方法在金融任务、数据或明确案例上开展应用验证。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=gmLD0DHaoZ
- 摘要来源：https://icml.cc/virtual/2025/poster/44455
- 本地 PDF：[打开](../../pdfs/ICML/2025/icml-2025-gmLD0DHaoZ__Algorithmic_Recourse_for_Long_Term_Improvement.pdf)；版本：publisher_version
- 金融依据类型：title_abstract_review
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Credit Scoring & Default / 信用评分与违约；Lending & Credit Data / 借贷与信贷数据应用
- 技术方法标签：Reinforcement Learning / 强化学习；Fairness & Recourse / 公平性与算法追索；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Bayesian；optimization
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Algorithmic recourse aims to provide a recourse action for altering an unfavorable prediction given by a model into a favorable one (e.g., loan approval). / In practice, it is also desirable to ensure that an action makes the real-world outcome better (e.g., loan repayment).

## 原始摘要

Algorithmic recourse aims to provide a recourse action for altering an unfavorable prediction given by a model into a favorable one (e.g., loan approval). In practice, it is also desirable to ensure that an action makes the real-world outcome better (e.g., loan repayment). We call this requirement *improvement*. Unfortunately, existing methods cannot ensure improvement unless we know the true oracle.  To address this issue, we propose a framework for suggesting improvement-oriented actions from a long-term perspective. Specifically, we introduce a new online learning task of assigning actions to a given sequence of instances. We assume that we can observe delayed feedback on whether the past suggested action achieved improvement. Using the feedback, we estimate an action that can achieve improvement for each instance. To solve this task, we propose two approaches based on contextual linear bandit and contextual Bayesian optimization. Experimental results demonstrated that our approaches could assign improvement-oriented actions to more instances than the existing methods.
