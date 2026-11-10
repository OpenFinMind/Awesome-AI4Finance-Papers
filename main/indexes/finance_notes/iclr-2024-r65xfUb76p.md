# UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition

ICLR 2024 · main · application

包含明确的金融任务、金融领域数据或金融案例验证。 主题：Financial NLP / 金融文本、情感与事件。

- 官方论文页：https://openreview.net/forum?id=r65xfUb76p
- 摘要来源：https://iclr.cc/virtual/2024/poster/17704
- 本地 PDF：[打开](../../pdfs/ICLR/2024/iclr-2024-r65xfUb76p__UniversalNER_Targeted_Distillation_from_Large_Language_Models_for_Open_Named_Entity_Recognition.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_financial_task_or_data
- 主方向：Financial NLP / 金融文本、情感与事件
- 细分方向：Entities, Events & Causality / 实体、事件与关系抽取
- 技术方法标签：Language Models & LLM / 语言模型与LLM
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：distillation；language models；LLMs
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

For evaluation, we assemble the largest NER benchmark to date, comprising 43 datasets across 9 diverse domains such as biomedicine, programming, social media, law, finance.

## 原始摘要

Large language models (LLMs) have demonstrated remarkable generalizability, such as understanding arbitrary entities and relations. Instruction tuning has proven effective for distilling LLMs into more cost-efficient models such as Alpaca and Vicuna. Yet such student models still trail the original LLMs by large margins in downstream applications. In this paper, we explore targeted distillation with mission-focused instruction tuning to train student models that can excel in a broad application class such as open information extraction. Using named entity recognition (NER) for case study, we show how ChatGPT can be distilled into much smaller UniversalNER models for open NER. For evaluation, we assemble the largest NER benchmark to date, comprising 43 datasets across 9 diverse domains such as biomedicine, programming, social media, law, finance. Without using any direct supervision, UniversalNER attains remarkable NER accuracy across tens of thousands of entity types, outperforming general instruction-tuned models such as Alpaca and Vicuna by over 30 absolute F1 points in average. With a tiny fraction of parameters, UniversalNER not only acquires ChatGPT's capability in recognizing arbitrary entity types, but also outperforms its NER accuracy by 7-9 absolute F1 points in average. Remarkably, UniversalNER even outperforms by a large margin state-of-the-art multi-task instruction-tuned systems such as InstructUIE, which uses supervised NER examples. We also conduct thorough ablation studies to assess the impact of various components in our distillation approach. We release the distillation recipe, data, and UniversalNER models to facilitate future research on targeted distillation.
