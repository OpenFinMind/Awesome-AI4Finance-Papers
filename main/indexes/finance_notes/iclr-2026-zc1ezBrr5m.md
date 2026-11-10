# TaTToo: Tool-Grounded Thinking PRM for Test-Time Scaling in Tabular Reasoning

ICLR 2026 · main · application

正文包含金融数据、金融训练数据、金融任务评测或具体金融场景案例。 主题：Document AI / 票据、财报与图表理解。

- 官方论文页：https://openreview.net/forum?id=zc1ezBrr5m
- 摘要来源：https://iclr.cc/virtual/2026/poster/10006442
- 本地 PDF：[打开](../../pdfs/ICLR/2026/iclr-2026-zc1ezBrr5m__TaTToo_Tool_Grounded_Thinking_PRM_for_Test_Time_Scaling_in_Tabular_Reasoning.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Document AI / 票据、财报与图表理解
- 细分方向：Financial Tables & Spreadsheets / 财务表格与电子表格
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Reinforcement Learning / 强化学习；Tabular Learning / 表格学习；Retrieval & RAG / 检索与RAG
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：fine-tuning；reinforcement learning；retrieval
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Bench (Wu et al., 2024). TableBench is a comprehensive benchmark specifically designed to evaluate the reasoning abilities of LLMs over tabular data. It consists of 3,681 unique tables drawn from diverse domains such as finance, sports, politics, and science, with each table containing on average 16.7 rows and 6.7 columns. The dataset emphasizes numerical reasoning, with over 65% of table cells containing numerical values. TableBench questions are organized into four major categories: fact-checking, numerical reasoning, data analysis, further divided into 18 subcategorie

## 原始摘要

Process Reward Models (PRMs) have recently emerged as a powerful framework for enhancing the reasoning capabilities of large reasoning models (LRMs), particularly in the context of test-time scaling (TTS). However, their potential for supervising LRMs on tabular reasoning domains remains underexplored.  Through detailed empirical analyses, we identify that existing PRMs, though widely adopted for supervising text-only reasoning steps, struggle with table-specific operations such as sub-table retrieval and schema interaction, leading to critical performance bottlenecks. To address this limitation, we propose TaTToo, a novel table-grounded PRM framework that (i) reasons explicitly over tabular reasoning steps and (ii) integrates tool-based verification to provide precise reward supervision. Concretely, we first design a scalable data curation pipeline that constructs over 60k high-quality step-level annotations by integrating table verification rationales with tool-based executions. Building on the collected data, we train TaTToo with a dual-stage paradigm: cold-start supervised fine-tuning to capture tool-use reasoning patterns, followed by reinforcement learning with tool-grounded reward shaping to align our model with table-based verification. We provide a comprehensive evaluation of the policy improvement induced by our newly designed PRM. Across 5 challenging tabular reasoning benchmarks covering numerical reasoning, fact-checking, and data analysis, TaTToo improves downstream policy LRMs by 30.9\% at inference, surpasses strong PRM baselines such as Qwen-2.5-Math-PRM-72B with only 8B parameters, and demonstrates strong generalizability across diverse TTS strategies.
