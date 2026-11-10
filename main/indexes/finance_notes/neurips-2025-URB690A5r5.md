# BlockScan: Detecting Anomalies in Blockchain Transactions

NeurIPS 2025 · main · core

研究金融业务、金融市场或金融系统中的具体问题。 主题：Fraud & AML / 欺诈检测与反洗钱；Blockchain & Digital Assets / 区块链与数字资产。

- 官方论文页：https://openreview.net/forum?id=URB690A5r5
- 摘要来源：https://neurips.cc/virtual/2025/poster/117763
- 本地 PDF：[打开](../../pdfs/NeurIPS/2025/neurips-2025-URB690A5r5__BlockScan_Detecting_Anomalies_in_Blockchain_Transactions.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_financial_task_or_data
- 主方向：Fraud & AML / 欺诈检测与反洗钱
- 细分方向：Payment & Transaction Fraud / 支付与交易欺诈；Crypto & Blockchain Transactions / 加密资产与链上交易
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Transformer / Transformer模型；Multimodal Learning / 多模态学习；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：language models；LLMs；Transformer
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

We propose BlockScan, a customized Transformer for anomaly detection in blockchain transactions. / Unlike existing methods that rely on rule-based systems or directly apply off-the-shelf large language models (LLMs), BlockScan introduces a series of customized designs to effectively model the unique data structure of blockchain transactions. / First, a blockchain transaction is multi-modal, containing blockchain-specific tokens, texts, and numbers. / This work sets a new benchmark for applying Transformer-based approaches in blockchain data analysis.

## 原始摘要

We propose BlockScan, a customized Transformer for anomaly detection in blockchain transactions. Unlike existing methods that rely on rule-based systems or directly apply off-the-shelf large language models (LLMs), BlockScan introduces a series of customized designs to effectively model the unique data structure of blockchain transactions. First, a blockchain transaction is multi-modal, containing blockchain-specific tokens, texts, and numbers. We design a novel modularized tokenizer to handle these multi-modal inputs, balancing the information across different modalities. Second, we design a customized masked language modeling mechanism for pretraining the Transformer architecture, incorporating RoPE embedding and FlashAttention for handling longer sequences. Finally, we design a novel anomaly detection method based on the model outputs. We further provide theoretical analysis for the detection method of our system.  Extensive evaluations on Ethereum and Solana transactions demonstrate BlockScan's exceptional capability in anomaly detection while maintaining a low false positive rate. Remarkably, BlockScan is the only method that successfully detects anomalous transactions on Solana with high accuracy, whereas all other approaches achieved very low or zero detection recall scores. This work sets a new benchmark for applying Transformer-based approaches in blockchain data analysis.
