# Online Conformal Prediction via Universal Portfolio Algorithms

ICML 2026 · main · application

正文包含金融数据、金融训练数据、金融任务评测或具体金融场景案例。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=EKmiOtjZjI
- 摘要来源：https://icml.cc/virtual/2026/poster/65365
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-EKmiOtjZjI__Online_Conformal_Prediction_via_Universal_Portfolio_Algorithms.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Probabilistic Forecasting & Calibration / 概率预测与校准
- 技术方法标签：Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：conformal
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

he target miscoverage rate α is typically chosen to be small (e.g., α = 0.05 or 0.01), implying that the positive and negative subgradients of the losses are very different. Instead, we propose reducing our problem to a portfolio selection problem, and leveraging the Universal Portfolio (UP) algorithm [Cover and Ordentlich, 2002] for OCP. In the following, we explain how UP methods lead to optimal solutions to online learning problems with asymmetric subgradients. For our reduction, considering pinball losses, we construct a market with two synthetic stocks, whose market gains ar

## 原始摘要

Online conformal prediction (OCP) seeks prediction intervals that achieve long-run $1-\alpha$ coverage for arbitrary (possibly adversarial) data streams, while remaining as informative as possible. Existing OCP methods often require manual learning-rate tuning to work well, and may also require algorithm-specific analyses. Here, we develop a general regret-to-coverage theory for interval-valued OCP based on the $(1-\alpha)$-pinball loss. Our first contribution is to identify *linearized regret* as a key notion, showing that controlling it implies coverage bounds for any online algorithm. This relies on a black-box reduction that depends only on the Fenchel conjugate of an upper bound on the linearized regret. Building on this theory, we propose UP-OCP, a parameter-free method for OCP, via a reduction to a two-asset portfolio selection problem, leveraging universal portfolio algorithms. We show strong finite-time bounds on the miscoverage of UP-OCP, even for polynomially growing predictions. Extensive experiments support that UP-OCP delivers consistently better size/coverage trade-offs than prior online conformal baselines.
