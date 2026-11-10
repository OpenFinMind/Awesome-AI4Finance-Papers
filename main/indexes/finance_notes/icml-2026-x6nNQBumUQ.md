# Towards Professional-Grade Financial Agents: Benchmarking, Tooling, and Structured Reasoning

ICML 2026 · main · core

以金融任务或金融数据为核心研究对象。 主题：Financial Agents / 金融Agent与决策；Financial Models & Benchmarks / 金融模型与评测资源。

- 官方论文页：https://openreview.net/forum?id=x6nNQBumUQ
- 摘要来源：https://icml.cc/virtual/2026/poster/60732
- PDF 状态：access_blocked
- 金融依据类型：title_abstract_review
- 主方向：Financial Agents / 金融Agent与决策
- 细分方向：Investment & Financial Research Agents / 投研与金融决策Agent；Financial Tools & Deep Research / 金融工具与深度研究；Cross-Task Financial Evaluation / 跨任务金融综合评测
- 技术方法标签：Language Models & LLM / 语言模型与LLM
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Language Model；LLM
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/tsinghua-fib-lab/ProFinAgent.

## 纳入依据

While Large Language Model (LLM) agents have shown encouraging progress in financial reasoning, their effectiveness in realistic financial workflows is severely hindered by the lack of holistic benchmarks and the fragility of unstructured reasoning. / To address this gap, we introduce ProFinR, the first Professional Finance Reasoning benchmark, covering four financial domain tasks and comprising 528 expert-designed problems. / To solve these complex financial reasoning questions, we construct the Financial Tool Universe, a tool library containing 53 domain-specific tools organized into 13 categories.

## 原始摘要

While Large Language Model (LLM) agents have shown encouraging progress in financial reasoning, their effectiveness in realistic financial workflows is severely hindered by the lack of holistic benchmarks and the fragility of unstructured reasoning. To address this gap, we introduce ProFinR, the first Professional Finance Reasoning benchmark, covering four financial domain tasks and comprising 528 expert-designed problems. To solve these complex financial reasoning questions, we construct the Financial Tool Universe, a tool library containing 53 domain-specific tools organized into 13 categories. Building on the tool library, we introduce ProFinAgent, a structured agent framework based on Directed Acyclic Graph (DAG) and Case-Based Memory (CBM). Compared with strictly sequential workflows, ProFinAgent coordinates tool execution through a DAG planner for parallel efficiency and uses CBM to retrieve prior cases for more reliable decision-making. Experimental results demonstrate that ProFinAgent achieves a 49.81% performance gain over state-of-the-art baselines with a 47.1% reduction in inference latency. Our code is available at https://github.com/tsinghua-fib-lab/ProFinAgent.
