# AlphaPROBE: Alpha Mining via principled retriveval and on-graph biased evolution

NeurIPS 2026 · main · core

以金融任务或金融数据为核心研究对象。 主题：Alpha Mining / 量化因子挖掘；Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=jnNAuSXHv2
- 摘要来源：https://neurips.cc/virtual/2026/poster/150234
- PDF 状态：access_blocked
- 金融依据类型：title_abstract_review
- 主方向：Alpha Mining / 量化因子挖掘
- 细分方向：Alpha Discovery / Alpha与因子发现；Financial Stochastic Processes / 金融随机过程
- 技术方法标签：Uncertainty & Robustness / 不确定性与鲁棒性；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Bayesian；optimization
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Extracting signals through alpha factor mining is a fundamental challenge in quantitative finance. / Extensive experiments on major Chinese and US stock market datasets against 8 competitive baselines demonstrate that AlphaPROBE significantly gains enhanced performance in predictive accuracy, return stability and training efficiency.

## 原始摘要

Extracting signals through alpha factor mining is a fundamental challenge in quantitative finance. Existing automated methods primarily follow two paradigms: Decoupled Factor Generation, which treats factor discovery as isolated events, and Iterative Factor Evolution, which focuses on local parent-child refinements. However, both paradigms lack a global structural view, often treating factor pools as unstructured collections or isolated single-lineage paths, which leads to redundant search and inefficient allocation of optimization effort. To address these limitations, we introduce AlphaPROBE, (**Alpha** Mining via **P**rincipled **R**etrieval and **O**n-graph **B**iased **E**volution), a framework that reframes alpha mining as the strategic navigation of a Directed Acyclic Graph (DAG). By modeling factors as nodes and evolutionary links as edges, AlphaPROBE treats the factor pool as a dynamic, interconnected ecosystem. The framework consists of two core components: a Bayesian Factor Retriever that identifies high-potential seeds by balancing exploitation and exploration through a posterior probability model, and a DAG-aware Factor Generator that leverages the full ancestral trace of factors to produce context-aware, non-redundant optimizations. Extensive experiments on major Chinese and US stock market datasets against 8 competitive baselines demonstrate that AlphaPROBE significantly gains enhanced performance in predictive accuracy, return stability and training efficiency. Our results confirm that leveraging global evolutionary topology is essential for efficient and robust automated alpha discovery. We have open-sourced our implementation at https://anonymous.4open.science/r/AlphaPROBE-A103.
