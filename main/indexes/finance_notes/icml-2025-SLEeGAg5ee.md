# DANCE: Dual Unbiased Expansion with Group-acquired Alignment for Out-of-distribution Graph Fairness Learning

ICML 2025 · main · application

正文包含明确金融数据、金融任务或金融案例；金融应用可属于通用方法的一个实验。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=SLEeGAg5ee
- 摘要来源：https://icml.cc/virtual/2025/poster/45227
- 本地 PDF：[打开](../../pdfs/ICML/2025/icml-2025-SLEeGAg5ee__DANCE_Dual_Unbiased_Expansion_with_Group_acquired_Alignment_for_Out_of_distribution_Graph_Fairness_Learni.pdf)；版本：publisher_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Credit Scoring & Default / 信用评分与违约；Lending & Credit Data / 借贷与信贷数据应用
- 技术方法标签：Graph Learning / 图学习；Fairness & Recourse / 公平性与算法追索；Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Graph neural networks
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

approaches, including MLP (Pal & Mitra, as follows: 1) Credit-Cs is derived from the Credit dataset 1992), GCN (Kipf & Welling, 2016). (B) Fair GNNs: GNNs (Yeh & Lien, 2009), where nodes represent credit card users. designed to improve fairness, including FairVGNN (Wang The task involves classifying users’ credit risk as either high et al., 2022), NIFTY (Agarwal et al., 2021), EDITS (Dong or low, with “age” designated as the sensitive attribute. To et al., 2022), CAF (Guo et al., 2023). (C) Ou

## 原始摘要

Graph neural networks (GNNs) have shown strong performance in graph fairness learning, which aims to ensure that predictions are unbiased with respect to sensitive attributes. However, existing approaches usually assume that training and test data share the same distribution, which rarely holds in the real world. To tackle this challenge, we propose a novel approach named Dual Unbiased Expansion with Group-acquired Alignment (DANCE) for graph fairness learning under distribution shifts. The core idea of our DANCE is to synthesize challenging yet unbiased virtual graph data in both graph and hidden spaces, simulating distribution shifts from a data-centric view. Specifically, we introduce the unbiased Mixup in the hidden space, prioritizing minor groups to address the potential imbalance of sensitive attributes. Simultaneously, we conduct fairness-aware adversarial learning in the graph space to focus on challenging samples and improve model robustness. To further bridge the domain gap, we propose a group-acquired alignment objective that prioritizes negative pair groups with identical sensitive labels. Additionally, a representation disentanglement objective is adopted to decorrelate sensitive attributes and target representations for enhanced fairness. Extensive experiments demonstrate the superior effectiveness of the proposed DANCE.
