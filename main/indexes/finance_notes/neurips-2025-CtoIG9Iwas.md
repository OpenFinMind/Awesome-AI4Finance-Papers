# Learning Pattern-Specific Experts for Time Series Forecasting Under Patch-level Distribution Shift

NeurIPS 2025 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：Exchange benchmark (currency series)。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=CtoIG9Iwas
- 摘要来源：https://neurips.cc/virtual/2025/poster/119258
- 本地 PDF：[打开](../../pdfs/NeurIPS/2025/neurips-2025-CtoIG9Iwas__Learning_Pattern_Specific_Experts_for_Time_Series_Forecasting_Under_Patch_level_Distribution_Shift.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测
- 技术方法标签：Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Time series；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/syrGitHub/TFPS.

## 纳入依据

0.206 0.088 0.210 0.086 0.206 0.084 0.205 0.089 0.206 0.105 0.233 0.089 0.219 0.136 0.265 Exchange 192 11.2% 0.174 0.297 0.178 0.300 0.181 0.304 0.181 0.304 0.176 0.299 0.178 0.302 0.219 0.342 0.180 0.319 0.279 0.384 336 10.4% 0.310 0.398 0.329 0.415 0.324 0.413 0.338 0.422 0.321 0.409 0.326 0.411 0.353 0.433 0.313 0.423 0.465

## 原始摘要

Time series forecasting, which aims to predict future values based on historical data, has garnered significant attention due to its broad range of applications. However, real-world time series often exhibit heterogeneous pattern evolution across segments, such as seasonal variations, regime changes, or contextual shifts, making accurate forecasting challenging. Existing approaches, which typically train a single model to capture all these diverse patterns, often struggle with the pattern drifts between patches and may lead to poor generalization. To address these challenges, we propose TFPS, a novel architecture that leverages pattern-specific experts for more accurate and adaptable time series forecasting. TFPS employs a dual-domain encoder to capture both time-domain and frequency-domain features, enabling a more comprehensive understanding of temporal dynamics. It then performs subspace clustering to dynamically identify distinct patterns across data segments. Finally, these patterns are modeled by specialized experts, allowing the model to learn multiple predictive functions. Extensive experiments on real-world datasets demonstrate that TFPS outperforms state-of-the-art methods, particularly on datasets exhibiting significant distribution shifts. The data and code are available: https://github.com/syrGitHub/TFPS.
