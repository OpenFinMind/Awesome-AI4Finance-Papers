# OLinear: A Linear Model for Time Series Forecasting in Orthogonally Transformed Domain

NeurIPS 2025 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：NASDAQ。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=DAyKP1tvwI
- 摘要来源：https://neurips.cc/virtual/2025/poster/119234
- 本地 PDF：[打开](../../pdfs/NeurIPS/2025/neurips-2025-DAyKP1tvwI__OLinear_A_Linear_Model_for_Time_Series_Forecasting_in_Orthogonally_Transformed_Domain.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；Representation & Foundation Models / 表征与基础模型
- 技术方法标签：Transformer / Transformer模型；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：time series；Transformer
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/jackyue1994/OLinear.

## 纳入依据

Datasets and implementation details We extensively evaluate OLinear using 24 diverse real- world datasets: ETT (four subsets), Weather, ECL, Traffic, Exchange, Solar-Energy, PEMS (four subsets), ILI, COVID-19, METR-LA, NASDAQ, Wiki, SP500, DowJones, CarSales, Power, Website, Unemp. The weighted L1 loss function from CARD [Wang et al., 2024b] is adopted. The embedding size d is set as 16. Dataset description and more implementation details are presented in Appendices C and D, respectively. 5.1 Forecasting performance Baselines We carefully choose 11 well-acknowledg

## 原始摘要

This paper presents $\mathbf{OLinear}$, a $\mathbf{linear}$-based multivariate time series forecasting model that operates in an $\mathbf{o}$rthogonally transformed domain. Recent forecasting models typically adopt the temporal forecast (TF) paradigm, which directly encode and decode time series in the time domain. However, the entangled step-wise dependencies in series data can hinder the performance of TF. To address this, some forecasters conduct encoding and decoding in the transformed domain using fixed, dataset-independent bases (e.g., sine and cosine signals in the Fourier transform). In contrast, we propose $\mathbf{OrthoTrans}$, a data-adaptive transformation based on an orthogonal matrix that diagonalizes the series' temporal Pearson correlation matrix. This approach enables more effective encoding and decoding in the decorrelated feature domain and can serve as a plug-in module to enhance existing forecasters. To enhance the representation learning for multivariate time series, we introduce a customized linear layer, $\mathbf{NormLin}$, which employs a normalized weight matrix to capture multivariate dependencies. Empirically, the NormLin module shows a surprising performance advantage over multi-head self-attention, while requiring nearly half the FLOPs. Extensive experiments on 24 benchmarks and 140 forecasting tasks demonstrate that OLinear consistently achieves state-of-the-art performance with high efficiency. Notably, as a plug-in replacement for self-attention, the NormLin module consistently enhances Transformer-based forecasters. The code and datasets are available at https://github.com/jackyue1994/OLinear.
