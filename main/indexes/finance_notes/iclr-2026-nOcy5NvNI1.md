# Constantly Improving Image Models Need Constantly Improving Benchmarks

ICLR 2026 · main · application

研究财务文档、企业 ESG 披露，或在金融评测与财务业务流程上开展验证。 主题：Document AI / 票据、财报与图表理解。

- 官方论文页：https://openreview.net/forum?id=nOcy5NvNI1
- 摘要来源：https://iclr.cc/virtual/2026/poster/10007477
- 本地 PDF：[打开](../../pdfs/ICLR/2026/iclr-2026-nOcy5NvNI1__Constantly_Improving_Image_Models_Need_Constantly_Improving_Benchmarks.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_financial_task_or_data
- 主方向：Document AI / 票据、财报与图表理解
- 细分方向：Receipts, Invoices & OCR / 票据发票与OCR
- 技术方法标签：Language Models & LLM / 语言模型与LLM
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Our analysis shows that ECHO (1) discovers creative and complex tasks absent from existing benchmarks, such as re-rendering product labels across languages or generating receipts with specified totals, (2) more clearly distinguishes state-of-the-art models from alternatives, and (3) surfaces community feedback that we use to inform the design of metrics for model quality (e.g., measuring observed shifts in color, identity, and structure).

## 原始摘要

Recent advances in image generation, often driven by proprietary systems like GPT-4o Image Gen, regularly introduce new capabilities that reshape how users interact with these models. Existing benchmarks often lag behind and fail to capture these emerging use cases, leaving a gap between community perceptions of progress and formal evaluation. To address this, we present ECHO, a framework for constructing benchmarks directly from real-world evidence of model use: social media posts that showcase novel prompts and qualitative user judgments. Applying this framework to GPT-4o Image Gen, we construct a dataset of over 35,000 prompts curated from such posts. Our analysis shows that ECHO (1) discovers creative and complex tasks absent from existing benchmarks, such as re-rendering product labels across languages or generating receipts with specified totals, (2) more clearly distinguishes state-of-the-art models from alternatives, and (3) surfaces community feedback that we use to inform the design of metrics for model quality (e.g., measuring observed shifts in color, identity, and structure). Our website is at https://echo-bench.github.io.
