# Robust Reinforcement Learning in Finance:  Modeling Market Impact with Elliptic Uncertainty Sets

NeurIPS 2025 · main · core

以金融任务或金融数据为核心研究对象。 主题：Portfolio & Investment / 投资组合与投资管理；Trading & Microstructure / 交易与市场微观结构；Financial Agents / 金融Agent与决策。

- 官方论文页：https://openreview.net/forum?id=IJGEtuVqwf
- 摘要来源：https://neurips.cc/virtual/2025/poster/118821
- 本地 PDF：[打开](../../pdfs/NeurIPS/2025/neurips-2025-IJGEtuVqwf__Robust_Reinforcement_Learning_in_Finance_Modeling_Market_Impact_with_Elliptic_Uncertainty_Sets.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_review
- 主方向：Trading & Microstructure / 交易与市场微观结构
- 细分方向：Portfolio Selection & Optimization / 组合选择与优化；Trading & Execution / 交易策略与执行；Order Books & Market Impact / 订单簿与市场冲击；Investment & Financial Research Agents / 投研与金融决策Agent
- 技术方法标签：Reinforcement Learning / 强化学习；Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：reinforcement learning
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

In financial applications, reinforcement learning (RL) agents are commonly trained on historical data, where their actions do not influence prices. / However, during deployment, these agents trade in live markets where their own transactions can shift asset prices, a phenomenon known as market impact. / Experiments on single-asset and multi-asset trading tasks demonstrate that our method achieves superior Sharpe ratio and remains robust under increasing trade volumes, offering a more faithful and scalable approach to RL in financial markets.

## 原始摘要

In financial applications, reinforcement learning (RL) agents are commonly trained on historical data, where their actions do not influence prices. However, during deployment, these agents trade in live markets where their own transactions can shift asset prices, a phenomenon known as market impact. This mismatch between training and deployment environments can significantly degrade performance.  Traditional robust RL approaches address this model misspecification by optimizing the worst-case performance over a set of uncertainties, but typically rely on symmetric structures that fail to capture the directional nature of market impact. To address this issue, we develop a novel class of elliptic uncertainty sets. We establish both implicit and explicit closed-form solutions for the worst-case uncertainty under these sets, enabling efficient and tractable robust policy evaluation. Experiments on single-asset and multi-asset trading tasks demonstrate that our method achieves superior Sharpe ratio and remains robust under increasing trade volumes, offering a more faithful and scalable approach to RL in financial markets.
