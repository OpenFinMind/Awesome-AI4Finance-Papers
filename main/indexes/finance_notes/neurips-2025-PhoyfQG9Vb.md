# Performative Validity of Recourse Explanations

NeurIPS 2025 · main · application

正文包含金融数据、金融训练数据、金融任务评测或具体金融场景案例。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=PhoyfQG9Vb
- 摘要来源：https://neurips.cc/virtual/2025/poster/118195
- 本地 PDF：[打开](../../pdfs/NeurIPS/2025/neurips-2025-PhoyfQG9Vb__Performative_Validity_of_Recourse_Explanations.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Credit Scoring & Default / 信用评分与违约
- 技术方法标签：Causal Learning / 因果学习；Fairness & Recourse / 公平性与算法追索
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：causal
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

distributions, we rely on discrete noise distributions with finite support. In addition, we include two real-world settings: College admission (GPA) and credit scoring (Credit). For GPA we assume the causal graph in [Harris et al., 2022] and fit a linear SCM with additive Gaussian noise on the dataset [OpenIntro, 2020]; For Credit we rely on the graph by Chen et al. [2023] and fit a random-forest based, nonlinear SCM with additive Gaussian noise [Yeh, 2009]. The Cred setting has eleven features; all others include one cause and one effect variable. To highlight the differences between methods, we choose the costs such that interventions on effects are more lucrative. Consequently, CE and CR intervene on the effect, while ICR only int

## 原始摘要

When applicants get rejected by a high-stakes algorithmic decision system, recourse explanations provide actionable suggestions for applicants on how to change their input features to get a positive evaluation. A crucial yet overlooked phenomenon is that recourse explanations are *performative*: When many applicants act according to their recommendations, their collective behavior may shift the data distribution and, once the model is refitted, also the decision boundary. Consequently, the recourse algorithm may render its own recommendations *invalid*, such that applicants who make the effort of implementing their recommendations may be rejected again when they reapply. In this work, we formally characterize the conditions under which recourse explanations remain valid under their own performative effects. In particular, we prove that recourse actions may become invalid if they are influenced by or if they intervene on non-causal variables. Based on this analysis, we caution against the use of standard counterfactual explanations and causal recourse methods, and instead advocate for recourse methods that recommend actions exclusively on causal variables.
