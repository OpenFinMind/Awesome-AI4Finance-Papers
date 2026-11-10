# AdaST: Adaptive Coupling for Spatial-Temporal Forecasting

NeurIPS 2026 · main · application

正文包含金融数据、金融训练数据、金融任务评测或具体金融场景案例。 主题：Time Series / 时间序列；Market Prediction / 股价、收益与波动率预测。

- 官方论文页：https://openreview.net/forum?id=2IWnVy1qoe
- 摘要来源：https://neurips.cc/Downloads/2026
- 本地 PDF：[打开](../../pdfs/NeurIPS/2026/neurips-2026-2IWnVy1qoe__AdaST_Adaptive_Coupling_for_Spatial_Temporal_Forecasting.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Market Prediction / 股价、收益与波动率预测
- 细分方向：Forecasting / 序列预测；FX & Crypto Forecasts / 汇率与加密资产预测
- 技术方法标签：未明确标注
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

16 C Additional Main Results We conduct additional experiments on three diverse dataset categories to further validate AdaST’s generalizability: ExchangeRate (financial), ETTh1 (energy), and METR-LA (highway traffic). We ex- pand the baseline comparison to include two state-of-the-art time-series-only methods, PatchTST [24] and DLinear [45]. For spatial-temporal baselines that require a predefined graph structure, we only compare against STID, HimNet, and STNorm, which operate without predefined graphs. Since som

## 原始摘要

Spatial-temporal (ST) forecasting underpins many real-world systems such as traffic, climate, and energy networks. While existing methods implicitly assume strong spatiotemporal coupling, we observe that real-world ST data exhibits distinct coupling regimes, ranging from temporal-dominated and spatial-dominated to strongly coupled patterns. This mismatch causes current models to suffer from spurious dependencies and degraded performance when one correlation dominates. To overcome this limitation, we aim to dynamically modulate spatial and temporal modeling based on the data's inherent coupling structure. However, three key challenges exist: unknown coupling structure, heterogeneous coupling dynamics, and suboptimal spatial modeling. We propose AdaST, an adaptive ST forecasting framework that tackles these challenges through a decompose-recompose paradigm. AdaST factorizes inputs into components capturing different coupling patterns using heterogeneity-aware experts. Each component is processed by role-aligned modules, and a correlation-informed adaptive recomposer integrates them for final prediction. Extensive experiments confirm that AdaST significantly outperforms state-of-the-art baselines, validating the necessity of an adaptive approach.
