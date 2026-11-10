# Adversarially Robust Control of Conditional Value-at-Risk via Rockafellar-Uryasev Conformal Inference

ICML 2026 · main · application

通用方法在金融任务、数据或明确案例上开展应用验证。 主题：Portfolio & Investment / 投资组合与投资管理。

- 官方论文页：https://openreview.net/forum?id=Vhesstbfg6
- 摘要来源：https://icml.cc/virtual/2026/poster/63594
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-Vhesstbfg6__Adversarially_Robust_Control_of_Conditional_Value_at_Risk_via_Rockafellar_Uryasev_Conformal_Inference.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_review
- 主方向：Portfolio & Investment / 投资组合与投资管理
- 细分方向：Investment Evaluation & Decisions / 投资评价与决策
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：conformal；Language Models；LLMs；variational
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

We demonstrate the effectiveness of our approach on portfolio risk management and toxicity mitigation for Large Language Models (LLMs), where rare but catastrophic failures dominate system risk.

## 原始摘要

We present an online, distribution-free framework for controlling the Conditional Value-at-Risk ($\operatorname{CVaR}$), extending conformal tail risk control to non-stationary and adversarial environments. Unlike classical risk control methods, which rely on stationarity or linearity of expectation, our approach provides provable safety guarantees for a nonlinear tail risk functional under arbitrary data-generating processes that may drift or shift strategically over time. By leveraging deep connections between conformal tail risk control, online learning, and the variational representation of $\operatorname{CVaR}$ introduced by Rockafellar and Uryasev, we develop a novel procedure for online $\operatorname{CVaR}$ control with adversarial regret guarantees. The proposed method operates without assumptions on the underlying data-generating process, making it broadly applicable in modern high-stakes deployment settings. We prove that the realized empirical $\operatorname{CVaR}$ is asymptotically controlled at the target level, and that the resulting control is asymptotically tight up to a finite-sample ${O}(1/\sqrt{T})$ conservatism gap. We demonstrate the effectiveness of our approach on portfolio risk management and toxicity mitigation for Large Language Models (LLMs), where rare but catastrophic failures dominate system risk.
