# Scam2Prompt: A Scalable Framework for Auditing Malicious Scam Endpoints in Production LLMs

ICML 2026 · main · core

研究金融业务、金融市场或金融系统中的具体问题。 主题：Trading & Microstructure / 交易与市场微观结构；Fraud & AML / 欺诈检测与反洗钱；Blockchain & Digital Assets / 区块链与数字资产。

- 官方论文页：https://openreview.net/forum?id=jEQQBE30m1
- 摘要来源：https://icml.cc/virtual/2026/poster/62158
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-jEQQBE30m1__Scam2Prompt_A_Scalable_Framework_for_Auditing_Malicious_Scam_Endpoints_in_Production_LLMs.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_financial_task_or_data
- 主方向：Fraud & AML / 欺诈检测与反洗钱
- 细分方向：Trading & Execution / 交易策略与执行；Scams & Financial Misinformation / 诈骗与金融虚假信息；Crypto & Blockchain Transactions / 加密资产与链上交易
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Uncertainty & Robustness / 不确定性与鲁棒性；Retrieval & RAG / 检索与RAG
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：LLM；LLMs；RAG
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

In November 2024, this risk materialized when a developer reportedly lost 2,500 USD after ChatGPT generated an otherwise routine cryptocurrency trading script containing a live phishing URL.

## 原始摘要

The insatiable demand for web-scale training data has exposed LLMs to a subtle but consequential threat: the absorption of malicious scam content into model weights and its subsequent reproduction during inference. In November 2024, this risk materialized when a developer reportedly lost 2,500 USD after ChatGPT generated an otherwise routine cryptocurrency trading script containing a live phishing URL. To systematically investigate this problem, we introduce Scam2Prompt, an automated auditing framework that crawls known scam websites, infers their functional intent, and synthesizes innocuous developer-style prompts — the kind of legitimate coding requests a programmer might naturally submit — to evaluate whether LLMs reproduce the underlying scam endpoints. Importantly, our approach requires neither jailbreaking nor adversarial prompting; all 1,377 prompts in our benchmark, Innoc2Scam-bench, which is automatically constructed by Scam2Prompt, were human-validated as benign coding tasks. Evaluation of seven production LLMs released in 2025 on Innoc2Scam-bench shows that the vulnerability proves both persistent and severe: malicious code generation rates range from 12.9% to 47.3% across the evaluated models, and no tested model proves immune. State-of-the-art guardrails and RAG-based agents offer only limited protection, underscoring an urgent need for explicit URL validation in LLM-assisted software development pipelines.
