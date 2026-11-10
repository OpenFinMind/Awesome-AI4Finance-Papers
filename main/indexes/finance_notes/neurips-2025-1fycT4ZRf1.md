# Scalable Signature Kernel Computations via Local Neumann Series Expansions

NeurIPS 2025 · main · application

通用方法在金融任务、数据或明确案例上开展应用验证。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=1fycT4ZRf1
- 摘要来源：https://neurips.cc/virtual/2025/poster/120206
- PDF 状态：access_blocked
- 金融依据类型：title_abstract_review
- 主方向：Time Series / 时间序列
- 细分方向：General Time-Series Methods / 综合序列方法
- 技术方法标签：Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

As demonstrated in our benchmarks, these advantages make our method particularly well-suited for rough-path-assisted machine learning, financial modeling, and signal processing applications involving very long and highly volatile sequential data.

## 原始摘要

The signature kernel is a recent state-of-the-art tool for analyzing high-dimensional sequential data, valued for its theoretical guarantees and strong empirical performance. In this paper, we present a novel method for efficiently computing the signature kernel of long, high-dimensional time series via adaptively truncated recursive local power series expansions. Building on the characterization of the signature kernel as the solution of a Goursat PDE, our approach employs tilewise Neumann‐series expansions to derive rapidly converging power series approximations of the signature kernel that are locally defined on subdomains and propagated iteratively across the entire domain of the Goursat solution by exploiting the geometry of the time series. Algorithmically, this involves solving a system of interdependent Goursat PDEs via adaptively truncated local power series expansions and recursive propagation of boundary conditions along a directed graph in a topological ordering. This method strikes an effective balance between computational cost and accuracy, achieving substantial performance improvements over state-of-the-art approaches for computing the signature kernel. It offers (a) adjustable and superior accuracy, even for time series with very high roughness; (b) drastically reduced memory requirements; and (c) scalability to efficiently handle very long time series (e.g., with up to one million data points or more) on a single GPU. As demonstrated in our benchmarks, these advantages make our method particularly well-suited for rough-path-assisted machine learning, financial modeling, and signal processing applications involving very long and highly volatile sequential data.
