# Distributionally Robust Fair Principal Components via Geodesic Descents

ICLR 2022 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：German Credit。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=9NVd-DMtThY
- 摘要来源：https://iclr.cc/virtual/2022/poster/6615
- 本地 PDF：[打开](../../pdfs/ICLR/2022/iclr-2022-9NVd-DMtThY__Distributionally_Robust_Fair_Principal_Components_via_Geodesic_Descents.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Credit Scoring & Default / 信用评分与违约
- 技术方法标签：Fairness & Recourse / 公平性与算法追索；Uncertainty & Robustness / 不确定性与鲁棒性；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：optimization
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Coli 1.1500 1.7210 1.5280 2.4799 1.1005 2.9466 5.1275 5.6674 Energy 0.0125 0.2238 0.0138 0.2225 0.1229 2.7318 0.1001 7.9511 German Credit 2.0588 43.9032 1.3670 44.0064 1.7845 43.9648 1.4955 49.5014 Image 0.7522 6.0199 1.6129 10.2616 1.1499 14.3725 4.7013 19.3356 Letter 0.1712 7.4176 1.2489 7.4470 0.4427 8.7445 0.5743 15.1779 Magic 1.831

## 原始摘要

Principal component analysis is a simple yet useful dimensionality reduction technique in modern machine learning pipelines. In consequential domains such as college admission, healthcare and credit approval, it is imperative to take into account emerging criteria such as the fairness and the robustness of the learned projection. In this paper, we propose a distributionally robust optimization problem for principal component analysis which internalizes a fairness criterion in the objective function. The learned projection thus balances the trade-off between the total reconstruction error and the reconstruction error gap between subgroups, taken in the min-max sense over all distributions in a moment-based ambiguity set. The resulting optimization problem over the Stiefel manifold can be efficiently solved by a Riemannian subgradient descent algorithm with a sub-linear convergence rate. Our experimental results on real-world datasets show the merits of our proposed method over state-of-the-art baselines.
