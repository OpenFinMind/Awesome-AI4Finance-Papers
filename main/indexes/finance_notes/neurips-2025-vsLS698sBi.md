# Attack by Yourself: Effective and Unnoticeable Multi-Category Graph Backdoor Attacks with Subgraph Triggers Pool

NeurIPS 2025 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：Elliptic。 主题：Blockchain & Digital Assets / 区块链与数字资产。

- 官方论文页：https://openreview.net/forum?id=vsLS698sBi
- 摘要来源：https://neurips.cc/virtual/2025/poster/115380
- 本地 PDF：[打开](../../pdfs/NeurIPS/2025/neurips-2025-vsLS698sBi__Attack_by_Yourself_Effective_and_Unnoticeable_Multi_Category_Graph_Backdoor_Attacks_with_Subgraph_Trigger.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Blockchain & Digital Assets / 区块链与数字资产
- 细分方向：Crypto & Blockchain Transactions / 加密资产与链上交易
- 技术方法标签：Graph Learning / 图学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Graph Neural Networks
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

ublic real-world datasets: vi ∈VT r X X Cora, Pubmed [Sen et al., 2008], Bitcoin [Elliptic, 2020], l(fs (a(GPi , Pyk )), yk ), (4) Facebook [Rozemberczki et al., 2021], Flickr [Zeng et al., vi ∈VP k∈{1,...,K} 2020], and OGB-arxiv [Hu et al., 2020a]. These datasets

## 原始摘要

Graph Neural Networks (GNNs) have achieved significant success in various real-world applications, including social networks, finance systems, and traffic management. Recent researches highlight their vulnerability to backdoor attacks in node classification, where GNNs trained on a poisoned graph misclassify a test node only when specific triggers are attached. These studies typically focus on single attack categories and use adaptive trigger generators to create node-specific triggers. However, adaptive trigger generators typically have a simple structure, limited parameters, and lack category-aware graph knowledge, which makes them struggle to handle backdoor attacks across multiple categories as the number of target categories increases. We address this gap by proposing a novel approach for Effective and Unnoticeable Multi-Category (EUMC) graph backdoor attacks, leveraging subgraph from the attacked graph as category-aware triggers to precisely control the target category. To ensure the effectiveness of our method, we construct a Multi-Category Subgraph Triggers Pool (MC-STP) using the subgraphs of the attacked graph as triggers. We then exploit the attachment probability shifts of each subgraph trigger as category-aware priors for target category determination. Moreover, we develop a ``select then attach'' strategy that connects suitable category-aware trigger to attacked nodes for unnoticeability. Extensive experiments across different real-world datasets confirm the efficacy of our method in conducting multi-category graph backdoor attacks on various GNN models and defense strategies.
