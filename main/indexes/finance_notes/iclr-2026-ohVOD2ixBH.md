# Human-LLM Collaborative Feature Engineering for Tabular Data

ICLR 2026 · main · application

正文包含金融数据、金融训练数据、金融任务评测或具体金融场景案例。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=ohVOD2ixBH
- 摘要来源：https://iclr.cc/virtual/2026/poster/10007382
- 本地 PDF：[打开](../../pdfs/ICLR/2026/iclr-2026-ohVOD2ixBH__Human_LLM_Collaborative_Feature_Engineering_for_Tabular_Data.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Lending & Credit Data / 借贷与信贷数据应用
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Uncertainty & Robustness / 不确定性与鲁棒性；Tabular Learning / 表格学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：language models；LLM；LLMs
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

%) wine 77.2 77.2 77.6 78.2 78.5 (+1.4%) 78.7 (+2.3%) 81.3 81.0 80.9 82.1 82.9 (+4.5%) 83.3 (+6.7%) loan 95.3 95.4 95.7 95.9 96.0 (+2.4%) 96.1 (+4.9%) 96.2 96.0 96.1 96.5 96.9 (+11.4%) 97.1 (+17.1%) diabetes 81.1 82.4 82.8 82.8 83.0 (+1.2%) 83.0 (+1.2%) 84.1 83.9 83.9 84.4 85.2 (+5.1%) 84.8 (+2.6%) titanic 84.1 84.3 86.3 86.5 86.8 (+2.2%) 87.0 (+3.7%) 85.0 84.8 87.0 87.4 87.9 (+4.0%) 88.3 (+7.1%) travel 80.4 80.3 81.1 81.7 82.0 (+1.6%) 82.3 (+3.3%) 83.6 83.2 83.6 84.6 85.3 (+4.5%) 85.7 (+7.1%) ai usage 67.8 67.5 68.2 68.0 68.5 (+0.9%) 68.3 (+0.3%) 71.8 71.5 71.3 72.4 73.3 (+3.3%) 73.8 (+5.1%) water 53.7 53.2 56.7 57.9 58.7 (+1.9%) 59.3 (+3.3%) 56.7 56.1 59.8 61.7 63.2 (+3.9%) 64.1 (+6.3%) heart 92.2 92.3 92.6 93.1 93.4

## 原始摘要

Large language models (LLMs) are increasingly used to automate feature engineering in tabular learning. Given task-specific information, LLMs can propose diverse feature transformation operations to enhance downstream model performance. However, current approaches typically assign the LLM as a black-box optimizer, responsible for both proposing and selecting operations based solely on its internal heuristics, which often lack calibrated estimations of operation utility and consequently lead to repeated exploration of low-yield operations without a principled strategy for prioritizing promising directions. In this paper, we propose a human–LLM collaborative feature engineering framework for tabular learning. We begin by decoupling the transformation operation proposal and selection processes, where LLMs are used solely to generate operation candidates, while the selection is guided by explicitly modeling the utility and uncertainty of each proposed operation. Since accurate utility estimation can be difficult especially in the early rounds of feature engineering, we design a mechanism within the framework that selectively elicits and incorporates human expert preference feedback—comparing which operations are more promising—into the selection process to help identify more effective operations. Our evaluations on both the synthetic study and the real user study demonstrate that the proposed framework improves feature engineering performance across a variety of tabular datasets and reduces users’ cognitive load during the feature engineering process.
