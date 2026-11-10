# Aurora: Towards Universal Generative Multimodal Time Series Forecasting

ICLR 2026 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：NYSE。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=VVJ6Ck9JBl
- 摘要来源：https://iclr.cc/virtual/2026/poster/10009133
- 本地 PDF：[打开](../../pdfs/ICLR/2026/iclr-2026-VVJ6Ck9JBl__Aurora_Towards_Universal_Generative_Multimodal_Time_Series_Forecasting.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；Representation & Foundation Models / 表征与基础模型；Generation & Simulation / 序列生成与仿真；Probabilistic Forecasting & Calibration / 概率预测与校准
- 技术方法标签：Diffusion & Flow / 扩散与流模型；Generative Modeling / 生成建模；Transformer / Transformer模型
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：distillation；Time Series；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

1.151 0.763 1.186 0.772 1.251 0.820 1.201 0.783 1.613 0.870 1.478 0.834 - - 1.425 0.848 1.299 0.795 1.337 0.829 NYSE 0.528 0.526 0.880 0.642 - - 0.988 0.704 0.623 0.536 1.129 0.720 - - 1.220 0.820 - - - - st 1 Count 27 21 11 13 3 1 0 0 1 2

## 原始摘要

Cross-domain generalization is very important in Time Series Forecasting because similar historical information may lead to distinct future trends due to the domain-specific characteristics. Recent works focus on building unimodal time series foundation models and end-to-end multimodal supervised models. Since domain-specific knowledge is often contained in modalities like texts, the former lacks the explicit utilization of them, thus hindering the performance. The latter is tailored for end-to-end scenarios and does not support zero-shot inference for cross-domain scenarios. In this work, we introduce Aurora, the first Multimodal Time Series Foundation Model, which supports multimodal inputs and zero-shot inference. Pretrained on Cross-domain Multimodal Time Series Corpus, Aurora can adaptively extract and focus on key domain knowledge contained in corresponding text or image modalities, thus possessing strong cross-domain generalization capability. Through tokenization, encoding, and distillation, Aurora can extract multimodal domain knowledge as guidance and then utilizes a Modality-Guided Multi-head Self-Attention to inject them into the modeling of temporal representations. In the decoding phase, the multimodal representations are used to generate the conditions and prototypes of future tokens, contributing to a novel Prototype-Guided Flow Matching for generative probabilistic forecasting. Comprehensive experiments on 5 well-recognized benchmarks, including TimeMMD, TSFM-Bench, ProbTS, TFB, and EPF, demonstrate the consistent state-of-the-art performance of Aurora on both unimodal and multimodal scenarios.
