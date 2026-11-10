# Learning Models for Actionable Recourse

NeurIPS 2021 · main · application

研究金融风险度量、金融决策或信贷场景的建模与理论方法。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=JZK9uP4Fev
- 摘要来源：https://neurips.cc/virtual/2021/poster/26899
- 本地 PDF：[打开](../../pdfs/NeurIPS/2021/neurips-2021-JZK9uP4Fev__Learning_Models_for_Actionable_Recourse.pdf)；版本：publisher_version
- 金融依据类型：financial_method_or_formal_case
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Lending & Credit Data / 借贷与信贷数据应用
- 技术方法标签：Fairness & Recourse / 公平性与算法追索；Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

As machine learning models are increasingly deployed in high-stakes domains such as legal and financial decision-making, there has been growing interest in post-hoc methods for generating counterfactual explanations. / Such explanations provide individuals adversely impacted by predicted outcomes (e.g., an applicant denied a loan) with recourse---i.e., a description of how they can change their features to obtain a positive outcome.

## 原始摘要

As machine learning models are increasingly deployed in high-stakes domains such as legal and financial decision-making, there has been growing interest in post-hoc methods for generating counterfactual explanations. Such explanations provide individuals adversely impacted by predicted outcomes (e.g., an applicant denied a loan) with recourse---i.e., a description of how they can change their features to obtain a positive outcome. We propose a novel algorithm that leverages adversarial training and PAC confidence sets to learn models that theoretically guarantee recourse to affected individuals with high probability without sacrificing accuracy. We demonstrate the efficacy of our approach via extensive experiments on real data.
