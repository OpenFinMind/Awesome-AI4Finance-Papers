# ProtoTS: Learning Hierarchical Prototypes for Explainable Time Series Forecasting

ICLR 2026 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：Exchange benchmark (currency series)。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=IbcdVwzLrp
- 摘要来源：https://iclr.cc/virtual/2026/poster/10010284
- 本地 PDF：[打开](../../pdfs/ICLR/2026/iclr-2026-IbcdVwzLrp__ProtoTS_Learning_Hierarchical_Prototypes_for_Explainable_Time_Series_Forecasting.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测
- 技术方法标签：未明确标注
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：time series
- 数据 / 评测名称（题名和摘要可确认）：finer
- 代码链接：https://github.com/SKURA502/ProtoTS.

## 纳入依据

0.085 0.205 0.090 0.209 0.086 0.206 0.093 0.217 0.088 0.205 0.256 0.367 0.094 0.218 0.107 0.234 0.088 0.218 0.267 0.396 0.111 0.237 0.197 0.323 Exchange 192 0.173 0.299 0.190 0.309 0.177 0.299 0.184 0.307 0.176 0.299 0.470 0.509 0.184 0.307 0.226 0.344 0.176 0.315 0.351 0.459 0.219 0.335 0.300 0.369 336 0.339 0.424 0.371 0.439 0.331 0.417 0.351 0.432 0.301 0.397 1.268 0.883 0.349 0.431 0.367 0.448 0.313 0.427 1.324 0.853 0.421 0.476 0.509 0.524 720 0.923 0.726 0.900 0.714 0.847 0.691 0.886 0.714 0.901 0.

## 原始摘要

While deep learning has achieved impressive performance in time series forecasting, it becomes increasingly crucial to understand its decision-making process for building trust in high-stakes scenarios. Existing interpretable models often provide only local and partial explanations, lacking the capability to reveal how heterogeneous and interacting input variables jointly shape the overall temporal patterns in the forecast curve. We propose ProtoTS, a novel interpretable forecasting framework that achieves both high accuracy and transparent decision-making through modeling prototypical temporal patterns. ProtoTS computes instance-prototype similarity based on a denoised representation that preserves abundant heterogeneous information. The prototypes are organized hierarchically to capture global temporal patterns with coarse prototypes while capturing finer-grained local variations with detailed prototypes, enabling expert steering and multi-level interpretability. Experiments on multiple realistic benchmarks, including a newly released LOF dataset, show that ProtoTS not only exceeds existing methods in forecast accuracy but also delivers expert-steerable interpretations for better model understanding and decision support. The source code is available at https://github.com/SKURA502/ProtoTS.
