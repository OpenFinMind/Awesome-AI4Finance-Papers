# SV-RAG: LoRA-Contextualizing Adaptation of  MLLMs for Long Document Understanding

ICLR 2025 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：Tat-qa。 主题：Financial QA & Reasoning / 金融问答与数值推理。

- 官方论文页：https://openreview.net/forum?id=FDaHjwInXO
- 摘要来源：https://iclr.cc/virtual/2025/poster/32102
- 本地 PDF：[打开](../../pdfs/ICLR/2025/iclr-2025-FDaHjwInXO__SV_RAG_LoRA_Contextualizing_Adaptation_of_MLLMs_for_Long_Document_Understanding.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Financial QA & Reasoning / 金融问答与数值推理
- 细分方向：Numerical & Table Reasoning / 数值与表格推理
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Retrieval & RAG / 检索与RAG
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：language models；RAG；retrieval
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

et We train our Col-retrieval modules using the original training data of ColPali (Faysse et al., 2024), which includes 39,463, 10,074, 13,251, 10,000, and 45,940 question-page pairs filtered from DocVQA, InfoVQA (Mathew et al., 2022), TATDQA (Zhu et al., 2024), arXivQA (Li et al., 2024), and synthetic data across various topics, including government reports, healthcare, artificial intelligence, and energy. We incorporated DocMatix-IR (Ma et al., 2024b) and PFL- DocVQA (Tito et al., 2023b), using GPT-4o to filter out duplicate images and unsuitable questions. The expanded dataset improved top-1 retrieval accuracy on MMLongBench-Doc by ∼1% without affecting other benchmarks. We fine-tuned our QA modules using the trai

## 原始摘要

Multimodal large language models (MLLMs) have recently shown great progress in text-rich image understanding, yet they still struggle with complex, multi-page visually-rich documents. Traditional methods using document parsers for retrieval-augmented generation suffer from performance and efficiency limitations, while directly presenting all pages to MLLMs leads to inefficiencies, especially with lengthy ones.  In this work, we present a novel framework named **S**elf-**V**isual **R**etrieval-**A**ugmented **G**eneration (SV-RAG), which can broaden horizons of *any* MLLM to support long-document understanding. We demonstrate that **MLLMs themselves can be an effective multimodal retriever** to fetch relevant pages and then answer user questions based on these pages. SV-RAG is implemented with two specific MLLM adapters, one for evidence page retrieval and the other for question answering. Empirical results show state-of-the-art performance on public benchmarks, demonstrating the effectiveness of SV-RAG.
