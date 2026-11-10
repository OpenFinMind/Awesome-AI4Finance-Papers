# CTBench: Cryptocurrency Time Series Generation Benchmark

ICLR 2026 · main · core

以金融任务或金融数据为核心研究对象。 主题：Time Series / 时间序列；Blockchain & Digital Assets / 区块链与数字资产。

- 官方论文页：https://openreview.net/forum?id=RzT2sombPD
- 摘要来源：https://iclr.cc/virtual/2026/poster/10009451
- 本地 PDF：[打开](../../pdfs/ICLR/2026/iclr-2026-RzT2sombPD__CTBench_Cryptocurrency_Time_Series_Generation_Benchmark.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_review
- 主方向：Time Series / 时间序列
- 细分方向：Generation & Simulation / 序列生成与仿真；Crypto & Blockchain Transactions / 加密资产与链上交易
- 技术方法标签：Generative Modeling / 生成建模
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Time Series；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/MilleXi/CTBench/}.

## 纳入依据

Synthetic time series are vital for data augmentation, stress testing, and prototyping in quantitative finance. / Yet in cryptocurrency markets, characterized by 24/7 trading, extreme volatility, and rapid regime shifts, existing Time Series Generation (TSG) methods and benchmarks often fall short, jeopardizing practical utility. / Most prior work targets non-financial or traditional financial domains, focuses narrowly on classification and forecasting while neglecting crypto-specific complexities, and lacks critical financial evaluations, particularly for trading applications. / It curates an open-source dataset of 452 tokens and evaluates models across 13 metrics spanning forecasting accuracy, rank fidelity, trading performance, risk assessment, and computational efficiency. / A key innovation is a dual-task evaluation framework: the Predictive Utility measures how well synthetic data preserves temporal and cross-sectional patterns for forecasting, while the Statistical Arbitrage assesses whether reconstructed series support mean-reverting signals for trading. / Notably, CTBench provides ranking analysis and practical guidance for deploying TSG models in crypto analytics and trading applications.

## 原始摘要

Synthetic time series are vital for data augmentation, stress testing, and prototyping in quantitative finance. Yet in cryptocurrency markets, characterized by 24/7 trading, extreme volatility, and rapid regime shifts, existing Time Series Generation (TSG) methods and benchmarks often fall short, jeopardizing practical utility. Most prior work targets non-financial or traditional financial domains, focuses narrowly on classification and forecasting while neglecting crypto-specific complexities, and lacks critical financial evaluations, particularly for trading applications. To bridge these gaps, we introduce \textbf{CTBench}, the first \textbf{C}ryptocurrency \textbf{T}ime series generation \textbf{Bench}mark. It curates an open-source dataset of 452 tokens and evaluates models across 13 metrics spanning forecasting accuracy, rank fidelity, trading performance, risk assessment, and computational efficiency. A key innovation is a dual-task evaluation framework: the Predictive Utility measures how well synthetic data preserves temporal and cross-sectional patterns for forecasting, while the Statistical Arbitrage assesses whether reconstructed series support mean-reverting signals for trading. We systematically benchmark eight state-of-the-art models from five TSG families across four market regimes, revealing trade-offs between statistical quality and real-world profitability. Notably, CTBench provides ranking analysis and practical guidance for deploying TSG models in crypto analytics and trading applications. The source code is available at \url{https://github.com/MilleXi/CTBench/}.
