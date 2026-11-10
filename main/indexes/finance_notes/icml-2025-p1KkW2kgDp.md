# Patch-wise Structural Loss for Time Series Forecasting

ICML 2025 · main · application

实验使用汇率、宏观金融、信用评估或财务文档等金融相关基准。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=p1KkW2kgDp
- 摘要来源：https://icml.cc/virtual/2025/poster/44030
- 本地 PDF：[打开](../../pdfs/ICML/2025/icml-2025-p1KkW2kgDp__Patch_wise_Structural_Loss_for_Time_Series_Forecasting.pdf)；版本：publisher_version
- 金融依据类型：fulltext_financial_benchmark
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测
- 技术方法标签：未明确标注
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/Dilfiraa/PS_Loss}.

## 纳入依据

0.420 0.355 0.436 0.345 0.427 0.386 0.454 0.332 0.417 0.333 0.441 0.325 0.432 0.393 0.462 0.377 0.450 Exchange 720 0.853 0.696 0.860 0.700 0.903 0.712 0.904 0.713 0.928 0.727 0.917 0.719 0.898 0.725 0.811 0.690 1.011 0.768 1.010 0.768 Avg 0.364 0.407 0.366 0.407 0.386 0.419 0.381 0.414 0.397 0.423 0.380 0.411 0.381 0.420 0.373 0.412 0.435 0.454 0.427 0.448 Table 2. LLM-based long-t

## 原始摘要

Time-series forecasting has gained significant attention in machine learning due to its crucial role in various domains. However, most existing forecasting models rely heavily on point-wise loss functions like Mean Squared Error, which treat each time step independently and neglect the structural dependencies inherent in time series data, making it challenging to capture complex temporal patterns accurately. To address these challenges, we propose a novel **P**atch-wise **S**tructural (**PS**) loss, designed to enhance structural alignment by comparing time series at the patch level. Through leveraging local statistical properties, such as correlation, variance, and mean, PS loss captures nuanced structural discrepancies overlooked by traditional point-wise losses. Furthermore, it integrates seamlessly with point-wise loss, simultaneously addressing local structural inconsistencies and individual time-step errors. PS loss establishes a novel benchmark for accurately modeling complex time series data and provides a new perspective on time series loss function design. Extensive experiments demonstrate that PS loss significantly improves the performance of state-of-the-art models across diverse real-world datasets. The data and code are publicly available at: \url{https://github.com/Dilfiraa/PS_Loss}.
