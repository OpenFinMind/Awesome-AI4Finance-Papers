# Learning Classifiers That Induce Markets

ICML 2025 · main · application

研究金融风险度量、金融决策或信贷场景的建模与理论方法。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=GA7JfZyJMw
- 摘要来源：https://icml.cc/virtual/2025/poster/45851
- 本地 PDF：[打开](../../pdfs/ICML/2025/icml-2025-GA7JfZyJMw__Learning_Classifiers_That_Induce_Markets.pdf)；版本：publisher_version
- 金融依据类型：financial_method_or_formal_case
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Lending & Credit Data / 借贷与信贷数据应用
- 技术方法标签：Fairness & Recourse / 公平性与算法追索
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

When learning is used to inform decisions about humans, such as for loans, hiring, or admissions, this can incentivize users to strategically modify their features, at a cost, to obtain positive predictions.

## 原始摘要

When learning is used to inform decisions about humans, such as for loans, hiring, or admissions, this can incentivize users to strategically modify their features, at a cost, to obtain positive predictions. The common assumption is that the function governing costs is exogenous, fixed, and predetermined. We challenge this assumption, and assert that costs emerge as a *result* of deploying a classifier. Our idea is simple: when users seek positive predictions, this creates demand for important features; and if features are available for purchase, then a market will form, and competition will give rise to prices. We extend the strategic classification framework to support this notion, and study learning in a setting where a classifier can induce a market for features. We present an analysis of the learning task, devise an algorithm for computing market prices, propose a differentiable learning framework, and conduct experiments to explore our novel setting and approach.
