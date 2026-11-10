# AceSearcher: Bootstrapping Reasoning and Search for LLMs via Reinforced Self-Play

NeurIPS 2025 · main · application

包含明确的金融任务、金融领域数据或金融案例验证。 主题：Financial IR & RAG / 金融检索与RAG。

- 官方论文页：https://openreview.net/forum?id=jSgCM0uZn3
- 摘要来源：https://neurips.cc/virtual/2025/poster/116458
- 本地 PDF：[打开](../../pdfs/NeurIPS/2025/neurips-2025-jSgCM0uZn3__AceSearcher_Bootstrapping_Reasoning_and_Search_for_LLMs_via_Reinforced_Self_Play.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_financial_task_or_data
- 主方向：Financial IR & RAG / 金融检索与RAG
- 细分方向：Financial RAG & Long Documents / 金融RAG与长文档
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Retrieval & RAG / 检索与RAG
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：fine-tuning；language model；LLM；LLMs；retrieval
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Remarkably, on document-level finance reasoning tasks, AceSearcher-32B matches the performance of the giant DeepSeek-V3 model using less than 5% of iits parameters.

## 原始摘要

Search-augmented LLMs often struggle with complex reasoning tasks due to ineffective multi-hop retrieval and limited reasoning ability. We propose AceSearcher, a cooperative self-play framework that trains a single large language model (LLM) to alternate between two roles: a decomposer that breaks down complex queries and a solver that integrates retrieved contexts for answer generation. AceSearcher couples supervised fine-tuning on a diverse mixture of search, reasoning, and decomposition tasks with reinforcement fine-tuning optimized for final answer accuracy, eliminating the need for intermediate annotations. Extensive experiments on three reasoning-intensive tasks across 10 datasets show that AceSearcher outperforms state-of-the-art baselines, achieving an average exact match improvement of 7.6%. Remarkably, on document-level finance reasoning tasks, AceSearcher-32B matches the performance of the giant DeepSeek-V3 model using less than 5% of iits parameters. Even at smaller scales (1.5B and 8B), AceSearcher often surpasses existing search-augmented LLMs with up to 9× more parameters, highlighting its exceptional efficiency and effectiveness in tackling complex reasoning tasks.
