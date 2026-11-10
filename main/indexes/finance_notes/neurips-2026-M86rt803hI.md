# Cost Efficient Fairness Audit Under Partial Feedback

NeurIPS 2026 · main · application

研究金融风险度量、金融决策或信贷场景的建模与理论方法。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=M86rt803hI
- 摘要来源：https://neurips.cc/Downloads/2026
- 本地 PDF：[打开](../../pdfs/NeurIPS/2026/neurips-2026-M86rt803hI__Cost_Efficient_Fairness_Audit_Under_Partial_Feedback.pdf)；版本：arxiv_author_version
- 金融依据类型：financial_method_or_formal_case
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Lending & Credit Data / 借贷与信贷数据应用
- 技术方法标签：Fairness & Recourse / 公平性与算法追索
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

We study the problem of auditing the fairness of a given classifier under partial feedback, where true labels are available only for positively classified individuals (e.g., loan repayment outcomes are observed only for approved applicants). / We introduce a novel cost model for acquiring additional labeled data, designed to more accurately reflect real-world costs such as credit assessment, loan processing, and potential defaults.

## 原始摘要

We study the problem of auditing the fairness of a given classifier under partial feedback, where true labels are available only for positively classified individuals (e.g., loan repayment outcomes are observed only for approved applicants). We introduce a novel cost model for acquiring additional labeled data, designed to more accurately reflect real-world costs such as credit assessment, loan processing, and potential defaults. Our goal is to find optimal fairness audit algorithms that are more cost-effective than random exploration and natural baselines.  In our work, we consider two audit settings: a black-box model with no assumptions on the data distribution, and a mixture model, where features and true labels follow a mixture of exponential family distributions. In the black-box setting, we propose a near-optimal auditing algorithm and show that a natural baseline can be strictly suboptimal. In the mixture model case, we design a novel algorithm that achieves significantly lower audit cost than the black-box case under mild assumptions. Our approach develops novel connections between partial feedback and learning from truncated samples. We also extend known results on maximum-a-posteriori oracles for spherical Gaussian mixtures to handle exponential family mixtures, which may be of independent interest. Moreover, our algorithms apply to popular fairness metrics including demographic parity, equal opportunity, and equalized odds. Empirically, we demonstrate strong performance of our algorithms on real-world fair classification datasets like Adult Income and Law School, consistently outperforming natural baselines by around 50% in terms of audit cost.
