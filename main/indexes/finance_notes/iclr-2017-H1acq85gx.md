# Maximum Entropy Flow Networks

ICLR 2017 · main · application

通用方法在金融任务、数据或明确案例上开展应用验证。 主题：Derivatives & Hedging / 衍生品定价与对冲。

- 官方论文页：https://openreview.net/forum?id=H1acq85gx
- 摘要来源：https://raw.githubusercontent.com/papercopilot/paperlists/main/iclr/iclr2017.json
- 本地 PDF：[打开](../../pdfs/ICLR/2017/iclr-2017-H1acq85gx__Maximum_Entropy_Flow_Networks.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_review
- 主方向：Derivatives & Hedging / 衍生品定价与对冲
- 细分方向：Option Pricing & PDEs / 期权定价与PDE
- 技术方法标签：Diffusion & Flow / 扩散与流模型；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：optimization
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Simulation results demonstrate the effectiveness of our method, and applications to finance and computer vision show the flexibility and accuracy of using maximum entropy flow networks.

## 原始摘要

Maximum entropy modeling is a flexible and popular framework for formulating statistical models given partial knowledge. In this paper, rather than the traditional method of optimizing over the continuous density directly, we learn a smooth and invertible transformation that maps a simple distribution to the desired maximum entropy distribution. Doing so is nontrivial in that the objective being maximized (entropy) is a function of the density itself.  By exploiting recent developments in normalizing flow networks, we cast the maximum entropy problem into a finite-dimensional constrained optimization, and solve the problem by combining stochastic optimization with the augmented Lagrangian method. Simulation results demonstrate the effectiveness of our method, and applications to finance and computer vision show the flexibility and accuracy of using maximum entropy flow networks.
