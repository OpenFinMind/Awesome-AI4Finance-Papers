# Signature-Informed Transformer for Asset Allocation

ICML 2026 · main · core

以金融任务或金融数据为核心研究对象。 主题：Portfolio & Investment / 投资组合与投资管理。

- 官方论文页：https://openreview.net/forum?id=eBM5ALLJNx
- 摘要来源：https://icml.cc/virtual/2026/poster/62694
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-eBM5ALLJNx__Signature_Informed_Transformer_for_Asset_Allocation.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_review
- 主方向：Portfolio & Investment / 投资组合与投资管理
- 细分方向：Asset Allocation / 资产配置
- 技术方法标签：Transformer / Transformer模型；Uncertainty & Robustness / 不确定性与鲁棒性；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：optimization；Transformer
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/Yoontae6719/Signature-Informed-Transformer-For-Asset-Allocation

## 纳入依据

We argue this creates a fundamental mismatch where minimizing prediction errors fails to yield robust portfolios. / By directly minimizing the Conditional Value at Risk we ensure the training objective aligns with financial goals.

## 原始摘要

Modern deep learning for asset allocation typically separates forecasting from optimization. We argue this creates a fundamental mismatch where minimizing prediction errors fails to yield robust portfolios. We propose the Signature Informed Transformer to address this by unifying feature extraction and decision making into a single policy. Our model employs path signatures to encode complex path dependencies and introduces a specialized attention mechanism that targets geometric asset relationships. By directly minimizing the Conditional Value at Risk we ensure the training objective aligns with financial goals. We prove that our attention module rigorously amplifies signature derived signals. Experiments across diverse equity universes show our approach significantly outperforms both traditional strategies and advanced forecasting baselines. The code is available at: https://github.com/Yoontae6719/Signature-Informed-Transformer-For-Asset-Allocation
