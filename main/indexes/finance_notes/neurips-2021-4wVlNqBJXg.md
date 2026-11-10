# Optimal Best-Arm Identification Methods for Tail-Risk Measures

NeurIPS 2021 · main · application

研究金融风险度量、金融决策或信贷场景的建模与理论方法。 主题：Insurance & Actuarial / 保险与精算。

- 官方论文页：https://openreview.net/forum?id=4wVlNqBJXg
- 摘要来源：https://neurips.cc/virtual/2021/poster/26325
- 本地 PDF：[打开](../../pdfs/NeurIPS/2021/neurips-2021-4wVlNqBJXg__Optimal_Best_Arm_Identification_Methods_for_Tail_Risk_Measures.pdf)；版本：publisher_version
- 金融依据类型：financial_method_or_formal_case
- 主方向：Insurance & Actuarial / 保险与精算
- 细分方向：Insurance & Claims / 承保与理赔
- 技术方法标签：Reinforcement Learning / 强化学习；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：optimization
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Conditional value-at-risk (CVaR) and value-at-risk (VaR) are popular tail-risk measures in finance and insurance industries as well as in highly reliable, safety-critical uncertain environments where often the underlying probability distributions are heavy-tailed. / The latter captures the risk-return trade-off common in finance.

## 原始摘要

Conditional value-at-risk (CVaR) and value-at-risk (VaR) are popular tail-risk measures in finance and insurance industries as well as in highly reliable, safety-critical uncertain environments where often the underlying probability distributions are heavy-tailed. We use the multi-armed bandit best-arm identification framework and consider the problem of identifying the arm from amongst finitely many that has the smallest CVaR, VaR, or weighted sum of CVaR and mean. The latter captures the risk-return trade-off common in finance. Our main contribution is an optimal $\delta$-correct algorithm that acts on general arms, including heavy-tailed distributions, and matches the lower bound on the expected number of samples needed, asymptotically (as $ \delta$ approaches $0$). The algorithm requires solving a non-convex optimization problem in the space of probability measures, that requires delicate analysis. En-route, we develop new non-asymptotic, anytime-valid, empirical-likelihood-based concentration inequalities for tail-risk measures.
