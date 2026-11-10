# Multi-Level Strategic Classification: Incentivizing Improvement through Promotion and Relegation Dynamics

ICML 2026 · main · application

正文包含明确金融数据、金融任务或金融案例；金融应用可属于通用方法的一个实验。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=Hnty5t1TNg
- 摘要来源：https://icml.cc/virtual/2026/poster/65013
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-Hnty5t1TNg__Multi_Level_Strategic_Classification_Incentivizing_Improvement_through_Promotion_and_Relegation_Dynamics.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Credit Scoring & Default / 信用评分与违约
- 技术方法标签：Fairness & Recourse / 公平性与算法追索
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

params Θ = {β, γ, c , c , r, δ}, dis- To evaluate the practical implications of our model, we sim- cretization step ∆x, max attribute Xmax , precision ε ulate a population of agents using the FICO credit score Require: VALUE I TERATE that approximates the agent’s dataset (Hardt et al., 2016). We model exclusively the initial optimal strategy on the discretized attribute space X attribute x0 using the FICO raw score distribution normal- 1: X ← discretized [0, Xmax ] with gap ∆x ized

## 原始摘要

Strategic classification studies the problem where self-interested individuals or agents manipulate their response to obtain favorable decision outcomes made by classifiers, typically turning to dishonest actions when they are less costly than genuine efforts. While existing studies on sequential strategic classification primarily focus on optimizing dynamic classifier weights, we depart from these weight-centric approaches by analyzing the design of classifier thresholds and difficulty progression within a multi-level promotion-relegation framework. Our model captures the critical inter-temporal incentives driven by an agent's farsightedness, skill retention, and a "leg-up" effect where qualification and attainment can be self-reinforcing. We characterize the agent’s optimal long-term strategy and demonstrate that a principal can design a sequence of thresholds to effectively incentivize honest effort. Crucially, we prove that under mild conditions, this mechanism enables agents to reach arbitrarily high levels solely through genuine improvement efforts.
