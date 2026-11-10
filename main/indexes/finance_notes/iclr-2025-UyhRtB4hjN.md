# Decision Tree Induction Through LLMs via Semantically-Aware Evolution

ICLR 2025 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：credit-g。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=UyhRtB4hjN
- 摘要来源：https://iclr.cc/virtual/2025/poster/29435
- 本地 PDF：[打开](../../pdfs/ICLR/2025/iclr-2025-UyhRtB4hjN__Decision_Tree_Induction_Through_LLMs_via_Semantically_Aware_Evolution.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Credit Scoring & Default / 信用评分与违约
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Generative Modeling / 生成建模；Uncertainty & Robustness / 不确定性与鲁棒性；Tabular Learning / 表格学习；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Language Models；LLMs；optimization
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

breast compas credit-g LLEGO 0.67 LLEGO LLEGO 0.700 Mean Pop Fitness

## 原始摘要

Decision trees are a crucial class of models offering robust predictive performance and inherent interpretability across various domains, including healthcare, finance, and logistics. However, current tree induction methods often face limitations such as suboptimal solutions from greedy methods or prohibitive computational costs and limited applicability of exact optimization approaches.To address these challenges, we propose an evolutionary optimization method for decision tree induction based on genetic programming (GP). Our key innovation is the integration of semantic priors and domain-specific knowledge about the search space into the optimization algorithm.To this end, we introduce $\texttt{LLEGO}$, a framework that incorporates semantic priors into genetic search operators through the use of Large Language Models (LLMs), thereby enhancing search efficiency and targeting regions of the search space that yield decision trees with superior generalization performance. This is operationalized through novel genetic operators that work with structured natural language prompts, effectively utilizing LLMs as conditional generative models and sources of semantic knowledge. Specifically, we introduce $\textit{fitness-guided}$ crossover to exploit high-performing regions, and $\textit{diversity-guided}$ mutation for efficient global exploration of the search space. These operators are controlled by corresponding hyperparameters that enable a more nuanced balance between exploration and exploitation across the search space. Empirically, we demonstrate across various benchmarks that $\texttt{LLEGO}$ evolves superior-performing trees compared to existing tree induction methods, and exhibits significantly more efficient search performance compared to conventional GP approaches.
