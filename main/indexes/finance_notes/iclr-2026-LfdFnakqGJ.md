# A2ASecBench: A Protocol-Aware Security Benchmark for Agent-to-Agent Multi-Agent Systems

ICLR 2026 · main · application

通用方法在金融任务、数据或明确案例上开展应用验证。 主题：Financial Safety & Compliance / 金融安全与合规。

- 官方论文页：https://openreview.net/forum?id=LfdFnakqGJ
- 摘要来源：https://iclr.cc/virtual/2026/poster/10010017
- PDF 状态：access_blocked
- 金融依据类型：title_abstract_review
- 主方向：Financial Safety & Compliance / 金融安全与合规
- 细分方向：Financial Privacy & Security / 金融隐私与信息安全
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：language models；LLMs；Multi-agent
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

We empirically validate our framework using official A2A Project demos across three representative high-stakes domains (travel, healthcare, and finance), demonstrating that the identified attacks are both pervasive and highly effective, consistently bypassing default safeguards.

## 原始摘要

Multi-agent systems (MAS) built on large language models (LLMs) increasingly rely on agent-to-agent (A2A) protocols to enable capability discovery, task orchestration, and artifact exchange across heterogeneous stacks. While these protocols promise interoperability, they also introduce new vulnerabilities. In this paper, we present the first comprehensive security evaluation of A2A-MAS. We develop a taxonomy and threat model that categorize risks into supply-chain manipulations and protocol-logic weaknesses, and we detail six concrete attacks spanning all A2A stages and components with impacts on confidentiality, integrity, and availability. Building on this taxonomy, we introduce A2ASecBench, the first A2A-specific security benchmark framework capable of probing diverse and previously unexplored attack vectors. Our framework incorporates a dynamic adapter layer for deployment across heterogeneous agent stacks and downstream workloads, alongside a joint safety–utility evaluation methodology that explicitly measures the trade-off between harmlessness and helpfulness by pairing adversarial trials with benign tasks. We empirically validate our framework using official A2A Project demos across three representative high-stakes domains (travel, healthcare, and finance), demonstrating that the identified attacks are both pervasive and highly effective, consistently bypassing default safeguards. These findings highlight the urgent need for protocol-level defenses and standardized benchmarking to secure the next generation of agentic ecosystems.
