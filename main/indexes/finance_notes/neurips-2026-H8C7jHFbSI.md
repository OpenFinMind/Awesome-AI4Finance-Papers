# AlphaPareto: Formulaic Alpha Discovery with LLM-Guided Multi-Objective Reinforcement Learning

NeurIPS 2026 · main · core

以金融任务或金融数据为核心研究对象。 主题：Alpha Mining / 量化因子挖掘；Trading & Microstructure / 交易与市场微观结构。

- 官方论文页：https://openreview.net/forum?id=H8C7jHFbSI
- 摘要来源：https://neurips.cc/virtual/2026/poster/153971
- 本地 PDF：[打开](../../pdfs/NeurIPS/2026/neurips-2026-H8C7jHFbSI__AlphaPareto_Formulaic_Alpha_Discovery_with_LLM_Guided_Multi_Objective_Reinforcement_Learning.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_review
- 主方向：Alpha Mining / 量化因子挖掘
- 细分方向：Alpha Discovery / Alpha与因子发现；Trading & Execution / 交易策略与执行
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Reinforcement Learning / 强化学习；Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：language model；LLM；reinforcement learning
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Formulaic alpha discovery is a core challenge in quantitative trading, as identifying alphas that work well together remains difficult.

## 原始摘要

Formulaic alpha discovery is a core challenge in quantitative trading, as identifying alphas that work well together remains difficult. Recent reinforcement learning (RL) methods formulate this task as a Markov decision process (MDP), but two important issues remain unresolved. First, as the alpha pool evolves, the reward function changes accordingly, making the MDP inherently non-stationary. Second, most existing methods optimize a single objective, typically predictive power, while ignoring other important properties of a high-quality alpha pool. Motivated by these challenges, we propose AlphaPareto, an RL method for formulaic alpha discovery. To address non-stationarity, AlphaPareto augments the state to include both the alpha under construction and the current alpha pool, and applies a large language model (LLM) to encode the pool. This design allows the agent to adapt to the evolving search environment. To overcome the limitation of single-objective reward design, AlphaPareto replaces the scalar reward with a multi-objective vector-valued reward that simultaneously captures predictive power, temporal stability, perturbation robustness, and diversity, and optimizes these objectives through a Pareto-regularized learning procedure. Empirical applications to real-world datasets show that our AlphaPareto method outperforms its competitors.
