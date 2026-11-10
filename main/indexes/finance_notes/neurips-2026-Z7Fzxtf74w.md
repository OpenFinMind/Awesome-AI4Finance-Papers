# Online Min-Max Optimization: From Individual Regrets to Cumulative Saddle Points

NeurIPS 2026 · main · application

通用方法在金融任务、数据或明确案例上开展应用验证。 主题：Portfolio & Investment / 投资组合与投资管理。

- 官方论文页：https://openreview.net/forum?id=Z7Fzxtf74w
- 摘要来源：https://neurips.cc/virtual/2026/poster/151634
- 本地 PDF：[打开](../../pdfs/NeurIPS/2026/neurips-2026-Z7Fzxtf74w__Online_Min_Max_Optimization_From_Individual_Regrets_to_Cumulative_Saddle_Points.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_review
- 主方向：Portfolio & Investment / 投资组合与投资管理
- 细分方向：Portfolio Selection & Optimization / 组合选择与优化
- 技术方法标签：Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：optimization
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

We derive our bounds for (SDual-Gap$_T$) and DSP-Reg$_T$ under strong convexity-strong concavity and a min-max notion of exponential concavity (min-max EC), and in addition we establish a class of functions satisfying min-max EC that captures a two-player variant of the classic portfolio selection problem.

## 原始摘要

We propose and study an online version of min-max optimization based on cumulative saddle points under a variety of performance measures beyond convex-concave settings. After first observing the incompatibility of (static) Nash equilibrium (SNE-Reg$_T$) with individual regrets even for strongly convex-strongly concave functions, we propose an alternate static duality gap (SDual-Gap$_T$) inspired by the online convex optimization (OCO) framework that is compatible with the individual regrets . We provide algorithms that achieve sub-linear regret bounds for (SDual-Gap$_T$) and the individual regrets and a novel dynamic saddle point regret (DSP-Reg$_T$), which we suggest naturally represents a min-max version of the dynamic regret in OCO. We derive our bounds for (SDual-Gap$_T$) and DSP-Reg$_T$ under strong convexity-strong concavity and a min-max notion of exponential concavity (min-max EC), and in addition we establish a class of functions satisfying min-max EC that captures a two-player variant of the classic portfolio selection problem. Finally, for a dynamic notion of regret compatible with individual regrets, we derive bounds under a two-sided Polyak-\L{}ojasiewicz (PL) condition.
