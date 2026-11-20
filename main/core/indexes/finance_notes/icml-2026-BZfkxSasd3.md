# Joint-Embedding Predictive Learning of Latent Market States in U.S. Equities

ICML 2026 · main · core

以金融任务或金融数据为核心研究对象。 主题：Time Series / 时间序列；Asset Pricing / 资产定价。

- 官方论文页：https://openreview.net/forum?id=BZfkxSasd3
- 摘要来源：https://icml.cc/virtual/2026/poster/65643
- PDF 状态：access_blocked
- 金融依据类型：title_abstract_review
- 主方向：Time Series / 时间序列
- 细分方向：Representation & Foundation Models / 表征与基础模型；Risk Factor Models / 市场风险因子建模
- 技术方法标签：Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

We jointly train a permutation-invariant tokenizer that maps each trading day's unordered per-asset features to a fixed set of learned factor tokens, together with a temporal JEPA using masked prediction to obtain a compact daily market-state embedding.

## 原始摘要

We investigate whether Joint-Embedding Predictive Architectures (JEPA) can learn useful representations of U.S. equity markets. We jointly train a permutation-invariant tokenizer that maps each trading day's unordered per-asset features to a fixed set of learned factor tokens, together with a temporal JEPA using masked prediction to obtain a compact daily market-state embedding. Our evaluations show that these embeddings are strongly associated with second-moment market structure (realized volatility, correlation concentration, effective factor dimensionality) and weakly associated with market direction. The embedding helps predict gradual recovery dynamics but not sudden stress onsets. Without any text supervision, latent regimes show statistically significant alignment with news-topic shifts.

## Classification / 分类

- Primary task / 主方向: Time Series / 时间序列
- Primary subcategory / 主要子分类: Sequence Representation and Pattern Discovery / 序列表示与模式发现
- Related tasks / 关联方向: Time Series / 时间序列; Pricing / 定价
- Subcategories / 子分类: Sequence Representation and Pattern Discovery / 序列表示与模式发现; Asset Pricing and Risk Premia / 资产定价与风险溢价
- Methods / 技术方法: Representation Learning / 表征学习
- Review status / 核对状态: `inherited_evidence_mapping`
- [Definitions / 分类定义](../finance_taxonomy.md) · [Evidence / 分类依据](../../checks/finance_taxonomy/assignments.json)
