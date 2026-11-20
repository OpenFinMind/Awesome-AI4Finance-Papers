# The Label Horizon Paradox: Rethinking Supervision Targets in Financial Forecasting

ICML 2026 · main · core

以金融任务或金融数据为核心研究对象。 主题：Market Prediction / 股价、收益与波动率预测。

- 官方论文页：https://openreview.net/forum?id=G43CIfmmxh
- 摘要来源：https://icml.cc/virtual/2026/poster/65178
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-G43CIfmmxh__The_Label_Horizon_Paradox_Rethinking_Supervision_Targets_in_Financial_Forecasting.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_review
- 主方向：Market Prediction / 股价、收益与波动率预测
- 细分方向：Stock Movement & Returns / 股价方向与收益预测
- 技术方法标签：Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：optimization
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

While deep learning has revolutionized financial forecasting through sophisticated architectures, the design of the supervision signal itself is rarely scrutinized. / Extensive experiments on large-scale financial datasets demonstrate consistent improvements over conventional baselines, thereby opening new avenues for label-centric research in financial forecasting.

## 原始摘要

While deep learning has revolutionized financial forecasting through sophisticated architectures, the design of the supervision signal itself is rarely scrutinized. We challenge the canonical assumption that training labels must strictly mirror inference targets, uncovering the Label Horizon Paradox: the optimal supervision signal often deviates from the prediction goal, shifting across intermediate horizons governed by market dynamics. We theoretically ground this phenomenon in a dynamic signal-noise trade-off, demonstrating that generalization hinges on the competition between marginal signal realization and noise accumulation. To operationalize this insight, we propose a bi-level optimization framework that autonomously identifies the optimal proxy label within a single training run. Extensive experiments on large-scale financial datasets demonstrate consistent improvements over conventional baselines, thereby opening new avenues for label-centric research in financial forecasting.

## Classification / 分类

- Primary task / 主方向: Valuation Prediction / 估值预测
- Primary subcategory / 主要子分类: Stock Price and Return Prediction / 股票价格与收益预测
- Related tasks / 关联方向: Valuation Prediction / 估值预测
- Subcategories / 子分类: Stock Price and Return Prediction / 股票价格与收益预测
- Methods / 技术方法: Optimization & Numerical Methods / 优化与数值方法
- Review status / 核对状态: `inherited_evidence_mapping`
- [Definitions / 分类定义](../finance_taxonomy.md) · [Evidence / 分类依据](../../checks/finance_taxonomy/assignments.json)
