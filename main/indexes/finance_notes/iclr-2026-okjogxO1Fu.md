# Let LLMs Speak Embedding Languages: Generative Text Embeddings via Iterative Contrastive Refinement

ICLR 2026 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：FiQA。 主题：Financial IR & RAG / 金融检索与RAG。

- 官方论文页：https://openreview.net/forum?id=okjogxO1Fu
- 摘要来源：https://iclr.cc/virtual/2026/poster/10007379
- 本地 PDF：[打开](../../pdfs/ICLR/2026/iclr-2026-okjogxO1Fu__Let_LLMs_Speak_Embedding_Languages_Generative_Text_Embeddings_via_Iterative_Contrastive_Refinement.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Financial IR & RAG / 金融检索与RAG
- 细分方向：Retrieval, Embedding & Reranking / 检索、嵌入与重排
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Generative Modeling / 生成建模；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：contrastive；Contrastive；language model；LLM；LLMs
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

2.14 70.78 68.15 71.44 71.01 69.81 FEVER 95.30 95.18 80.71 96.94 94.38 96.15 94.23 95.41 FiQA 60.50 65.08 68.23 61.46 65.98 68.07 60.79 55.90 HotpotQA 86.16 91.64 82.06 88.14 91.09 91.05 88.10 88.31 MSMARCO 66.58 66.51 70.

## 原始摘要

Existing large language model (LLM)-based embeddings typically adopt an encoder-only paradigm, treating LLMs as static feature extractors and overlooking their core gener- ative strengths. We introduce GIRCSE (Generative Iterative Refinement for Contrastive Sentence Embeddings), a novel framework that leverages autoregressive generation to iter- atively refine semantic representations. By producing sequences of soft tokens optimized under a contrastive objective, GIRCSE captures latent concepts and implicit semantics that encoder-only methods often miss. To guide this process, we propose an Iterative Contrastive Refinement (ICR) objective that encourages each refinement step to yield bet- ter representations. Extensive experiments show that GIRCSE outperforms strong LLM- based embedding baselines on the MTEB embedding benchmark. Moreover, GIRCSE ex- hibits an emergent test-time scaling property: generating more tokens at inference steadily improves embedding quality. Our results establish generative iterative refinement as a new paradigm for representation learning.
