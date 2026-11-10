# MAFE: Enabling Equitable Algorithm Design in Multi-Agent Multi-Stage Decision-Making Systems

ICML 2026 · main · application

通用方法在金融任务、数据或明确案例上开展应用验证。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=viOFFYQPgL
- 摘要来源：https://icml.cc/virtual/2026/poster/60878
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-viOFFYQPgL__MAFE_Enabling_Equitable_Algorithm_Design_in_Multi_Agent_Multi_Stage_Decision_Making_Systems.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_review
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Lending & Credit Data / 借贷与信贷数据应用
- 技术方法标签：Reinforcement Learning / 强化学习；Fairness & Recourse / 公平性与算法追索
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：multi-agent；Multi-Agent；reinforcement learning
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

We demonstrate MAFEs in three domains—loan processing, healthcare, and higher education—supporting heterogeneous agents, configurable interventions, and fairness metrics.

## 原始摘要

Algorithmic fairness is often studied in static or single-agent settings, yet many real-world decision-making systems involve multiple interacting entities whose multi-stage actions jointly influence long-term outcomes. Existing fairness methods applied at isolated decision points frequently fail to mitigate disparities that accumulate over time. Although recent work has modeled fairness as a sequential decision-making problem, it typically assumes centralized agents or simplified dynamics, limiting its applicability to complex social systems. We introduce **MAFE**, a suite of *Multi-Agent Fair Environments* designed to simulate realistic, modular, and dynamic systems in which fairness emerges from the interplay of multiple agents. We demonstrate MAFEs in three domains—loan processing, healthcare, and higher education—supporting heterogeneous agents, configurable interventions, and fairness metrics. The environments are open-source and compatible with standard multi-agent reinforcement learning (MARL) libraries, enabling reproducible evaluation of fairness-aware policies. Through extensive experiments on cooperative use cases, we demonstrate how MAFE facilitates the design of equitable multi-agent algorithms and reveals critical trade-offs between fairness, performance, and coordination. MAFE provides a foundation for systematic progress in dynamic, multi-agent fairness research.
