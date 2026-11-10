# Retrieval-based Disentangled Representation Learning with Natural Language Supervision

ICLR 2024 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：FiQA。 主题：Financial IR & RAG / 金融检索与RAG。

- 官方论文页：https://openreview.net/forum?id=ZlQRiFmq7Y
- 摘要来源：https://iclr.cc/virtual/2024/poster/18384
- 本地 PDF：[打开](../../pdfs/ICLR/2024/iclr-2024-ZlQRiFmq7Y__Retrieval_based_Disentangled_Representation_Learning_with_Natural_Language_Supervision.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Financial IR & RAG / 金融检索与RAG
- 细分方向：Retrieval, Embedding & Reranking / 检索、嵌入与重排
- 技术方法标签：Multimodal Learning / 多模态学习；Retrieval & RAG / 检索与RAG；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：retrieval；Retrieval
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

.6 41.3 34.5 39.9 39.0 42.4 41.0 FEVER 75.3 73.0 63.8 74.8 74.0 66.9 69.6 75.8 65.7 69.2 77.4 80.0 58.2 FiQA 23.6 28.7 23.7 29.3 28.8 29.5 31.1 32.9 29.2 32.8 31.6 35.2 36.4 HotpotQA 60.3 63.6 45.2 68.4 65.5 45.6 66.1 63.8 58.1 58.9 63.5 71.6 62.2 NFCorpus 32.5 31.3 26.1

## 原始摘要

Disentangled representation learning remains challenging as the underlying factors of variation in the data do not naturally exist. The inherent complexity of real-world data makes it unfeasible to exhaustively enumerate and encapsulate all its variations within a finite set of factors. However, it is worth noting that most real-world data have linguistic equivalents, typically in the form of textual descriptions. These linguistic counterparts can represent the data and effortlessly decomposed into distinct tokens. In light of this, we present Vocabulary Disentangled Retrieval (VDR), a retrieval-based framework that harnesses natural language as proxies of the underlying data variation to drive disentangled representation learning. Our approach employ a bi-encoder model to represent both data and natural language in a vocabulary space, enabling the model to distinguish dimensions that capture intrinsic characteristics within data through its natural language counterpart, thus facilitating disentanglement. We extensively assess the performance of VDR across 15 retrieval benchmark datasets, covering text-to-text and cross-modal retrieval scenarios, as well as human evaluation. Our experimental results compellingly demonstrate the superiority of VDR over previous bi-encoder retrievers with comparable model size and training costs, achieving an impressive 8.7% improvement in NDCG@10 on the BEIR benchmark, a 5.3\% increase on MS COCO, and a 6.0% increase on Flickr30k in terms of mean recall in the zero-shot setting. Moreover, The results from human evaluation indicate that interpretability of our method is on par with SOTA captioning models.
