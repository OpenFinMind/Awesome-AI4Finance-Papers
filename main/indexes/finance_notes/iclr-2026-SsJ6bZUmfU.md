# From Samples to Scenarios: A New Paradigm for Probabilistic Forecasting

ICLR 2026 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：Exchange benchmark (currency series)。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=SsJ6bZUmfU
- 摘要来源：https://iclr.cc/virtual/2026/poster/10009377
- 本地 PDF：[打开](../../pdfs/ICLR/2026/iclr-2026-SsJ6bZUmfU__From_Samples_to_Scenarios_A_New_Paradigm_for_Probabilistic_Forecasting.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；Probabilistic Forecasting & Calibration / 概率预测与校准
- 技术方法标签：Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

future, in datasets containing similar histories but diverse futures. Table 3: Inference FLOPs. FLOPs required to generate S forecast samples on the Exchange dataset with batch size = 1. The cost for TimeMCL and TimePrism is constant as they produce all scenarios in a single forward pass. Sampling S DeepAR TimeGrad TempFlow Trf.Flow TACTiS-2 TimeMCLTimePrism 1 2.9 × 104 1.9 × 108 5.8 × 106 1.4 × 107 2.5 × 107 10 2.9 × 105 1.9 × 109 5.8 × 107 1.3 × 108 1.2 × 108 8.8 × 106 5.1 × 105 100 2.9 × 106 1.9 × 1010 5.8 × 108 1.3

## 原始摘要

Most state-of-the-art probabilistic time series forecasting models rely on sampling to represent future uncertainty. However, this paradigm suffers from inherent limitations, such as lacking explicit probabilities, inadequate coverage, and high computational costs. In this work, we introduce **Probabilistic Scenarios**, an alternative paradigm designed to address the limitations of sampling. It operates by directly producing a finite set of {Scenario, Probability} pairs, thus avoiding Monte Carlo-like approximation. To validate this paradigm, we propose **TimePrism**, a simple model composed of only three parallel linear layers. Surprisingly, TimePrism achieves 9 out of 10 state-of-the-art results across five benchmark datasets on two metrics. The effectiveness of our paradigm comes from a fundamental reframing of the learning objective. Instead of modeling an entire continuous probability space, the model learns to represent a set of plausible scenarios and corresponding probabilities. Our work demonstrates the potential of the Probabilistic Scenarios paradigm, opening a promising research direction in forecasting beyond sampling.
