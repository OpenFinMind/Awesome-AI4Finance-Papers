# Prediction without Preclusion: Recourse Verification with Reachable Sets

ICLR 2024 · main · application

通用方法在金融任务、数据或明确案例上开展应用验证。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=SCQfYpdoGE
- 摘要来源：https://iclr.cc/virtual/2024/poster/18612
- 本地 PDF：[打开](../../pdfs/ICLR/2024/iclr-2024-SCQfYpdoGE__Prediction_without_Preclusion_Recourse_Verification_with_Reachable_Sets.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_review
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Lending & Credit Data / 借贷与信贷数据应用
- 技术方法标签：未明确标注
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Machine learning models are often used to decide who receives a loan, a job interview, or a public benefit. / As a result, they can assign predictions that are \emph{fixed} -- meaning that individuals who are denied loans and interviews are, in fact, *precluded from access* to credit and employment. / We conduct a comprehensive empirical study on the infeasibility of recourse on datasets from consumer finance.

## 原始摘要

Machine learning models are often used to decide who receives a loan, a job interview, or a public benefit. Models in such settings use features without considering their *actionability*. As a result, they can assign predictions that are \emph{fixed} -- meaning that individuals who are denied loans and interviews are, in fact, *precluded from access* to credit and employment. In this work, we introduce a procedure called *recourse verification* to test if a model assigns fixed predictions to its decision subjects. We propose a model-agnostic approach for verification with *reachable sets* -- i.e., the set of all points that a person can reach through their actions in feature space. We develop methods to construct reachable sets for discrete feature spaces, which can certify the responsiveness of *any model* by simply querying its predictions. We conduct a comprehensive empirical study on the infeasibility of recourse on datasets from consumer finance. Our results highlight how models can inadvertently preclude access by assigning fixed predictions and underscore the need to account for actionability in model development.
