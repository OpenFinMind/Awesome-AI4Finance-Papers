# Channel Normalization for Time Series Channel Identification

ICML 2025 · main · application

实验使用汇率、宏观金融、信用评估或财务文档等金融相关基准。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=PqpPrlAQqa
- 摘要来源：https://icml.cc/virtual/2025/poster/45365
- 本地 PDF：[打开](../../pdfs/ICML/2025/icml-2025-PqpPrlAQqa__Channel_Normalization_for_Time_Series_Channel_Identification.pdf)；版本：publisher_version
- 金融依据类型：fulltext_financial_benchmark
- 主方向：Time Series / 时间序列
- 细分方向：General Time-Series Methods / 综合序列方法
- 技术方法标签：未明确标注
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/seunghan96/CN](https://github.com/seunghan96/CN

## 纳入依据

PEMS08 .254 .306 .159 .223 .153 .221 37.4% 39.8% .277 .333 .247 .308 .187 .279 10.8% 32.5% Exchange .368 .409 .352 .401 .349 .398 4.4% 5.2% .356 .403 .355 .400 .353 .399 0.3% 0.8% Weather .260 .281 .247 .273 .245 .271 5.0% 5.8% .272 .292 .249 .274 .246 .273 8.5% 9.6% Solar .234 .261 .228 .258 .220 .253 2.6% 6.0% .261 .313 .248 .276 .242 .277 5.0%

## 原始摘要

Channel identifiability (CID) refers to the ability to distinguish among individual channels in time series (TS) modeling. The absence of CID often results in producing identical outputs for identical inputs, disregarding channel-specific characteristics. In this paper, we highlight the importance of CID and propose Channel Normalization (CN), a simple yet effective normalization strategy that enhances CID by assigning distinct affine transformation parameters to each channel. We further extend CN in two ways: 1) Adaptive CN (ACN) dynamically adjusts parameters based on the input TS, improving adaptability in TS models, and 2) Prototypical CN (PCN) introduces a set of learnable prototypes instead of per-channel parameters, enabling applicability to datasets with unknown or varying number of channels and facilitating use in TS foundation models. We demonstrate the effectiveness of CN and its variants by applying them to various TS models, achieving significant performance gains for both non-CID and CID models. In addition, we analyze the success of our approach from an information theory perspective. Code is available at [https://github.com/seunghan96/CN](https://github.com/seunghan96/CN).
