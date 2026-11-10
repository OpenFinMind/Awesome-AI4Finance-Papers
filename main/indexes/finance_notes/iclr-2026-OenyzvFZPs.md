# Adaptive Mamba Neural Operators

ICLR 2026 · main · application

包含明确的金融任务、金融领域数据或金融案例验证。 主题：Financial Models & Benchmarks / 金融模型与评测资源。

- 官方论文页：https://openreview.net/forum?id=OenyzvFZPs
- 摘要来源：https://iclr.cc/virtual/2026/poster/10009760
- 本地 PDF：[打开](../../pdfs/ICLR/2026/iclr-2026-OenyzvFZPs__Adaptive_Mamba_Neural_Operators.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_financial_task_or_data
- 主方向：Financial Models & Benchmarks / 金融模型与评测资源
- 细分方向：Numerical Finance / 计算金融与数值方法
- 技术方法标签：Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/checlams/AMO.

## 纳入依据

In several challenging benchmark PDE problems in the fields of fluid physics, solid physics, and finance on point clouds, structured meshes, regular grids, and irregular domains, AMO consistently outperforms state-of-the-art solvers in terms of relative $L^2$ error.

## 原始摘要

Accurately solving partial differential equations (PDEs) on arbitrary geometries and a variety of meshes is an important task in science and engineering applications. In this paper, we propose Adaptive Mamba Neural Operators (AMO), which integrates reproducing kernels for state-space models (SSMs) rather than the kernel integral formulation of SSMs. This is achieved by constructing Takenaka-Malmquist systems for the PDEs. AMO offers new representations that align well with the adaptive Fourier decomposition (AFD) theory and can approximate the solution manifold of PDEs on a wide range of geometries and meshes. In several challenging benchmark PDE problems in the fields of fluid physics, solid physics, and finance on point clouds, structured meshes, regular grids, and irregular domains, AMO consistently outperforms state-of-the-art solvers in terms of relative $L^2$ error. Overall, this work presents a new paradigm for designing explainable neural operator frameworks. The code is available at https://github.com/checlams/AMO.
