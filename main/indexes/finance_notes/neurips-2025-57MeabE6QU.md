# Distributionally Robust Performative Optimization

NeurIPS 2025 · main · application

通用方法在金融任务、数据或明确案例上开展应用验证。 主题：Portfolio & Investment / 投资组合与投资管理。

- 官方论文页：https://openreview.net/forum?id=57MeabE6QU
- 摘要来源：https://neurips.cc/virtual/2025/poster/119893
- 本地 PDF：[打开](../../pdfs/NeurIPS/2025/neurips-2025-57MeabE6QU__Distributionally_Robust_Performative_Optimization.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_review
- 主方向：Portfolio & Investment / 投资组合与投资管理
- 细分方向：Portfolio Selection & Optimization / 组合选择与优化
- 技术方法标签：Fairness & Recourse / 公平性与算法追索；Uncertainty & Robustness / 不确定性与鲁棒性；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：optimization
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Extensive numerical experiments in strategic classification, revenue management, and portfolio optimization demonstrate significant performance gains over state-of-the-art baselines, highlighting the practical value of our approach.

## 原始摘要

In performative stochastic optimization, decisions can influence the distribution of random parameters, rendering the data-generating process itself decision-dependent. In practice, decision-makers rarely have access to the true distribution map and must instead rely on imperfect surrogate models, which can lead to severely suboptimal solutions under misspecification. Data scarcity or costly collection further exacerbates these challenges in real-world settings. To address these challenges, we propose a distributionally robust framework for performative optimization that explicitly accounts for ambiguity in the decision-dependent distribution. Our framework introduces three modeling paradigms that capture a broad range of applications in machine learning and decision-making under uncertainty. This latter setting has not previously been explored in the performative optimization literature. To tackle the intractability of the resulting nonconvex objectives, we develop an iterative algorithm named repeated robust risk minimization, which alternates between solving a decision-independent distributionally robust optimization problem and updating the ambiguity set based on the previous decision. This decoupling ensures computational tractability at each iteration while enhancing robustness to model uncertainty. We provide reformulations compatible with off-the-shelf solvers and establish theoretical guarantees on convergence and suboptimality. Extensive numerical experiments in strategic classification, revenue management, and portfolio optimization demonstrate significant performance gains over state-of-the-art baselines, highlighting the practical value of our approach.
