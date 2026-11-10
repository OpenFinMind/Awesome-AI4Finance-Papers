# LaRA: Benchmarking Retrieval-Augmented Generation and Long-Context LLMs – No Silver Bullet for LC or RAG Routing

ICML 2025 · main · application

正文包含金融数据、金融任务或金融领域评测。 主题：Financial IR & RAG / 金融检索与RAG。

- 官方论文页：https://openreview.net/forum?id=CLF25dahgA
- 摘要来源：https://icml.cc/virtual/2025/poster/46069
- 本地 PDF：[打开](../../pdfs/ICML/2025/icml-2025-CLF25dahgA__LaRA_Benchmarking_Retrieval_Augmented_Generation_and_Long_Context_LLMs_No_Silver_Bullet_for_LC_or_RAG_Rou.pdf)；版本：publisher_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Financial IR & RAG / 金融检索与RAG
- 细分方向：Retrieval, Embedding & Reranking / 检索、嵌入与重排
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Retrieval & RAG / 检索与RAG
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Language Model；LLM；LLMs；RAG；retrieval；Retrieval
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/Alibaba-NLP/LaRA

## 纳入依据

reflect real-world information needs. 2. Revisiting RAG vs. Long Context Specifically, LaRA includes three of the most common types Benchmarks of long contexts—novels, academic papers, and financial Desipte a lot of benchmarks has been used to compare statements—selected to represent diverse writing styles and RAG with feeding lanuage model with long context, there information densities. LaRA features four types of question- lacks a clear guidelines and conclusion on when and where answering tasks designed to ass

## 原始摘要

As Large Language Model (LLM) context windows expand, the necessity of Retrieval-Augmented Generation (RAG) for integrating external knowledge is debated. Existing RAG vs. long-context (LC) LLM comparisons are often inconclusive due to benchmark limitations. We introduce LaRA, a novel benchmark with 2326 test cases across four QA tasks and three long context types, for rigorous evaluation. Our analysis of eleven LLMs reveals the optimal choice between RAG and LC depends on a complex interplay of model capabilities, context length, task type, and retrieval characteristics, offering actionable guidelines for practitioners. Our code and dataset is provided at:https://github.com/Alibaba-NLP/LaRA
