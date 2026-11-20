# Benchmarking Fraud Detectors on Private Graph Data

KDD 2025 · Research Track · Main · application · long

- Official paper: https://doi.org/10.1145/3690624.3709170
- Research Track: https://kdd.org/kdd2025/research-track-papers-2/
- Primary task: Fraud & AML / 欺诈检测与反洗钱
- Tasks: Fraud & AML / 欺诈检测与反洗钱
- Subtopics: Payment, Transaction and Insurance Fraud / 支付、交易及保险欺诈
- Methods: Privacy & Federated Learning / 隐私与联邦学习
- Financial evidence source: https://arxiv.org/pdf/2507.22347
- Long-paper evidence: regular Research full-paper track ([format policy](https://kdd.org/kdd2025/research-track-call-for-papers/)).

## Financial evidence

ed above for benign vertices, that is, we partition the benign vertices into k disjoint sets of equal size. However, in fraud graphs, there are often very few fraudulent vertices. For example, in the Elliptic Bitcoin financial fraud dataset [WDC+ 19] there are only 11 fraudsters out of over 6, 000 vertices. Partitioning these fraud vertices into a reasonable number of partitions to achieve low sensitivity (say k ≥ 5) would destroy any structure of the sub-graph of fraud vertices. We therefore modify typical subsample-and-aggregate for the fraudulent vertices by allowing duplication of fraudsters across partitions. For each partition, we sample a subset of fraudulent vertices, where the rate of sub-sampling is controlled by a parameter ρ. We term this instance of subsample-and-aggregate as Partition, Dupli

## Abstract

We introduce the novel problem of benchmarking fraud detectors on private graph-structured data. Currently, many types of fraud are managed in part by automated detection algorithms that operate over graphs. We consider the scenario where a data holder wishes to outsource development of fraud detectors to third parties (e.g., vendors or researchers). The third parties submit their fraud detectors to the data holder, who evaluates these algorithms on a private dataset and then publicly communicates the results. We propose a realistic privacy attack on this system that allows an adversary to de-anonymize individuals' data based only on the evaluation results. In simulations of a privacy-sensitive benchmark for facial recognition algorithms by the National Institute of Standards and Technology (NIST), our attack achieves near perfect accuracy in identifying whether individuals' data is present in a private dataset, with a True Positive Rate of 0.98 at a False Positive Rate of 0.00. We then study how to benchmark algorithms while satisfying a formal differential privacy (DP) guarantee. We empirically evaluate two classes of solutions: subsample-and-aggregate and DP synthetic graph data. We demonstrate through extensive experiments that current approaches do not provide utility when guaranteeing DP. Our results indicate that the error arising from DP trades off between bias from distorting graph structure and variance from adding random noise. Current methods lie on different points along this bias-variance trade-off, but more complex methods tend to require high-variance noise addition, undermining utility.

[PDF](../../pdfs/KDD/2025/kdd-2025-fd7ac2fcb9c0__Benchmarking_Fraud_Detectors_on_Private_Graph_Data.pdf)

Version: `arxiv` · SHA-256: `a59ee58045a0a20d14227de03f5a83902e4d84ff49b8289dd87c6b9810fbdd3f`

## Classification / 分类

- Primary task / 主方向: Financial Safety / 金融安全
- Primary subcategory / 主要子分类: Payment, Transaction and Insurance Fraud / 支付、交易及保险欺诈
- Related tasks / 关联方向: Financial Safety / 金融安全
- Subcategories / 子分类: Payment, Transaction and Insurance Fraud / 支付、交易及保险欺诈
- Methods / 技术方法: Privacy & Federated Learning / 隐私与联邦学习
- Review status / 核对状态: `inherited_evidence_mapping`
- [Definitions / 分类定义](../finance_taxonomy.md) · [Evidence / 分类依据](../../checks/finance_taxonomy/assignments.json)
