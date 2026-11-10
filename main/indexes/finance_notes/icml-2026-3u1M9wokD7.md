# ComplexMCP: Evaluation of LLM Agents in Dynamic, Interdependent, and Large-Scale Tool Sandbox

ICML 2026 · main · application

包含明确的金融任务、金融领域数据或金融案例验证。 主题：Financial Agents / 金融Agent与决策。

- 官方论文页：https://openreview.net/forum?id=3u1M9wokD7
- 摘要来源：https://icml.cc/virtual/2026/poster/66421
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-3u1M9wokD7__ComplexMCP_Evaluation_of_LLM_Agents_in_Dynamic_Interdependent_and_Large_Scale_Tool_Sandbox.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_financial_task_or_data
- 主方向：Financial Agents / 金融Agent与决策
- 细分方向：Investment & Financial Research Agents / 投研与金融决策Agent
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Retrieval & RAG / 检索与RAG
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：LLM；LLMs；RAG；retrieval
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/AIDC-AI/complex-mcp.

## 纳入依据

Built on the Model Context Protocol (MCP), $\textbf{ComplexMCP}$ provides over 300 meticulously tested tools derived from 7 stateful sandboxes, ranging from office suites to financial systems.

## 原始摘要

Current LLM agents are proficient at calling isolated APIs but struggle with the "last mile" of commercial software automation. In real-world scenarios, tools are not independent; they are atomic, interdependent, and prone to environmental noise. We introduce $\textbf{ComplexMCP}$, a benchmark designed to evaluate agents in these rigorous conditions. Built on the Model Context Protocol (MCP), $\textbf{ComplexMCP}$ provides over 300 meticulously tested tools derived from 7 stateful sandboxes, ranging from office suites to financial systems. Unlike existing datasets, our benchmark utilizes a seed-driven architecture to simulate dynamic environment states and unpredictable API failures, ensuring a deterministic yet diverse evaluation.  We evaluate various LLMs across full-context and RAG paradigms, revealing a stark performance gap: even top-tier models fail to exceed a 60% success rate, far trailing human performance 90%. Granular trajectory analysis identifies three fundamental bottlenecks: (1) $\textbf{tool retrieval saturation}$ as action spaces scale; (2) $\textbf{over-confidence}$, where agents skip essential environment verifications; and (3) $\textbf{strategic defeatism}$, a tendency to rationalize failure rather than pursuing recovery. These findings underscore the insufficiency of current agents for interdependent workflows, positioning $\textbf{ComplexMCP}$ as a critical testbed for the next generation of resilient autonomous systems. The codebase and benchmark implementation are publicly available at https://github.com/AIDC-AI/complex-mcp.
