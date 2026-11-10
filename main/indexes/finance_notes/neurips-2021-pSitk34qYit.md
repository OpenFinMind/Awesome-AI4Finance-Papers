# Risk Bounds and Calibration for a Smart Predict-then-Optimize Method

NeurIPS 2021 · main · application

通用方法在金融任务、数据或明确案例上开展应用验证。 主题：Portfolio & Investment / 投资组合与投资管理。

- 官方论文页：https://openreview.net/forum?id=pSitk34qYit
- 摘要来源：https://neurips.cc/virtual/2021/poster/26757
- 本地 PDF：[打开](../../pdfs/NeurIPS/2021/neurips-2021-pSitk34qYit__Risk_Bounds_and_Calibration_for_a_Smart_Predict_then_Optimize_Method.pdf)；版本：publisher_version
- 金融依据类型：title_abstract_review
- 主方向：Portfolio & Investment / 投资组合与投资管理
- 细分方向：Portfolio Selection & Optimization / 组合选择与优化
- 技术方法标签：Uncertainty & Robustness / 不确定性与鲁棒性；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：optimization
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

We perform experiments to empirically demonstrate the strength of the SPO+ surrogate, as compared to standard $\ell_1$ and squared $\ell_2$ prediction error losses, on portfolio allocation and cost-sensitive multi-class classification problems.

## 原始摘要

The predict-then-optimize framework is fundamental in practical stochastic decision-making problems:  first predict unknown parameters of an optimization model, then solve the problem using the predicted values. A natural loss function in this setting is defined by measuring the decision error induced by the predicted parameters, which was named the Smart Predict-then-Optimize (SPO) loss by Elmachtoub and Grigas [2021]. Since the SPO loss is typically nonconvex and possibly discontinuous, Elmachtoub and Grigas [2021] introduced a convex surrogate, called the SPO+ loss, that importantly accounts for the underlying structure of the optimization model. In this paper, we greatly expand upon the consistency results for the SPO+ loss provided by Elmachtoub and Grigas [2021]. We develop risk bounds and uniform calibration results for the SPO+ loss relative to the SPO loss, which provide a quantitative way to transfer the excess surrogate risk to excess true risk. By combining our risk bounds with generalization bounds, we show that the empirical minimizer of the SPO+ loss achieves low excess true risk with high probability. We first demonstrate these results in the case when the feasible region of the underlying optimization problem is a polyhedron, and then we show that the results can be strengthened substantially when the feasible region is a level set of a strongly convex function. We perform experiments to empirically demonstrate the strength of the SPO+ surrogate, as compared to standard $\ell_1$ and squared $\ell_2$ prediction error losses, on portfolio allocation and cost-sensitive multi-class classification problems.
