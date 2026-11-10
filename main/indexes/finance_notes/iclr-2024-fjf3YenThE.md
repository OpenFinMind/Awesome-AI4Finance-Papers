# New Insight of Variance reduce in Zero-Order Hard-Thresholding: Mitigating Gradient Error and Expansivity Contradictions

ICLR 2024 · main · application

包含明确的金融任务、金融领域数据或金融案例验证。 主题：Portfolio & Investment / 投资组合与投资管理。

- 官方论文页：https://openreview.net/forum?id=fjf3YenThE
- 摘要来源：https://iclr.cc/virtual/2024/poster/18174
- 本地 PDF：[打开](../../pdfs/ICLR/2024/iclr-2024-fjf3YenThE__New_Insight_of_Variance_reduce_in_Zero_Order_Hard_Thresholding_Mitigating_Gradient_Error_and_Expansivity_.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_financial_task_or_data
- 主方向：Portfolio & Investment / 投资组合与投资管理
- 细分方向：Portfolio Selection & Optimization / 组合选择与优化
- 技术方法标签：Uncertainty & Robustness / 不确定性与鲁棒性；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：optimization
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Finally, we illustrate the utility of our method on a portfolio optimization problem as well as black-box adversarial attacks.

## 原始摘要

Hard-thresholding is an important type of algorithm in machine learning that is used to solve $\ell_0$ constrained optimization problems. However,  the true gradient of the objective function can be difficult to access in certain scenarios, which normally can be approximated by zeroth-order (ZO) methods. SZOHT algorithm is the only algorithm tackling $\ell_0$ sparsity constraints with zeroth-order gradients so far. Unfortunately,  SZOHT  has a notable limitation on the number of random directions due to the inherent conflict between the deviation of ZO gradients and the expansivity of the hard-thresholding operator. This paper approaches this problem by considering the role of variance and provides a new insight into variance reduction: mitigating the unique conflicts between ZO gradients and hard-thresholding.  Under this perspective, we propose a generalized variance reduced ZO hard-thresholding algorithm as well as the generalized convergence analysis under standard assumptions. The theoretical results demonstrate the new algorithm eliminates the restrictions on the number of random directions, leading to improved convergence rates and broader applicability compared with SZOHT.  Finally, we illustrate the utility of our method on a portfolio optimization problem as well as black-box adversarial attacks.
