# Private Rate-Constrained Optimization with Applications to Fair Learning

ICLR 2026 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：Credit-Card。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=mex3rvs2KX
- 摘要来源：https://iclr.cc/virtual/2026/poster/10007554
- 本地 PDF：[打开](../../pdfs/ICLR/2026/iclr-2026-mex3rvs2KX__Private_Rate_Constrained_Optimization_with_Applications_to_Fair_Learning.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Lending & Credit Data / 借贷与信贷数据应用
- 技术方法标签：Fairness & Recourse / 公平性与算法追索；Privacy & Federated Learning / 隐私与联邦学习；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：optimization
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

trong privacy guarantees; (iii) scales to a large number of constraints, and (iv) is computationally efficient. Setup. We evaluate RaCO-DP on three constraint types: demographic parity (on Adult (Becker & Kohavi, 1996), Credit-Card (Yeh, 2009), Parkinsons Little (2007), ACSEmployment (Ding et al., 2021), CelebA (Liu et al., 2015)), false negative rate (on Adult, Heart Alex Teboul), and equalized odds (on Credit-Card). We benchmark against DP-FERMI (Lowy et al., 2023), Tran et al. (2021), and Jagielski et al. (2019), reporting their results from Lowy et al. (2023) where avail

## 原始摘要

Many problems in trustworthy ML can be expressed as constraints on prediction rates across subpopulations, including group fairness constraints (demographic parity, equalized odds, etc.). In this work, we study such constrained minimization problems under differential privacy (DP). Standard DP optimization techniques like DP-SGD rely on objectives that decompose over individual examples, enabling per-example gradient clipping and noise addition. Rate constraints, however, depend on aggregate statistics across groups, creating inter-sample dependencies that violate this decomposability. To address this, we develop RaCO-DP, a DP variant of Stochastic Gradient Descent-Ascent (SGDA) that solves the Lagrangian formulation of rate constraint problems. We show that the additional privacy cost of incorporating these constraints reduces to privately estimating a histogram over the mini-batch at each step. We prove convergence of our algorithm through a novel analysis of SGDA that leverages the linear structure of the dual parameter. Empirical results show that our method Pareto-dominates existing private learning approaches under group fairness constraints and also achieves strong privacy–utility–fairness performance on neural networks.
