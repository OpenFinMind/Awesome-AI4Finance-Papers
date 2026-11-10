# Reinforcement Learning with Imperfect Transition Predictions: A Bellman-Jensen Approach

NeurIPS 2025 · main · application

通用方法在金融任务、数据或明确案例上开展应用验证。 主题：Market Prediction / 股价、收益与波动率预测；Financial Agents / 金融Agent与决策。

- 官方论文页：https://openreview.net/forum?id=DYuPwwDy9n
- 摘要来源：https://neurips.cc/virtual/2025/poster/119213
- 本地 PDF：[打开](../../pdfs/NeurIPS/2025/neurips-2025-DYuPwwDy9n__Reinforcement_Learning_with_Imperfect_Transition_Predictions_A_Bellman_Jensen_Approach.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_review
- 主方向：Market Prediction / 股价、收益与波动率预测
- 细分方向：Stock Movement & Returns / 股价方向与收益预测；Investment & Financial Research Agents / 投研与金融决策Agent
- 技术方法标签：Reinforcement Learning / 强化学习；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Bayesian；reinforcement learning
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

In many real-world applications, such as energy management and stock investment, agents can access multi-step predictions of future states, which provide additional advantages for decision making.

## 原始摘要

Traditional reinforcement learning (RL) assumes the agents make decisions based on Markov decision processes (MDPs) with one-step transition models. In many real-world applications, such as energy management and stock investment, agents can access multi-step predictions of future states, which provide additional advantages for decision making. However, multi-step predictions are inherently high-dimensional: naively embedding these predictions into an MDP leads to an exponential blow-up in state space and the curse of dimensionality. Moreover, existing RL theory provides few tools to analyze prediction-augmented MDPs, as it typically works on one-step transition kernels and cannot accommodate multi-step predictions with errors or partial action-coverage. We address these challenges with three key innovations: First, we propose the \emph{Bayesian value function} to characterize the optimal prediction-aware policy tractably. Second, we develop a novel \emph{Bellman–Jensen Gap} analysis on the Bayesian value function, which enables characterizing the value of imperfect predictions. Third, we introduce BOLA (Bayesian Offline Learning with Online Adaptation), a two-stage model-based RL algorithm that separates offline Bayesian value learning from lightweight online adaptation to real-time predictions. We prove that BOLA remains sample-efficient even under imperfect predictions. We validate our theory and algorithm on synthetic MDPs and a real-world wind energy storage control problem.
