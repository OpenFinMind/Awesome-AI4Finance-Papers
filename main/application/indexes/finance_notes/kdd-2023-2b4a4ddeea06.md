# Data-Efficient and Interpretable Tabular Anomaly Detection

KDD 2023 · Research Track · Main · application · long

- Official paper: https://doi.org/10.1145/3580305.3599294
- Research Track: https://kdd.org/kdd2023/wp-content/uploads/2023/08/toc.html
- Primary task: Fraud & AML / 欺诈检测与反洗钱
- Tasks: Fraud & AML / 欺诈检测与反洗钱
- Subtopics: Payment, Transaction and Insurance Fraud / 支付、交易及保险欺诈
- Methods: Tabular Learning / 表格学习
- Financial evidence source: https://arxiv.org/pdf/2203.02034
- Long-paper evidence: regular Research full-paper track ([format policy](https://kdd.org/kdd2023/call-for-research-track-papers/)).

## Financial evidence

by Generalized Additive Anomaly detection (AD) has numerous real-world applications, Models (GAMs) and GA2 M (see Sec. 3), that have been shown to especially for tabular data, including detection of fraudulent trans- obtain high accuracy and interpretability for tabular data [4, 6, 16], actions, intrusions related to cybersecurity, and adverse outcomes and have been used in applications like finding outlier patterns and auditing fairness [33]. We propose to employ intuitive notions Permission to make digital or hard copies of part or all of this work for personal or of Partial Identification (PID) as an AD objective and learn them classroom use is granted without fee provided that copies are not made or distributed with a differentiable GA2 M (NodeGA2 M, Chang et al. [5]). Our for profit or co

## Abstract

Anomaly detection (AD) plays an important role in numerous applications. In this paper, we focus on two understudied aspects of AD that are critical for integration into real-world applications. First, most AD methods cannot incorporate labeled data that are often available in practice in small quantities and can be crucial to achieve high accuracy. Second, most AD methods are not interpretable, a bottleneck that prevents stakeholders from understanding the reason behind the anomalies. In this paper, we propose a novel AD framework, DIAD, that adapts a white-box model class, Generalized Additive Models, to detect anomalies using a partial identification objective which naturally handles noisy or heterogeneous features. DIAD can incorporate a small amount of labeled data to further boost AD performances in semi-supervised settings. We demonstrate the superiority of DIAD compared to previous work in both unsupervised and semi-supervised settings on multiple datasets. We also present explainability capabilities of DIAD, on its rationale behind predicting certain samples as anomalies.

[PDF](../../pdfs/KDD/2023/kdd-2023-2b4a4ddeea06__Data-Efficient_and_Interpretable_Tabular_Anomaly_Detection.pdf)

Version: `arxiv` · SHA-256: `fe95eaba3d3096678107209bd1fff7bdd203b3e6c64c390f86a6da483e1aa81e`

## Classification / 分类

- Primary task / 主方向: Financial Safety / 金融安全
- Primary subcategory / 主要子分类: Payment, Transaction and Insurance Fraud / 支付、交易及保险欺诈
- Related tasks / 关联方向: Financial Safety / 金融安全
- Subcategories / 子分类: Payment, Transaction and Insurance Fraud / 支付、交易及保险欺诈
- Methods / 技术方法: Tabular Learning / 表格学习
- Review status / 核对状态: `inherited_evidence_mapping`
- [Definitions / 分类定义](../finance_taxonomy.md) · [Evidence / 分类依据](../../checks/finance_taxonomy/assignments.json)
