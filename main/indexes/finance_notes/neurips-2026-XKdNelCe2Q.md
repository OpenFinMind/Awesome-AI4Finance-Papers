# FLAME: Flow Enhanced Legendre Memory Models for General Time Series Forecasting

NeurIPS 2026 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：NYSE。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=XKdNelCe2Q
- 摘要来源：https://neurips.cc/Downloads/2026
- 本地 PDF：[打开](../../pdfs/NeurIPS/2026/neurips-2026-XKdNelCe2Q__FLAME_Flow_Enhanced_Legendre_Memory_Models_for_General_Time_Series_Forecasting.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；Representation & Foundation Models / 表征与基础模型；Probabilistic Forecasting & Calibration / 概率预测与校准
- 技术方法标签：Diffusion & Flow / 扩散与流模型；Generative Modeling / 生成建模；Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Time Series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

1.042 0.733 1.186 0.772 1.292 0.836 1.251 0.820 1.201 0.783 1.478 0.834 - - 1.337 0.829 1.299 0.795 NYSE 0.527 0.553 0.442 0.430 0.529 0.507 0.880 0.642 0.620 0.626 - - 0.988 0.704 1.129 0.720 - - - - 0.492 0.441 1st Count 8 8 6 4 15 9

## 原始摘要

In this work, we introduce FLAME, a family of extremely lightweight and capable Time Series Foundation Models, which support versatile forecasting tasks via generative probabilistic modeling, while ensuring both efficiency and robustness. FLAME utilizes the Legendre Memory for strong generalization capabilities. Through adapting variants of Legendre Memory, i.e., translated Legendre (LegT) and scaled Legendre (LegS), in the Encoding and Decoding phases, FLAME can effectively capture the inherent inductive bias within data and make efficient long-range inferences. To enhance the accuracy of probabilistic forecasting while keeping efficient, FLAME adopts a Normalizing Flow based forecasting head, which can model the arbitrarily intricate distributions over the forecasting horizon in a generative manner. Comprehensive experiments on four well-recognized benchmarks, including TSFM-Bench, ProbTS, TFB, and GIFT-EVAL, demonstrate that FLAME is a strong out-of-the-box tool of decision intelligence.
