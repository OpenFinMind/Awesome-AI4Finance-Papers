# Contextual Bandits with Knapsacks for a Conversion Model

NeurIPS 2022 · main · application

正文包含明确金融数据、金融任务或金融案例；金融应用可属于通用方法的一个实验。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=OoN6TVb4Vkq
- 摘要来源：https://neurips.cc/virtual/2022/poster/54788
- 本地 PDF：[打开](../../pdfs/NeurIPS/2022/neurips-2022-OoN6TVb4Vkq__Contextual_Bandits_with_Knapsacks_for_a_Conversion_Model.pdf)；版本：publisher_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Credit Scoring & Default / 信用评分与违约；Lending & Credit Data / 借贷与信贷数据应用
- 技术方法标签：Reinforcement Learning / 强化学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

ly many clusters, for instance. We do so in our experiments. Simulation study. A simulation study on partially simulated but realistic data may be found in Appendix F. The underlying dataset is the standard “default of credit card clients” dataset of UCI [2016], initially provided by Yeh and Lien [2009]. (It may be used under a Creative Commons Attribution 4.0 International [CC BY 4.0] license.) 6 4 Analysis for a Known Context Distribution ν Since Θ is bounded, the following quantity, standardly introduced in

## 原始摘要

We consider contextual bandits with knapsacks, with an underlying structure between rewards generated and cost vectors suffered. We do so motivated by sales with commercial discounts. At each round, given the stochastic i.i.d.\ context $\mathbf{x}_t$ and the arm picked $a_t$ (corresponding, e.g., to a discount level), a customer conversion may be obtained, in which case a reward $r(a,\mathbf{x}_t)$ is gained and vector costs $\mathbf{c}(a_t,\mathbf{x}_t)$ are suffered (corresponding, e.g., to losses of earnings). Otherwise, in the absence of a conversion, the reward and costs are null. The reward and costs achieved are thus coupled through the binary variable measuring conversion or the absence thereof. This underlying structure between rewards and costs is different from the linear structures considered by Agrawal and Devanur [2016] (but we show that the techniques introduced in the present article may also be applied to the case of these linear structures). The adaptive policies exhibited in this article solve at each round a linear program based on upper-confidence estimates of the probabilities of conversion given $a$ and $\mathbf{x}$. This kind of policy is most natural and achieves a regret bound of the typical order $(\mathrm{OPT}/B) \smash{\sqrt{T}}$, where $B$ is the total budget allowed, $\mathrm{OPT}$ is the optimal expected reward achievable by a static policy, and $T$ is the number of rounds.
