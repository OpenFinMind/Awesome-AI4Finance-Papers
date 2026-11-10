# LightRetriever: A LLM-based Text Retrieval Architecture with Extremely Faster Query Inference

ICLR 2026 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：FiQA。 主题：Financial IR & RAG / 金融检索与RAG。

- 官方论文页：https://openreview.net/forum?id=vNEY32I8Y8
- 摘要来源：https://iclr.cc/virtual/2026/poster/10006816
- 本地 PDF：[打开](../../pdfs/ICLR/2026/iclr-2026-vNEY32I8Y8__LightRetriever_A_LLM_based_Text_Retrieval_Architecture_with_Extremely_Faster_Query_Inference.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Financial IR & RAG / 金融检索与RAG
- 细分方向：Retrieval, Embedding & Reranking / 检索、嵌入与重排
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Retrieval & RAG / 检索与RAG；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Language Models；LLM；LLMs；retrieval
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

uses the preprocessed fine-tuning data from tDRO (Ma et al., 2025) and Sentence Transformers Training Data. English datasets include Amazon Review (Ni et al., 2019), Eli5 (Fan et al., 2019), FEVER (Thorne et al., 2018), FiQA (Maia et al., 2018), GooAQ (Khashabi et al., 2021), HotpotQA (Yang et al., 2018b), MSMARCO (Nguyen et al., 2016), NFCorpus (Boteva et al., 2016), NPR (Lucas et al., 2023), NQ (Kwiatkowski et al., 2019), PAQ (Lewis et al., 2021), Quora Duplicates (Iyer et al., 2017), S2ORC (Lo et al., 2020), Scifact (Wadden et al., 2020), Specter (Co- han et al., 2

## 原始摘要

Large Language Models (LLMs)-based text retrieval retrieves documents relevant to search queries based on vector similarities. Documents are pre-encoded offline, while queries arrive in real-time, necessitating an efficient online query encoder. Although LLMs significantly enhance retrieval capabilities, serving deeply parameterized LLMs slows down query inference throughput and increases demands for online deployment resources. In this paper, we propose LightRetriever, a novel LLM-based retriever with extremely lightweight query encoders. Our method retains a full-sized LLM for document encoding, but reduces the workload of query encoding to no more than an embedding lookup. Compared to serving a full LLM on an A800 GPU, our method achieves over a thousand times of speedup in query encoding and over 10× increase in end-to-end retrieval throughput. Extensive experiments on large-scale retrieval benchmarks show that LightRetriever generalizes well across diverse tasks, maintaining an average of 95% retrieval performance.
