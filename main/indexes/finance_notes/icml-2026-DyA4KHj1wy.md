# Universal Redundancies in Time Series Foundation Models

ICML 2026 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：m4_daily。M4 年度至日度子集包含金融序列，未把仅使用 M4 Hourly 的论文据此纳入。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=DyA4KHj1wy
- 摘要来源：https://icml.cc/virtual/2026/poster/65406
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-DyA4KHj1wy__Universal_Redundancies_in_Time_Series_Foundation_Models.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Representation & Foundation Models / 表征与基础模型
- 技术方法标签：Transformer / Transformer模型；Uncertainty & Robustness / 不确定性与鲁棒性；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：fine-tuning；Time Series；time series；transformer；transformers
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

ast_storage/H/short 0.72 0.72 0.72 0.72 0.72 0.71 0.71 0.71 0.71 0.71 0.71 0.71 0.71 ett1/H/long 0.93 0.93 0.93 0.94 0.93 0.93 0.92 0.92 0.92 0.92 0.92 0.92 0.92 m4_daily/D/short 1.04 1.04 1.04 1.03 1.03 1.03 1.03 1.03 1.03 1.04 1.03 1.02 1.02 20 bitbrain

## 原始摘要

Time Series Foundation Models (TSFMs) leverage extensive pretraining to accurately predict unseen time series during inference, without the need for task-specific fine-tuning. Through large-scale evaluations on standard benchmarks, we find that leading transformer-based TSFMs exhibit redundant components in their intermediate layers. We introduce a set of tools for mechanistic interpretability of TSFMs, including ablations of specific components and direct logit attribution on the residual stream. Our findings are consistent across several leading TSFMs with diverse architectures, and across a diverse set of real-world and synthetic time-series datasets. We discover that all models in our study are robust to ablations of entire layers. Furthermore, we develop a theoretical framework framing transformers as kernel regressors, motivating a purely intrinsic strategy for ablating heads based on the stable rank of the per-head projection matrices. Using this approach, we uncover the specific heads responsible for degenerate phenomena widely observed in TSFMs, such as parroting of motifs from the context and seasonality bias. Our study sheds light on the universal properties of this emerging class of architectures for continuous-time sequence modeling.
