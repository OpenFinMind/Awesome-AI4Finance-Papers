# Beyond Extrapolation: Knowledge Utilization Paradigm with Bidirectional Inspiration for Time Series Forecasting

ICML 2026 · main · application

实验使用汇率、宏观金融、信用评估或财务文档等金融相关基准。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=XAyI76nJRt
- 摘要来源：https://icml.cc/virtual/2026/poster/63442
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-XAyI76nJRt__Beyond_Extrapolation_Knowledge_Utilization_Paradigm_with_Bidirectional_Inspiration_for_Time_Series_Foreca.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_benchmark
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测
- 技术方法标签：未明确标注
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

ILI 2.347 1.089 2.336 1.086 2.292 1.069 1.580 0.852 1.520 0.825 1.496 0.807 2.438 0.955 2.328 0.984 2.114 0.900 1.383 0.718 1.366 0.713 1.365 0.712 Exchange 0.369 0.418 0.362 0.416 0.313 0.390 0.394 0.426 0.390 0.418 0.371 0.410 0.415 0.440 0.399 0.434 0.383 0.427 0.364 0.403 0.363 0.403 0.358 0.402 making its effect more sensitive to the backbone–horizon Table 2. Performance comparison of retrieval-based continuation construction and PBCC on the ETT datasets with a DL

## 原始摘要

Time-series forecasting is critical in various scenarios, such as energy, transportation, and public health.   However, most existing forecasters rely primarily on one-way inference, \textit{i.e.}, mapping \textbf{history} to \textbf{target}, and overlook the structural information provided by a revised natural chain (``\textbf{history} (model input) --  \textbf{target} (ground-truth output)  --  \textbf{post-target continuation}''). The post-target continuation records how trajectories evolve after the target, which can help stabilize forecasting, but it is not observable at inference time. In this work, we aim to obtain an approximate proxy of the post-target continuation for the current input, providing structural knowledge for bidirectional forecasting. This idea is instantiated as KUP-BI (Knowledge Utilization Paradigm with Bidirectional Inspiration), a new time-series modeling paradigm that distills continuation-style knowledge (as an approximate post-target continuation proxy) from a \emph{train-only} historical library and integrates it into standard forecasting backbones. The input stream and the continuation-proxy stream are fused via a lightweight feature-level gating module. This design does not introduce information beyond what is already contained in the training trajectories; instead, it provides a structured inductive bias that helps backbones exploit typical continuation patterns rather than relying solely on parametric extrapolation. Experimental results on six public datasets show that KUP-BI consistently improves the forecasting performance of state-of-the-art models, with small additional overhead.
