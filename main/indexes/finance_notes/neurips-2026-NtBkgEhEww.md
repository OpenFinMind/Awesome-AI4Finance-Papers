# AgenticOCR: Parsing Only What You Need for Efficient Retrieval-Augmented Generation

NeurIPS 2026 · main · application

正文包含金融数据、金融训练数据、金融任务评测或具体金融场景案例。 主题：Financial IR & RAG / 金融检索与RAG；Document AI / 票据、财报与图表理解。

- 官方论文页：https://openreview.net/forum?id=NtBkgEhEww
- 摘要来源：https://neurips.cc/Downloads/2026
- 本地 PDF：[打开](../../pdfs/NeurIPS/2026/neurips-2026-NtBkgEhEww__AgenticOCR_Parsing_Only_What_You_Need_for_Efficient_Retrieval_Augmented_Generation.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Financial IR & RAG / 金融检索与RAG
- 细分方向：Retrieval, Embedding & Reranking / 检索、嵌入与重排；Financial RAG & Long Documents / 金融RAG与长文档；Charts & Visual Understanding / 金融图表与视觉理解；Report Layout & Structured Extraction / 财报版面与结构提取
- 技术方法标签：Retrieval & RAG / 检索与RAG；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：RAG；retrieval
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

standing. On FinRAGBench-V, the same configuration achieves 78.6 accuracy, outperforming all prior agentic frameworks. This highlights the effectiveness of our query-driven extraction paradigm in dense, visually complex financial documents. Strengths on Text, Layout, and Figure Modalities. AgenticOCR exhibits particularly strong per- formance on text-only (TXT), layout (LAY), and figure (FIG) subsets of MMLongBench-Doc. Our 8B 8 AgenticOCR: Parsing Only What You Need for Efficient Retrieval-Augmented Generation

## 原始摘要

The expansion of retrieval-augmented generation (RAG) into multimodal domains has intensified the challenge for processing complex visual documents, such as financial reports. While page-level chunking and retrieval is a natural starting point, it creates a critical bottleneck: delivering entire pages to the generator introduces excessive extraneous context. This not only overloads the generator's attention mechanism but also dilutes the most salient evidence. Moreover, compressing these information-rich pages into a limited visual token budget further increases the risk of hallucinations. To address this, we introduce AgenticOCR, a dynamic parsing approach that extends optical character recognition (OCR) from a static, full-text process into a query-driven, on-demand extraction system. By autonomously analyzing document layout in a "thinking with images" manner, AgenticOCR identifies and selectively recognizes regions of interest. This approach performs on-demand decompression of visual tokens precisely where needed, effectively decoupling retrieval granularity from rigid page-level chunking. AgenticOCR has the potential to serve as the "third building block" of the visual document RAG stack, operating alongside and enhancing standard Embedding and Reranking modules. Experimental results demonstrate that AgenticOCR improves both the accuracy and efficiency of visual RAG systems with pixel-adaptive per-image token allocation (e.g., Qwen3.5 generator), achieving expert-level performance in long document understanding. Our repository is anonymously available at https://anonymous.4open.science/r/AgenticOCR.
