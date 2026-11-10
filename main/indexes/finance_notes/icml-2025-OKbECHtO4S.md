# Nested Expectations with Kernel Quadrature

ICML 2025 · main · application

通用方法在金融任务、数据或明确案例上开展应用验证。 主题：Derivatives & Hedging / 衍生品定价与对冲。

- 官方论文页：https://openreview.net/forum?id=OKbECHtO4S
- 摘要来源：https://icml.cc/virtual/2025/poster/45450
- 本地 PDF：[打开](../../pdfs/ICML/2025/icml-2025-OKbECHtO4S__Nested_Expectations_with_Kernel_Quadrature.pdf)；版本：publisher_version
- 金融依据类型：title_abstract_review
- 主方向：Derivatives & Hedging / 衍生品定价与对冲
- 细分方向：Option Pricing & PDEs / 期权定价与PDE
- 技术方法标签：Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Bayesian
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

We then demonstrate empirically that our proposed method does indeed require the fewest number of samples to estimate nested expectations over a range of real-world application areas from Bayesian optimisation to option pricing and health economics.

## 原始摘要

This paper considers the challenging computational task of estimating nested expectations. Existing algorithms, such as nested Monte Carlo or multilevel Monte Carlo, are known to be consistent but require a large number of samples at both inner and outer levels to converge. Instead, we propose a novel estimator consisting of nested kernel quadrature estimators and we prove that it has a faster convergence rate than all baseline methods when the integrands have sufficient smoothness. We then demonstrate empirically that our proposed method does indeed require the fewest number of samples to estimate nested expectations over a range of real-world application areas from Bayesian optimisation to option pricing and health economics.
