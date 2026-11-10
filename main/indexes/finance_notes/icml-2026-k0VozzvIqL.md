# Privasis: Synthesizing the Largest "Public" Private Dataset from Scratch

ICML 2026 · main · application

包含明确的金融任务、金融领域数据或金融案例验证。 主题：Financial Safety & Compliance / 金融安全与合规。

- 官方论文页：https://openreview.net/forum?id=k0VozzvIqL
- 摘要来源：https://icml.cc/virtual/2026/poster/62079
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-k0VozzvIqL__Privasis_Synthesizing_the_Largest_Public_Private_Dataset_from_Scratch.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_financial_task_or_data
- 主方向：Financial Safety & Compliance / 金融安全与合规
- 细分方向：Financial Privacy & Security / 金融隐私与信息安全
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Generative Modeling / 生成建模
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：language models
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Compared to existing datasets, Privasis, comprising 1.4 million records, offers orders-of-magnitude larger scale with quality, and far greater diversity across various document types, including medical records, legal documents, financial records, calendars, emails, meeting transcripts, and text-messages with a total of 55.1 million annotated attributes such as ethnicity, date of birth, workplace, etc.

## 原始摘要

Research involving privacy-sensitive data has always been constrained by data scarcity, standing in sharp contrast to other areas that have benefited from data scaling. To quench this thirst, we present Privasis (i.e., privacy oasis), the first million-scale fully synthetic dataset entirely built from scratch—an expansive reservoir of texts with rich and diverse private information—designed to broaden and accelerate research in areas where processing sensitive social data is inevitable. Compared to existing datasets, Privasis, comprising 1.4 million records, offers orders-of-magnitude larger scale with quality, and far greater diversity across various document types, including medical records, legal documents, financial records, calendars, emails, meeting transcripts, and text-messages with a total of 55.1 million annotated attributes such as ethnicity, date of birth, workplace, etc. We leverage Privasis to construct a parallel corpus for text sanitization with our pipeline that recursively decomposes texts and applies targeted sanitization. Our compact sanitization models ($\leq$ 4B) trained on this dataset outperform state-of-the-art large language models, such as GPT-5 and Qwen-3 235B.
