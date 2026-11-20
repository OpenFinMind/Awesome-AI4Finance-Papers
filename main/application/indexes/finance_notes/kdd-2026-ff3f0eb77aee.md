# Combating Web-Based E-Commerce Fraud Syndicates: Fairness-Aware Hypergraph Contrastive Fraud Detection with Multi-Dimensional Reinforcement Rewards

KDD 2026 · Research Track · Main · application · long

- Official paper: https://doi.org/10.1145/3770855.3818200
- Research Track: https://kdd2026.kdd.org/papers/
- Primary task: Fraud & AML / 欺诈检测与反洗钱
- Tasks: Fraud & AML / 欺诈检测与反洗钱
- Subtopics: Payment, Transaction and Insurance Fraud / 支付、交易及保险欺诈; Financial Model and Agent Safety / 金融模型及智能体安全
- Methods: Graph Learning / 图学习; Fairness & Recourse / 公平性与算法追索; Optimization & Numerical Methods / 优化与数值方法; Representation Learning / 表征学习
- Financial evidence source: https://openalex.org/W7196990542
- Long-paper evidence: regular Research full-paper track ([format policy](https://kdd2026.kdd.org/research-track-call-for-papers/)).

## Financial evidence

roup separation, thus effectively detecting cross-view camouflage by identifying inherent representational inconsistencies across heterogeneous dimensions. Extensive experiments on six real-world web financial transaction datasets demonstrate MHMRC's superiority over 14 SOTA models, achieving average improvements of 5.74% in AUC, 4.94% in F1, and 13.20% in AP.

## Abstract

The proliferation of web-based e-commerce and digital payment platforms, while promoting financial inclusion, has inadvertently heightened the risks of collusive fraud, which disproportionately impacts vulnerable populations such as the elderly and low-income communities. This challenge underscores an urgent need for responsible web AI that ensures social fairness and transparency to protect the most susceptible users. To address this issue and contribute to building safer and more inclusive web ecosystems, we propose MHMRC, a novel semi-supervised model that integrates Multi-view Heterogeneous Hypergraph Contrastive learning (MHHC) and Multi-Dimensional Reinforcement reward driven Community detection (MDRC) for web-based e-commerce collusive fraud detection. First, MDRC quantifies intra-group node similarity using policy optimization guided by three specialized rewards: modularity, connectivity, and consistency. This process transforms isolated users into behaviorally correlated entities, enabling the precise identification of latent fraud syndicates even in the absence of explicit interaction links. This is particularly crucial for identifying coordinated attacks that target vulnerable groups. Second, MHHC integrates temporal, user-centric, and item-centric perspectives through hypergraph fusion. It applies contrastive objectives at node and hyperedge levels to preserve multimodal relationships while maximizing inter-group separation, thus effectively detecting cross-view camouflage by identifying inherent representational inconsistencies across heterogeneous dimensions. Extensive experiments on six real-world web financial transaction datasets demonstrate MHMRC's superiority over 14 SOTA models, achieving average improvements of 5.74% in AUC, 4.94% in F1, and 13.20% in AP.

## Classification / 分类

- Primary task / 主方向: Financial Safety / 金融安全
- Primary subcategory / 主要子分类: Payment, Transaction and Insurance Fraud / 支付、交易及保险欺诈
- Related tasks / 关联方向: Financial Safety / 金融安全
- Subcategories / 子分类: Payment, Transaction and Insurance Fraud / 支付、交易及保险欺诈; Financial Model and Agent Safety / 金融模型及智能体安全
- Methods / 技术方法: Graph Learning / 图学习; Fairness & Recourse / 公平性与算法追索; Optimization & Numerical Methods / 优化与数值方法; Representation Learning / 表征学习
- Review status / 核对状态: `inherited_evidence_mapping`
- [Definitions / 分类定义](../finance_taxonomy.md) · [Evidence / 分类依据](../../checks/finance_taxonomy/assignments.json)
