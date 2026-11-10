# A Set-Sequence Model for Time Series

NeurIPS 2026 · main · core

以金融任务或金融数据为核心研究对象。 主题：Time Series / 时间序列；Portfolio & Investment / 投资组合与投资管理；Market Prediction / 股价、收益与波动率预测；Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=y1ZoyGsVuL
- 摘要来源：https://neurips.cc/virtual/2026/poster/148413
- 本地 PDF：[打开](../../pdfs/NeurIPS/2026/neurips-2026-y1ZoyGsVuL__A_Set_Sequence_Model_for_Time_Series.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_review
- 主方向：Time Series / 时间序列
- 细分方向：General Time-Series Methods / 综合序列方法；Portfolio Selection & Optimization / 组合选择与优化；Stock Movement & Returns / 股价方向与收益预测；Lending & Credit Data / 借贷与信贷数据应用
- 技术方法标签：Transformer / Transformer模型；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：optimization；Time Series；Transformer
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Many practical settings, however, involve predicting the evolution of a set of MTSs -- an unordered collection of units (e.g., a basket of stocks, a pool of loans, a fleet of sensors). / Across a synthetic contagion task and two large-scale real-world applications -- equity portfolio optimization and loan risk prediction -- Set-Sequence consistently improves sequence backbones and outperforms domain-specific baselines, delivering higher Sharpe ratios, improved AUCs, and interpretable cross-sectional summaries.

## 原始摘要

Sequence models have advanced Multivariate Time Series (MTS) modeling by learning complex, long-range temporal dependencies. Many practical settings, however, involve predicting the evolution of a set of MTSs -- an unordered collection of units (e.g., a basket of stocks, a pool of loans, a fleet of sensors). This cross-sectional structure offers an opportunity to leverage signals shared across units (e.g., market volatility, correlated defaults) that are missed when each MTS is processed independently. Crucially, treating the entire cross-section as a single high-dimensional MTS is infeasible because the number of units varies dynamically at inference. We propose Set-Sequence, a backbone-agnostic architecture for set-of-MTS prediction that leverages this cross-sectional structure. A permutation-invariant Set module extracts a summary of the population, while a Sequence module (e.g., Transformer/SSM/RNN) then models each unit’s temporal dynamics conditioned on both its own history and the learned cross-sectional context. This architecture naturally accommodates varying set cardinalities, supports unaligned series, integrates with standard sequence backbones, and scales linearly in cross-sectional size. Across a synthetic contagion task and two large-scale real-world applications -- equity portfolio optimization and loan risk prediction -- Set-Sequence consistently improves sequence backbones and outperforms domain-specific baselines, delivering higher Sharpe ratios, improved AUCs, and interpretable cross-sectional summaries.
