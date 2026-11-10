# Hermes: A Multi-Scale Spatial-Temporal Hypergraph Network for Stock Time Series Forecasting

NeurIPS 2026 · main · core

以金融市场为研究对象，或包含明确的金融领域数据和应用评测。 主题：Time Series / 时间序列；Market Prediction / 股价、收益与波动率预测。

- 官方论文页：https://openreview.net/forum?id=nMUDgtUWOF
- 摘要来源：https://neurips.cc/Downloads/2026
- 本地 PDF：[打开](../../pdfs/NeurIPS/2026/neurips-2026-nMUDgtUWOF__Hermes_A_Multi_Scale_Spatial_Temporal_Hypergraph_Network_for_Stock_Time_Series_Forecasting.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_financial_task_or_data
- 主方向：Market Prediction / 股价、收益与波动率预测
- 细分方向：Forecasting / 序列预测；Stock Movement & Returns / 股价方向与收益预测
- 技术方法标签：Graph Learning / 图学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Time series；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Time series forecasting occurs in a range of financial applications providing essential decision-making support to investors, regulatory institutions, and analysts. / Unlike multivariate time series from other domains, stock time series exhibit industry correlation. / This study proposes the \textbf{Hermes} framework for stock time series forecasting that aims to improve the exploitation of industry correlation by addressing these limitations. / Experimental results on multiple real-world stock datasets show that Hermes outperforms existing state-of-the-art methods.

## 原始摘要

Time series forecasting occurs in a range of financial applications providing essential decision-making support to investors, regulatory institutions, and analysts. Unlike multivariate time series from other domains, stock time series exhibit industry correlation. Exploiting this kind of correlation can improve forecasting accuracy. However, existing methods based on hypergraphs can only capture industry correlation relatively superficially. These methods face two key limitations: they do not fully consider inter-industry lead-lag interactions, and they do not model multi-scale information within and among industries. This study proposes the \textbf{Hermes} framework for stock time series forecasting that aims to improve the exploitation of industry correlation by addressing these limitations. The framework integrates moving aggregation and  multi-scale fusion modules in a hypergraph network. Specifically, to more flexibly capture the lead-lag relationships among industries, Hermes proposes a hyperedge-based moving aggregation module. This module incorporates a sliding window and utilizes dynamic temporal aggregation operations to consider lead-lag dependencies among industries. Additionally, to effectively model multi-scale information, Hermes employs cross-scale, edge-to-edge message passing to integrate information from different scales while maintaining the consistency of each scale. Experimental results on multiple real-world stock datasets show that Hermes outperforms existing state-of-the-art methods.
