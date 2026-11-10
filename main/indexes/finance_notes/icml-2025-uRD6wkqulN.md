# BRIDGE: Bootstrapping Text to Control Time-Series Generation via Multi-Agent Iterative Optimization and Diffusion Modeling

ICML 2025 · main · application

实验使用汇率、宏观金融、信用评估或财务文档等金融相关基准。 主题：Time Series / 时间序列；Macro & Economic Forecasting / 宏观经济与预测。

- 官方论文页：https://openreview.net/forum?id=uRD6wkqulN
- 摘要来源：https://icml.cc/virtual/2025/poster/43728
- 本地 PDF：[打开](../../pdfs/ICML/2025/icml-2025-uRD6wkqulN__BRIDGE_Bootstrapping_Text_to_Control_Time_Series_Generation_via_Multi_Agent_Iterative_Optimization_and_Di.pdf)；版本：publisher_version
- 金融依据类型：fulltext_financial_benchmark
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；Generation & Simulation / 序列生成与仿真；Macro Indicators & Policy / 宏观指标与政策
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Diffusion & Flow / 扩散与流模型；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：LLM；Multi-Agent；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

NN5 0.591 ± 0.029 0.628 ± 0.021 0.748 ± 0.134 1.424 ± 0.043 2.758 ± 0.142 2.121 ± 0.094 2.871 ± 0.045 Fred-MD 0.258 ± 0.045 0.271 ± 0.056 0.359 ± 0.097 2.932 ± 0.133 4.028 ± 0.130 4.026 ± 0.087 2.902 ± 0.215 Exchange 0.374 ± 0.053 0.376 ± 0.058 0.382 ± 0.041 0.993 ± 0.058 1.553 ± 0.122 1.355 ± 0.072 1.331 ± 0.042 Electricity 0.011 ± 0.010 0.014 ± 0.013 0.01

## 原始摘要

Time-series Generation (TSG) is a prominent research area with broad applications in simulations, data augmentation, and counterfactual analysis. While existing methods have shown promise in unconditional single-domain TSG, real-world applications demand for cross-domain approaches capable of controlled generation tailored to domain-specific constraints and instance-level requirements. In this paper, we argue that text can provide semantic insights, domain information and instance-specific temporal patterns, to guide and improve TSG.  We introduce ``Text-Controlled TSG'', a task focused on generating realistic time series by incorporating textual descriptions.To address data scarcity in this setting, we propose a novel LLM-based Multi-Agent framework that synthesizes diverse, realistic text-to-TS datasets. Furthermore, we introduce Bridge, a hybrid text-controlled TSG framework that integrates semantic prototypes with text description for supporting domain-level guidance. This approach achieves state-of-the-art generation fidelity on 11 of 12 datasets, and improves controllability by up to 12% on MSE and 6% MAE compared to no text input generation, highlighting its potential for generating tailored time-series data.
