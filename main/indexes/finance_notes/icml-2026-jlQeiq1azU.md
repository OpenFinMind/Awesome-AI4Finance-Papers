# When Tabular Foundation Models Meet Strategic Tabular Data: A Prior Alignment Approach

ICML 2026 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：Bank-Marketing。 主题：Banking & Customer Service / 银行业务与客户服务。

- 官方论文页：https://openreview.net/forum?id=jlQeiq1azU
- 摘要来源：https://icml.cc/virtual/2026/poster/62109
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-jlQeiq1azU__When_Tabular_Foundation_Models_Meet_Strategic_Tabular_Data_A_Prior_Alignment_Approach.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Banking & Customer Service / 银行业务与客户服务
- 细分方向：Bank Marketing & Churn / 银行营销与客户流失
- 技术方法标签：Uncertainty & Robustness / 不确定性与鲁棒性；Tabular Learning / 表格学习；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

that do not involve fea- sion rules. Formal definitions and details are included in ture manipulation, such as Bank-Marketing and Phishing. Appendix H.4. Detailed dataset descriptions are provided in Appendix H.1. Methods. We compare the proposed SPN against two broad classes of tabular learning approaches. First, we consider

## 原始摘要

Tabular foundation models based on pretrained prior-data fitted networks (PFNs) have shown strong generalization on diverse tabular tasks, but they are typically designed for non-strategic settings where data distributions are independent of deployed classifiers. In many real-world decision scenarios, however, individuals may strategically modify their features after deployment to obtain favorable outcomes, inducing a post-deployment distribution shift. This paper studies whether PFN-style tabular foundation models can generalize to such strategic tabular data. We show that strategic manipulation creates a fundamental mismatch between the non-strategic prior learned during pretraining and the post-manipulation strategic prior encountered at deployment, which leads to an irreducible structural prediction bias. To address this issue, we propose the Strategic Prior-data Fitted Network (SPN), an inference-time strategy-aware framework that adapts tabular foundation models to strategic environments without retraining or architectural modification. SPN constructs strategic in-context examples to approximate post-manipulation inputs and aligns PFN predictions with the induced strategic distribution via in-context learning, with theoretical guarantees on bias reduction. Experiments on real-world and synthetic tabular datasets show that SPN consistently improves robustness and predictive performance under strategic manipulation compared with both tabular foundation models and classical tabular methods.
