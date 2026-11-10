# Contrastive Retrieval Heads for Improved Attention-Based Reranking

NeurIPS 2026 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：FiQA。 主题：Financial IR & RAG / 金融检索与RAG。

- 官方论文页：https://openreview.net/forum?id=el3L9KxeOE
- 摘要来源：https://neurips.cc/Downloads/2026
- 本地 PDF：[打开](../../pdfs/NeurIPS/2026/neurips-2026-el3L9KxeOE__Contrastive_Retrieval_Heads_for_Improved_Attention_Based_Reranking.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Financial IR & RAG / 金融检索与RAG
- 细分方向：Retrieval, Embedding & Reranking / 检索、嵌入与重排
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Transformer / Transformer模型；Retrieval & RAG / 检索与RAG
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：contrastive；Language Models；LLMs；retrieval；transformer
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

.2 SciDocs 22.5 16.6 17.3 19.5 18.5 19.7 20.2 20.8 20.3 21.6 18.4 20.3 20.0 FiQA 36.9 35.8 40.3 41.4 41.3 44.0 44.1 40.2 41.4 44.0 39.7 41.6 42.4 NQ 51.6 55.4 56.5 58.1 60.8 63.0 63.2 61.5 61.8 64.1

## 原始摘要

The strong zero-shot and long-context capabilities of recent Large Language Models (LLMs) have enabled highly effective list-wise reranking systems. Attention-based rerankers leverage transformer attention patterns as retrieval signals, but not all attention heads contribute equally: many introduce noise and redundancy, limiting both reranking quality and efficiency. In this work, we introduce CoRe heads, a small subset of retrieval-specialized heads identified through a contrastive scoring objective that rewards attention to relevant documents while penalizing attention to distractors. This contrastive criterion isolates highly discriminative retrieval heads and yields a strong training-free list-wise reranker. Our analysis reveals that retrieval-relevant computation in transformer rerankers is highly sparse and structurally localized: fewer than 1% of attention heads account for most reranking performance across models and datasets, and these heads consistently concentrate in middle transformer layers. This localization enables aggressive layer pruning for efficient reranking: removing the final 50% of transformer layers preserves nearly identical reranking accuracy while substantially reducing inference latency and GPU memory usage.
