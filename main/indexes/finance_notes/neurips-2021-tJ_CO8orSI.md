# Adjusting for Autocorrelated Errors in Neural Networks for Time Series

NeurIPS 2021 · main · application

正文包含金融数据、金融任务或金融领域评测。 主题：Time Series / 时间序列；Macro & Economic Forecasting / 宏观经济与预测。

- 官方论文页：https://openreview.net/forum?id=tJ_CO8orSI
- 摘要来源：https://neurips.cc/virtual/2021/poster/26808
- 本地 PDF：[打开](../../pdfs/NeurIPS/2021/neurips-2021-tJ_CO8orSI__Adjusting_for_Autocorrelated_Errors_in_Neural_Networks_for_Time_Series.pdf)；版本：publisher_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；Macro Indicators & Policy / 宏观指标与政策
- 技术方法标签：未明确标注
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

M4-competition (M4-Yearly, M4-Quarterly, M4-Monthly, M4-Weekly, M4-Daily, M4- Hourly) [42]: re-arranged data from the M4-competition where each dataset consists of series from microeconomics, macroeconomics, financial, industry, demographic, and other. M4-Hourly is used in Conv-T. 6 Table 2: RRMSE for the best grid-searched hyperparameters averaged over ten runs. Best performance in boldface and is superscribed with † if the p-value of paired t-test is lower

## 原始摘要

An increasing body of research focuses on using neural networks to model time series. A common assumption in training neural networks via maximum likelihood estimation on time series is that the errors across time steps are uncorrelated. However, errors are actually autocorrelated in many cases due to the temporality of the data, which makes such maximum likelihood estimations inaccurate. In this paper, in order to adjust for autocorrelated errors, we propose to learn the autocorrelation coefficient jointly with the model parameters. In our experiments, we verify the effectiveness of our approach on time series forecasting. Results across a wide range of real-world datasets with various state-of-the-art models show that our method enhances performance in almost all cases. Based on these results, we suggest empirical critical values to determine the severity of autocorrelated errors. We also analyze several aspects of our method to demonstrate its advantages. Finally, other time series tasks are also considered to validate that our method is not restricted to only forecasting.
