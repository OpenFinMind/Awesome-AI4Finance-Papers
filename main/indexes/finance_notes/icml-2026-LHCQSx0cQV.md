# Design Linear Constrained Neural Layers with Implicit Convex Optimization

ICML 2026 · main · application

通用方法在金融任务、数据或明确案例上开展应用验证。 主题：Portfolio & Investment / 投资组合与投资管理。

- 官方论文页：https://openreview.net/forum?id=LHCQSx0cQV
- 摘要来源：https://icml.cc/virtual/2026/poster/64648
- PDF 状态：access_blocked
- 金融依据类型：title_abstract_review
- 主方向：Portfolio & Investment / 投资组合与投资管理
- 细分方向：Portfolio Selection & Optimization / 组合选择与优化
- 技术方法标签：Graph Learning / 图学习；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：optimization
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Experiments on linear programming, as well as two real-world problems: partial graph matching and portfolio allocation which involve other discrete constraints.

## 原始摘要

One essential limitation of neural networks is how to enforce (hard) constraints on prediction. We propose a plug-in, differentiable layer, which involves a fast implicit (convex) optimization procedure to enforce the general linear constraint. It aims to minimize a divergence between unconstrained and constrained outputs. Connecting to and beyond existing handcrafted layers, we show that our layer degrades to classic layers like Softmax, Sinkhorn and tanh etc. when the corresponding constraint is enforced by KL-divergence minimization. We further show that by replacing the KL-div with a Euclidean distance, a closed-form solution can be derived for highly-efficient constraint enforcing. We evaluate the above two variants of layers, termed as BLCLayer and GLCLayer, with their corresponding neural solver BLCNet and GLCNet with simple MLP/GNN-like backbone. Experiments on linear programming, as well as two real-world problems: partial graph matching and portfolio allocation which involve other discrete constraints.
