# CARD: Channel Aligned Robust Blend Transformer for Time Series Forecasting

ICLR 2024 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：M4 Weekly。M4 年度至日度子集包含金融序列，未把仅使用 M4 Hourly 的论文据此纳入。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=MJksrOhurE
- 摘要来源：https://iclr.cc/virtual/2024/poster/18830
- 本地 PDF：[打开](../../pdfs/ICLR/2024/iclr-2024-MJksrOhurE__CARD_Channel_Aligned_Robust_Blend_Transformer_for_Time_Series_Forecasting.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测
- 技术方法标签：Transformer / Transformer模型；Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：time series；transformer；Transformer
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/wxie9/CARD.

## 纳入依据

ride model dim FFN dim dropout blend size learning rate warm-up batch size M4 Hourly 16 1 128 512 0.1 2 5e-4 0 128 M4 Weekly 16 1 128 512 0.1 2 5e-4 0 128 M4 Daily 16 1 128 512 0.1 2 5e-4 0 128 M4 Monthly 16 1 128 512 0.1 2 5e-4 0 128 M4 Quarterly 4 1 128 512 0.1 2 5e-4 0 128

## 原始摘要

Recent studies have demonstrated the great power of Transformer models for time series forecasting. One of the key elements that lead to the transformer's success is the channel-independent (CI) strategy to improve the training robustness. However, the ignorance of the correlation among different channels in CI would limit the model's forecasting capacity. In this work, we design a special Transformer, i.e., **C**hannel **A**ligned **R**obust Blen**d**  Transformer (CARD for short), that addresses key shortcomings of CI type Transformer in time series forecasting. First, CARD introduces a channel-aligned attention structure that allows it to capture both temporal correlations among signals and dynamical dependence among multiple variables over time. Second, in order to efficiently utilize the multi-scale knowledge, we design a token blend module to generate tokens with different resolutions. Third, we introduce a robust loss function for time series forecasting to alleviate the potential overfitting issue. This new loss function weights the importance of forecasting over a finite horizon based on prediction uncertainties. Our evaluation of multiple long-term and short-term forecasting datasets demonstrates that CARD significantly outperforms state-of-the-art time series forecasting methods. The code is available at the following repository: https://github.com/wxie9/CARD.
