# Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models

ICLR 2026 · main · core

以金融任务或金融数据为核心研究对象。 主题：Financial Agents / 金融Agent与决策；Financial Models & Benchmarks / 金融模型与评测资源。

- 官方论文页：https://openreview.net/forum?id=eC4ygDs02R
- 摘要来源：https://iclr.cc/virtual/2026/poster/10008343
- 本地 PDF：[打开](../../pdfs/ICLR/2026/iclr-2026-eC4ygDs02R__Agentic_Context_Engineering_Evolving_Contexts_for_Self_Improving_Language_Models.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_review
- 主方向：Financial Agents / 金融Agent与决策
- 细分方向：Investment & Financial Research Agents / 投研与金融决策Agent；Financial Pretraining & Adaptation / 金融预训练与领域适配
- 技术方法标签：Language Models & LLM / 语言模型与LLM
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：language model；LLM
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Across agent and domain-specific benchmarks, ACE optimizes contexts both offline (e.g., system prompts) and online (e.g., agent memory), consistently outperforming strong baselines: +10.6\% on agents and +8.6\% on finance, while significantly reducing adaptation latency and rollout cost.

## 原始摘要

Large language model (LLM) applications such as agents and domain-specific reasoning increasingly rely on *context adaptation*: modifying inputs with instructions, strategies, or evidence, rather than weight updates.  Prior approaches improve usability but often suffer from brevity bias, which drops domain insights for concise summaries, and from context collapse, where iterative rewriting erodes details over time.  We introduce ACE (**A**gentic **C**ontext **E**ngineering), a framework that treats contexts as evolving playbooks that accumulate, refine, and organize strategies through a modular process of generation, reflection, and curation.  ACE prevents collapse with structured, incremental updates that preserve detailed knowledge and scale with long-context models. Across agent and domain-specific benchmarks, ACE optimizes contexts both offline (e.g., system prompts) and online (e.g., agent memory), consistently outperforming strong baselines: +10.6\% on agents and +8.6\% on finance, while significantly reducing adaptation latency and rollout cost.  Notably, ACE could adapt effectively without labeled supervision and instead by leveraging natural execution feedback.  On the AppWorld leaderboard, ACE matches the top-ranked production-level agent on the overall average and surpasses it on the harder test-challenge split, despite using a smaller open-source model. These results show that comprehensive, evolving contexts enable scalable, efficient, and self-improving LLM systems with low overhead.
