# SpreadsheetArena: Decomposing Preference in LLM Generation of Spreadsheet Workbooks

ICML 2026 · main · core

以金融任务或金融数据为核心研究对象。 主题：Document AI / 票据、财报与图表理解。

- 官方论文页：https://openreview.net/forum?id=20x0qoSG2f
- 摘要来源：https://icml.cc/virtual/2026/poster/66626
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-20x0qoSG2f__SpreadsheetArena_Decomposing_Preference_in_LLM_Generation_of_Spreadsheet_Workbooks.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_review
- 主方向：Document AI / 票据、财报与图表理解
- 细分方向：Financial Tables & Spreadsheets / 财务表格与电子表格
- 技术方法标签：Language Models & LLM / 语言模型与LLM
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：language models；LLM；LLMs
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Expert evaluations of spreadsheets for finance prompts suggest that even highly ranked models do not reliably produce spreadsheets aligned with domain-specific best practices.

## 原始摘要

We consider the task of end-to-end **spreadsheet generation**, where language models are prompted to produce spreadsheet artifacts to satisfy users' explicit and implicit constraints, specified in natural language.  We introduce **SpreadsheetArena**, a platform for evaluating models' performance on the task via blind pairwise evaluations of LLM-generated spreadsheet workbooks. As with other complex, open-ended tasks, relevant evaluation criteria can vary greatly across use cases and prompts, often in ways that are difficult to formalize. Compared to general dialogue or text generation settings, spreadsheet generation presents unique challenges and opportunities: the task output structure is well-defined and multi-dimensional, and there are often complex interactivity and layout considerations. We observe that stylistic, structural, and functional features of preferred spreadsheets vary meaningfully across prompts. Expert evaluations of spreadsheets for finance prompts suggest that even highly ranked models do not reliably produce spreadsheets aligned with domain-specific best practices. We host a live arena and release a dataset of prompts, generated spreadsheets, and preference votes, which we hope will facilitate further study of tasks operating over spreadsheets as a challenging and interesting class of complex, open-ended tasks for LLMs.
