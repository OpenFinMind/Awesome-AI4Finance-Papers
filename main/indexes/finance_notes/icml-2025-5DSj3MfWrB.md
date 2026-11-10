# VisionTS: Visual Masked Autoencoders Are Free-Lunch Zero-Shot Time Series Forecasters

ICML 2025 · main · application

实验使用包含金融序列的 M4 非小时子集；金融子集由官方元数据核验。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=5DSj3MfWrB
- 摘要来源：https://icml.cc/virtual/2025/poster/46441
- 本地 PDF：[打开](../../pdfs/ICML/2025/icml-2025-5DSj3MfWrB__VisionTS_Visual_Masked_Autoencoders_Are_Free_Lunch_Zero_Shot_Time_Series_Forecasters.pdf)；版本：publisher_version
- 金融依据类型：benchmark_with_financial_subset
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；Representation & Foundation Models / 表征与基础模型
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Multimodal Learning / 多模态学习；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：fine-tuning；language models；LLMs；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/Keytoyze/VisionTS.

## 纳入依据

699.3 798.38 M3 Other 315.85 300.3 263.54 278.43 277.83 215.35 189.42 194.98 193.02 234.43 318.13 240.17 247.56 221.85 245.29 239.24 M4 Monthly 666.54 728.27 597.6 671.27 625.24 563.58 589.52 582.6 575.36 596.19 611.69 612.52 615.22 578.48 655.51 780.47 M4 Weekly 404.23 518.44 339.76 347.99 336.82 333.32 296.15 335.66 321.61 293.21 364.65 338.37 351.78 277.73 359.46 378.89 M4 Daily 215.63 266.52 189.1 180.83 178

## 原始摘要

Foundation models have emerged as a promising approach in time series forecasting (TSF). Existing approaches either repurpose large language models (LLMs) or build large-scale time series datasets to develop TSF foundation models for universal forecasting. However, these methods face challenges due to the severe cross-domain gap or in-domain heterogeneity. This paper explores a new road to building a TSF foundation model from rich, high-quality natural images. Our key insight is that a visual masked autoencoder, pre-trained on the ImageNet dataset, can naturally be a numeric series forecaster. By reformulating TSF as an image reconstruction task, we bridge the gap between image pre-training and TSF downstream tasks. Surprisingly, without further adaptation in the time series domain, the proposed VisionTS could achieve better zero-shot forecast performance than existing TSF foundation models. With fine-tuning for one epoch, VisionTS could further improve the forecasting and achieve state-of-the-art performance in most cases. Extensive experiments reveal intrinsic similarities between images and real-world time series, suggesting that visual models may offer a "free lunch" for TSF and highlight the potential for future cross-modality research. Our code is available in the https://github.com/Keytoyze/VisionTS.
