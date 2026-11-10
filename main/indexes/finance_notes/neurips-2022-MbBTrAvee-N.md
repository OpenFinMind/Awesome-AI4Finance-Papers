# Hedging as Reward Augmentation in Probabilistic Graphical Models

NeurIPS 2022 · main · application

正文包含金融场景的案例或形式化分析。 主题：Derivatives & Hedging / 衍生品定价与对冲；Corporate Finance & Accounting / 公司金融与会计。

- 官方论文页：https://openreview.net/forum?id=MbBTrAvee-N
- 摘要来源：https://neurips.cc/virtual/2022/poster/53885
- 本地 PDF：[打开](../../pdfs/NeurIPS/2022/neurips-2022-MbBTrAvee-N__Hedging_as_Reward_Augmentation_in_Probabilistic_Graphical_Models.pdf)；版本：publisher_version
- 金融依据类型：fulltext_financial_case_or_formal_model
- 主方向：Derivatives & Hedging / 衍生品定价与对冲
- 细分方向：Hedging / 对冲；Earnings & Corporate Disclosures / 盈利与公司披露
- 技术方法标签：未明确标注
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Bayesian
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

h the price of crude oil. Augmenting their situation with a reward that is a deterministic function of any of the three uncertain nodes would result in a simple hedge. Hedging on node A.P. is a classic case of corporate financial hedging. 4.1 The Value of a Hedge There is a natural important question to address: how much does a hedge balance out the uncertainty in the rewards from the current situation, for a decision-theoretic decision maker? The hedging value of the augmented reward is defined as the additional improvement in the agent’s certain equivalent from inclu

## 原始摘要

Most people associate the term `hedging' exclusively with financial applications, particularly the use of financial derivatives. We argue that hedging is an activity that human and machine agents should engage in more broadly, even when the agent's value is not necessarily in monetary units. In this paper, we propose a decision-theoretic view of hedging based on augmenting a probabilistic graphical model -- specifically a Bayesian network or an influence diagram -- with a reward. Hedging is therefore posed as a particular kind of graph manipulation, and can be viewed as analogous to control/intervention and information gathering related analysis. Effective hedging occurs when a risk-averse agent finds opportunity to balance uncertain rewards in their current situation. We illustrate the concepts with examples and counter-examples, and conduct experiments to demonstrate the properties and applicability of the proposed computational tools that enable agents to proactively identify potential hedging opportunities in real-world situations.
