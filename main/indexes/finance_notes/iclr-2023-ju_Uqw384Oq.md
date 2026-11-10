# TimesNet: Temporal 2D-Variation Modeling for General Time Series Analysis

ICLR 2023 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：Exchange benchmark (currency series)。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=ju_Uqw384Oq
- 摘要来源：https://iclr.cc/virtual/2023/poster/11976
- 本地 PDF：[打开](../../pdfs/ICLR/2023/iclr-2023-ju_Uqw384Oq__TimesNet_Temporal_2D_Variation_Modeling_for_General_Time_Series_Analysis.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；Representation & Foundation Models / 表征与基础模型；Imputation & Irregular Series / 缺失与不规则序列
- 技术方法标签：未明确标注
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Time series；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/thuml/TimesNet.

## 纳入依据

0.422 Weather 0.259 0.287 0.271 0.334 0.261 0.312 0.265 0.317 0.309 0.360 0.288 0.314 0.338 0.382 0.946 0.717 0.634 0.548 0.696 0.602 0.803 0.656 Exchange 0.416 0.443 0.410 0.427 0.385 0.447 0.354 0.414 0.519 0.500 0.461 0.454 0.613 0.539 1.913 1.159 1.550 0.998 1.402 0.968 1.280 0.932 ILI 2.139 0.931 2.497 1.004 7.382 2.003 2.616 1.090 2.847 1.144 2.077 0.914 3.006 1.161 7.635 2.050 5.137 1.544 4.839 1.485 4.724 1.445 Table 3: Short-term forecasting task on M4. The prediction lengths are in [6, 48] and results are weighted averaged from several datasets unde

## 原始摘要

Time series analysis is of immense importance in extensive applications, such as weather forecasting, anomaly detection, and action recognition. This paper focuses on temporal variation modeling, which is the common key problem of extensive analysis tasks. Previous methods attempt to accomplish this directly from the 1D time series, which is extremely challenging due to the intricate temporal patterns. Based on the observation of multi-periodicity in time series, we ravel out the complex temporal variations into the multiple intraperiod- and interperiod-variations. To tackle the limitations of 1D time series in representation capability, we extend the analysis of temporal variations into the 2D space by transforming the 1D time series into a set of 2D tensors based on multiple periods. This transformation can embed the intraperiod- and interperiod-variations into the columns and rows of the 2D tensors respectively, making the 2D-variations to be easily modeled by 2D kernels. Technically, we propose the TimesNet with TimesBlock as a task-general backbone for time series analysis. TimesBlock can discover the multi-periodicity adaptively and extract the complex temporal variations from transformed 2D tensors by a parameter-efficient inception block. Our proposed TimesNet achieves consistent state-of-the-art in five mainstream time series analysis tasks, including short- and long-term forecasting, imputation, classification, and anomaly detection. Code is available at this repository: https://github.com/thuml/TimesNet.
