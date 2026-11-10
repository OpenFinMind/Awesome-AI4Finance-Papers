# REGATE: Confidence-Calibrated Integration of Temporally-Aligned Exogenous Texts for Dynamic Graphs

NeurIPS 2026 · main · core

以金融任务或金融数据为核心研究对象。 主题：Fraud & AML / 欺诈检测与反洗钱。

- 官方论文页：https://openreview.net/forum?id=hi0wCR0EYw
- 摘要来源：https://neurips.cc/virtual/2026/poster/150490
- PDF 状态：access_blocked
- 金融依据类型：title_abstract_review
- 主方向：Fraud & AML / 欺诈检测与反洗钱
- 细分方向：Payment & Transaction Fraud / 支付与交易欺诈
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Graph Learning / 图学习；Causal Learning / 因果学习；Uncertainty & Robustness / 不确定性与鲁棒性；Retrieval & RAG / 检索与RAG；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：causal；LLM；retrieval
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Risk assessment and anomaly detection in financial interaction networks often fail under regime shifts triggered by external events such as policy changes or enforcement actions—models may retain high AUC yet suffer sharp drops in average precision and calibration.

## 原始摘要

Risk assessment and anomaly detection in financial interaction networks often fail under regime shifts triggered by external events such as policy changes or enforcement actions—models may retain high AUC yet suffer sharp drops in average precision and calibration. Although news and regulatory filings contain actionable signals, naïvely injecting raw text or off-the-shelf LLM embeddings into temporal GNNs can introduce temporal leakage, misalignment, and unstable out-of-time ranking. We propose REGATE, a time-causal framework that integrates exogenous documents into dynamic graphs through three coupled components: (1) a schema-guided extractor that converts unstructured documents into auditable, time- and entity-aligned policy tokens with explicit confidence scores; (2) a bounded gating mechanism that fuses these tokens into temporal GNN states as a residual update, downweighting uncertain or stale evidence with a stability guarantee under direction consistency; and (3) a closed-loop retrieval adaptation module that distills the model's own routing attention into a lightweight document scorer without manual relevance labels. On established dynamic-graph benchmarks with documented regime shifts and six backbone architectures (TGN, TGAT, DyGFormer, GraphMixer, CTAN, GeneralDyG), REGATE yields up to +0.16 AP and up to 90% ECE reduction in post-shift windows on Elliptic; cross-domain pilots on credit and equity networks confirm consistent gains. Ablations show improvements stem from time-aligned semantic content rather than timestamps alone, and we report quality–cost trade-offs across open-source and commercial extractors.
