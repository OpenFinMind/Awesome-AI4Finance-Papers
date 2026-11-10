# Statistically Optimal $K$-means Clustering via Nonnegative Low-rank Semidefinite Programming

ICLR 2024 · main · application

正文包含金融领域的数据、模型、任务或独立金融评测。 主题：Fraud & AML / 欺诈检测与反洗钱。

- 官方论文页：https://openreview.net/forum?id=v7ZPwoHU1j
- 摘要来源：https://iclr.cc/virtual/2024/poster/17550
- 本地 PDF：[打开](../../pdfs/ICLR/2024/iclr-2024-v7ZPwoHU1j__Statistically_Optimal_K_means_Clustering_via_Nonnegative_Low_rank_Semidefinite_Programming.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_model_or_task
- 主方向：Fraud & AML / 欺诈检测与反洗钱
- 细分方向：Banknote Authentication / 钞票真伪识别
- 技术方法标签：Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：optimization
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

constraints, a basic but fundamental difficulty is the need to store and optimize over the n2 individual elements of the matrix. Even a small dataset with n ≈ 1000, such as the banknote authentication 1 Published as a conference paper at ICLR 2024 Computational complexity & Statistical performance trade-off 10 2 CPU time [seconds] 10 0

## 原始摘要

$K$-means clustering is a widely used machine learning method for identifying patterns in large datasets. Recently, semidefinite programming (SDP) relaxations have been proposed for solving the $K$-means optimization problem, which enjoy strong statistical optimality guarantees. However, the prohibitive cost of implementing an SDP solver renders these guarantees inaccessible to practical datasets. In contrast, nonnegative matrix factorization (NMF) is a simple clustering algorithm widely used by machine learning practitioners, but it lacks a solid statistical underpinning and theoretical guarantees. In this paper, we consider an NMF-like algorithm that solves a nonnegative low-rank restriction of the SDP-relaxed $K$-means formulation using a nonconvex Burer--Monteiro factorization approach. The resulting algorithm is as simple and scalable as state-of-the-art NMF algorithms while also enjoying the same strong statistical optimality guarantees as the SDP. In our experiments, we observe that our algorithm achieves significantly smaller mis-clustering errors compared to the existing state-of-the-art while maintaining scalability.
