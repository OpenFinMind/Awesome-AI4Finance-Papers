# HyperIV: Real-time Implied Volatility Smoothing

ICML 2025 · main · core

以金融任务或金融数据为核心研究对象。 主题：Derivatives & Hedging / 衍生品定价与对冲；Trading & Microstructure / 交易与市场微观结构。

- 官方论文页：https://openreview.net/forum?id=o9jtS7HupI
- 摘要来源：https://icml.cc/virtual/2025/poster/44077
- 本地 PDF：[打开](../../pdfs/ICML/2025/icml-2025-o9jtS7HupI__HyperIV_Real_time_Implied_Volatility_Smoothing.pdf)；版本：publisher_version
- 金融依据类型：title_abstract_review
- 主方向：Derivatives & Hedging / 衍生品定价与对冲
- 细分方向：Implied Volatility / 隐含波动率曲面；Trading & Execution / 交易策略与执行
- 技术方法标签：Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/qmfin/hyperiv.

## 纳入依据

These key features -- rapid adaptation to market conditions, guaranteed absence of arbitrage, and minimal data requirements -- make HyperIV particularly valuable for real-time trading applications.

## 原始摘要

We propose HyperIV, a novel approach for real-time implied volatility smoothing that eliminates the need for traditional calibration procedures. Our method employs a hypernetwork to generate parameters for a compact neural network that constructs complete volatility surfaces within 2 milliseconds, using only 9 market observations. Moreover, the generated surfaces are guaranteed to be free of static arbitrage. Extensive experiments across 8 index options demonstrate that HyperIV achieves superior accuracy compared to existing methods while maintaining computational efficiency. The model also exhibits strong cross-asset generalization capabilities, indicating broader applicability across different market instruments. These key features -- rapid adaptation to market conditions, guaranteed absence of arbitrage, and minimal data requirements -- make HyperIV particularly valuable for real-time trading applications. We make code available at https://github.com/qmfin/hyperiv.
