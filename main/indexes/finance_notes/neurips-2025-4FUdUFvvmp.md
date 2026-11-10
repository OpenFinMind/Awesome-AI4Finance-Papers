# PANTHER: Generative Pretraining Beyond Language for Sequential User Behavior Modeling

NeurIPS 2025 · main · core

以金融任务或金融数据为核心研究对象。 主题：Fraud & AML / 欺诈检测与反洗钱。

- 官方论文页：https://openreview.net/forum?id=4FUdUFvvmp
- 摘要来源：https://neurips.cc/virtual/2025/poster/119962
- 本地 PDF：[打开](../../pdfs/NeurIPS/2025/neurips-2025-4FUdUFvvmp__PANTHER_Generative_Pretraining_Beyond_Language_for_Sequential_User_Behavior_Modeling.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_review
- 主方向：Fraud & AML / 欺诈检测与反洗钱
- 细分方向：Payment & Transaction Fraud / 支付与交易欺诈；Scams & Financial Misinformation / 诈骗与金融虚假信息
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Generative Modeling / 生成建模；Transformer / Transformer模型；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：language models；LLMs；transformer
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

PANTHER introduces: (1) Structured Tokenization to compress multi-dimensional transaction attributes into an interpretable vocabulary; (2) Sequence Pattern Recognition Module (SPRM) for modeling periodic transaction motifs; (3) a Unified User-Profile Embedding that fuses static demographics with dynamic transaction histories, enabling both personalized predictions and population-level knowledge transfer; and (4) Real-time scalability enabled by offline caching of pre-trained embeddings for millisecond-level inference.Fully deployed and operational online at WeChat Pay, PANTHER delivers a 25.6\% boost in next-transaction prediction HitRate@1 and a 38.6\% relative improvement in fraud detection recall over baselines.

## 原始摘要

Large language models (LLMs) have shown that generative pretraining can distill vast world knowledge into compact token representations. While LLMs encapsulate extensive world knowledge, they remain limited in modeling the behavioral knowledge contained within user interaction histories. User behavior forms a distinct modality, where each action—defined by multi-dimensional attributes such as time, context, and transaction type—constitutes a behavioral token. Modeling these high-cardinality, sparse, and irregular sequences is challenging, and discriminative models often falter under limited supervision. To bridge this gap, we extend generative pretraining to user behavior, learning transferable representations from unlabeled behavioral data analogous to how LLMs learn from text. We present PANTHER, a hybrid generative–discriminative framework that unifies user behavior pretraining and downstream adaptation, enabling large-scale sequential user representation learning and real-time inference. PANTHER introduces: (1) Structured Tokenization to compress multi-dimensional transaction attributes into an interpretable vocabulary; (2) Sequence Pattern Recognition Module (SPRM) for modeling periodic transaction motifs; (3) a Unified User-Profile Embedding that fuses static demographics with dynamic transaction histories, enabling both personalized predictions and population-level knowledge transfer; and (4) Real-time scalability enabled by offline caching of pre-trained embeddings for millisecond-level inference.Fully deployed and operational online at WeChat Pay, PANTHER delivers a 25.6\% boost in next-transaction prediction HitRate@1 and a 38.6\% relative improvement in fraud detection recall over baselines. Cross-domain evaluations on public benchmarks (CCT, MBD, MovieLens-1M, Yelp) show strong generalization, achieving up to 21\% HitRate@1 gains over transformer baselines, establishing PANTHER as a scalable, high-performance framework for industrial user sequential behavior modeling.
