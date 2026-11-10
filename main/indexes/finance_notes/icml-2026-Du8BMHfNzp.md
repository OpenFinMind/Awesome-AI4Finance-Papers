# PATRA: Pattern-Aware Alignment and Balanced Reasoning for Time Series Question Answering

ICML 2026 · main · application

正文包含金融数据、金融训练数据、金融任务评测或具体金融场景案例。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=Du8BMHfNzp
- 摘要来源：https://icml.cc/virtual/2026/poster/65414
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-Du8BMHfNzp__PATRA_Pattern_Aware_Alignment_and_Balanced_Reasoning_for_Time_Series_Question_Answering.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Causality & Dynamics / 序列因果与动力学
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Multimodal Learning / 多模态学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：LLM；Time series；time series；Time Series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

prediction. Simultaneously, in the Table 1 presents the overall performance of all baseline complex Finance domain, it also achieves SOTA perfor- models and our PATRA model on four task types. Our PA- mance across all six metrics for both short-term (7-day) and TRA achieves the best results across all metrics, surpassing long-term (30-day) trend prediction and numerical forecast- pure text models and significantly outperforming the multi- ing. The details of MTBench are shown in Appendix D. modal model ChatTS, highlighting its strong cross-modality modeling and reasoning capabilities. 5.6. Ablation Studies In detail, PATRA achieves 56.03% accuracy on Comprehen- We conduct ablation experiments to assess the contribu- sion, ex

## 原始摘要

Time series reasoning demands both the perception of complex dynamics and logical depth. However, existing LLM-based approaches exhibit two limitations: they often treat time series merely as text or images, failing to capture the patterns like trends and seasonalities needed to answer specific questions; and when trained on a mix of simple and complex tasks, simpler objectives often dominate the learning process, hindering the development of deep reasoning capabilities. To address these limitations, we propose the Pattern-Aware Alignment and Balanced Reasoning model (PATRA), introducing a pattern-aware mechanism that extracts trend and seasonality patterns from time series to achieve deep alignment. Furthermore, we design a task-aware balanced reward to harmonize learning across tasks of varying difficulty, incentivizing the generation of coherent Chains of Thought. Extensive experiments show that PATRA outperforms strong baselines across diverse Time Series Question Answering (TSQA) tasks, demonstrating superior cross-modal understanding and reasoning capability.
