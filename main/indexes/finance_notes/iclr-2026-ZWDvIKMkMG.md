# Healthcare Insurance Fraud Detection via Continual Fiedler Vector Graph Model

ICLR 2026 · main · core

以金融任务或金融数据为核心研究对象。 主题：Insurance & Actuarial / 保险与精算；Fraud & AML / 欺诈检测与反洗钱。

- 官方论文页：https://openreview.net/forum?id=ZWDvIKMkMG
- 摘要来源：https://iclr.cc/virtual/2026/poster/10008798
- PDF 状态：access_blocked
- 金融依据类型：title_abstract_review
- 主方向：Fraud & AML / 欺诈检测与反洗钱
- 细分方向：Insurance & Claims / 承保与理赔；Payment & Transaction Fraud / 支付与交易欺诈；Scams & Financial Misinformation / 诈骗与金融虚假信息
- 技术方法标签：Graph Learning / 图学习；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Healthcare insurance fraud detection presents unique machine learning challenges: labeled data are scarce due to delayed verification processes, and fraudulent behaviors evolve rapidly, often manifesting in complex, graph-structured interactions. / Pretraining routines typically overlook structural anomalies under limited supervision, while online models often fail to adapt to changing fraud patterns without labeled updates. / To address these issues, we propose the Continual Fiedler Vector Graph model (ConFVG), a fraud detection framework designed for label-scarce and non-stationary environments. / The Fiedler Vector, derived from the second smallest eigenvalue of the graph Laplacian, captures global topological signals such as community boundaries and connectivity bottlenecks, which are patterns frequently associated with collusive fraud. / This design allows the model to adapt to new fraud patterns in real time. / Experiments on real-world medical fraud datasets demonstrate that the Continual Fiedler Vector Graph model outperforms state-of-the-art baselines in both low-label and distribution-shift scenarios, offering a scalable and structure-sensitive solution for real-time fraud detection.

## 原始摘要

Healthcare insurance fraud detection presents unique machine learning challenges: labeled data are scarce due to delayed verification processes, and fraudulent behaviors evolve rapidly, often manifesting in complex, graph-structured interactions. Existing methods struggle in such settings. Pretraining routines typically overlook structural anomalies under limited supervision, while online models often fail to adapt to changing fraud patterns without labeled updates. To address these issues, we propose the Continual Fiedler Vector Graph model (ConFVG), a fraud detection framework designed for label-scarce and non-stationary environments. The framework comprises two key components. To mitigate label scarcity, we develop a Fiedler Vector-guided graph autoencoder that leverages spectral graph properties to learn structure-aware node representations. The Fiedler Vector, derived from the second smallest eigenvalue of the graph Laplacian, captures global topological signals such as community boundaries and connectivity bottlenecks, which are patterns frequently associated with collusive fraud. This enables the model to identify structurally anomalous nodes without relying on labels. To handle evolving graph streams, we propose a Subgraph Attention Fusion (SAF) module that constructs neighborhood subgraphs and applies attention-based reweighting to emphasize emerging high-risk structures. This design allows the model to adapt to new fraud patterns in real time. A Mean Teacher mechanism further stabilizes online updates and prevents forgetting of previously acquired knowledge. Experiments on real-world medical fraud datasets demonstrate that the Continual Fiedler Vector Graph model outperforms state-of-the-art baselines in both low-label and distribution-shift scenarios, offering a scalable and structure-sensitive solution for real-time fraud detection.
