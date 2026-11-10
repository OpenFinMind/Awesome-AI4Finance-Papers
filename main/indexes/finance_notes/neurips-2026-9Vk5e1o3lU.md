# BayesRAG: Probabilistic Mutual Evidence Corroboration for Multimodal Retrieval-Augmented Generation

NeurIPS 2026 · main · application

正文包含金融数据、金融训练数据、金融任务评测或具体金融场景案例。 主题：Financial IR & RAG / 金融检索与RAG。

- 官方论文页：https://openreview.net/forum?id=9Vk5e1o3lU
- 摘要来源：https://neurips.cc/virtual/2026/poster/154974
- 本地 PDF：[打开](../../pdfs/NeurIPS/2026/neurips-2026-9Vk5e1o3lU__BayesRAG_Probabilistic_Mutual_Evidence_Corroboration_for_Multimodal_Retrieval_Augmented_Generation.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Financial IR & RAG / 金融检索与RAG
- 细分方向：Retrieval, Embedding & Reranking / 检索、嵌入与重排
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Uncertainty & Robustness / 不确定性与鲁棒性；Multimodal Learning / 多模态学习；Retrieval & RAG / 检索与RAG
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Bayesian；Language Models；LLMs；RAG；retrieval；Retrieval
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

- MMLongBench-Doc (Ma et al., 2024). DocBench rectly feeding PDFs into GPT-4o-mini. For docu- comprises 229 documents across five domains (e.g., ments with fewer than 50 pages, we use page-level Finance, Law) with 1,102 QA pairs, featuring sub- screenshots as input. For longer documents, we stantial length (avg. 66 pages, ∼46k tokens) to randomly sample 50 screenshots as input. test long-context capabilities. MMLongBench-Doc Evaluation Metrics. For DocBench, we stri

## 原始摘要

Retrieval-Augmented Generation (RAG) has become a pivotal paradigm for Large Language Models (LLMs), yet current approaches struggle with visually rich documents by treating text and images as isolated retrieval targets. Existing methods relying solely on cosine similarity often fail to capture the semantic reinforcement provided by cross-modal alignment and layout-induced coherence. To address these limitations, we propose **BayesRAG**, a novel multimodal retrieval framework grounded in Bayesian inference and Dempster-Shafer evidence theory. Unlike traditional approaches that rank candidates strictly by similarity, BayesRAG models the intrinsic consistency of retrieved candidates across modalities as probabilistic evidence to refine retrieval confidence. Specifically, our method computes the posterior association probability for combinations of multimodal retrieval results, prioritizing text-image pairs that mutually corroborate each other in terms of both semantics and layout. Extensive experiments demonstrate that BayesRAG significantly outperforms state-of-the-art (SOTA) methods on challenging multimodal benchmarks. This study establishes a new paradigm for multimodal retrieval fusion that effectively resolves the isolation of heterogeneous modalities through an evidence fusion mechanism and enhances the robustness of retrieval outcomes. Our code is available at https://anonymous.4open.science/r/BayesRAG-4C6B/.
