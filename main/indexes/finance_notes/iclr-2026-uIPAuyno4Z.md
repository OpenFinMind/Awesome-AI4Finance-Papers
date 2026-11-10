# Routing Channel-Patch Dependencies in Time Series Forecasting with Graph Spectral Decomposition

ICLR 2026 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：Exchange benchmark (currency series)。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=uIPAuyno4Z
- 摘要来源：https://iclr.cc/virtual/2026/poster/10006906
- 本地 PDF：[打开](../../pdfs/ICLR/2026/iclr-2026-uIPAuyno4Z__Routing_Channel_Patch_Dependencies_in_Time_Series_Forecasting_with_Graph_Spectral_Decomposition.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测
- 技术方法标签：未明确标注
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/Clearloveyuan/xCPD].

## 纳入依据

0.209 0.083 0.203 0.083 0.206 0.081 0.202 0.088 0.205 0.083 0.201 0.107 0.234 0.103 0.228 Electricity Weather Solar-Eng. Exchange 192 0.195 0.315 0.173 0.296 0.153 0.286 0.150 0.283 0.176 0.299 0.168 0.294 0.226 0.344 0.221 0.335 336 0.343 0.421 0.304 0.399 0.289 0.404 0.266 0.386 0.301 0.397 0.297 0.392 0.367 0.448 0.356 0.439 720 0.898 0.710

## 原始摘要

Time series forecasting has attracted significant attention in the field of AI. Previous works have revealed that the Channel-Independent (CI) strategy improves forecasting performance by modeling each channel individually, but it often suffers from poor generalization and overlooks meaningful inter-channel interactions. Conversely, Channel-Dependent (CD) strategies aggregate all channels, which may introduce irrelevant information and lead to oversmoothing. Despite recent progress, few existing methods offer the flexibility to adaptively balance CI and CD strategies in response to varying channel dependencies. To address this, we propose a generic plugin xCPD, that can adaptively model the channel-patch dependencies from the perspective of graph spectral decomposition. Specifically, xCPD first projects multivariate signals into the frequency domain using a shared graph Fourier basis, and groups patches into low-, mid-, and high-frequency bands based on their spectral energy responses. xCPD then applies a channel-adaptive routing mechanism that dynamically adjusts the degree of inter-channel interaction for each patch, enabling selective activation of frequency-specific experts. This facilitates fine-grained input-aware modeling of smooth trends, local fluctuations, and abrupt transitions. xCPD can be seamlessly integrated on top of existing CI and CD forecasting models, consistently enhancing both accuracy and generalization across benchmarks. The code is available [https://github.com/Clearloveyuan/xCPD].
