# TANGOS: Regularizing Tabular Neural Networks through Gradient Orthogonalization and Specialization

ICLR 2023 · main · application

正文包含金融数据、金融训练数据、金融任务评测或具体金融场景案例。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=n6H86gW8u0d
- 摘要来源：https://iclr.cc/virtual/2023/poster/11186
- 本地 PDF：[打开](../../pdfs/ICLR/2023/iclr-2023-n6H86gW8u0d__TANGOS_Regularizing_Tabular_Neural_Networks_through_Gradient_Orthogonalization_and_Specialization.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Credit Scoring & Default / 信用评分与违约
- 技术方法标签：Tabular Learning / 表格学习；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：optimization
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

ion 9 699 Street et al. (1993) Cervical (CE) “00383” Classification 136 858 Fernandes et al. (2017) Credit (CR) “credit-screening” Classification 40 677 Dua et al. (2017) HCV (HC) “00571” Classification 12 615 Hoffmann et al. (2018) Australian (AU) “statlog” Classification 55 690 Quinlan (1987) Tumor (TU) “primary-tumor” Classification 25 339 Michalski et al. (1986) Entrance (EN) “00582” Classification 38 666 Hussain et al. (2018) Thoracic (TH) “00277” Classification 24 470 Zikeba et al. (2013) Soybean (SO) “soybean” Classification 484 683 Fisher & Schlimmer (1988) [1] This dataset has now been removed due to ethical issues. For more information see the following url https://medium.com/@docintangible/racist-data-destructi

## 原始摘要

Despite their success with unstructured data, deep neural networks are not yet a panacea for structured tabular data. In the tabular domain, their efficiency crucially relies on various forms of regularization to prevent overfitting and provide strong generalization performance. Existing regularization techniques include broad modelling decisions such as choice of architecture, loss functions, and optimization methods. In this work, we introduce Tabular Neural Gradient Orthogonalization and Specialization (TANGOS), a novel framework for regularization in the tabular setting built on latent unit attributions. The gradient attribution of an activation with respect to a given input feature suggests how the neuron attends to that feature, and is often employed to interpret the predictions of deep networks. In TANGOS, we take a different approach and incorporate neuron attributions directly into training to encourage orthogonalization and specialization of latent attributions in a fully-connected network. Our regularizer encourages neurons to focus on sparse, non-overlapping input features and results in a set of diverse and specialized latent units. In the tabular domain, we demonstrate that our approach can lead to improved out-of-sample generalization performance, outperforming other popular regularization methods. We provide insight into why our regularizer is effective and demonstrate that TANGOS can be applied jointly with existing methods to achieve even greater generalization performance.
