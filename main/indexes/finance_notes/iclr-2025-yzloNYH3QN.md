# Attention in Large Language Models Yields Efficient Zero-Shot Re-Rankers

ICLR 2025 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：FiQA。 主题：Financial IR & RAG / 金融检索与RAG。

- 官方论文页：https://openreview.net/forum?id=yzloNYH3QN
- 摘要来源：https://iclr.cc/virtual/2025/poster/27696
- 本地 PDF：[打开](../../pdfs/ICLR/2025/iclr-2025-yzloNYH3QN__Attention_in_Large_Language_Models_Yields_Efficient_Zero_Shot_Re_Rankers.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Financial IR & RAG / 金融检索与RAG
- 细分方向：Retrieval, Embedding & Reranking / 检索、嵌入与重排
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Generative Modeling / 生成建模；Uncertainty & Robustness / 不确定性与鲁棒性；Retrieval & RAG / 检索与RAG
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：language models；LLM；LLMs；retrieval
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

n the BEIR benchmark (Thakur et al., 2021), including TREC-COVID (Voorhees et al., 2021), NFCorpus (Boteva et al., 2016),DBPedia-entity (Hasibi et al., 2017), SciFact (Wadden et al., 2020), SciDocs (Cohan et al., 2020), FiQA (Maia et al., 2018), FEVER (Thorne et al., 2018), Climate- FEVER (Diggelmann et al., 2020), and NQ (Kwiatkowski et al., 2019). Following Sun et al. (2023), we re-rank the top 100 documents returned by BM25(Robertson & Zaragoza, 2009) and report nDCG@10. We apply a sliding window of size 20 and stride 10 for RankGPT. For ICR, we directly re-rank al

## 原始摘要

Information retrieval (IR) systems have played a vital role in modern digital life and have cemented their continued usefulness in this new era of generative AI via retrieval-augmented generation. With strong language processing capabilities and remarkable versatility, large language models (LLMs) have become popular choices for zero-shot re-ranking in IR systems. So far, LLM-based re-ranking methods rely on strong generative capabilities, which restricts their use to either specialized or powerful proprietary models. Given these restrictions, we ask: is autoregressive generation necessary and optimal for LLMs to perform re-ranking? We hypothesize that there are abundant signals relevant to re-ranking within LLMs that might not be used to their full potential via generation. To more  directly leverage such signals, we propose in-context re-ranking (ICR), a novel method  that leverages the change in attention pattern caused by the search query for accurate and efficient re-ranking. We assume that more relevant documents should receive more attention weights when an LLM is processing the query tokens, and leverage such signals for re-ranking. To mitigate the intrinsic biases in LLMs, we propose a calibration method using a content-free query. Due to the absence of generation, ICR only requires two ($O(1)$) forward passes to re-rank $N$ documents, making it substantially more efficient than generative re-ranking methods that require at least $O(N)$ forward passes. Our novel design also enables ICR to be applied to any LLM without specialized training while guaranteeing a well-formed ranking. Extensive experiments with two popular open-weight LLMs on standard single-hop and multi-hop information retrieval benchmarks show that ICR outperforms RankGPT while cutting the latency by more than 60% in practice. Through detailed analyses, we show that ICR's performance is specially strong on tasks that require more complex re-ranking signals, such as handling contextualization and contradiction between the query and passages, as well as information integration across multiple passages. Our findings call for further exploration on novel ways of utilizing open-weight LLMs beyond text generation.
