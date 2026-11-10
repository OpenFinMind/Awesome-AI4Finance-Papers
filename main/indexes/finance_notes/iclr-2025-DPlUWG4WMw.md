# Operator Deep Smoothing for Implied Volatility

ICLR 2025 · main · core

以金融任务或金融数据为核心研究对象。 主题：Derivatives & Hedging / 衍生品定价与对冲；Trading & Microstructure / 交易与市场微观结构。

- 官方论文页：https://openreview.net/forum?id=DPlUWG4WMw
- 摘要来源：https://iclr.cc/virtual/2025/poster/32104
- 本地 PDF：[打开](../../pdfs/ICLR/2025/iclr-2025-DPlUWG4WMw__Operator_Deep_Smoothing_for_Implied_Volatility.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_review
- 主方向：Derivatives & Hedging / 衍生品定价与对冲
- 细分方向：Option Pricing & PDEs / 期权定价与PDE；Implied Volatility / 隐含波动率曲面；Trading & Execution / 交易策略与执行
- 技术方法标签：Graph Learning / 图学习；Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：S&P 500
- 代码链接：摘要未提供可确认链接

## 纳入依据

We devise a novel method for nowcasting implied volatility based on neural operators.Better known as implied volatility smoothing in the financial industry, nowcasting of implied volatility means constructing a smooth surface that is consistent with the prices presently observed on a given option market.Option price data arises highly dynamically in ever-changing spatial configurations, which poses a major limitation to foundational machine learning approaches using classical neural networks.While large models in language and image processing deliver breakthrough results on vast corpora of raw data, in financial engineering the generalization from big historical datasets has been hindered by the need for considerable data pre-processing.In particular, implied volatility smoothing has remained an instance-by-instance, hands-on process both for neural network-based and traditional parametric strategies.Our general *operator deep smoothing* approach, instead, directly maps observed data to smoothed surfaces.We adapt the graph neural operator architecture to do so with high accuracy on ten years of raw intraday S&P 500 options data, using a single model instance.The trained operator adheres to critical no-arbitrage constraints and is robust with respect to subsampling of inputs (occurring in practice in the context of outlier removal).We provide extensive historical benchmarks and showcase the generalization capability of our approach in a comparison with classical neural networks and SVI, an industry standard parametrization for implied volatility. / The operator deep smoothing approach thus opens up the use of neural networks on large historical datasets in financial engineering.

## 原始摘要

We devise a novel method for nowcasting implied volatility based on neural operators.Better known as implied volatility smoothing in the financial industry, nowcasting of implied volatility means constructing a smooth surface that is consistent with the prices presently observed on a given option market.Option price data arises highly dynamically in ever-changing spatial configurations, which poses a major limitation to foundational machine learning approaches using classical neural networks.While large models in language and image processing deliver breakthrough results on vast corpora of raw data, in financial engineering the generalization from big historical datasets has been hindered by the need for considerable data pre-processing.In particular, implied volatility smoothing has remained an instance-by-instance, hands-on process both for neural network-based and traditional parametric strategies.Our general *operator deep smoothing* approach, instead, directly maps observed data to smoothed surfaces.We adapt the graph neural operator architecture to do so with high accuracy on ten years of raw intraday S&P 500 options data, using a single model instance.The trained operator adheres to critical no-arbitrage constraints and is robust with respect to subsampling of inputs (occurring in practice in the context of outlier removal).We provide extensive historical benchmarks and showcase the generalization capability of our approach in a comparison with classical neural networks and SVI, an industry standard parametrization for implied volatility. The operator deep smoothing approach thus opens up the use of neural networks on large historical datasets in financial engineering.
