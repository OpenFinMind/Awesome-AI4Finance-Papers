# Long-term Fairness with Selective Labels

ICML 2026 · main · application

包含明确的金融任务、金融领域数据或金融案例验证。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=Ykdbje3SDK
- 摘要来源：https://icml.cc/virtual/2026/poster/63248
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-Ykdbje3SDK__Long_term_Fairness_with_Selective_Labels.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_financial_task_or_data
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Lending & Credit Data / 借贷与信贷数据应用
- 技术方法标签：Reinforcement Learning / 强化学习；Fairness & Recourse / 公平性与算法追索
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：reinforcement learning
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

However, in scenarios such as hiring or lending, the labels (e.g., ability to repay the loan) are _selective labels_ as they are only revealed based on positive decisions (e.g., when a loan is granted).

## 原始摘要

Long-term fairness algorithms aim to satisfy fairness beyond static and short-term notions by accounting for the dynamics between decision-making policies and population behavior. Most previous approaches evaluate performance and fairness measures from observable features and a label, which is assumed to be fully observed. However, in scenarios such as hiring or lending, the labels (e.g., ability to repay the loan) are _selective labels_ as they are only revealed based on positive decisions (e.g., when a loan is granted). In this paper, we study long-term fairness in the selective labels setting and analytically show that naive solutions do not guarantee fairness. To address this gap, we then introduce a novel framework that leverages both the observed data and a label predictor model to estimate the true fairness measure value by decomposing it into the observed fairness and bias from label predictions. This allows us to derive  sufficient conditions to satisfy true fairness from observable quantities by using the confidence in the predictor model.  Finally,  we rely on our theoretical results to propose a novel reinforcement learning algorithm for effective long-term fair decision-making with selective labels. In semisynthetic environments, the proposed algorithm reached comparable fairness and performance to an agent with oracle access to the true labels.
