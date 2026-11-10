# AlphaQCM: Alpha Discovery in Finance with Distributional Reinforcement Learning

ICML 2025 · main · core

以金融任务或金融数据为核心研究对象。 主题：Alpha Mining / 量化因子挖掘。

- 官方论文页：https://openreview.net/forum?id=3sXMHlhBSs
- 摘要来源：https://icml.cc/virtual/2025/poster/46517
- 本地 PDF：[打开](../../pdfs/ICML/2025/icml-2025-3sXMHlhBSs__AlphaQCM_Alpha_Discovery_in_Finance_with_Distributional_Reinforcement_Learning.pdf)；版本：publisher_version
- 金融依据类型：title_abstract_review
- 主方向：Alpha Mining / 量化因子挖掘
- 细分方向：Alpha Discovery / Alpha与因子发现
- 技术方法标签：Reinforcement Learning / 强化学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：reinforcement learning
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

For researchers and practitioners in finance, finding synergistic formulaic alphas is very important but challenging. / Empirical applications to real-world datasets demonstrate that our AlphaQCM method significantly outperforms its competitors, particularly when dealing with large datasets comprising numerous stocks.

## 原始摘要

For researchers and practitioners in finance, finding synergistic formulaic alphas is very important but challenging. In this paper, we reconsider the discovery of synergistic formulaic alphas from the viewpoint of sequential decision-making, and conceptualize the entire alpha discovery process as a non-stationary and reward-sparse Markov decision process. To overcome the challenges of non-stationarity and reward-sparsity, we propose the AlphaQCM method, a novel distributional reinforcement learning method designed to search for synergistic formulaic alphas efficiently. The AlphaQCM method first learns the Q function and quantiles via a Q network and a quantile network, respectively. Then, the AlphaQCM method applies the quantiled conditional moment method to learn unbiased variance from the potentially biased quantiles. Guided by the learned Q function and variance, the AlphaQCM method navigates the non-stationarity and reward-sparsity to explore the vast search space of formulaic alphas with high efficacy. Empirical applications to real-world datasets demonstrate that our AlphaQCM method significantly outperforms its competitors, particularly when dealing with large datasets comprising numerous stocks.
