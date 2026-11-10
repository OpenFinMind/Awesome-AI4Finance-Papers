# A General Framework for Producing Interpretable Semantic Text Embeddings

ICLR 2025 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：FiQA。 主题：Financial IR & RAG / 金融检索与RAG。

- 官方论文页：https://openreview.net/forum?id=23uY3FpQxc
- 摘要来源：https://iclr.cc/virtual/2025/poster/31167
- 本地 PDF：[打开](../../pdfs/ICLR/2025/iclr-2025-23uY3FpQxc__A_General_Framework_for_Producing_Interpretable_Semantic_Text_Embeddings.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Financial IR & RAG / 金融检索与RAG
- 细分方向：Retrieval, Embedding & Reranking / 检索、嵌入与重排
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Contrastive；LLM
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/dukesun99/CQG-MBQA}.

## 纳入依据

7 Table 3: Retrieval results evaluated by nDCG@10. Evaluated on seven diverse datasets: MS MARCO (Bajaj et al., 2016), NewsSpectrum (NSP) (Sun et al., 2024), ArguAna (Wachsmuth et al., 2018), FiQA-2018 (FQA) (Maia et al., 2018), NFCorpus (NFC) (Boteva et al., 2016), SCIDOCS (Cohan et al., 2020), and SciFact (Wadden et al., 2020). MS MARCO is evaluated on a 1% sample of its dev set, while NewsSpectrum uses news titles as queries with corresponding articles as targets. The remaining datasets are assessed using the MTEB evaluation suite.

## 原始摘要

Semantic text embedding is essential to many tasks in Natural Language Processing (NLP). While black-box models are capable of generating high-quality embeddings, their lack of interpretability limits their use in tasks that demand transparency. Recent approaches have improved interpretability by leveraging domain-expert-crafted or LLM-generated questions, but these methods rely heavily on expert input or well-prompt design, which restricts their generalizability and ability to generate discriminative questions across a wide range of tasks. To address these challenges, we introduce \algo{CQG-MBQA} (Contrastive Question Generation - Multi-task Binary Question Answering), a general framework for producing interpretable semantic text embeddings across diverse tasks. Our framework systematically generates highly discriminative, low cognitive load yes/no questions through the \algo{CQG} method and answers them efficiently with the \algo{MBQA} model, resulting in interpretable embeddings in a cost-effective manner. We validate the effectiveness and interpretability of \algo{CQG-MBQA} through extensive experiments and ablation studies, demonstrating that it delivers embedding quality comparable to many advanced black-box models while maintaining inherently interpretability. Additionally, \algo{CQG-MBQA} outperforms other interpretable text embedding methods across various downstream tasks. The source code is available at \url{https://github.com/dukesun99/CQG-MBQA}.
