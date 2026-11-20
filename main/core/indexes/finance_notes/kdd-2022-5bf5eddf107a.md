# Detecting Cash-out Users via Dense Subgraphs

KDD 2022 · Research Track · Main · core · long

- Official paper: https://doi.org/10.1145/3534678.3539252
- Research Track: https://www.kdd.org/kdd2022/toc.html
- Primary task: Fraud & AML / 欺诈检测与反洗钱
- Tasks: Fraud & AML / 欺诈检测与反洗钱
- Subtopics: Payment, Transaction and Insurance Fraud / 支付、交易及保险欺诈
- Methods:
- Financial evidence source: https://www.kdd.org/kdd2022/toc.html
- Long-paper evidence: regular Research full-paper track ([format policy](https://www.kdd.org/kdd2022/cfpResearch.html)).

## Financial evidence

Cash-out fraud refers to the withdrawal of cash from a credit card by illegitimate payments with merchants. To further spot cash-out behaviors in complex scenarios, recent efforts adopt graph models to exploit the interaction relations rich in financial transactions. However, most existing graph-based methods are proposed for online payment activities in internet financial institutions. Moreover, these methods commonly rely on a large amount of online user data, which are not well suitable for the traditional credit card services in commercial banks. In this paper, we focus on discerning fraudulent cash-out users by taking advantage of only the personal credit card data from banks.

## Abstract

Cash-out fraud refers to the withdrawal of cash from a credit card by illegitimate payments with merchants. Conventional data-driven approaches for cash-out detection commonly construct a classifier with domain specific feature engineering. To further spot cash-out behaviors in complex scenarios, recent efforts adopt graph models to exploit the interaction relations rich in financial transactions. However, most existing graph-based methods are proposed for online payment activities in internet financial institutions. Moreover, these methods commonly rely on a large amount of online user data, which are not well suitable for the traditional credit card services in commercial banks. In this paper, we focus on discerning fraudulent cash-out users by taking advantage of only the personal credit card data from banks. To alleviate the scarcity of available labeled data, we formulate the cash-out detection problem as identifying dense blocks. First, we define a bipartite multigraph to hold transactions between users and merchants, where cash-out activities generate cyclically intensive and high-volume flows. Second, we give a formal definition of cash-out behaviors from four perspectives: time, capital, cyclicity, and topotaxy. Then, we develop ANTICO, with a class of metrics to capture suspicious signals of the activities and a greedy algorithm to spot suspicious blocks by optimizing the proposed metric. Theoretical analysis shows a provable upper bound of ANTICO on the effectiveness of detecting cash-out users. Experimental results show that ANTICO outperforms state-of-the-art methods in accurately detecting cash-out users on both synthetic and real-world banking data.

## Classification / 分类

- Primary task / 主方向: Financial Safety / 金融安全
- Primary subcategory / 主要子分类: Payment, Transaction and Insurance Fraud / 支付、交易及保险欺诈
- Related tasks / 关联方向: Financial Safety / 金融安全
- Subcategories / 子分类: Payment, Transaction and Insurance Fraud / 支付、交易及保险欺诈
- Methods / 技术方法: Not labeled / 暂未标注
- Review status / 核对状态: `inherited_evidence_mapping`
- [Definitions / 分类定义](../finance_taxonomy.md) · [Evidence / 分类依据](../../checks/finance_taxonomy/assignments.json)
