# Context is Key: A Benchmark for Forecasting with Essential Textual Information

ICML 2025 · main · application

实验使用汇率、宏观金融、信用评估或财务文档等金融相关基准。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=ih2WuBT1Fn
- 摘要来源：https://icml.cc/virtual/2025/poster/44343
- 本地 PDF：[打开](../../pdfs/ICML/2025/icml-2025-ih2WuBT1Fn__Context_is_Key_A_Benchmark_for_Forecasting_with_Essential_Textual_Information.pdf)；版本：publisher_version
- 金融依据类型：fulltext_financial_benchmark
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；Representation & Foundation Models / 表征与基础模型
- 技术方法标签：Language Models & LLM / 语言模型与LLM
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：LLM；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

0.409 0.465 ETTm2 0.181 0.248 0.315 0.417 Exchange 0.090 0.180 0.322 0.862 Weather 0.179 0.224 0.278 0.354 Electricity 0.198 0.202 0.217 0.257 24 36 48 60 Illness 2.284 2.515 2.5

## 原始摘要

Forecasting is a critical task in decision-making across numerous domains. While historical numerical data provide a start, they fail to convey the complete context for reliable and accurate predictions. Human forecasters frequently rely on additional information, such as background knowledge and constraints, which can efficiently be communicated through natural language. However, in spite of recent progress with LLM-based forecasters, their ability to effectively integrate this textual information remains an open question. To address this, we introduce "Context is Key" (CiK), a time-series forecasting benchmark that pairs numerical data with diverse types of carefully crafted textual context, requiring models to integrate both modalities; crucially, every task in CiK requires understanding textual context to be solved successfully. We evaluate a range of approaches, including statistical models, time series foundation models, and LLM-based forecasters, and propose a simple yet effective LLM prompting method that outperforms all other tested methods on our benchmark. Our experiments highlight the importance of incorporating contextual information, demonstrate surprising performance when using LLM-based forecasting models, and also reveal some of their critical shortcomings. This benchmark aims to advance multimodal forecasting by promoting models that are both accurate and accessible to decision-makers with varied technical expertise.The benchmark can be visualized at https://servicenow.github.io/context-is-key-forecasting/v0.
