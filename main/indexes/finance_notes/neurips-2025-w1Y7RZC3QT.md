# Document Summarization with Conformal Importance Guarantees

NeurIPS 2025 · main · application

正文包含金融数据、金融训练数据、金融任务评测或具体金融场景案例。 主题：Financial NLP / 金融文本、情感与事件；Corporate Finance & Accounting / 公司金融与会计。

- 官方论文页：https://openreview.net/forum?id=w1Y7RZC3QT
- 摘要来源：https://neurips.cc/virtual/2025/poster/115366
- 本地 PDF：[打开](../../pdfs/NeurIPS/2025/neurips-2025-w1Y7RZC3QT__Document_Summarization_with_Conformal_Importance_Guarantees.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Corporate Finance & Accounting / 公司金融与会计
- 细分方向：Generation & Summarization / 金融文本生成与摘要；Earnings & Corporate Disclosures / 盈利与公司披露
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Conformal；conformal；language models；LLMs
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

stractive summarization with an LLM to our hybrid extractive-abstractive approach. 4.1 Datasets We use 5 datasets to evaluate the performance of our framework: ECTSum [46] contains complete transcripts from corporate earnings calls, as well as expert-curated extractive summaries at the sentence level; CSDS [40] is a dataset of Chinese language customer-client conversations. Although the summaries are abstractive, each conversation has sentence-level labels for use as an extractive benchmark; CNN/DM [32] covers news sourced from CNN and The Daily Mail with human-written summa

## 原始摘要

Automatic summarization systems have advanced rapidly with large language models (LLMs), yet they still lack reliable guarantees on inclusion of critical content in high-stakes domains like healthcare, law, and finance. In this work, we introduce Conformal Importance Summarization, the first framework for importance-preserving summary generation which uses conformal prediction to provide rigorous, distribution-free coverage guarantees. By calibrating thresholds on sentence-level importance scores, we enable extractive document summarization with user-specified coverage and recall rates over critical content. Our method is model-agnostic, requires only a small calibration set, and seamlessly integrates with existing black-box LLMs. Experiments on established summarization benchmarks demonstrate that Conformal Importance Summarization achieves the theoretically assured information coverage rate. Our work suggests that Conformal Importance Summarization can be combined with existing techniques to achieve reliable, controllable automatic summarization, paving the way for safer deployment of AI summarization tools in critical applications. Code is available at github.com/layer6ai-labs/conformal-importance-summarization.
