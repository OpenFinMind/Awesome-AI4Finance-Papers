# SCINet: Time Series Modeling and Forecasting with Sample Convolution and Interaction

NeurIPS 2022 · main · application

实验使用汇率、宏观金融、信用评估或财务文档等金融相关基准。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=AyajSjTAzmg
- 摘要来源：https://neurips.cc/virtual/2022/poster/53511
- 本地 PDF：[打开](../../pdfs/NeurIPS/2022/neurips-2022-AyajSjTAzmg__SCINet_Time_Series_Modeling_and_Forecasting_with_Sample_Convolution_and_Interaction.pdf)；版本：publisher_version
- 金融依据类型：fulltext_financial_benchmark
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；Causality & Dynamics / 序列因果与动力学
- 技术方法标签：Transformer / Transformer模型
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：time series；Transformer
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/cure-lab/SCINet.

## 纳入依据

0.9787 0.0400 0.9458 0.1392 0.9473 0.0689 0.9759 0.0217 0.9693 0.0202 0.9712 0.0226 0.9735 0.0174 0.979 1.72% Exchange 6 0.0240 0.9704 0.0481 0.9197 0.1548 0.9207 0.0806 0.9671 0.0263 0.9633 0.0257 0.9628 0.0280 0.9658 0.0241 0.9709 0.41% Rate 12 0.0331 0.9553 0.0638 0.9054 0.1793 0.8817 0.0893 0.9476 0.0393 0.9531 0.0352 0.9501 0.0356 0.9511 0.0341 0.9564 2.93% 24 0.0436 0.9396 0.0651 0.8952 0.1998 0.7715 0.1

## 原始摘要

One unique property of time series is that the temporal relations are largely preserved after downsampling into two sub-sequences. By taking advantage of this property, we propose a novel neural network architecture that conducts sample convolution and interaction for temporal modeling and forecasting, named SCINet. Specifically, SCINet is a recursive downsample-convolve-interact architecture. In each layer, we use multiple convolutional filters to extract distinct yet valuable temporal features from the downsampled sub-sequences or features. By combining these rich features aggregated from multiple resolutions, SCINet effectively models time series with complex temporal dynamics. Experimental results show that SCINet achieves significant forecasting accuracy improvements over both existing convolutional models and Transformer-based solutions across various real-world time series forecasting datasets. Our codes and data are available at https://github.com/cure-lab/SCINet.
