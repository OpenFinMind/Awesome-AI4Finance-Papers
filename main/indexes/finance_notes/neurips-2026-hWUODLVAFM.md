# Neural Slack Variables for Shape Constraints

NeurIPS 2026 · main · application

包含明确的金融任务、金融领域数据或金融案例验证。 主题：Derivatives & Hedging / 衍生品定价与对冲；Trading & Microstructure / 交易与市场微观结构。

- 官方论文页：https://openreview.net/forum?id=hWUODLVAFM
- 摘要来源：https://neurips.cc/virtual/2026/poster/150516
- 本地 PDF：[打开](../../pdfs/NeurIPS/2026/neurips-2026-hWUODLVAFM__Neural_Slack_Variables_for_Shape_Constraints.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_financial_task_or_data
- 主方向：Derivatives & Hedging / 衍生品定价与对冲
- 细分方向：Implied Volatility / 隐含波动率曲面；Trading & Execution / 交易策略与执行
- 技术方法标签：Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Neural slack variables close the gap to hard constraints on monotonicity and low-dimensional convexity, and maintain effectiveness on nonlinear constraints in neural barrier certificates and no-arbitrage volatility surfaces.

## 原始摘要

Enforcing functional inequality constraints such as monotonicity and convexity in neural networks is a fundamental challenge in many industrial and scientific applications. Classical one-sided penalty methods, just like primal-dual methods gated by complementary slackness, provide gradients only at violated locations, resulting in fragile constraint satisfaction. Hard architectural constraints, on the other hand, cover only the simplest cases and tend to compromise the network's expressive power. We introduce *neural slack variables*, a deep learning-native primal-side approach that converts constraint enforcement into a two-sided regression problem by coupling the primary network with a jointly learned auxiliary network. The auxiliary network serves as a valid target for the primary network's constraint quantities, inducing feasibility and regularity. Theoretically, neural slack variables can be understood as a variable splitting method with parametrized variable projection. Neural slack variables close the gap to hard constraints on monotonicity and low-dimensional convexity, and maintain effectiveness on nonlinear constraints in neural barrier certificates and no-arbitrage volatility surfaces.
