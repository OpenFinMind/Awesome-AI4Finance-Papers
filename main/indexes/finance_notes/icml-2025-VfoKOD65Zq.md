# LangTime: A Language-Guided Unified Model for Time Series Forecasting with Proximal Policy Optimization

ICML 2025 · main · application

实验使用汇率、宏观金融、信用评估或财务文档等金融相关基准。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=VfoKOD65Zq
- 摘要来源：https://icml.cc/virtual/2025/poster/45059
- 本地 PDF：[打开](../../pdfs/ICML/2025/icml-2025-VfoKOD65Zq__LangTime_A_Language_Guided_Unified_Model_for_Time_Series_Forecasting_with_Proximal_Policy_Optimization.pdf)；版本：publisher_version
- 金融依据类型：fulltext_financial_benchmark
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；Representation & Foundation Models / 表征与基础模型
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Reinforcement Learning / 强化学习；Multimodal Learning / 多模态学习；Optimization & Numerical Methods / 优化与数值方法；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：fine-tuning；language models；LLMs；reinforcement learning；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

0.201 0.118 0.246 0.087 0.202 0.083 0.203 0.087 0.208 0.084 0.201 0.088 0.205 0.107 0.234 Exchange 192 0.175 0.300 0.218 0.338 0.253 0.357 0.175 0.298 0.212 0.332 0.178 0.298 0.178 0.299 0.178 0.302 0.178 0.299 0.176 0.299 0.226 0.344 336 0.329 0.412 0.367 0.443 0.390 0.452 0.329 0.409 0.360 0.438 0.329 0.413 0.328 0.415 0.338

## 原始摘要

Recent research has shown an increasing interest in utilizing pre-trained large language models (LLMs) for a variety of time series applications. However, there are three main challenges when using LLMs as foundational models for time series forecasting: (1) Cross-domain generalization. (2) Cross-modality alignment. (3) Error accumulation in autoregressive frameworks. To address these challenges, we proposed **LangTime**, a **lan**guage-**g**uided unified model for **time** series forecasting that incorporates cross-domain pre-training with reinforcement learning-based fine-tuning. Specifically, LangTime constructs Temporal Comprehension Prompts (TCPs), which include dataset-wise and channel-wise instructions, to facilitate domain adaptation and condense time series into a single token, enabling LLMs to understand better and align temporal data. To improve autoregressive forecasting, we introduce TimePPO, a reinforcement learning-based fine-tuning algorithm. TimePPO mitigates error accumulation by leveraging a multidimensional rewards function tailored for time series and a repeat-based value estimation strategy. Extensive experiments demonstrate that LangTime achieves state-of-the-art cross-domain forecasting performance, while TimePPO fine-tuning effectively enhances the stability and accuracy of autoregressive forecasting.
