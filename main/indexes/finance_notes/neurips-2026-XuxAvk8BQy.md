# Masked Sobolev Training for Feasibility-Reliable Optimization Proxies

NeurIPS 2026 · main · application

以金融市场为研究对象，或包含明确的金融领域数据和应用评测。 主题：Portfolio & Investment / 投资组合与投资管理。

- 官方论文页：https://openreview.net/forum?id=XuxAvk8BQy
- 摘要来源：https://neurips.cc/Downloads/2026
- PDF 状态：access_blocked
- 金融依据类型：title_abstract_financial_task_or_data
- 主方向：Portfolio & Investment / 投资组合与投资管理
- 细分方向：Investment Evaluation & Decisions / 投资评价与决策
- 技术方法标签：Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：distillation；Optimization；optimization
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

A mean--variance portfolio study identifies the complementary limitation: when sensitivities are highly local or vanish across active-set regimes, derivative supervision can be less useful than value-only training.

## 原始摘要

Optimization proxies amortize parametric constrained optimization by learning fast approximations of solution maps. Because these maps are smooth only within active-set regimes, the parameter space may split into combinatorially many critical regions, making finite-sample generalization and reliable constraint behavior central challenges. To address this challenge, this paper develops sparse stochastic masked Sobolev training for optimization proxies, augmenting value supervision with randomly selected solver-sensitivity targets rather than dense Jacobian matching. The mask acts as an algorithmic control: it exposes the proxy to local derivative information while avoiding overconstraint from conflicting active constraint set signals. We provide approximation bounds showing that, under coverage and regularity, joint value-and-Jacobian matching improves finite-sample generalization. Experiments characterize when and how this benefit appears. In smooth optimal-control distillation, where feasibility is guaranteed by construction, and only a few active-set regimes arise, Sobolev supervision reaches 95\% of teacher performance about $2.5\times$ faster than value-only training. In AC optimal power flow, masked Sobolev training keeps optimality gaps below 0.22\% across three PGLib networks while reducing the median worst-case constraint violation by up to $4\times$. A mean--variance portfolio study identifies the complementary limitation: when sensitivities are highly local or vanish across active-set regimes, derivative supervision can be less useful than value-only training.
