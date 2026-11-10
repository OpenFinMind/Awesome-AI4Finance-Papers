# Scaleformer: Iterative Multi-scale Refining Transformers for Time Series Forecasting

ICLR 2023 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：Exchange benchmark (currency series)。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=sCrnllCtjoE
- 摘要来源：https://iclr.cc/virtual/2023/poster/11535
- 本地 PDF：[打开](../../pdfs/ICLR/2023/iclr-2023-sCrnllCtjoE__Scaleformer_Iterative_Multi_scale_Refining_Transformers_for_Time_Series_Forecasting.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测
- 技术方法标签：Transformer / Transformer模型
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：time series；transformer；transformers
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/BorealisAI/scaleformer.

## 纳入依据

192 0.274 0.384 0.241 0.353 0.356 0.428 0.253 0.373 1.088 0.842 0.427 0.484 1.597 1.029 0.375 0.446 1.339 0.904 0.439 0.486 Exchange 336 0.452 0.498 0.471 0.508 0.441 0.495 0.519 0.538 1.598 1.016 0.500 0.535 1.712 1.070 0.605 0.591 1.081 0.844 0.563 0.577 720 1.172 0.839 1.259 0.865 1.118 0.819 0.928 0.751 2.679 1.340 1.017 0.790 1.918 1.160 1.089 0.857 0.867 0.766 1.219 0.882 96 0.288 0.365 0.220 0.289 0.267 0.334 0.163 0.226 0.388 0.435 0.210 0.279 0.347 0.388 0.199

## 原始摘要

The performance of time series forecasting has recently been greatly improved by the introduction of transformers. In this paper, we propose a general multi-scale framework that can be applied to state-of-the-art transformer-based time series forecasting models(FEDformer, Autoformer, etc.). Using iteratively refining a forecasted time series at multiple scales with shared weights, architecture adaptations and a specially-designed normalization scheme, we are able to achieve significant performance improvements with minimal additional computational overhead. Via detailed ablation studies, we demonstrate the effectiveness of our proposed architectural and methodological innovations. Furthermore, our experiments on various public datasets demonstrate that the proposed method outperforms the corresponding baselines. Depending on the choice of transformer architecture, our mutli-scale framework results in mean squared error reductions ranging from 5.5% to 38.5%. Our code is publicly available in https://github.com/BorealisAI/scaleformer.
