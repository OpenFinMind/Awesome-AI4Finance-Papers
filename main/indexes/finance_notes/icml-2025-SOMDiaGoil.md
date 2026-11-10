# On the Vulnerability of Applying Retrieval-Augmented Generation within Knowledge-Intensive Application Domains

ICML 2025 · main · application

通用方法在金融任务、数据或明确案例上开展应用验证。 主题：Financial IR & RAG / 金融检索与RAG。

- 官方论文页：https://openreview.net/forum?id=SOMDiaGoil
- 摘要来源：https://icml.cc/virtual/2025/poster/45226
- 本地 PDF：[打开](../../pdfs/ICML/2025/icml-2025-SOMDiaGoil__On_the_Vulnerability_of_Applying_Retrieval_Augmented_Generation_within_Knowledge_Intensive_Application_Do.pdf)；版本：publisher_version
- 金融依据类型：title_abstract_review
- 主方向：Financial IR & RAG / 金融检索与RAG
- 细分方向：Retrieval, Embedding & Reranking / 检索、嵌入与重排
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Uncertainty & Robustness / 不确定性与鲁棒性；Retrieval & RAG / 检索与RAG；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：language models；LLMs；RAG；retrieval；Retrieval
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Retrieval-Augmented Generation (RAG) has been empirically shown to enhance the performance of large language models (LLMs) in knowledge-intensive domains such as healthcare, finance, and legal contexts.

## 原始摘要

Retrieval-Augmented Generation (RAG) has been empirically shown to enhance the performance of large language models (LLMs) in knowledge-intensive domains such as healthcare, finance, and legal contexts. Given a query, RAG retrieves relevant documents from a corpus and integrates them into the LLMs’ generation process. In this study, we investigate the adversarial robustness of RAG, focusing specifically on examining the retrieval system. First, across 225 different setup combinations of corpus, retriever, query, and targeted information, we show that retrieval systems are vulnerable to universal poisoning attacks in medical Q&A. In such attacks, adversaries generate poisoned documents containing a broad spectrum of targeted information, such as personally identifiable information. When these poisoned documents are inserted into a corpus, they can be accurately retrieved by any users, as long as attacker-specified queries are used. To understand this vulnerability, we discovered that the deviation from the query’s embedding to that of the poisoned document tends to follow a pattern in which the high similarity between the poisoned document and the query is retained, thereby enabling precise retrieval. Based on these findings, we develop a new detection-based defense to ensure the safe use of RAG. Through extensive experiments spanning various Q&A domains, we observed that our proposed method consistently achieves excellent detection rates in nearly all cases.
