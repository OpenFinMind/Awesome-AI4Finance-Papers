# Washing The Unwashable : On The (Im)possibility of Fairwashing Detection

NeurIPS 2022 · main · application

正文包含明确金融数据、金融任务或金融案例；金融应用可属于通用方法的一个实验。 主题：Banking & Customer Service / 银行业务与客户服务。

- 官方论文页：https://openreview.net/forum?id=3vmKQUctNy
- 摘要来源：https://neurips.cc/virtual/2022/poster/54741
- 本地 PDF：[打开](../../pdfs/NeurIPS/2022/neurips-2022-3vmKQUctNy__Washing_The_Unwashable_On_The_Im_possibility_of_Fairwashing_Detection.pdf)；版本：publisher_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Banking & Customer Service / 银行业务与客户服务
- 细分方向：Bank Marketing & Churn / 银行营销与客户流失
- 技术方法标签：Fairness & Recourse / 公平性与算法追索；Uncertainty & Robustness / 不确定性与鲁棒性；Tabular Learning / 表格学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/cleverhans-lab/FRAUD-Detect.

## 纳入依据

on trees as interpretable models with respect to black-box Deep Neural Networks, AdaBoost [24], Gradient Boosted Decision Trees [17] and Random Forests [13] on three benchmark datasets: COMPAS [5], Adult Income [22] and Bank Marketing [34]. We evaluate the strength of our detector in the presence of an informed adversary representing an informed dishonest entity with knowledge of FRAUD-Detect that seeks to fairwash and bypass detection by constraining the divergence over subpopulation-wise confusion matrices. Our empirical experiments quantify the capacity of this informed adve

## 原始摘要

The use of black-box models (e.g., deep neural networks) in high-stakes decision-making systems, whose internal logic is complex, raises the need for providing explanations about their decisions. Model explanation techniques mitigate this problem by generating an interpretable and high-fidelity surrogate model (e.g., a logistic regressor or decision tree) to explain the logic of black-box models. In this work, we investigate the issue of fairwashing, in which model explanation techniques are manipulated to rationalize decisions taken by an unfair black-box model using deceptive surrogate models. More precisely, we theoretically characterize and analyze fairwashing, proving that this phenomenon is difficult to avoid due to an irreducible factor---the unfairness of the black-box model. Based on the theory developed, we propose a novel technique, called FRAUD-Detect (FaiRness AUDit Detection), to detect fairwashed models by measuring a divergence over subpopulation-wise fidelity measures of the interpretable model. We empirically demonstrate that this divergence is significantly larger in purposefully fairwashed interpretable models than in honest ones. Furthermore, we show that our detector is robust to an informed adversary trying to bypass our detector. The code implementing FRAUD-Detect is available at https://github.com/cleverhans-lab/FRAUD-Detect.
