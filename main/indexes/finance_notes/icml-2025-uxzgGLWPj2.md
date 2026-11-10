# In-Context Fine-Tuning for Time-Series Foundation Models

ICML 2025 · main · application

正文包含金融数据、金融任务或金融领域评测。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=uxzgGLWPj2
- 摘要来源：https://icml.cc/virtual/2025/poster/43707
- 本地 PDF：[打开](../../pdfs/ICML/2025/icml-2025-uxzgGLWPj2__In_Context_Fine_Tuning_for_Time_Series_Foundation_Models.pdf)；版本：publisher_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；Representation & Foundation Models / 表征与基础模型
- 技术方法标签：未明确标注
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：fine-tuning；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

s that cov- ers granularities ranging from minutes to years and domains including finance, demand forecasting, weather, and traffic. 6. Experimental Results We report our results on the 23 datasets from this benchmark Similar to prior works, we report our results on the Chronos that were not used during training of TimesFM-ICF (or the zero-shot benchmarks from

## 原始摘要

Motivated by the recent success of time-series foundation models for zero-shot forecasting, we present a methodology for _in-context fine-tuning_ of a time-series foundation model. In particular, we design a pretrained foundation model that can be prompted (at inference time) with multiple time-series examples, in order to forecast a target time-series into the future. Our foundation model is specifically trained to utilize examples from multiple related time-series in its context window (in addition to the history of the target time-series) to help it adapt to the specific distribution of the target domain at inference time.  We show that such a foundation model that uses in-context examples at inference time can obtain much better performance on popular forecasting benchmarks compared to supervised deep learning methods, statistical models, and other time series foundation models.  Interestingly, our in-context fine-tuning approach even matches the performance of a foundation model that is explicitly fine-tuned on the target domain.
