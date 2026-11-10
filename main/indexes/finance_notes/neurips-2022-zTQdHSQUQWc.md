# FiLM: Frequency improved Legendre Memory Model for Long-term Time Series Forecasting

NeurIPS 2022 · main · application

实验使用汇率、宏观金融、信用评估或财务文档等金融相关基准。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=zTQdHSQUQWc
- 摘要来源：https://neurips.cc/virtual/2022/poster/55013
- 本地 PDF：[打开](../../pdfs/NeurIPS/2022/neurips-2022-zTQdHSQUQWc__FiLM_Frequency_improved_Legendre_Memory_Model_for_Long_term_Time_Series_Forecasting.pdf)；版本：publisher_version
- 金融依据类型：fulltext_financial_benchmark
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测
- 技术方法标签：Transformer / Transformer模型
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：time series；Transformers
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/tianzhou2011/FiLM/.

## 纳入依据

96 0.086 0.204 0.086 0.208 0.087 0.210 Exchange 192 0.188 0.292 0.187 0.318 0.207 0.340 336 0.356 0.433 0.358 0.437 0.353 0.461 720 0.727 0.669 0.788 0.680 0.748 0.674

## 原始摘要

Recent studies have shown that deep learning models such as RNNs and Transformers have brought significant performance gains for long-term forecasting of time series because they effectively utilize historical information. We found, however, that there is still great room for improvement in how to preserve historical information in neural networks while avoiding overfitting to noise present in the history. Addressing this allows better utilization of the capabilities of deep learning models. To this end, we design a Frequency improved Legendre Memory model, or FiLM: it applies Legendre polynomial projections to approximate historical information, uses Fourier projection to remove noise, and adds a low-rank approximation to speed up computation. Our empirical studies show that the proposed FiLM significantly improves the accuracy of state-of-the-art models in multivariate and univariate long-term forecasting by (19.2%, 22.6%), respectively. We also demonstrate that the representation module developed in this work can be used as a general plugin to improve the long-term prediction performance of other deep learning modules. Code is available at  https://github.com/tianzhou2011/FiLM/.
