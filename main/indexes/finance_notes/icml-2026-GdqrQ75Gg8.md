# Desirable Effort Fairness and Optimality Trade-offs in Strategic Learning

ICML 2026 · main · application

正文包含金融数据、金融训练数据、金融任务评测或具体金融场景案例。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=GdqrQ75Gg8
- 摘要来源：https://icml.cc/virtual/2026/poster/65118
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-GdqrQ75Gg8__Desirable_Effort_Fairness_and_Optimality_Trade_offs_in_Strategic_Learning.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Credit Scoring & Default / 信用评分与违约
- 技术方法标签：Causal Learning / 因果学习；Fairness & Recourse / 公平性与算法追索；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：causal；optimization
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

, we additionally compare realized losses with the theoretical bounds in Table 1. Setup. We use the TAIWAN credit-default dataset, which contains financial and demographic in- formation about clients and is commonly used to predict whether a client is likely to default on repayment. We study three population partitions based on age, education, and marital status. Each partition induces a corresponding pair of projection matrices, Π1 , Π2 . Similarly to the previ- ous experiment, we compute the β-fair equilibrium for various cost matrices, A1 , A2 and desirable feature sets ΠD . A full description of the setup can be found in Section A.5. Results. Figure 4 compares the realized losses with the theoretical upper bounds from Table 1. The main

## 原始摘要

Strategic classification examines how decision rules interact with agents who strategically adapt their features. Most existing models focus on maximizing predictive performance, assuming agents best respond to the learned classifier. However, real decision-making systems are rarely optimized solely for accuracy: ethical, economic, and institutional considerations often make some feature changes more desirable than others. At the same time, principals may wish to incentivize these changes fairly across heterogeneous agents. While prior work has studied causal structure between features, notions of desirability, and information disparities in isolation, this work initiates a unified treatment of these components within a single framework. We frame the problem as a constrained optimization problem that captures the trade-offs between optimality, desirability, and fairness. We provide theoretical guarantees on the principal's optimality loss constrained to a particular desirability fairness tolerance for multiple broad classes of fairness measures. Finally, through experiments on real datasets, we show the explicit tradeoff between maximizing accuracy and fairness in desirability effort.
