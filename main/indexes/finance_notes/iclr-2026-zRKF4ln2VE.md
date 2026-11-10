# AlphaSAGE: Structure-Aware Alpha Mining via GFlowNets for Robust Exploration

ICLR 2026 · main · core

以金融任务或金融数据为核心研究对象。 主题：Alpha Mining / 量化因子挖掘。

- 官方论文页：https://openreview.net/forum?id=zRKF4ln2VE
- 摘要来源：https://iclr.cc/virtual/2026/poster/10006456
- 本地 PDF：[打开](../../pdfs/ICLR/2026/iclr-2026-zRKF4ln2VE__AlphaSAGE_Structure_Aware_Alpha_Mining_via_GFlowNets_for_Robust_Exploration.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_review
- 主方向：Alpha Mining / 量化因子挖掘
- 细分方向：Alpha Discovery / Alpha与因子发现
- 技术方法标签：Reinforcement Learning / 强化学习；Graph Learning / 图学习；Generative Modeling / 生成建模；Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Reinforcement Learning
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

The automated mining of predictive signals, or alphas, is a central challenge in quantitative finance. / Third, the standard RL objective of maximizing expected returns inherently drives policies towards a single optimal mode, directly contradicting the practical need for a diverse portfolio of non-correlated alphas. / Empirical results demonstrate that AlphaSAGE outperforms existing baselines in mining a more diverse, novel, and highly predictive portfolio of alphas, thereby proposing a new paradigm for automated alpha mining.

## 原始摘要

The automated mining of predictive signals, or alphas, is a central challenge in quantitative finance. While Reinforcement Learning (RL) has emerged as a promising paradigm for generating formulaic alphas, existing frameworks are fundamentally hampered by a triad of interconnected issues. First, they suffer from reward sparsity, where meaningful feedback is only available upon the completion of a full formula, leading to inefficient and unstable exploration. Second, they rely on semantically inadequate sequential representations of mathematical expressions, failing to capture the structure that determine an alpha's behavior. Third, the standard RL objective of maximizing expected returns inherently drives policies towards a single optimal mode, directly contradicting the practical need for a diverse portfolio of non-correlated alphas. To overcome these challenges, we introduce **AlphaSAGE** (**S**tructure-**A**ware Alpha Mining via **G**enerative Flow Networks for Robust **E**xploration), a novel framework is built upon three cornerstone innovations: (1) a structure-aware encoder based on Relational Graph Convolutional Network (RGCN); (2) a new framework with Generative Flow Networks (GFlowNets); and (3) a dense, multi-faceted reward structure. Empirical results demonstrate that AlphaSAGE outperforms existing baselines in mining a more diverse, novel, and highly predictive portfolio of alphas, thereby proposing a new paradigm for automated alpha mining. Our code is available at https://anonymous.4open.science/r/AlphaSAGE-3BA9.
