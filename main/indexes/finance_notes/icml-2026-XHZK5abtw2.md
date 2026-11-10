# $\tau$-Knowledge: Evaluating Conversational Agents over Unstructured Knowledge

ICML 2026 · main · core

以金融任务或金融数据为核心研究对象。 主题：Banking & Customer Service / 银行业务与客户服务。

- 官方论文页：https://openreview.net/forum?id=XHZK5abtw2
- 摘要来源：https://icml.cc/virtual/2026/poster/63427
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-XHZK5abtw2__tau_Knowledge_Evaluating_Conversational_Agents_over_Unstructured_Knowledge.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_review
- 主方向：Banking & Customer Service / 银行业务与客户服务
- 细分方向：Banking Dialogue & Intent / 银行对话与意图
- 技术方法标签：Retrieval & RAG / 检索与RAG；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：retrieval
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Our new domain, $\tau$-Banking, models realistic fintech customer support workflows in which agents must navigate roughly 700 interconnected knowledge documents while executing tool-mediated account updates.

## 原始摘要

Conversational agents are increasingly deployed in knowledge-intensive settings, where correct behavior depends on retrieving and applying domain-specific knowledge from large, proprietary, and unstructured corpora during live interactions with users. Yet most existing benchmarks evaluate retrieval or tool use independently of each other, creating a gap in realistic, fully agentic evaluation over unstructured data in long-horizon interactions. We introduce $\tau$-Knowledge, an extension of $\tau$-Bench for evaluating agents in environments where success depends on coordinating external, natural-language knowledge with tool outputs to produce verifiable, policy-compliant state changes. Our new domain, $\tau$-Banking, models realistic fintech customer support workflows in which agents must navigate roughly 700 interconnected knowledge documents while executing tool-mediated account updates. Across embedding-based retrieval and terminal-based search, even frontier models with high reasoning budgets achieve only $\sim$25.5\% pass^1, with reliability degrading sharply over repeated trials. Agents struggle to retrieve the correct documents from densely interlinked knowledge bases and to reason accurately over complex internal policies. Overall, $\tau$-Knowledge provides a realistic testbed for developing agents that integrate unstructured knowledge in human-facing deployments.
