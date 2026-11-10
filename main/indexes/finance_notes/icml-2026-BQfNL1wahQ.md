# From Similarity to Vulnerability: Key Collision Attack on LLM Semantic Caching

ICML 2026 · main · application

通用方法在金融任务、数据或明确案例上开展应用验证。 主题：Financial Agents / 金融Agent与决策。

- 官方论文页：https://openreview.net/forum?id=BQfNL1wahQ
- 摘要来源：https://icml.cc/virtual/2026/poster/65663
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-BQfNL1wahQ__From_Similarity_to_Vulnerability_Key_Collision_Attack_on_LLM_Semantic_Caching.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_review
- 主方向：Financial Agents / 金融Agent与决策
- 细分方向：Investment & Financial Research Agents / 投研与金融决策Agent
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Uncertainty & Robustness / 不确定性与鲁棒性；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：LLM
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

A case study on a financial agent further illustrates the real-world impact.

## 原始摘要

Semantic caching has emerged as a pivotal technique for scaling LLM applications, widely adopted by providers including AWS and Microsoft. By utilizing embedding vectors as cache keys, this mechanism effectively minimizes latency and redundant computation for semantically similar queries. In this work, we conceptualize semantic cache keys as a form of fuzzy hashes. We demonstrate that the locality required to maximize cache hit rates fundamentally conflicts with the cryptographic avalanche effect necessary for collision resistance.  Our conceptual analysis formalizes this inherent trade-off between performance (locality) and security (collision resilience), revealing that semantic caching is inherently vulnerable to key collision attacks. While prior research has focused on side-channel and privacy risks, we present the first systematic study of integrity risks arising from cache collisions. We introduce CacheAttack, an automated framework for launching black-box collision attacks.  We evaluate CacheAttack in security-critical tasks and agentic workflows. It achieves a hit rate of 86\% in LLM response hijacking and can induce malicious behaviors in LLM agent, while preserving strong transferability across different embedding models.  A case study on a financial agent further illustrates the real-world impact.  Finally, we discuss mitigation strategies, highlighting a persistent trade-off between cache efficiency and robustness.
