# Implicit Generative Copulas

NeurIPS 2021 · main · application

通用方法在金融任务、数据或明确案例上开展应用验证。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=h1bPe7spQkr
- 摘要来源：https://neurips.cc/virtual/2021/poster/28065
- 本地 PDF：[打开](../../pdfs/NeurIPS/2021/neurips-2021-h1bPe7spQkr__Implicit_Generative_Copulas.pdf)；版本：publisher_version
- 金融依据类型：title_abstract_review
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Financial Risk / 金融风险管理
- 技术方法标签：Generative Modeling / 生成建模
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：copula；Copulas；copulas
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

A popular remedy is to construct a tree-based hierarchy of conditional bivariate copulas.In this paper, we propose a flexible, yet conceptually simple alternative based on implicit generative neural networks.The key challenge is to ensure marginal uniformity of the estimated copula distribution.We achieve this by learning a multivariate latent distribution with unspecified marginals but the desired dependency structure.By applying the probability integral transform, we can then obtain samples from the high-dimensional copula distribution without relying on parametric assumptions or the need to find a suitable tree structure.Experiments on synthetic and real data from finance, physics, and image generation demonstrate the performance of this approach.

## 原始摘要

Copulas are a powerful tool for modeling multivariate distributions as they allow to separately estimate the univariate marginal distributions and the joint dependency structure. However, known parametric copulas offer limited flexibility especially in high dimensions, while commonly used non-parametric methods suffer from the curse of dimensionality. A popular remedy is to construct a tree-based hierarchy of conditional bivariate copulas.In this paper, we propose a flexible, yet conceptually simple alternative based on implicit generative neural networks.The key challenge is to ensure marginal uniformity of the estimated copula distribution.We achieve this by learning a multivariate latent distribution with unspecified marginals but the desired dependency structure.By applying the probability integral transform, we can then obtain samples from the high-dimensional copula distribution without relying on parametric assumptions or the need to find a suitable tree structure.Experiments on synthetic and real data from finance, physics, and image generation demonstrate the performance of this approach.
