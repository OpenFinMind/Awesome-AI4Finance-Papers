# Online Portfolio Selection with ML Predictions

NeurIPS 2025 · main · core

以金融任务或金融数据为核心研究对象。 主题：Portfolio & Investment / 投资组合与投资管理；Market Prediction / 股价、收益与波动率预测。

- 官方论文页：https://openreview.net/forum?id=zOFxp98km2
- 摘要来源：https://neurips.cc/virtual/2025/poster/115052
- PDF 状态：access_blocked
- 金融依据类型：title_abstract_review
- 主方向：Portfolio & Investment / 投资组合与投资管理
- 细分方向：Portfolio Selection & Optimization / 组合选择与优化；Stock Movement & Returns / 股价方向与收益预测
- 技术方法标签：Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Online portfolio selection seeks to determine a sequence of allocations to maximize capital growth. / Classical universal strategies asymptotically match the best constant-rebalanced portfolio but ignore potential forecasts, whereas heuristic methods often collapse when belief fails. / We formalize this tension in a learning-augmented setting in which an investor observes (possibly erroneous) predictions prior to each decision moment, and we introduce the Rebalanced Arithmetic Mean portfolio with predictions (RAM). / RAM advantages over universal-portfolio variants equipped with side information across various regimes.

## 原始摘要

Online portfolio selection seeks to determine a sequence of allocations to maximize capital growth. Classical universal strategies asymptotically match the best constant-rebalanced portfolio but ignore potential forecasts, whereas heuristic methods often collapse when belief fails. We formalize this tension in a learning-augmented setting in which an investor observes (possibly erroneous) predictions prior to each decision moment, and we introduce the Rebalanced Arithmetic Mean portfolio with predictions (RAM). Under arbitrary return sequences, we prove that RAM captures at least a constant fraction of the hindsight-optimal wealth when forecasts are perfect while still exceeding the geometric mean of the sequence even when the predictions are adversarial. Comprehensive experiments on large-scale equity data strengthen our theory, spanning both synthetic prediction streams and production-grade machine-learning models. RAM advantages over universal-portfolio variants equipped with side information across various regimes. These results demonstrate that modest predictive power can be reliably converted into tangible gains without sacrificing worst-case guarantees.
