# Higher Order Kernel Mean Embeddings to Capture Filtrations of Stochastic Processes

NeurIPS 2021 · main · core

以金融任务或金融数据为核心研究对象。 主题：Derivatives & Hedging / 衍生品定价与对冲。

- 官方论文页：https://openreview.net/forum?id=CtugaUzfYw
- 摘要来源：https://neurips.cc/virtual/2021/poster/27239
- 本地 PDF：[打开](../../pdfs/NeurIPS/2021/neurips-2021-CtugaUzfYw__Higher_Order_Kernel_Mean_Embeddings_to_Capture_Filtrations_of_Stochastic_Processes.pdf)；版本：publisher_version
- 金融依据类型：title_abstract_review
- 主方向：Derivatives & Hedging / 衍生品定价与对冲
- 细分方向：Option Pricing & PDEs / 期权定价与PDE
- 技术方法标签：Causal Learning / 因果学习；Uncertainty & Robustness / 不确定性与鲁棒性；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：causal
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

In addition, leveraging our higher order MMDs we construct a family of universal kernels on stochastic processes that allows to solve real-world calibration and optimal stopping problems in quantitative finance (such as the pricing of American options) via classical kernel-based regression methods.

## 原始摘要

Stochastic processes are random variables with values in some space of paths. However, reducing a stochastic process to a path-valued random variable ignores its filtration, i.e. the flow of information carried by the process through time. By conditioning the process on its filtration, we introduce a family of higher order kernel mean embeddings (KMEs) that generalizes the notion of KME to capture additional information related to the filtration. We derive empirical estimators for the associated higher order maximum mean discrepancies (MMDs) and prove consistency. We then construct a filtration-sensitive kernel two-sample test able to capture information that gets missed by the standard MMD test. In addition, leveraging our higher order MMDs we construct a family of universal kernels on stochastic processes that allows to solve real-world calibration and optimal stopping problems in quantitative finance (such as the pricing of American options) via classical kernel-based regression methods. Finally, adapting existing tests for conditional independence to the case of stochastic processes, we design a causal-discovery algorithm to recover the causal graph of structural dependencies among interacting bodies solely from observations of their multidimensional trajectories.
