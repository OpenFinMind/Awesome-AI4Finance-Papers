# Learning to Solve Differential Equation Constrained Optimization Problems

ICLR 2025 · main · application

包含明确的金融任务、金融领域数据或金融案例验证。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=VeMC6Bn0ZB
- 摘要来源：https://iclr.cc/virtual/2025/poster/29404
- 本地 PDF：[打开](../../pdfs/ICLR/2025/iclr-2025-VeMC6Bn0ZB__Learning_to_Solve_Differential_Equation_Constrained_Optimization_Problems.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_financial_task_or_data
- 主方向：Time Series / 时间序列
- 细分方向：Causality & Dynamics / 序列因果与动力学
- 技术方法标签：Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：optimization
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Differential equations (DE) constrained optimization plays a critical role in numerous scientific and engineering fields, including energy systems, aerospace engineering, ecology, and finance, where optimal configurations or control strategies must be determined for systems governed by ordinary or stochastic differential equations. / This combination enables the approximation of optimal strategies while accounting for dynamic constraints in near real-time.Experiments across problems in energy optimization and finance modeling show that this method provides full compliance with dynamic constraints and it produces results up to 25 times more precise than other methods which do not explicitly model the system's dynamic equations.

## 原始摘要

Differential equations (DE) constrained optimization plays a critical role in numerous scientific and engineering fields, including energy systems, aerospace engineering, ecology, and finance, where optimal configurations or control strategies must be determined for systems governed by ordinary or stochastic differential equations. Despite its significance, the computational challenges associated with these problems have limited their practical use. To address these limitations, this paper introduces a learning-based approach to DE-constrained optimization that combines techniques from proxy optimization \citep{kotary2021end} and neural differential equations \citep{chen2019neural}. The proposed approach uses a dual-network architecture, with one approximating the control strategies, focusing on steady-state constraints, and another solving the associated DEs. This combination enables the approximation of optimal strategies while accounting for dynamic constraints in near real-time.Experiments across problems in energy optimization and finance modeling show that this method provides full compliance with dynamic constraints and it produces results up to 25 times more precise than other methods which do not explicitly model the system's dynamic equations.
