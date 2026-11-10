# GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning

ICLR 2026 · main · application

正文包含金融场景的案例或形式化分析。 主题：Financial Models & Benchmarks / 金融模型与评测资源。

- 官方论文页：https://openreview.net/forum?id=RQm2KQTM5r
- 摘要来源：https://iclr.cc/virtual/2026/poster/10009493
- 本地 PDF：[打开](../../pdfs/ICLR/2026/iclr-2026-RQm2KQTM5r__GEPA_Reflective_Prompt_Evolution_Can_Outperform_Reinforcement_Learning.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_case_or_formal_model
- 主方向：Financial Models & Benchmarks / 金融模型与评测资源
- 细分方向：Financial Pretraining & Adaptation / 金融预训练与领域适配
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Reinforcement Learning / 强化学习；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：language models；LLM；LLMs；optimization；Optimization；reinforcement learning
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/gepa-ai/gepa.

## 纳入依据

to the claim, followed by a concise summary that clearly states whether the claim is supported or refuted based on the aggregated information. Ensure the reasoning explicitly a data table format that includes stock prices, dividend payouts, and percentage changes over various time intervals such as 5 days, 1 month, year-to-date, 1 year, and 5 years. Outline key indicators that investors typically weigh when making decisions, how to interpret short-term versus long-term performance trends, and suggest strategies or metrics to use when making

## 原始摘要

Large language models (LLMs) are increasingly adapted to downstream tasks via reinforcement learning (RL) methods like Group Relative Policy Optimization (GRPO), which often require thousands of rollouts to learn new tasks. We argue that the interpretable nature of language often provides a much richer learning medium for LLMs, compared to policy gradients derived from sparse, scalar rewards. To test this, we introduce GEPA (Genetic-Pareto), a prompt optimizer that thoroughly incorporates natural language reflection to learn high-level rules from trial and error.     Given any AI system containing one or more LLM prompts, GEPA samples trajectories (e.g., reasoning, tool calls, and tool outputs) and reflects on them in natural language to diagnose problems, propose and test prompt updates, and combine complementary lessons from the Pareto frontier of its own attempts. As a result of GEPA's design, it can often turn even just a few rollouts into a large quality gain.     Across six tasks, GEPA outperforms GRPO by 6 percentage points on average and by up to 19pp, while using up to 35x fewer rollouts. GEPA also outperforms the leading prompt optimizer, MIPROv2, by over 10 percentage points (e.g., +12pp on AIME-2025), and demonstrates promising results as an inference-time search strategy for code optimization. We release our code at https://github.com/gepa-ai/gepa.
