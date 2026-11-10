# CounterFlowNet: From Minimal Changes to Meaningful Counterfactual Explanations

NeurIPS 2026 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：German Credit。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=wL6SWD7afK
- 摘要来源：https://neurips.cc/virtual/2026/poster/148627
- 本地 PDF：[打开](../../pdfs/NeurIPS/2026/neurips-2026-wL6SWD7afK__CounterFlowNet_From_Minimal_Changes_to_Meaningful_Counterfactual_Explanations.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Credit Scoring & Default / 信用评分与违约
- 技术方法标签：Reinforcement Learning / 强化学习；Generative Modeling / 生成建模；Fairness & Recourse / 公平性与算法追索；Tabular Learning / 表格学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

valid domain V (d). Upon Method Spars.(%)↑ Div.(%)↑ H. Mean(%)↑ Val.(%)↑ Cov.(%)↑ Unary(%)↑ reaching a terminal state x′ , we compute the composite re- German Credit (Logistic Regression) ward R(x′ | x0 , y ′ ) (Equation (7)). The policy parameters L2C 61.35 37.31 46.39 100.00 100.00 99.06 θ and flow estimator parameters ψ are updated jointly via DICE-R 88.23 15.29 26.06 100.00 100.00 90.81

## 原始摘要

Counterfactual explanations (CFs) provide human-interpretable insights into model's predictions by identifying minimal changes to input features that would alter the model's output. However, existing methods struggle to generate multiple high-quality explanations that (1) affect only a small portion of the features, (2) can be applied to tabular data with heterogeneous features, and (3) are consistent with the user-defined constraints. We proposeCounterFlowNet, a generative approach that formulates CF generation as sequential feature modification using conditional Generative Flow Networks (GFlowNet). CounterFlowNet is trained to sample CFs proportionally to a user-specified reward function that can encode key CF desiderata: validity, sparsity, proximity and plausibility, encouraging high-quality explanations. The sequential formulation yields highly sparse edits, while a unified action space seamlessly supports continuous and categorical features. Moreover, actionability constraints, such as immutability and monotonicity of features, can be enforced at inference time via action masking, without retraining. Experiments on eight datasets under two evaluation protocols demonstrate that CounterFlowNet achieves superior trade-offs between validity, sparsity, plausibility, and diversity with full satisfaction of the given constraints.
