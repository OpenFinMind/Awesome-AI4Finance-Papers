# Bandit Learning with Delayed Impact of Actions

NeurIPS 2021 · main · application

研究金融风险度量、金融决策或信贷场景的建模与理论方法。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=4QrgRSAAroI
- 摘要来源：https://neurips.cc/virtual/2021/poster/26027
- 本地 PDF：[打开](../../pdfs/NeurIPS/2021/neurips-2021-4QrgRSAAroI__Bandit_Learning_with_Delayed_Impact_of_Actions.pdf)；版本：publisher_version
- 金融依据类型：financial_method_or_formal_case
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Lending & Credit Data / 借贷与信贷数据应用
- 技术方法标签：Reinforcement Learning / 强化学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

For example, the capability to pay back a loan for people in a certain social group might depend on historically how frequently that group has been approved loan applications. / If banks keep rejecting loan applications to people in a disadvantaged group, it could create a feedback loop and further damage the chance of getting loans for people in that group.

## 原始摘要

We consider a stochastic multi-armed bandit (MAB) problem with delayed impact of actions. In our setting, actions taken in the pastimpact the arm rewards in the subsequent future. This delayed impact of actions is prevalent in the real world. For example, the capability to pay back a loan for people in a certain social group might depend on historically how frequently that group has been approved loan applications. If banks keep rejecting loan applications to people in a disadvantaged group, it could create a feedback loop and further damage the chance of getting loans for people in that group. In this paper, we formulate this delayed and long-term impact of actions within the context of multi-armed bandits. We generalize the bandit setting to encode the dependency of this ``bias" due to the action history during learning. The goal is to maximize the collected utilities over time while taking into account the dynamics created by the delayed impacts of historical actions. We propose an algorithm that achieves a regret of $\tilde{O}(KT^{2/3})$ and show a matching regret lower bound of $\Omega(KT^{2/3})$, where $K$ is the number of arms and $T$ is the learning horizon. Our results complement the bandit literature by adding techniques to deal with actions with long-term impacts and have implications in designing fair algorithms.
