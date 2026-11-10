# Adapting Large Language Models via Reading Comprehension

ICLR 2024 · main · application

通用方法在金融任务、数据或明确案例上开展应用验证。 主题：Financial Models & Benchmarks / 金融模型与评测资源。

- 官方论文页：https://openreview.net/forum?id=y886UXPEZ0
- 摘要来源：https://iclr.cc/virtual/2024/poster/17426
- PDF 状态：access_blocked
- 金融依据类型：title_abstract_review
- 主方向：Financial Models & Benchmarks / 金融模型与评测资源
- 细分方向：Cross-Task Financial Evaluation / 跨任务金融综合评测
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：language model；language models
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/microsoft/LMOps.

## 纳入依据

Our method, highly scalable and applicable to any pre-training corpora, consistently enhances performance across various tasks in three different domains: biomedicine, finance, and law.

## 原始摘要

We explore how continued pre-training on domain-specific corpora influences large language models, revealing that training on the raw corpora endows the model with domain knowledge, but drastically hurts its prompting ability for question answering. Taken inspiration from human learning via reading comprehension--practice after reading improves the ability to answer questions based on the learned knowledge--we propose a simple method for transforming raw corpora into reading comprehension texts. Each raw text is enriched with a series of tasks related to its content. Our method, highly scalable and applicable to any pre-training corpora, consistently enhances performance across various tasks in three different domains: biomedicine, finance, and law. Notably, our 7B language model achieves competitive performance with domain-specific models of much larger scales, such as BloombergGPT-50B. Furthermore, we demonstrate that domain-specific reading comprehension texts can improve the model's performance even on general benchmarks, showing the potential to develop a general model across even more domains. Our model, code, and data are available at https://github.com/microsoft/LMOps.
