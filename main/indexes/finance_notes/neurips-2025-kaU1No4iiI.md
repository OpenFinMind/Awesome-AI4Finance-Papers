# Collective Counterfactual Explanations: Balancing Individual Goals and Collective Dynamics

NeurIPS 2025 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：HELOC。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=kaU1No4iiI
- 摘要来源：https://neurips.cc/virtual/2025/poster/116367
- 本地 PDF：[打开](../../pdfs/NeurIPS/2025/neurips-2025-kaU1No4iiI__Collective_Counterfactual_Explanations_Balancing_Individual_Goals_and_Collective_Dynamics.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Credit Scoring & Default / 信用评分与违约
- 技术方法标签：Fairness & Recourse / 公平性与算法追索；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：optimization
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Math-Jacobs/bfm?tab=readme-ov-file) 7 Adult COMPAS HELOC Moons 1.00 Cost of Competition

## 原始摘要

Counterfactual explanations provide individuals with cost-optimal recommendations to achieve their desired outcomes. However, when a significant number of individuals seek similar state modifications, this individual-centric approach can inadvertently create competition and introduce unforeseen costs. Additionally, disregarding the underlying data distribution may lead to recommendations that individuals perceive as unusual or impractical. To address these challenges, we propose a novel framework that extends standard counterfactual explanations by incorporating a population dynamics model. This framework penalizes deviations from equilibrium after individuals follow the recommendations, effectively mitigating externalities caused by correlated changes across the population. By balancing individual modification costs with their impact on others, our method ensures a more equitable and efficient outcome. We show how this approach reframes the counterfactual explanation problem from an individual-centric task to a collective optimization problem. Augmenting our theoretical insights, we design and implement scalable algorithms for computing collective counterfactuals, showcasing their effectiveness and advantages over existing recourse methods, particularly in aligning with collective objectives.
