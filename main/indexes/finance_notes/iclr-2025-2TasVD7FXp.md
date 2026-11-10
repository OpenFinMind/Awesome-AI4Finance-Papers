# InvestESG: A multi-agent reinforcement learning benchmark for studying climate investment as a social dilemma

ICLR 2025 · main · core

以金融任务或金融数据为核心研究对象。 主题：Portfolio & Investment / 投资组合与投资管理；Financial Agents / 金融Agent与决策；ESG & Sustainable Finance / ESG与可持续金融。

- 官方论文页：https://openreview.net/forum?id=2TasVD7FXp
- 摘要来源：https://iclr.cc/virtual/2025/poster/31135
- 本地 PDF：[打开](../../pdfs/ICLR/2025/iclr-2025-2TasVD7FXp__InvestESG_A_multi_agent_reinforcement_learning_benchmark_for_studying_climate_investment_as_a_social_dile.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_review
- 主方向：ESG & Sustainable Finance / ESG与可持续金融
- 细分方向：Investment & Financial Research Agents / 投研与金融决策Agent；ESG Disclosure & Greenwashing / ESG披露与漂绿；Sustainable Investment / 可持续投资；Investment Evaluation & Decisions / 投资评价与决策
- 技术方法标签：Reinforcement Learning / 强化学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：multi-agent；reinforcement learning
- 数据 / 评测名称（题名和摘要可确认）：InvestESG
- 代码链接：摘要未提供可确认链接

## 纳入依据

**InvestESG** is a novel multi-agent reinforcement learning (MARL) benchmark designed to study the impact of Environmental, Social, and Governance (ESG) disclosure mandates on corporate climate investments. / The benchmark models an intertemporal social dilemma where companies balance short-term profit losses from climate mitigation efforts and long-term benefits from reducing climate risk, while ESG-conscious investors attempt to influence corporate behavior through their investment decisions. / However, when a critical mass of investors prioritizes ESG, corporate cooperation increases, which in turn reduces climate risks and enhances long-term financial stability.

## 原始摘要

**InvestESG** is a novel multi-agent reinforcement learning (MARL) benchmark designed to study the impact of Environmental, Social, and Governance (ESG) disclosure mandates on corporate climate investments. The benchmark models an intertemporal social dilemma where companies balance short-term profit losses from climate mitigation efforts and long-term benefits from reducing climate risk, while ESG-conscious investors attempt to influence corporate behavior through their investment decisions. Companies allocate capital across mitigation, greenwashing, and resilience, with varying strategies influencing climate outcomes and investor preferences. We are releasing open-source versions of InvestESG in both PyTorch and JAX, which enable scalable and hardware-accelerated simulations for investigating competing incentives in mitigate climate change. Our experiments show that without ESG-conscious investors with sufficient capital, corporate mitigation efforts remain limited under the disclosure mandate. However, when a critical mass of investors prioritizes ESG, corporate cooperation increases, which in turn reduces climate risks and enhances long-term financial stability. Additionally, providing more information about global climate risks encourages companies to invest more in mitigation, even without investor involvement. Our findings align with empirical research using real-world data, highlighting MARL's potential to inform policy by providing insights into large-scale socio-economic challenges through efficient testing of alternative policy and market designs.
