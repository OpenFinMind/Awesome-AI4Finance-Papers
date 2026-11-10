# Optimizing Conditional Value-At-Risk of Black-Box Functions

NeurIPS 2021 · main · application

正文包含金融数据、金融任务或金融领域评测。 主题：Portfolio & Investment / 投资组合与投资管理。

- 官方论文页：https://openreview.net/forum?id=Tc6Uk03Te7g
- 摘要来源：https://neurips.cc/virtual/2021/poster/27263
- 本地 PDF：[打开](../../pdfs/NeurIPS/2021/neurips-2021-Tc6Uk03Te7g__Optimizing_Conditional_Value_At_Risk_of_Black_Box_Functions.pdf)；版本：publisher_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Portfolio & Investment / 投资组合与投资管理
- 细分方向：Portfolio Selection & Optimization / 组合选择与优化
- 技术方法标签：Uncertainty & Robustness / 不确定性与鲁棒性；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Bayesian；optimization
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

aR. We empirically evaluate the performance of both CV-UCB and CV-TS in optimizing CVaR of synthetic benchmark functions, an optimization problem of the residuary resistance per unit weight of displacement of a yacht, a portfolio optimization problem, and a simulated robot task (Sec. 5). Related works. Existing solutions to optimizing a black-box function f (x, W) with an environ- mental random variable W are different in the assumptions about W and the objective function. Other than the aforementioned works of [4, 13] where we adopt the assumptions that the distribution of W is

## 原始摘要

This paper presents two Bayesian optimization (BO) algorithms with theoretical performance guarantee to maximize the conditional value-at-risk (CVaR) of a black-box function: CV-UCB and CV-TS which are based on the well-established principle of optimism in the face of uncertainty and Thompson sampling, respectively. To achieve this, we develop an upper confidence bound of CVaR and prove the no-regret guarantee of CV-UCB by utilizing an interesting connection between CVaR and value-at-risk (VaR). For CV-TS, though it is straightforwardly performed with Thompson sampling, bounding its Bayesian regret is non-trivial because it requires a tail expectation bound for the distribution of CVaR of a black-box function, which has not been shown in the literature. The performances of both CV-UCB and CV-TS are empirically evaluated in optimizing CVaR of synthetic benchmark functions and simulated real-world optimization problems.
