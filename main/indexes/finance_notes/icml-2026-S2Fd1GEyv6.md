# From Text to Forecasts: Bridging Modality Gap with Temporal Evolution Semantic Space

ICML 2026 · main · application

正文包含金融领域数据、模型、实验或分领域评测。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=S2Fd1GEyv6
- 摘要来源：https://icml.cc/virtual/2026/poster/63982
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-S2Fd1GEyv6__From_Text_to_Forecasts_Bridging_Modality_Gap_with_Temporal_Evolution_Semantic_Space.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_domain_data_or_experiment
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测
- 技术方法标签：Language Models & LLM / 语言模型与LLM
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：LLM
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/olivia3395/TESS.

## 纳入依据

0.0125 Text helps (gain > 0) 2024], a financial dataset exhibiting pronounced non- 2.0 0.0100 Text hurts (gain < 0) stationarity, and extract real numerical sequences 1.5

## 原始摘要

Incorporating textual information into time-series forecasting holds promise for addressing event-driven non-stationarity; however, a fundamental modality gap hinders effective fusion: textual descriptions express temporal impacts implicitly and qualitatively, whereas forecasting models rely on explicit and quantitative signals. Through controlled semi-synthetic experiments, we show that existing methods over-attend to redundant tokens and struggle to reliably translate textual semantics into usable numerical cues. To bridge this gap, we propose \method{}, which introduces a Temporal Evolution Semantic Space as an intermediate bottleneck between modalities. This space consists of interpretable, numerically grounded temporal primitives—mean shift, volatility, shape, and lag—extracted from text by an LLM via structured prompting and filtered through confidence-aware gating. Experiments on four real-world datasets demonstrate up to a 29\% reduction in forecasting error compared to state-of-the-art uni-modal and multimodal baselines. The code is available at https://anonymous.4open.science/r/MMTSF.
