# GAPrune: Gradient-Alignment Pruning for Domain-Aware Embeddings

ICLR 2026 · main · application

通用方法在金融任务、数据或明确案例上开展应用验证。 主题：Financial IR & RAG / 金融检索与RAG；Financial Agents / 金融Agent与决策。

- 官方论文页：https://openreview.net/forum?id=GLELajHnCo
- 摘要来源：https://iclr.cc/virtual/2026/poster/10010504
- 本地 PDF：[打开](../../pdfs/ICLR/2026/iclr-2026-GLELajHnCo__GAPrune_Gradient_Alignment_Pruning_for_Domain_Aware_Embeddings.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_review
- 主方向：Financial IR & RAG / 金融检索与RAG
- 细分方向：Retrieval, Embedding & Reranking / 检索、嵌入与重排；Investment & Financial Research Agents / 投研与金融决策Agent
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Retrieval & RAG / 检索与RAG；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：LLMs；retrieval
- 数据 / 评测名称（题名和摘要可确认）：FinMTEB
- 代码链接：摘要未提供可确认链接

## 纳入依据

Domain-specific embedding models have shown promise for applications that require specialized semantic understanding, such as coding agents and financial retrieval systems, often achieving higher performance gains than general models.

## 原始摘要

Domain-specific embedding models have shown promise for applications that require specialized semantic understanding, such as coding agents and financial retrieval systems, often achieving higher performance gains than general models. However, state-of-the-art embedding models are typically based on LLMs, which contain billions of parameters, making deployment challenging in resource-constrained environments. Model compression through pruning offers a promising solution, but existing pruning methods treat all parameters uniformly, failing to distinguish between general semantic representations and domain-specific patterns, leading to suboptimal pruning decisions. Thus, we propose GAPrune, a pruning framework that addresses this challenge by considering both domain importance and preserving general linguistic foundation. Our method uses Fisher Information to measure importance and general-domain gradient alignment to assess parameter behavior, then combines these signals using our Domain Alignment Importance (DAI) scoring. Lower DAI scores indicate that the parameter is either less important for the domain task or creates conflicts between domain and general objectives. Experiments on two domain benchmarks, FinMTEB and ChemTEB, show that GAPrune maintains performance within 2.5\% of dense models in one-shot pruning at 50\% sparsity, while outperforming all baselines. With retraining in 100 steps, GAPrune achieves +4.51\% improvement on FinMTEB and +1.73\% on ChemTEB, demonstrating that our pruning strategy not only preserves but enhances domain-specific capabilities. Our findings demonstrate that principled pruning strategies can achieve model compression and enhanced domain specialization, providing the research community with a new approach for development.
