# TimeRecipe: A Time-Series Forecasting Recipe via Benchmarking Module Level Effectiveness

ICLR 2026 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：Exchange Rate。 主题：Time Series / 时间序列；Market Prediction / 股价、收益与波动率预测。

- 官方论文页：https://openreview.net/forum?id=CsoR8ztROC
- 摘要来源：https://iclr.cc/virtual/2026/poster/10010822
- 本地 PDF：[打开](../../pdfs/ICLR/2026/iclr-2026-CsoR8ztROC__TimeRecipe_A_Time_Series_Forecasting_Recipe_via_Benchmarking_Module_Level_Effectiveness.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；FX & Crypto Forecasts / 汇率与加密资产预测
- 技术方法标签：未明确标注
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Patch MLP 0.8542 10 0.6954 8 9.0 ✓ ✗ Temporal Invert MLP 0.8493 9 0.6958 10 9.5 Table 10: Top-10 configurations for the Exchange Rate dataset multivariate forecasting. IN: Instance Norm, SD: Series Decomposition. ✓ indicates module used, ✗ indicates not used. Red/blue highlights indicate best and second-best performances. 28 Published as a conference paper at ICLR 2026 Setup IN SD Fusion Embed FF-Type MSE Rank MAE Rank Total ✓ ✗

## 原始摘要

Time-series forecasting is an essential task with wide real-world applications across domains. While recent advances in deep learning have enabled time-series forecasting models with accurate predictions, there remains considerable debate over which architectures and design components, such as series decomposition or normalization, are most effective under varying conditions. Existing benchmarks primarily evaluate models at a high level, offering limited insight into why certain designs work better. To mitigate this gap, we propose TIMERECIPE, a unified benchmarking framework that systematically evaluates time-series forecasting methods at the module level. TIMERECIPE conducts over 10,000 experiments to assess the effectiveness of individual components across a diverse range of datasets, forecasting horizons, and task settings. Our results reveal that exhaustive exploration of the design space can yield models that outperform existing state-of-the-art methods and uncover meaningful intuitions linking specific design choices to forecasting scenarios. Furthermore, we release a practical toolkit within TIMERECIPE that recommends suitable model architectures based on these empirical insights.
