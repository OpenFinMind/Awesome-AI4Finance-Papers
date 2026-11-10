# Rating Quality of Diverse Time Series Data by Meta-learning from LLM Judgment

ICLR 2026 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：Exchange benchmark (currency series)。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=TwrgmA1tw0
- 摘要来源：https://iclr.cc/virtual/2026/poster/10009270
- 本地 PDF：[打开](../../pdfs/ICLR/2026/iclr-2026-TwrgmA1tw0__Rating_Quality_of_Diverse_Time_Series_Data_by_Meta_learning_from_LLM_Judgment.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；Representation & Foundation Models / 表征与基础模型
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：LLMs；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

he model TimeMixer. The metric is RMSE. Best results are bolded, and second-best are underlined. Criteria Weather Electricity Exchange Traffic trend 0.475 0.366 0.239 0.291 frequency 0.476 0.392 0.216 0.294 amplitude 0.418 0.336 0.242 0.320 pattern 0.500 0.396 0.234 0.265 fusion 0.433 0.318 0.223

## 原始摘要

High-quality time series (TS) data are essential for ensuring TS model performance, rendering research on rating TS data quality indispensable. Existing methods have shown promising rating accuracy within individual domains, primarily by extending data quality rating techniques such as influence functions and Shapley values to account for temporal characteristics. However, they neglect the fact that real-world TS data can span vastly different domains and exhibit distinct properties, hampering the accurate and efficient rating of diverse TS data.   In this paper, we propose TSRating, a novel and unified framework for rating the quality of time series data crawled from diverse domains. TSRating leverages LLMs' inherent ample knowledge, acquired during their extensive pretraining, to comprehend and discern quality differences in diverse TS data. We verify this by devising a series of prompts to elicit quality comparisons from LLMs for pairs of TS samples. We then fit a dedicated rating model, termed TSRater, to convert the LLMs' judgments into efficient quality predictions by inferring future TS samples through TSRater's inference. To ensure cross-domain adaptability, we develop a meta-learning scheme to train TSRater on quality comparisons collected from nine distinct domains. To improve training efficiency, we employ signSGD for inner-loop updates, thus circumventing the demanding computation of hypergradients. Extensive experimental results on eleven benchmark datasets across three time series tasks, each using both conventional TS models and TS foundation models, demonstrate that TSRating outperforms baselines in terms of estimation accuracy, efficiency, and domain adaptability.
