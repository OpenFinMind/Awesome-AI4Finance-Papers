# Stochastic Differentially Private and Fair Learning

ICLR 2023 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：Credit-Card。 主题：Credit & Financial Risk / 信贷与金融风险；Financial Safety & Compliance / 金融安全与合规。

- 官方论文页：https://openreview.net/forum?id=3nM5uhPlfv6
- 摘要来源：https://iclr.cc/virtual/2023/poster/12184
- 本地 PDF：[打开](../../pdfs/ICLR/2023/iclr-2023-3nM5uhPlfv6__Stochastic_Differentially_Private_and_Fair_Learning.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Financial Privacy & Security / 金融隐私与信息安全；Lending & Credit Data / 借贷与信贷数据应用
- 技术方法标签：Fairness & Recourse / 公平性与算法追索；Privacy & Federated Learning / 隐私与联邦学习；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：optimization
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

equalized odds. We compare DP-FERMI against all applicable publicly available baselines in each expeiment. 4.1.1 D EMOGRAPHIC PARITY We use four benchmark tabular datasets: Adult Income, Retired Adult, Parkinsons, and Credit-Card dataset from the UCI machine learning repository (Dua & Graff (2017)). The predicted variables and sensitive attributes are both binary in these datasets. We analyze fairness-accuracy trade-offs with four different values of ϵ P t0.5, 1, 3, 9u for each dataset. We compare against state-of-the-art algorithms proposed in Tran et al. (2021a) and (the

## 原始摘要

Machine learning models are increasingly used in high-stakes decision-making systems. In such applications, a major concern is that these models sometimes discriminate against certain demographic groups such as individuals with certain race, gender, or age. Another major concern in these applications is the violation of the privacy of users. While fair learning algorithms have been developed to mitigate discrimination issues, these algorithms can still leak sensitive information, such as individuals’ health or financial records. Utilizing the notion of differential privacy (DP), prior works aimed at developing learning algorithms that are both private and fair. However, existing algorithms for DP fair learning are either not guaranteed to converge or require full batch of data in each iteration of the algorithm to converge. In this paper, we provide the first stochastic differentially private algorithm for fair learning that is guaranteed to converge. Here, the term “stochastic" refers to the fact that our proposed algorithm converges even when minibatches of data are used at each iteration (i.e. stochastic optimization). Our framework is flexible enough to permit different fairness notions, including demographic parity and equalized odds. In addition, our algorithm can be applied to non-binary classification tasks with multiple (non-binary) sensitive attributes. As a byproduct of our convergence analysis, we provide the first utility guarantee for a DP algorithm for solving nonconvex-strongly concave min-max problems. Our numerical experiments show that the proposed algorithm consistently offers significant performance gains over the state-of-the-art baselines, and can be applied to larger scale problems with non-binary target/sensitive attributes.
