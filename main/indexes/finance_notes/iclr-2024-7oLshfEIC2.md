# TimeMixer: Decomposable Multiscale Mixing for Time Series Forecasting

ICLR 2024 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：M4-Yearly。M4 年度至日度子集包含金融序列，未把仅使用 M4 Hourly 的论文据此纳入。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=7oLshfEIC2
- 摘要来源：https://iclr.cc/virtual/2024/poster/19347
- 本地 PDF：[打开](../../pdfs/ICLR/2024/iclr-2024-7oLshfEIC2__TimeMixer_Decomposable_Multiscale_Mixing_for_Time_Series_Forecasting.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测
- 技术方法标签：未明确标注
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Time series；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

622,5622) 5min 0.58 Transportation Short-term PEMS08 170 12 (10690,3548,265) 5min 0.52 Transportation Forecasting M4-Yearly 1 6 (23000, 0, 23000) Yearly 0.43 Demographic M4-Quarterly 1 8 (24000, 0, 24000) Quarterly 0.47 Finance M4-Monthly 1 18 (48000, 0, 48000) Monthly 0.44 Industry M4-Weakly 1 13 (359, 0,

## 原始摘要

Time series forecasting is widely used in extensive applications, such as traffic planning and weather forecasting. However, real-world time series usually present intricate temporal variations, making forecasting extremely challenging. Going beyond the mainstream paradigms of plain decomposition and multiperiodicity analysis, we analyze temporal variations in a novel view of multiscale-mixing, where time series present distinct patterns in different sampling scales. Specifically, the microscopic and the macroscopic information are reflected in fine and coarse scales, respectively, and thereby complex variations are inherently disentangled. Based on this observation, we propose TimeMixer as a fully MLP-based architecture with Past-Decomposable-Mixing (PDM) and Future-Multipredictor-Mixing (FMM) blocks to take full advantage of disentangled multiscale series in both past extraction and future prediction phases. Concretely, PDM applies the decomposition to multiscale series and further mixes the decomposed seasonal and trend components in fine-to-coarse and coarse-to-fine directions separately, which successively aggregates the microscopic seasonal and macroscopic trend information. FMM further ensembles multiple predictors to utilize complementary forecasting capabilities in multiscale observations. Consequently, our proposed TimeMixer is able to achieve consistent state-of-the-art performances in both long-term and short-term forecasting tasks with favorable run-time efficiency.
