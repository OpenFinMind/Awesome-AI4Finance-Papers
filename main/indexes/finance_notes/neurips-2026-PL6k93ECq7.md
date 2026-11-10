# Combating Camouflage and Forgetting: Spatio-Temporal Dual Denoising for Money Laundering Detection

NeurIPS 2026 · main · core

以金融市场为研究对象，或包含明确的金融领域数据和应用评测。 主题：Fraud & AML / 欺诈检测与反洗钱。

- 官方论文页：https://openreview.net/forum?id=PL6k93ECq7
- 摘要来源：https://neurips.cc/Downloads/2026
- PDF 状态：access_blocked
- 金融依据类型：title_abstract_financial_task_or_data
- 主方向：Fraud & AML / 欺诈检测与反洗钱
- 细分方向：Payment & Transaction Fraud / 支付与交易欺诈；Anti-Money Laundering / 反洗钱
- 技术方法标签：Graph Learning / 图学习；Transformer / Transformer模型
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Transformer
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Money laundering detection on financial transaction graphs is critical but challenging. / Laundering activities often conceal illicit fund flows within dense legitimate transaction neighborhoods and disperse suspicious behaviors over extended time spans. / In this paper, we propose a spatio-temporal dual denoising framework for money laundering detection on evolving graphs, named EvoDen. / For spatial denoising, instead of relying on passive neighborhood aggregation, we design a risk-potential guided walk mechanism to extract denoised and suspicion-biased transaction sequences, enabling the model to isolate anomalous fund flows from noisy local neighborhoods. / We conduct experiments on three transaction datasets, and the results show that EvoDen outperforms state-of-the-art baselines in accurately identifying concealed money laundering entities.

## 原始摘要

Money laundering detection on financial transaction graphs is critical but challenging. Laundering activities often conceal illicit fund flows within dense legitimate transaction neighborhoods and disperse suspicious behaviors over extended time spans. These patterns cause weak illicit signals to be spatially diluted and temporally forgotten, limiting the effectiveness of standard graph learning methods in AML scenarios. In this paper, we propose a spatio-temporal dual denoising framework for money laundering detection on evolving graphs, named EvoDen. For spatial denoising, instead of relying on passive neighborhood aggregation, we design a risk-potential guided walk mechanism to extract denoised and suspicion-biased transaction sequences, enabling the model to isolate anomalous fund flows from noisy local neighborhoods. For temporal denoising, we propose a continual Transformer-based sequence learning method driven by a reconstruction objective, which learns denoised sequence representations while enabling latent-space replay of historical knowledge to mitigate representation drift. We conduct experiments on three transaction datasets, and the results show that EvoDen outperforms state-of-the-art baselines in accurately identifying concealed money laundering entities.
