# From Chats to Markets: AgenticPay for LLM-Powered Negotiation in Multi-Agent Commerce

NeurIPS 2026 · main · application

以金融市场为研究对象，或包含明确的金融领域数据和应用评测。 主题：Financial Agents / 金融Agent与决策。

- 官方论文页：https://openreview.net/forum?id=BjCh5p36da
- 摘要来源：https://neurips.cc/Downloads/2026
- PDF 状态：access_blocked
- 金融依据类型：title_abstract_financial_task_or_data
- 主方向：Financial Agents / 金融Agent与决策
- 细分方向：Investment & Financial Research Agents / 投研与金融决策Agent
- 技术方法标签：Language Models & LLM / 语言模型与LLM
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：language models
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Agents based on large language models are increasingly expected to autonomously handle negotiation and transactions.

## 原始摘要

Agents based on large language models are increasingly expected to autonomously handle negotiation and transactions. However, existing benchmarks predominantly focus on text-only, bilateral, zero-sum price haggling, failing to capture the complexity of real-world commerce. To address this gap, we introduce Agenticpay, a unified framework and benchmark for evaluating how well multimodal agents reach high-welfare, multi-dimensional agreements in realistic markets. Built around four core components ( Environments, Tasks, Agents, and Metrics), Agenticpay comprises 160 multimodal tasks spanning 4 real-world business scenarios (E-commerce, Food Delivery, Ride-hailing, and Apartment Rental) and 8 market topologies, scaling from 1-to-1 bargaining to many-to-many (N-to-N) competitive markets. Beyond price haggling, agents must read product images, infer each opponent's hidden preferences, and trade off multiple binding contract terms (e.g., price, lease duration, return policy, delivery speed). Agents communicate through multi-round natural-language dialogue, with each turn proposing or revising a full contract, and outcomes are scored by a utility-based framework that rewards agreements maximizing joint welfare. Evaluations on state-of-the-art proprietary (GPT-5.4, Claude Sonnet 4.6, Gemini 3.1 Pro Preview) and open-weight (Qwen3-VL-32B-Instruct, InternVL3-38B) multimodal models reveal substantial gaps in non-zero-sum value creation and market reasoning: even the strongest agent (Gemini 3.1 Pro Preview) reaches a GlobalScore of only 42.3/100, and performance consistently degrades as markets scale from bilateral to multi-sided, with the average GlobalScore dropping by 5.7 points and open-weight models suffering the largest declines (up to 11.5 points). These findings establish Agenticpay as a foundational testbed for multimodal agentic commerce. Code and dataset are available at: https://anonymous.4open.science/r/AgenticPay-4BBB/README.md.
