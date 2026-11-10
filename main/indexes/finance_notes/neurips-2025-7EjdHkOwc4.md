# PANGEA: Projection-Based Augmentation with Non-Relevant General Data for Enhanced Domain Adaptation in LLMs

NeurIPS 2025 · main · application

通用方法在金融任务、数据或明确案例上开展应用验证。 主题：Financial QA & Reasoning / 金融问答与数值推理。

- 官方论文页：https://openreview.net/forum?id=7EjdHkOwc4
- 摘要来源：https://neurips.cc/virtual/2025/poster/119724
- PDF 状态：access_blocked
- 金融依据类型：title_abstract_review
- 主方向：Financial QA & Reasoning / 金融问答与数值推理
- 细分方向：Numerical & Table Reasoning / 数值与表格推理
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Generative Modeling / 生成建模
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：fine-tuning；language models；LLMs
- 数据 / 评测名称（题名和摘要可确认）：FinQA
- 代码链接：摘要未提供可确认链接

## 纳入依据

Our extensive experiments on domain-specific benchmarks, including GSM8K, MedQA, and FinQA, as well as a custom domain-specific language task, validate the effectiveness of our approach.

## 原始摘要

Modern large language models (LLMs) achieve competitive performance across a wide range of natural language processing tasks through zero-shot or few-shot prompting. However, domain-specific tasks often still require fine-tuning, which is frequently hindered by data scarcity, i.e., collecting sufficient domain-specific data remains a practical challenge. A widely adopted solution is to generate synthetic data using LLMs by augmenting a small set of available domain-specific examples. In this work, we first identify fundamental limitations of such approach in terms of both data diversity and quality, particularly when relying on only a handful of domain-specific examples. We then propose our method, PANGEA, which leverages large-scale, publicly available general-purpose data---entirely unrelated to the target domain---to generate more diverse and higher-quality synthetic data. Our extensive experiments on domain-specific benchmarks, including GSM8K, MedQA, and FinQA, as well as a custom domain-specific language task, validate the effectiveness of our approach.
