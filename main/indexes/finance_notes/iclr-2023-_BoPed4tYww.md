# Timing is Everything: Learning to Act Selectively with Costly Actions and Budgetary Constraints

ICLR 2023 · main · application

包含明确的金融任务、金融领域数据或金融案例验证。 主题：Portfolio & Investment / 投资组合与投资管理。

- 官方论文页：https://openreview.net/forum?id=_BoPed4tYww
- 摘要来源：https://iclr.cc/virtual/2023/poster/11201
- 本地 PDF：[打开](../../pdfs/ICLR/2023/iclr-2023-_BoPed4tYww__Timing_is_Everything_Learning_to_Act_Selectively_with_Costly_Actions_and_Budgetary_Constraints.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_financial_task_or_data
- 主方向：Portfolio & Investment / 投资组合与投资管理
- 细分方向：Investment Evaluation & Decisions / 投资评价与决策
- 技术方法标签：Reinforcement Learning / 强化学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：reinforcement learning
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Many real-world settings involve costs for performing actions; transaction costsin financial systems and fuel costs being common examples. / We show LICRA learns theoptimal value function and ensures budget constraints are satisfied almost surely.We demonstrate empirically LICRA’s superior performance against benchmarkRL methods in OpenAI gym’s Lunar Lander and in Highway environments and avariant of the Merton portfolio problem within finance.

## 原始摘要

Many real-world settings involve costs for performing actions; transaction costsin financial systems and fuel costs being common examples. In these settings,performing actions at each time step quickly accumulates costs leading to vastlysuboptimal outcomes. Additionally, repeatedly acting produces wear and tear andultimately, damage. Determining when to act is crucial for achieving successfuloutcomes and yet, the challenge of efficiently learning to behave optimally whenactions incur minimally bounded costs remains unresolved. In this paper, we intro-duce a reinforcement learning (RL) framework named Learnable Impulse ControlReinforcement Algorithm (LICRA), for learning to optimally select both whento act and which actions to take when actions incur costs. At the core of LICRAis a nested structure that combines RL and a form of policy known as impulsecontrol which learns to maximise objectives when actions incur costs. We provethat LICRA, which seamlessly adopts any RL method, converges to policies thatoptimally select when to perform actions and their optimal magnitudes. We thenaugment LICRA to handle problems in which the agent can perform at most k < ∞actions and more generally, faces a budget constraint. We show LICRA learns theoptimal value function and ensures budget constraints are satisfied almost surely.We demonstrate empirically LICRA’s superior performance against benchmarkRL methods in OpenAI gym’s Lunar Lander and in Highway environments and avariant of the Merton portfolio problem within finance.
