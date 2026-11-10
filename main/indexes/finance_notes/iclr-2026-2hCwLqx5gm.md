# Numerion: A Multi-Hypercomplex Model for Time Series Forecasting

ICLR 2026 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：Exchange benchmark (currency series)。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=2hCwLqx5gm
- 摘要来源：https://iclr.cc/virtual/2026/poster/10011709
- 本地 PDF：[打开](../../pdfs/ICLR/2026/iclr-2026-2hCwLqx5gm__Numerion_A_Multi_Hypercomplex_Model_for_Time_Series_Forecasting.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测
- 技术方法标签：Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

2 Traffic 0.281 0.468 0.298 0.485 0.298 0.485 0.282 0.428 0.300 0.470 0.340 0.521 0.304 0.481 0.426 0.667 0.336 0.620 0.376 0.610 0.383 0.625 Exchange 0.399 0.358 0.432 0.416 0.453 0.391 0.470 0.519 0.464 0.515 0.414 0.379 0.404 0.367 0.707 0.940 0.443 0.416 0.429 0.519 0.414 0.354 Table 1 showcases the comparison results of our method against other approaches, with all outcomes representing the average across four prediction lengths {96, 192, 336, 720}. The complete experi- mental results are detailed in Appendix C. It is evident that our method achieves

## 原始摘要

Many methods aim to enhance time series forecasting by decomposing the series through intricate model structures and prior knowledge, yet they are inevitably limited by computational complexity and the robustness of the assumptions. Our research uncovers that in the complex domain and higher-order hypercomplex spaces, the characteristic frequencies of time series naturally decrease. Leveraging this insight, we propose Numerion, a time series forecasting model based on multiple hypercomplex spaces. Specifically, grounded in theoretical support, we generalize linear layers and activation functions to hypercomplex spaces of arbitrary power-of-two dimensions and introduce a novel Real-Hypercomplex-Real Domain Multi-Layer Perceptron (RHR-MLP) architecture. Numerion utilizes multiple RHR-MLPs to map time series into hypercomplex spaces of varying dimensions, naturally decomposing and independently modeling the series, and adaptively fuses the latent patterns exhibited in different spaces through a dynamic fusion mechanism. Experiments validate the model’s performance, achieving state-of-the-art results on multiple public datasets. Visualizations and quantitative analyses comprehensively demonstrate the ability of multi-dimensional RHR-MLPs to naturally decompose time series and reveal the tendency of higher-dimensional hypercomplex spaces to capture lower-frequency features.
