# Global Merger-Arbitrage Forecasting with Language Models

ICML 2026 · main · core

以金融任务或金融数据为核心研究对象。 主题：Trading & Microstructure / 交易与市场微观结构；Financial IR & RAG / 金融检索与RAG；Corporate Finance & Accounting / 公司金融与会计。

- 官方论文页：https://openreview.net/forum?id=wDaX9bFufS
- 摘要来源：https://icml.cc/virtual/2026/poster/60833
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-wDaX9bFufS__Global_Merger_Arbitrage_Forecasting_with_Language_Models.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_review
- 主方向：Trading & Microstructure / 交易与市场微观结构
- 细分方向：Trading & Execution / 交易策略与执行；Financial RAG & Long Documents / 金融RAG与长文档；Mergers & Acquisitions / 并购与公司事件
- 技术方法标签：Language Models & LLM / 语言模型与LLM
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：language models；LLM；LLMs
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

We present a language-model forecasting system for merger arbitrage, a specialized high-stakes financial setting in which the task is to predict the outcome of announced M\&A deals. / These results, together with ablation studies, show that LLM-based forecasting can succeed in specialized, long-context financial workflows, with hindsight-based supervision and expert-designed context playing a critical role.

## 原始摘要

We present a language-model forecasting system for merger arbitrage, a specialized high-stakes financial setting in which the task is to predict the outcome of announced M\&A deals. Unlike prior work on judgmental forecasting with LLMs, which has focused on broad mixed-topic benchmarks and short context such as news snippets, we study a setting that requires long-context reasoning over hundreds of pages of technical documents. Our system combines expert-guided context engineering with finetuning on hindsight-guided reasoning traces derived from historical deals. Given an announced deal, it outputs a probability distribution over three mutually exclusive outcomes: closing at announced terms, a higher bid, or deal termination. On an out-of-sample set of more than 400 large deals spanning 42 countries, our finetuned system achieves the best performance of any method we evaluate, reducing class-balanced Brier score to 0.151. This is 24% below calibrated market-implied probabilities, 19% below XGBoost, and 25-42% below frontier language models. These results, together with ablation studies, show that LLM-based forecasting can succeed in specialized, long-context financial workflows, with hindsight-based supervision and expert-designed context playing a critical role.
