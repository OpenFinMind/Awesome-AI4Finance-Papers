# AdaSplash: Adaptive Sparse Flash Attention

ICML 2025 · main · application

正文包含金融领域的数据、模型、任务或独立金融评测。 主题：Financial IR & RAG / 金融检索与RAG。

- 官方论文页：https://openreview.net/forum?id=OWIPDWhUcO
- 摘要来源：https://icml.cc/virtual/2025/oral/47229
- 本地 PDF：[打开](../../pdfs/ICML/2025/icml-2025-OWIPDWhUcO__AdaSplash_Adaptive_Sparse_Flash_Attention.pdf)；版本：publisher_version
- 金融依据类型：fulltext_financial_data_model_or_task
- 主方向：Financial IR & RAG / 金融检索与RAG
- 细分方向：Retrieval, Embedding & Reranking / 检索、嵌入与重排
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Transformer / Transformer模型；Retrieval & RAG / 检索与RAG
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：retrieval；transformers
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

t classification with different sequence lengths. In cases where the full batch could not fit in memory, Model Seq. SciFact NFC FiQA TREC-C gradient accumulation was used. Memory values represent the RoBERTa 512 51.7 23.1 27.8 60.1 effective peak memory required to process a batch of 16 samples. RoBERTa (α = 1.5) 512 50.8 24.2 27.6 71.0 RoBERTa (α = 2.0) 512 52.2 23.8 25.7 65.5

## 原始摘要

The computational cost of softmax-based attention in transformers limits their applicability to long-context tasks. Adaptive sparsity, of which $\alpha$-entmax attention is an example, offers a flexible data-dependent alternative, but existing implementations are inefficient and do not leverage the sparsity to obtain runtime and memory gains. In this work, we propose AdaSplash, which combines the efficiency of GPU-optimized algorithms with the sparsity benefits of $\alpha$-entmax. We first introduce a hybrid Halley-bisection algorithm, resulting in a 7-fold reduction in the number of iterations needed to compute the $\alpha$-entmax transformation. Then, we implement custom Triton kernels to efficiently handle adaptive sparsity. Experiments with RoBERTa and ModernBERT for text classification and single-vector retrieval, along with GPT-2 for language modeling, show that our method achieves substantial improvements in runtime and memory efficiency compared to existing $\alpha$-entmax implementations. It approaches---and in some cases surpasses---the efficiency of highly optimized softmax implementations like FlashAttention-2, enabling long-context training while maintaining strong task performance.
