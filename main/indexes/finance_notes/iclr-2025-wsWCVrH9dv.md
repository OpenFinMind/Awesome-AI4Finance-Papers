# Feature Responsiveness Scores: Model-Agnostic Explanations for Recourse

ICLR 2025 · main · core

以金融任务或金融数据为核心研究对象。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=wsWCVrH9dv
- 摘要来源：https://iclr.cc/virtual/2025/poster/27815
- 本地 PDF：[打开](../../pdfs/ICLR/2025/iclr-2025-wsWCVrH9dv__Feature_Responsiveness_Scores_Model_Agnostic_Explanations_for_Recourse.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_review
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Lending & Credit Data / 借贷与信贷数据应用
- 技术方法标签：未明确标注
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Our results show that standard practices in consumer finance can backfire by presenting consumers with *reasons without recourse*, and demonstrate how our approach improves consumer protection by highlighting responsive features and identifying fixed predictions.

## 原始摘要

Machine learning models routinely automate decisions in applications like lending and hiring. In such settings, consumer protection rules require companies that deploy models to explain predictions to decision subjects. These rules are motivated, in part, by the belief that explanations can promote *recourse* by revealing information that individuals can use to contest or improve their outcomes. In practice, many companies comply with these rules by providing individuals with a list of the most important features for their prediction, which they identify based on feature importance scores from feature attribution methods such as SHAP or LIME. In this work, we show how these practices can undermine consumers by highlighting features that would not lead to an improved outcome and by explaining predictions that cannot be changed. We propose to address these issues by highlighting features based on their *responsiveness score*—i.e., the probability that an individual can attain a target prediction by changing a specific feature. We develop efficient methods to compute responsiveness scores for any model and any dataset. We conduct an extensive empirical study on the responsiveness of explanations in lending. Our results show that standard practices in consumer finance can backfire by presenting consumers with *reasons without recourse*, and demonstrate how our approach improves consumer protection by highlighting responsive features and identifying fixed predictions.
