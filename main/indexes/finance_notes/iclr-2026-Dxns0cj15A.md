# EDINET-Bench: Evaluating LLMs on Complex Financial Tasks using Japanese Financial Statements

ICLR 2026 · main · core

以金融任务或金融数据为核心研究对象。 主题：Fraud & AML / 欺诈检测与反洗钱；Document AI / 票据、财报与图表理解；Corporate Finance & Accounting / 公司金融与会计；Financial Models & Benchmarks / 金融模型与评测资源。

- 官方论文页：https://openreview.net/forum?id=Dxns0cj15A
- 摘要来源：https://iclr.cc/virtual/2026/poster/10010730
- 本地 PDF：[打开](../../pdfs/ICLR/2026/iclr-2026-Dxns0cj15A__EDINET_Bench_Evaluating_LLMs_on_Complex_Financial_Tasks_using_Japanese_Financial_Statements.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_review
- 主方向：Document AI / 票据、财报与图表理解
- 细分方向：Scams & Financial Misinformation / 诈骗与金融虚假信息；Report Layout & Structured Extraction / 财报版面与结构提取；Earnings & Corporate Disclosures / 盈利与公司披露；Financial Pretraining & Adaptation / 金融预训练与领域适配
- 技术方法标签：Language Models & LLM / 语言模型与LLM
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Language Models；LLMs
- 数据 / 评测名称（题名和摘要可确认）：EDINET-Bench
- 代码链接：摘要未提供可确认链接

## 纳入依据

In contrast, the financial domain poses higher entry barriers due to its demand for specialized expertise, and benchmarks remain relatively scarce compared to those in mathematics or coding. / We introduce EDINET-Bench, an open-source Japanese financial benchmark designed to evaluate LLMs on challenging tasks such as accounting fraud detection, earnings forecasting, and industry classification. / EDINET-Bench is constructed from ten years of annual reports filed by Japanese companies. / These tasks require models to process entire annual reports and integrate information across multiple tables and textual sections, demanding expert-level reasoning that is challenging even for human professionals. / Our experiments show that even state-of-the-art LLMs struggle in this domain, performing only marginally better than logistic regression in binary classification tasks such as fraud detection and earnings forecasting. / This highlights the need for benchmark frameworks that better reflect the environments in which financial professionals operate, with richer scaffolding such as realistic simulations and task-specific reasoning support to enable more effective problem solving.

## 原始摘要

Large Language Models (LLMs) have made remarkable progress, surpassing human performance on several benchmarks in domains such as mathematics and coding. A key driver of this progress has been the development of benchmark datasets. In contrast, the financial domain poses higher entry barriers due to its demand for specialized expertise, and benchmarks remain relatively scarce compared to those in mathematics or coding. We introduce EDINET-Bench, an open-source Japanese financial benchmark designed to evaluate LLMs on challenging tasks such as accounting fraud detection, earnings forecasting, and industry classification. EDINET-Bench is constructed from ten years of annual reports filed by Japanese companies. These tasks require models to process entire annual reports and integrate information across multiple tables and textual sections, demanding expert-level reasoning that is challenging even for human professionals. Our experiments show that even state-of-the-art LLMs struggle in this domain, performing only marginally better than logistic regression in binary classification tasks such as fraud detection and earnings forecasting. Our results show that simply providing reports to LLMs in a straightforward setting is not enough. This highlights the need for benchmark frameworks that better reflect the environments in which financial professionals operate, with richer scaffolding such as realistic simulations and task-specific reasoning support to enable more effective problem solving. We make our dataset and code publicly available to support future research.
