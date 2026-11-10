# Embedding-Based Context-Aware Reranker

ICLR 2026 · main · application

正文包含金融数据、金融训练数据、金融任务评测或具体金融场景案例。 主题：ESG & Sustainable Finance / ESG与可持续金融。

- 官方论文页：https://openreview.net/forum?id=OBMcxeSK5U
- 摘要来源：https://iclr.cc/virtual/2026/poster/10009807
- 本地 PDF：[打开](../../pdfs/ICLR/2026/iclr-2026-OBMcxeSK5U__Embedding_Based_Context_Aware_Reranker.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：ESG & Sustainable Finance / ESG与可持续金融
- 细分方向：ESG Disclosure & Greenwashing / ESG披露与漂绿
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Retrieval & RAG / 检索与RAG；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：language models；RAG；retrieval；Retrieval
- 数据 / 评测名称（题名和摘要可确认）：finer
- 代码链接：https://github.com/BorealisAI/EBCAR.

## 纳入依据

here relevant information may be scattered across long passages. (iv) COVID-QA (COVID) is a biomedical QA dataset based on scientific research documents, which similarly requires reasoning over long and dense texts. (v) ESG Re- ports are long-form corporate documents sourced from the ViDoRe benchmark, re-annotated for text-based QA to test document-wide contextual understanding capabilities. (vi) Football and (vii) Geography (Geog) are constructed from rephrased Wikipedia summaries in which explicit entity mentions have been replaced by pronouns via GPT-4o. This setu

## 原始摘要

Retrieval-Augmented Generation (RAG) systems rely on retrieving  relevant evidence from a corpus to support downstream generation.  The common practice of splitting a long document into multiple shorter passages enables finer-grained and targeted information retrieval.  However, it also introduces challenges when a correct retrieval would require inference across passages, such as resolving coreference, disambiguating entities, and aggregating evidence scattered across multiple sources. Many state-of-the-art (SOTA) reranking methods, despite utilizing powerful large pretrained language models with potentially high inference costs, still neglect the aforementioned challenges. Therefore, we propose Embedding-Based Context-Aware Reranker (EBCAR), a lightweight reranking framework operating directly on embeddings of retrieved passages with enhanced cross-passage understandings through the structural information of the passages and a hybrid attention mechanism, which captures both high-level interactions across documents and low-level relationships within each document. We evaluate EBCAR against SOTA rerankers on the ConTEB benchmark, demonstrating its effectiveness for information retrieval requiring cross-passage inference and its advantages in both accuracy and efficiency. Our source code is available at https://github.com/BorealisAI/EBCAR.
