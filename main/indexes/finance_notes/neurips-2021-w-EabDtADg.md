# Fair Sequential Selection Using Supervised Learning Models

NeurIPS 2021 · main · application

正文包含明确金融数据、金融任务或金融案例；金融应用可属于通用方法的一个实验。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=w-EabDtADg
- 摘要来源：https://neurips.cc/virtual/2021/poster/28457
- 本地 PDF：[打开](../../pdfs/NeurIPS/2021/neurips-2021-w-EabDtADg__Fair_Sequential_Selection_Using_Supervised_Learning_Models.pdf)；版本：publisher_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Credit Scoring & Default / 信用评分与违约；Financial Risk / 金融风险管理
- 技术方法标签：Fairness & Recourse / 公平性与算法追索
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

(16) Similar to optimization (13), if R = {ρ1 , ρ2 , . . . , ρn′ }, then solution to (16) can be found through the exhaustive search with time complexity O((n′ )2 ). 5 Numerical Example FICO credit score dataset [41].7 FICO credit scores have been used in the US to determine the creditworthiness of people. The dataset used in this experiment includes credit scores from four 7 The datasets used in this paper do not include any identifiable information. The codes are available here.

## 原始摘要

We consider a selection problem where sequentially arrived applicants apply for a limited number of positions/jobs. At each time step, a decision maker accepts or rejects the given applicant using a pre-trained supervised learning model until all the vacant positions are filled. In this paper, we discuss whether the fairness notions (e.g., equal opportunity, statistical parity, etc.) that are commonly used in classification problems are suitable for the sequential selection problems. In particular, we show that even with a pre-trained model that satisfies the common fairness notions, the selection outcomes may still be biased against certain demographic groups. This observation implies that the fairness notions used in classification problems are not suitable for a selection problem where the applicants compete for a limited number of positions.  We introduce a new fairness notion, ``Equal Selection (ES),'' suitable for sequential selection problems and propose a post-processing approach to satisfy the ES fairness notion. We also consider a setting where the applicants have privacy concerns, and the decision maker only has access to the noisy version of sensitive attributes. In this setting, we can show that the \textit{perfect} ES fairness can still be attained under certain conditions.
