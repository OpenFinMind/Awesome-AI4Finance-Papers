# Differentiable Optimization Layers for Guaranteed Fairness in Deep Learning

ICML 2026 · main · application

正文包含金融数据、金融训练数据、金融任务评测或具体金融场景案例。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=9SLQACsSbw
- 摘要来源：https://icml.cc/virtual/2026/poster/65851
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-9SLQACsSbw__Differentiable_Optimization_Layers_for_Guaranteed_Fairness_in_Deep_Learning.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Credit Scoring & Default / 信用评分与违约；Lending & Credit Data / 借贷与信贷数据应用
- 技术方法标签：Fairness & Recourse / 公平性与算法追索；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：optimization
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/dtroxell19/FairDL-ICML-2026.git

## 纳入依据

in all other directions are unaffected. This ensures that backpropagation never encourages the 5.2. Loan Default Prediction model to move in directions that would violate active fair- This first experimental setting concerns loan default pre- ness constraints, while allowing learning to proceed freely dictions for small businesses. Note for any given random in all feasible directions. train, validation, and test split, the dataset sizes are relatively small. Therefore, we repeat the entire experiment (includ- 5. Numerical Experiments ing λ selection for penalty models) 25 times, each with a new, random dataset split to reduce the impact of any given We conduct numerical experiments across four distinct random data split on t

## 原始摘要

Differentiable optimization layers are traditionally integrated in predict-then-optimize frameworks where a neural model estimates parameters that subsequently serve as fixed inputs to downstream decision-making optimization problems. In this work, we introduce the concept of a "fairness layer": a differentiable optimization layer appended to a model's output layer that guarantees a chosen notion of output parity is satisfied when integrated into a neural network. Additionally, we introduce an online primal-dual inference algorithm that provides provable aggregate fairness guarantees for streaming predictions with arbitrarily small batch sizes, where traditional per-batch constraints become overly restrictive. Numerical experiments demonstrate the effectiveness of the fairness layer and associated algorithm, and theoretical analysis characterizes the layer's differentiability and stability properties during model training and backpropagation. Our code for these experiments is publicly available on GitHub: https://github.com/dtroxell19/FairDL-ICML-2026.git and our public Python package documentation can be found online: https://dtroxell19.github.io/fairness_training/.
