# Learning Latent Seasonal-Trend Representations for Time Series Forecasting

NeurIPS 2022 · main · application

实验使用汇率、宏观金融、信用评估或财务文档等金融相关基准。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=C9yUwd72yy
- 摘要来源：https://neurips.cc/virtual/2022/poster/55179
- 本地 PDF：[打开](../../pdfs/NeurIPS/2022/neurips-2022-C9yUwd72yy__Learning_Latent_Seasonal_Trend_Representations_for_Time_Series_Forecasting.pdf)；版本：publisher_version
- 金融依据类型：fulltext_financial_benchmark
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；Representation & Foundation Models / 表征与基础模型
- 技术方法标签：Generative Modeling / 生成建模；Transformer / Transformer模型；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：time series；Transformer；variational
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

0.033 0.122 0.033 0.127 0.108 0.252 0.105 0.236 0.064 0.178 0.060 0.178 0.611 0.626 2.483 1.327 Exchange 48 0.056 0.162 0.058 0.165 0.200 0.341 0.162 0.270 0.133 0.262 0.091 0.222 0.680 0.644 2.328 1.256 168 0.190 0.320 0.198 0.327 0.412 0.492 0.397 0.480 0.334 0.432 0.405 0.473 1.097 0.825 2.372 1.279 336 0.430 0.482 0.512 0.523 1.339 0.901 1.008 0.8

## 原始摘要

Forecasting complex time series is ubiquitous and vital in a range of applications but challenging. Recent advances endeavor to achieve progress by incorporating various deep learning techniques (e.g., RNN and Transformer) into sequential models. However, clear patterns are still hard to extract since time series are often composed of several intricately entangled components. Motivated by the success of disentangled variational autoencoder in computer vision and classical time series decomposition, we plan to infer a couple of representations that depict seasonal and trend components of time series. To achieve this goal, we propose LaST, which, based on variational inference, aims to disentangle the seasonal-trend representations in the latent space. Furthermore, LaST supervises and disassociates representations from the perspectives of themselves and input reconstruction, and introduces a series of auxiliary objectives. Extensive experiments prove that LaST achieves state-of-the-art performance on time series forecasting task against the most advanced representation learning and end-to-end forecasting models. For reproducibility, our implementation is publicly available on Github.
