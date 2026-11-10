# Adaptive Test Case Discovery for LLM-Assisted Decision Making in High-Stakes Domains

NeurIPS 2026 · main · application

通用方法在金融任务、数据或明确案例上开展应用验证。 主题：Market Prediction / 股价、收益与波动率预测；Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=vWITPJYgBo
- 摘要来源：https://neurips.cc/virtual/2026/poster/148727
- PDF 状态：access_blocked
- 金融依据类型：title_abstract_review
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Stock Movement & Returns / 股价方向与收益预测；Credit Scoring & Default / 信用评分与违约；Lending & Credit Data / 借贷与信贷数据应用
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：language models；LLM；LLMs；optimization
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

We evaluate the method across several LLM-assisted decision-making tasks: bank loan approval, stock prediction from news articles, and disaster resource allocation from tweets and images.

## 原始摘要

Large language models (LLMs) are increasingly used for assistive decision-making in high-stakes domains, yet their outputs can be unreliable and difficult to audit. This necessitates pre-deployment testing, which can be used to identify scenarios where an LLM-assisted pipeline fails to produce satisfactory decisions. Existing testing strategies are often not sample-efficient and struggle to adapt to diverse testing objectives, application domains, and rapidly evolving models. We introduce a sample-efficient scenario design strategy for testing LLM-based decision-making pipelines. Our approach formulates testing as adaptive experimental design, using a flow-based surrogate model to sequentially acquire scenarios that balance optimization to discover challenging test cases with diverse exploration. We evaluate the method across several LLM-assisted decision-making tasks: bank loan approval, stock prediction from news articles, and disaster resource allocation from tweets and images. Our approach consistently discovers challenging scenarios that satisfy the testing objective across all tasks, providing high coverage over scenario space.
