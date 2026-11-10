# CoGenCast: A Coupled Autoregressive–Flow Generative Framework for Time Series Forecasting

ICML 2026 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：Exchange benchmark (currency series)。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=LULx50RKAz
- 摘要来源：https://icml.cc/virtual/2026/poster/64629
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-LULx50RKAz__CoGenCast_A_Coupled_Autoregressive_Flow_Generative_Framework_for_Time_Series_Forecasting.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；Representation & Foundation Models / 表征与基础模型；Generation & Simulation / 序列生成与仿真
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Diffusion & Flow / 扩散与流模型；Generative Modeling / 生成建模；Causal Learning / 因果学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：causal；diffusion；language models；LLMs；Time series；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/liuyaguo/_CoGenCast}.

## 纳入依据

0.396 0.320 0.400 0.316 0.395 0.349 0.425 0.334 0.419 0.844 0.680 0.311 0.397 0.314 0.399 0.315 0.403 0.314 0.401 0.309 0.397 0.319 0.406 0.366 0.461 Exchange 0.031 0.118 0.037 0.134 0.035 0.130 0.037 0.133 0.061 0.185 0.046 0.153 0.320 0.444 0.033 0.125 0.034 0.127 0.034 0.126 0.040 0.138 0.033 0.127 0.033 0.123 0.087 0.214 Health 1.444 0.812 1.576 0.848 1.611 0.887 1.679 0.923 1.736 0.943 1.591 0.897 2.486 1.439 1.535 0.857 1.510 0.852 1.592 0.889 1.690 0.896 1.540 0.857 1.685 0.903 1.828 1.018 Wind 0.531 0.425 0.544 0.444 0.543 0.444 0.591 0.484 0.651 0.497 0.583

## 原始摘要

Time series forecasting can be  viewed as a generative problem that requires both semantic understanding over contextual conditions and stochastic modeling of continuous temporal dynamics. Existing approaches typically rely on either autoregressive large language models (LLMs) for semantic context modeling or diffusion-like models for continuous probabilistic generation. However, neither method alone can adequately model both aspects simultaneously. In this work, we propose CoGenCast, a hybrid generative framework that couples pre-trained LLMs with flow-matching mechanism for effective time series forecasting. Specifically, we reconfigure  pre-trained decoder-only LLMs into a  native forecasting encoder–decoder backbone by modifying only the attention topology, enabling bidirectional context encoding and causal representation generation. Building on this, a flow-matching mechanism  is further integrated to model temporal evolution, capturing continuous stochastic dynamics conditioned on the autoregressively generated representation. Notably, CoGenCast naturally supports multimodal forecasting and cross-domain unified training. Extensive experiments on multiple benchmarks show that CoGenCast achieves  competitive performance compared to previous  baselines. Code is available at \url{https://github.com/liuyaguo/_CoGenCast}.
