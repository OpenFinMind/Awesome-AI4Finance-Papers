# MMIE: Massive Multimodal Interleaved Comprehension Benchmark for Large Vision-Language Models

ICLR 2025 · main · application

正文包含金融领域数据、模型、实验或分领域评测。 主题：Document AI / 票据、财报与图表理解。

- 官方论文页：https://openreview.net/forum?id=HnhNRrLPwm
- 摘要来源：https://iclr.cc/virtual/2025/poster/30211
- 本地 PDF：[打开](../../pdfs/ICLR/2025/iclr-2025-HnhNRrLPwm__MMIE_Massive_Multimodal_Interleaved_Comprehension_Benchmark_for_Large_Vision_Language_Models.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_domain_data_or_experiment
- 主方向：Document AI / 票据、财报与图表理解
- 细分方向：Charts & Visual Understanding / 金融图表与视觉理解
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Multimodal Learning / 多模态学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Language Models
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

liable and automated metrics. MMIE is cu- rated from four multimodal datasets, involving 3 categories, 12 fields, and 102 subfields, including mathematics, physics, coding, statistics, literature, philosophy, education, finance, health, sports, art, and EECS (Electrical Engineering and Computer Science). The dataset comprises 20K multimodal questions, supporting both interleaved inputs and outputs. It features a mix of multiple-choice and open-ended question formats to evaluate a broad spectrum of competencies across various fields. As shown in Table 2, MMIE surpasses ex

## 原始摘要

Interleaved multimodal comprehension and generation, enabling models to produce and interpret both images and text in arbitrary sequences, have become a pivotal area in multimodal learning. Despite significant advancements, the evaluation of this capability remains insufficient. Existing benchmarks suffer from limitations in data scale, scope, and evaluation depth, while current evaluation metrics are often costly or biased, lacking in reliability for practical applications. To address these challenges, we introduce MMIE, a large-scale knowledge-intensive benchmark for evaluating interleaved multimodal comprehension and generation in Large Vision-Language Models (LVLMs). MMIE comprises 20K meticulously curated multimodal queries, spanning 3 categories, 12 fields, and 102 subfields, including mathematics, coding, physics, literature, health, and arts. It supports both interleaved inputs and outputs, offering a mix of multiple-choice and open-ended question formats to evaluate diverse competencies. Moreover, we propose a reliable automated evaluation metric, leveraging a scoring model fine-tuned with human-annotated data and systematic evaluation criteria, aimed at reducing bias and improving evaluation accuracy. Extensive experiments demonstrate the effectiveness of our benchmark and metrics in providing a comprehensive evaluation of interleaved LVLMs. Specifically, we evaluate eight LVLMs, revealing that even the best models show significant room for improvement, with most achieving only moderate results. We believe MMIE will drive further advancements in the development of interleaved LVLMs.
