# Synthetic Series-Symbol Data Generation for Time Series Foundation Models

NeurIPS 2025 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：Exchange benchmark (currency series)。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=xB1ZNgq0Xp
- 摘要来源：https://neurips.cc/virtual/2025/poster/115260
- 本地 PDF：[打开](../../pdfs/NeurIPS/2025/neurips-2025-xB1ZNgq0Xp__Synthetic_Series_Symbol_Data_Generation_for_Time_Series_Foundation_Models.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Representation & Foundation Models / 表征与基础模型；Generation & Simulation / 序列生成与仿真
- 技术方法标签：Generative Modeling / 生成建模；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/wwhenxuan/SymTime.

## 纳入依据

ETTh1 ETTh2 Weather Electircity Traffic Exchange Average Metrics MSE MAE MSE MAE MSE MAE MSE MAE MSE MAE MSE MAE MSE MAE MSE MAE MSE MAE 0B 0.401 0.409 0.293 0.339 0.487 0.474 0.376 0.412 0.257 0.289 0.193 0.284 0.471 0.310 0.383 0.415 0.358 0.366 1B 0.376 0.398 0.292 0.331 0.461 0.459 0.403 0.419 0.257 0.282 0.199 0.285 0.473 0.303 0.370 0.410 0.354 0.361 10B 0.376 0.393 0.281 0.329 0.444 0.444 0.376 0.408 0.2

## 原始摘要

Foundation models for time series analysis (TSA) have attracted significant attention. However, challenges such as training data scarcity and imbalance continue to hinder their development. Inspired by complex dynamic system theories, we design a series-symbol data generation mechanism, enabling the unrestricted creation of high-quality time series data paired with corresponding symbolic expressions. To leverage series-symbol data pairs with strong correlations, we develop SymTime, a pre-trained foundation model for enhancing time series representation using symbolic information. SymTime demonstrates competitive performance across five major TSA tasks when fine-tunes with downstream tasks, rivaling foundation models pre-trained on real-world datasets. This approach underscores the potential of series-symbol data generation and pretraining mechanisms in overcoming data scarcity and enhancing task performance. The code is available at https://github.com/wwhenxuan/SymTime.
