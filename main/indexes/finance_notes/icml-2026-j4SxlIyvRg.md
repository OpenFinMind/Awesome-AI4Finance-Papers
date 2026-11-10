# Evolving Quantitative Reasoning through Self-Play in Digital Twin Markets

ICML 2026 · main · core

以金融任务或金融数据为核心研究对象。 主题：Trading & Microstructure / 交易与市场微观结构；Financial Agents / 金融Agent与决策。

- 官方论文页：https://openreview.net/forum?id=j4SxlIyvRg
- 摘要来源：https://icml.cc/virtual/2026/poster/62173
- PDF 状态：access_blocked
- 金融依据类型：title_abstract_review
- 主方向：Trading & Microstructure / 交易与市场微观结构
- 细分方向：Trading & Execution / 交易策略与执行；Investment & Financial Research Agents / 投研与金融决策Agent
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：language models；LLM；LLMs
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/MTMQuantAI/Agent-Trading-Arena.git.

## 纳入依据

All code and data are available at https://github.com/MTMQuantAI/Agent-Trading-Arena.git.

## 原始摘要

Large language models (LLMs) demonstrate strong capabilities in high-level semantic reasoning and strategic planning, making them appealing for complex decision-making tasks; however, their quantitative reasoning remains unreliable despite recent progress in tool-augmented and structured inference. To address this limitation, we decouple reasoning from computation by assigning LLMs to planning, analysis, and result interpretation, while delegating numerical computation and statistical inference to specialized external tools. Rather than being hard-coded, these tools are constructed in a constrained and structured manner during planning as explicit intermediate reasoning artifacts, enabling adaptive and scenario-dependent quantitative reasoning. LLMs iteratively analyze tool outputs under diverse market conditions and leverage performance-based feedback to refine subsequent tool selection and construction, thereby forming a bounded self-evolving loop. We instantiate this process through self-play in a controllable digital twin market, DecoupledMarket, where LLM agents continuously test, compare, and adapt their strategies. By coupling high-level planning with robust quantitative execution, the proposed framework enhances the quantitative reliability of LLM-driven decision-making. All code and data are available at https://github.com/MTMQuantAI/Agent-Trading-Arena.git.
