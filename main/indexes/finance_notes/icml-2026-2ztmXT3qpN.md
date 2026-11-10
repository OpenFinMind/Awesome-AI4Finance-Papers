# ECSEL: Explainable Classification via Signomial Equation Learning

ICML 2026 · main · application

通用方法在金融任务、数据或明确案例上开展应用验证。 主题：Fraud & AML / 欺诈检测与反洗钱。

- 官方论文页：https://openreview.net/forum?id=2ztmXT3qpN
- 摘要来源：https://icml.cc/virtual/2026/poster/66518
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-2ztmXT3qpN__ECSEL_Explainable_Classification_via_Signomial_Equation_Learning.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_review
- 主方向：Fraud & AML / 欺诈检测与反洗钱
- 细分方向：Scams & Financial Misinformation / 诈骗与金融虚假信息
- 技术方法标签：未明确标注
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Experiments on benchmark datasets and two real-world case studies i.e., e-commerce and fraud detection, demonstrate that the learned equations expose dataset biases, support counterfactual reasoning, and yield actionable insights.

## 原始摘要

We introduce ECSEL, an explainable classification method that learns formal expressions in the form of signomial equations, motivated by the observation that many symbolic regression benchmarks admit compact signomial structure. ECSEL directly constructs a structural, closed-form expression that serves as both a classifier and an explanation. On standard symbolic regression benchmarks, our method recovers a larger fraction of target equations than competing state-of-the-art approaches while requiring substantially less computation. Leveraging this efficiency, ECSEL achieves classification accuracy competitive with established machine learning models without sacrificing interpretability. Further, we show that ECSEL satisfies some desirable properties regarding global feature behaviour, decision-boundary analysis, and local feature attributions. Experiments on benchmark datasets and two real-world case studies i.e., e-commerce and fraud detection, demonstrate that the learned equations expose dataset biases, support counterfactual reasoning, and yield actionable insights.
