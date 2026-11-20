# Finding Counterfactual Evidences for Node Classification

KDD 2025 · Research Track · Main · application · long

- Official paper: https://doi.org/10.1145/3711896.3736960
- Research Track: https://kdd.org/kdd2025/research-track-papers-2/
- Primary task: Financial Safety & Compliance / 金融安全与合规
- Tasks: Financial Safety & Compliance / 金融安全与合规; Credit & Financial Risk / 信贷与金融风险
- Subtopics: Credit Risk and Default Prediction / 信用风险与违约预测
- Methods: Graph Learning / 图学习; Causal Learning / 因果学习; Fairness & Recourse / 公平性与算法追索
- Financial evidence source: https://arxiv.org/pdf/2505.11396
- Long-paper evidence: regular Research full-paper track ([format policy](https://kdd.org/kdd2025/research-track-call-for-papers/)).

## Financial evidence

ntributions. We tackle the problem of extracting, from a Figure 1: (Left) The 1-hop neighborhood 𝐺 of the node of interest, given graph, a pair of nodes (together with their neighborhoods), 𝑢97, from German Credit dataset [3]. Each customer has important such that they exhibit high similarity in both structure and features, features for classification, as shown in the table. (Center) 𝐺 1 is a coun- yet they are classified differently by a GNN. Our is a data mining terfactual explanation induced from 𝐺, highlighting the important problem, that is, we define a novel structure of interest in a large parts of the input graph. (Right) 𝑢862 is the counterfactual evidence graph based on a pre-trained GNN model’s output and we then that shares similar node features and surrounding structures (𝐺 2 ) with 𝑢97, b

## Abstract

Counterfactual learning is emerging as an important paradigm, rooted in causality, which promises to alleviate common issues of graph neural networks (GNNs), such as fairness and interpretability. However, as in many real-world application domains where conducting randomized controlled trials is impractical, one has to rely on available observational (factual) data to detect counterfactuals. In this paper, we introduce and tackle the problem of searching for counterfactual evidences for the GNN-based node classification task. A counterfactual evidence is a pair of nodes such that, regardless they exhibit great similarity both in the features and in their neighborhood subgraph structures, they are classified differently by the GNN. We develop effective and efficient search algorithms and a novel indexing solution that leverages both node features and structural information to identify counterfactual evidences, and generalizes beyond any specific GNN. Through various downstream applications, we demonstrate the potential of counterfactual evidences to enhance fairness and accuracy of GNNs.

[PDF](../../pdfs/KDD/2025/kdd-2025-c8fdceeb2bcb__Finding_Counterfactual_Evidences_for_Node_Classification.pdf)

Version: `arxiv` · SHA-256: `14d4947b79f89425e240f2d9a39da4ab29b5919812211b8ac837117644b810a0`

## Classification / 分类

- Primary task / 主方向: Financial Risk / 金融风险
- Primary subcategory / 主要子分类: Credit Risk and Default Prediction / 信用风险与违约预测
- Related tasks / 关联方向: Financial Risk / 金融风险; Financial Safety / 金融安全
- Subcategories / 子分类: Credit Risk and Default Prediction / 信用风险与违约预测
- Methods / 技术方法: Graph Learning / 图学习; Causal Learning / 因果学习; Fairness & Recourse / 公平性与算法追索
- Review status / 核对状态: `contribution_evidence_review`
- [Definitions / 分类定义](../finance_taxonomy.md) · [Evidence / 分类依据](../../checks/finance_taxonomy/assignments.json)
