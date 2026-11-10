# Performative Prediction with Selective Labels

NeurIPS 2026 · main · application

包含明确的金融任务、金融领域数据或金融案例验证。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=4KuDZUSGv3
- 摘要来源：https://neurips.cc/Downloads/2026
- 本地 PDF：[打开](../../pdfs/NeurIPS/2026/neurips-2026-4KuDZUSGv3__Performative_Prediction_with_Selective_Labels.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_financial_task_or_data
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Lending & Credit Data / 借贷与信贷数据应用
- 技术方法标签：Fairness & Recourse / 公平性与算法追索；Uncertainty & Robustness / 不确定性与鲁棒性；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：optimization
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Experiments in a lending application with fairness regularization show that our robust optimization approach closely matches the performance of RRM with complete label access.

## 原始摘要

Many social applications of machine learning exhibit performative effects: population behavior changes in response to deployed models. Performative prediction studies this interaction through a distribution map that relates each model to the population distribution it induces. One of the main results in this framework showed that repeated risk minimization (RRM), which updates models by retraining on the most recent data, can converge to a stable model that minimizes risk on its own induced distribution. However, existing analyses typically assume access to the complete distributions of features and labels after model deployment, ignoring the possibility of _selective labels_: observing labels only for the accepted subset of the population. In this work, we formalize performative prediction with selective labels and show that retraining only on observed data can misguide the retraining procedure and undermine the guarantees of convergence to a stable solution. We then propose a worst-case objective based on knowledge of a confidence interval on the probability of a positive label. Applying RRM to this objective permits us to remain within a bounded distance to the true stable point. Under a sensitivity assumption on the conditional label distribution, we further show how previously accepted data can tighten these confidence intervals over time. Experiments in a lending application with fairness regularization show that our robust optimization approach closely matches the performance of RRM with complete label access.
