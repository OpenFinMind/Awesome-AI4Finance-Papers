# Dynamic Dual-Feedback Conformal Inference for Time Series Forecasting

NeurIPS 2026 · main · application

正文包含金融数据、金融训练数据、金融任务评测或具体金融场景案例。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=3lps4PsA4p
- 摘要来源：https://neurips.cc/virtual/2026/poster/155680
- 本地 PDF：[打开](../../pdfs/NeurIPS/2026/neurips-2026-3lps4PsA4p__Dynamic_Dual_Feedback_Conformal_Inference_for_Time_Series_Forecasting.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；Probabilistic Forecasting & Calibration / 概率预测与校准
- 技术方法标签：Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Conformal；conformal；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

iance penalty bounded by O(ϵ/ (w)). 5 Experiments 5.1 Settings Datasets. Three synthetic datasets (described in the Section 5.2.1) and five public datasets are used to evaluate methods (Google/Amazon/Microsoft stock price, Delhi temperature and Electricity, described in the Appendix B.1). Due to the limit of pages, the results and analysis for Delhi temperature and Electricity datasets are given in the Appendix B.2.1. Underlying Time Series Forecasting Algorithms. Four algorithms are used: Prophet [39], AutoRe- gressive (AR) [14], Theta [8] and Transformer [41]. Th

## 原始摘要

Quantifying uncertainty in time series forecasting is particularly demanding because sequential data exhibit temporal dependence and are prone to distributional changes. Conformal inference has emerged as a powerful uncertainty quantification approach through the construction of prediction sets. Recent advances have introduced online conformal methods that adaptively adjust prediction thresholds through feedback mechanisms. However, the existing feedback mechanism typically relies solely on miscoverage indicators (actual feedback)—whether the true label falls within the interval at each time step—while overlooking the empirical prediction threshold (estimated feedback) that is derived from the oracle conformal method. In this paper, we propose $\textit{Dynamic Dual-feedback Conformal Inference}$ (DDCI), which incorporates a dual-feedback mechanism consisting of $\textit{actual feedback}$ and $\textit{estimated feedback}$. The former drives the primary adjustment of the intervals based on true observations, while the latter dampens excessive expansions or contractions by leveraging empirical thresholds from conformal inference during updates. By balancing these two signals, DDCI achieves more stable and narrower prediction intervals in sequential settings while adhering to the target coverage rate in practice.
