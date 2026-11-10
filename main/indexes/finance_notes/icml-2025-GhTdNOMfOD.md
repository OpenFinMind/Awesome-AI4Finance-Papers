# TimeBase: The Power of Minimalism in Efficient Long-term Time Series Forecasting

ICML 2025 · main · application

实验使用汇率、宏观金融、信用评估或财务文档等金融相关基准。 主题：Time Series / 时间序列；Market Prediction / 股价、收益与波动率预测。

- 官方论文页：https://openreview.net/forum?id=GhTdNOMfOD
- 摘要来源：https://icml.cc/virtual/2025/poster/45815
- 本地 PDF：[打开](../../pdfs/ICML/2025/icml-2025-GhTdNOMfOD__TimeBase_The_Power_of_Minimalism_in_Efficient_Long_term_Time_Series_Forecasting.pdf)；版本：publisher_version
- 金融依据类型：fulltext_financial_benchmark
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；FX & Crypto Forecasts / 汇率与加密资产预测
- 技术方法标签：未明确标注
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/hqh0728/TimeBase}.

## 纳入依据

et al., 2018), Wind (Li et al., 2022), , METR-LA (Li et al., G = X⊤ basis Xbasis (5) 2017), Exchange Rate (Lai et al., 2018), ZafNoo (Poy- atos et al., 2020) and CzeLan (Poyatos et al., 2020), 2 AQShunyi (Zhang et al., 2017), AQWan (Zhang et al., 2017), Lorth = ∥G − diag(G)∥F (6) and 4 very large datasets: CA (4.52B), GLA (2.02B), GBA

## 原始摘要

Long-term time series forecasting (LTSF) has traditionally relied on  large parameters to capture extended temporal dependencies, resulting in substantial computational costs and inefficiencies in both memory usage and processing time. However, time series data, unlike high-dimensional images or text, often exhibit temporal pattern similarity and  low-rank structures, especially in long-term horizons.  By leveraging this structure, models can be guided to focus on more essential, concise temporal data, improving both accuracy and computational efficiency. In this paper, we introduce TimeBase, an ultra-lightweight network  to harness the power of minimalism in LTSF.  TimeBase 1) extracts core basis temporal components and 2) transforms traditional point-level forecasting into efficient segment-level forecasting, achieving optimal utilization of both data and parameters. Extensive experiments on diverse  real-world datasets show that TimeBase achieves remarkable efficiency and secures competitive forecasting performance. Additionally, TimeBase can also serve as a very effective plug-and-play complexity reducer for any patch-based forecasting models. Code is available at \url{https://github.com/hqh0728/TimeBase}.
