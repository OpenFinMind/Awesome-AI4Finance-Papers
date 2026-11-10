# EVMbench: Evaluating AI Agents on Smart Contract Security

ICML 2026 · main · core

研究金融业务、金融市场或金融系统中的具体问题。 主题：Blockchain & Digital Assets / 区块链与数字资产。

- 官方论文页：https://openreview.net/forum?id=K5S8N5NgD8
- 摘要来源：https://icml.cc/virtual/2026/poster/64768
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-K5S8N5NgD8__EVMbench_Evaluating_AI_Agents_on_Smart_Contract_Security.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_financial_task_or_data
- 主方向：Blockchain & Digital Assets / 区块链与数字资产
- 细分方向：Crypto & Blockchain Transactions / 加密资产与链上交易；Smart Contracts & DeFi / 智能合约与DeFi
- 技术方法标签：未明确标注
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

EVMbench draws on 117 curated vulnerabilities from 40 repositories and, in the most realistic setting, uses programmatic grading based on tests and blockchain state under a local Ethereum execution environment. / We evaluate a range of frontier agents and find that they are capable of discovering and exploiting vulnerabilities end-to-end against live blockchain instances.

## 原始摘要

Smart contracts on public blockchains now manage large amounts of value, and vulnerabilities in these systems can lead to substantial losses. As AI agents become more capable at reading, writing, and running code, it is natural to ask how well they can already navigate this landscape, both in ways that improve security and in ways that might increase risk.  We introduce EVMbench, an evaluation that measures the ability of agents to detect, patch, and exploit smart contract vulnerabilities. EVMbench draws on 117 curated vulnerabilities from 40 repositories and, in the most realistic setting, uses programmatic grading based on tests and blockchain state under a local Ethereum execution environment. We evaluate a range of frontier agents and find that they are capable of discovering and exploiting vulnerabilities end-to-end against live blockchain instances. We release code, tasks, and tooling to support continued measurement of these capabilities and future work on security.
