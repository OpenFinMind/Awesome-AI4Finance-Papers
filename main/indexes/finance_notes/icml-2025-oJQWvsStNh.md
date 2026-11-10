# Stable Fair Graph Representation Learning with Lipschitz Constraint

ICML 2025 · main · application

正文包含金融数据、金融任务或金融领域评测。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=oJQWvsStNh
- 摘要来源：https://icml.cc/virtual/2025/poster/44069
- 本地 PDF：[打开](../../pdfs/ICML/2025/icml-2025-oJQWvsStNh__Stable_Fair_Graph_Representation_Learning_with_Lipschitz_Constraint.pdf)；版本：publisher_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Credit Scoring & Default / 信用评分与违约
- 技术方法标签：Graph Learning / 图学习；Fairness & Recourse / 公平性与算法追索；Uncertainty & Robustness / 不确定性与鲁棒性；Optimization & Numerical Methods / 优化与数值方法；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Graph Neural Network
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/sh-qiangchen/SFG.

## 纳入依据

(a) German (b) Bail (c) Credit Figure 4. Training accuracy curve on German, Bail and Credit datasets. The shaded area represents the rolling standard deviation with a window size of 5, which can be used to measure the stability between epochs. Table 1. Comparison results of SFG with baseline fairness methods. In each row, the best result is indicated in bold, while the runner-up result is marked with an underline.

## 原始摘要

Group fairness based on adversarial training has gained significant attention on graph data, which was implemented by masking sensitive attributes to generate fair feature views. However, existing models suffer from training instability due to uncertainty of the generated masks and the trade-off between fairness and utility. In this work, we propose a stable fair Graph Neural Network (SFG) to maintain training stability while preserving accuracy and fairness performance. Specifically, we first theoretically derive a tight upper Lipschitz bound to control the stability of existing adversarial-based models and employ a stochastic projected subgradient algorithm to constrain the bound, which operates in a block-coordinate manner. Additionally, we construct the uncertainty set to train the model, which can prevent unstable training by dropping some overfitting nodes caused by chasing fairness. Extensive experiments conducted on three real-world datasets demonstrate that SFG is stable and outperforms other state-of-the-art adversarial-based methods in terms of both fairness and utility performance. Codes are available at https://github.com/sh-qiangchen/SFG.
