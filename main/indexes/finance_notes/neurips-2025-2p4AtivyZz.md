# OPHR: Mastering Volatility Trading with Multi-Agent Deep Reinforcement Learning

NeurIPS 2025 · main · core

以金融任务或金融数据为核心研究对象。 主题：Derivatives & Hedging / 衍生品定价与对冲；Trading & Microstructure / 交易与市场微观结构；Financial Agents / 金融Agent与决策；Blockchain & Digital Assets / 区块链与数字资产。

- 官方论文页：https://openreview.net/forum?id=2p4AtivyZz
- 摘要来源：https://neurips.cc/virtual/2025/poster/120100
- PDF 状态：access_blocked
- 金融依据类型：title_abstract_review
- 主方向：Trading & Microstructure / 交易与市场微观结构
- 细分方向：Hedging / 对冲；Implied Volatility / 隐含波动率曲面；Trading & Execution / 交易策略与执行；Investment & Financial Research Agents / 投研与金融决策Agent；Crypto & Blockchain Transactions / 加密资产与链上交易
- 技术方法标签：Reinforcement Learning / 强化学习；Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：multi-agent；reinforcement learning
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/Edwicn/OPHR-MasteringVolatilityTradingwithMultiAgentDeepReinforcementLearning

## 纳入依据

Options markets represent one of the most sophisticated segments of the financial ecosystem, with prices that directly reflect market uncertainty. / In this paper, we introduce the first reinforcement learning (RL) framework specifically designed for volatility trading through options, focusing on profit from the difference between implied volatility and realized volatility. / Our multi-agent architecture consists of an Option Position Agent (OP-Agent) responsible for volatility timing by controlling long/short volatility positions, and a Hedger Routing Agent (HR-Agent) that manages risk and maximizes path-dependent profits by selecting optimal hedging strategies with different risk preferences. / Evaluating our approach using cryptocurrency options data from 2021-2024, we demonstrate superior performance on BTC and ETH, significantly outperforming traditional strategies and machine learning baselines across all profit and risk-adjusted metrics while exhibiting sophisticated trading behavior.

## 原始摘要

Options markets represent one of the most sophisticated segments of the financial ecosystem, with prices that directly reflect market uncertainty. In this paper, we introduce the first reinforcement learning (RL) framework specifically designed for volatility trading through options, focusing on profit from the difference between implied volatility and realized volatility. Our multi-agent architecture consists of an Option Position Agent (OP-Agent) responsible for volatility timing by controlling long/short volatility positions, and a Hedger Routing Agent (HR-Agent) that manages risk and maximizes path-dependent profits by selecting optimal hedging strategies with different risk preferences. Evaluating our approach using cryptocurrency options data from 2021-2024, we demonstrate superior performance on BTC and ETH, significantly outperforming traditional strategies and machine learning baselines across all profit and risk-adjusted metrics while exhibiting sophisticated trading behavior. The code framework and sample data of this paper have been released on https://github.com/Edwicn/OPHR-MasteringVolatilityTradingwithMultiAgentDeepReinforcementLearning
