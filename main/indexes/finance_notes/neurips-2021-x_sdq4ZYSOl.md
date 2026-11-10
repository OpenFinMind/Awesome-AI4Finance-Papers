# Improved Regret Bounds for Tracking Experts with Memory

NeurIPS 2021 · main · application

正文包含金融场景的案例或形式化分析。 主题：Portfolio & Investment / 投资组合与投资管理；Financial Safety & Compliance / 金融安全与合规。

- 官方论文页：https://openreview.net/forum?id=x_sdq4ZYSOl
- 摘要来源：https://neurips.cc/virtual/2021/poster/25982
- 本地 PDF：[打开](../../pdfs/NeurIPS/2021/neurips-2021-x_sdq4ZYSOl__Improved_Regret_Bounds_for_Tracking_Experts_with_Memory.pdf)；版本：publisher_version
- 金融依据类型：fulltext_financial_case_or_formal_model
- 主方向：Portfolio & Investment / 投资组合与投资管理
- 细分方向：Portfolio Selection & Optimization / 组合选择与优化；Trust, Compliance & Bias / 可信、合规与偏差审计
- 技术方法标签：Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：optimization
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

costs proportional to the amount bought or sold (see e.g., [2, 32]). In Section 3.3 we motivate the use of projections over weight-sharing in this context, proving that projections are strictly more “efficient”. Online portfolio selection with transaction costs is an active area of research [9, 30, 32, 33]. 2.1 Related work Switching (without memory) in online learning was first introduced in [35] (see also the earlier [34] and independently in the context of universal coding in [43]), and extended with the Fixed-Share algorithm [23]. An extensive literature has built on the

## 原始摘要

We address the problem of sequential prediction with expert advice in a non-stationary environment with long-term memory guarantees in the sense of Bousquet and Warmuth [4]. We give a linear-time algorithm that improves on the best known regret bound [27]. This algorithm incorporates a relative entropy projection step. This projection is advantageous over previous weight-sharing approaches in that weight updates may come with implicit costs as in for example portfolio optimization. We give an algorithm to compute this projection step in linear time, which may be of independent interest.
