# MCP-SafetyBench: A Benchmark for Safety Evaluation of Large Language Models with Real-World MCP Servers

ICLR 2026 · main · application

通用方法在金融任务、数据或明确案例上开展应用验证。 主题：Financial IR & RAG / 金融检索与RAG。

- 官方论文页：https://openreview.net/forum?id=7XYjeL46co
- 摘要来源：https://iclr.cc/virtual/2026/poster/10011290
- 本地 PDF：[打开](../../pdfs/ICLR/2026/iclr-2026-7XYjeL46co__MCP_SafetyBench_A_Benchmark_for_Safety_Evaluation_of_Large_Language_Models_with_Real_World_MCP_Servers.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_review
- 主方向：Financial IR & RAG / 金融检索与RAG
- 细分方向：Retrieval, Embedding & Reranking / 检索、嵌入与重排
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：language models；LLMs
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/xjzzzzzzzz/MCPSafety.

## 纳入依据

We present **MCP-SafetyBench**, a comprehensive benchmark built on real MCP servers that supports realistic multi-turn evaluation across five domains—browser automation, financial analysis, location navigation, repository management, and web search.

## 原始摘要

Large language models (LLMs) are evolving into agentic systems that reason, plan, and operate external tools.  The Model Context Protocol (MCP) is a key enabler of this transition, offering a standardized interface for connecting LLMs with heterogeneous tools and services.  Yet MCP's openness and multi-server workflows introduce new safety risks that existing benchmarks fail to capture, as they focus on isolated attacks or lack real-world coverage.  We present **MCP-SafetyBench**, a comprehensive benchmark built on real MCP servers that supports realistic multi-turn evaluation across five domains—browser automation, financial analysis, location navigation, repository management, and web search.  It incorporates a unified taxonomy of 20 MCP attack types spanning server, host, and user sides, and includes tasks requiring multi-step reasoning and cross-server coordination under uncertainty.  Using MCP-SafetyBench, we systematically evaluate leading open- and closed-source LLMs, revealing that all models remain vulnerable to MCP attacks, with a notable safety-utility trade-off.  Our results highlight the urgent need for stronger defenses and establish MCP-SafetyBench as a foundation for diagnosing and mitigating safety risks in real-world MCP deployments. Our benchmark is available at https://github.com/xjzzzzzzzz/MCPSafety.
