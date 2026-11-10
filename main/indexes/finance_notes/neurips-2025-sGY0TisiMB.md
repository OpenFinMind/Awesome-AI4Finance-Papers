# Individual Fairness In Strategic Classification

NeurIPS 2025 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：FICO。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=sGY0TisiMB
- 摘要来源：https://neurips.cc/virtual/2025/poster/115707
- 本地 PDF：[打开](../../pdfs/NeurIPS/2025/neurips-2025-sGY0TisiMB__Individual_Fairness_In_Strategic_Classification.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Credit Scoring & Default / 信用评分与违约
- 技术方法标签：Fairness & Recourse / 公平性与算法追索
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

7 6 Experiment Dataset and Implementation. In this section, we conduct experiments on two real-world datasets to evaluate the effectiveness of our proposed methods. The first dataset is the FICO dataset, pre- processed by [15]. This dataset provides the cumulative distribution of credit scores across different racial groups. In our experiments, we generate 5,000 data points according to the distributions for the racial groups Black and Non-Hispanic White. Each feature vector is defined as x := [κ, a], where κ denotes the credit score and

## 原始摘要

Strategic classification, where individuals modify their features to influence machine learning (ML) decisions, presents critical fairness challenges. While group fairness in this setting has been widely studied, individual fairness remains underexplored. We analyze threshold-based classifiers and prove that deterministic thresholds violate individual fairness. Then, we investigate the possibility of using a randomized classifier to achieve individual fairness. We introduce conditions under which a randomized classifier ensures individual fairness and leverage these conditions to find an optimal and individually fair randomized classifier through a linear programming problem. Additionally, we demonstrate that our approach can be extended to group fairness notions. Experiments on real-world datasets confirm that our method effectively mitigates unfairness and improves the fairness-accuracy trade-off.
