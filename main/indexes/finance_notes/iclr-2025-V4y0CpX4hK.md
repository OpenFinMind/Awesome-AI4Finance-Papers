# Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-based Agents

ICLR 2025 · main · application

通用方法在金融任务、数据或明确案例上开展应用验证。 主题：Financial Safety & Compliance / 金融安全与合规。

- 官方论文页：https://openreview.net/forum?id=V4y0CpX4hK
- 摘要来源：https://iclr.cc/virtual/2025/poster/29432
- 本地 PDF：[打开](../../pdfs/ICLR/2025/iclr-2025-V4y0CpX4hK__Agent_Security_Bench_ASB_Formalizing_and_Benchmarking_Attacks_and_Defenses_in_LLM_based_Agents.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_review
- 主方向：Financial Safety & Compliance / 金融安全与合规
- 细分方向：Financial Privacy & Security / 金融隐私与信息安全
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Retrieval & RAG / 检索与RAG
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Language Models；LLM；LLMs；retrieval
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/agiresearch/ASB.

## 纳入依据

To address this, we introduce Agent Security Bench (ASB), a comprehensive framework designed to formalize, benchmark, and evaluate the attacks and defenses of LLM-based agents, including 10 scenarios (e.g., e-commerce, autonomous driving, finance), 10 agents targeting the scenarios, over 400 tools, 27 different types of attack/defense methods, and 7 evaluation metrics.

## 原始摘要

Although LLM-based agents, powered by Large Language Models (LLMs), can use external tools and memory mechanisms to solve complex real-world tasks, they may also introduce critical security vulnerabilities. However, the existing literature does not comprehensively evaluate attacks and defenses against LLM-based agents. To address this, we introduce Agent Security Bench (ASB), a comprehensive framework designed to formalize, benchmark, and evaluate the attacks and defenses of LLM-based agents, including 10 scenarios (e.g., e-commerce, autonomous driving, finance), 10 agents targeting the scenarios, over 400 tools, 27 different types of attack/defense methods, and 7 evaluation metrics. Based on ASB, we benchmark 10 prompt injection attacks, a memory poisoning attack, a novel Plan-of-Thought backdoor attack, 4 mixed attacks, and 11 corresponding defenses across 13 LLM backbones. Our benchmark results reveal critical vulnerabilities in different stages of agent operation, including system prompt, user prompt handling, tool usage, and memory retrieval, with the highest average attack success rate of 84.30\%, but limited effectiveness shown in current defenses, unveiling important works to be done in terms of agent security for the community. We also introduce a new metric to evaluate the agents' capability to balance utility and security. Our code can be found at https://github.com/agiresearch/ASB.
