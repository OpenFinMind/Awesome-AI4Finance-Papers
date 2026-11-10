# Distributional Adversarial Attacks and Training in Deep Hedging

NeurIPS 2025 · main · core

以金融任务或金融数据为核心研究对象。 主题：Derivatives & Hedging / 衍生品定价与对冲。

- 官方论文页：https://openreview.net/forum?id=vBtfIafffU
- 摘要来源：https://neurips.cc/virtual/2025/poster/115434
- 本地 PDF：[打开](../../pdfs/NeurIPS/2025/neurips-2025-vBtfIafffU__Distributional_Adversarial_Attacks_and_Training_in_Deep_Hedging.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_review
- 主方向：Derivatives & Hedging / 衍生品定价与对冲
- 细分方向：Hedging / 对冲
- 技术方法标签：Uncertainty & Robustness / 不确定性与鲁棒性；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：optimization
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

In this paper, we study the robustness of classical deep hedging strategies under distributional shifts by leveraging the concept of adversarial attacks. / We first demonstrate that standard deep hedging models are highly vulnerable to small perturbations in the input distribution, resulting in significant performance degradation. / Motivated by this, we propose an adversarial training framework tailored to increase the robustness of deep hedging strategies. / This enables the efficient training of hedging strategies that are resilient to distributional perturbations. / Through extensive numerical experiments, we show that adversarially trained deep hedging strategies consistently outperform their classical counterparts in terms of out-of-sample performance and resilience to model misspecification. / Our findings establish a practical and effective framework for robust deep hedging under realistic market uncertainties.

## 原始摘要

In this paper, we study the robustness of classical deep hedging strategies under distributional shifts by leveraging the concept of adversarial attacks. We first demonstrate that standard deep hedging models are highly vulnerable to small perturbations in the input distribution, resulting in significant performance degradation. Motivated by this, we propose an adversarial training framework tailored to increase the robustness of deep hedging strategies. Our approach extends pointwise adversarial attacks to the distributional setting and introduces a computationally tractable reformulation of the adversarial optimization problem over a Wasserstein ball. This enables the efficient training of hedging strategies that are resilient to distributional perturbations. Through extensive numerical experiments, we show that adversarially trained deep hedging strategies consistently outperform their classical counterparts in terms of out-of-sample performance and resilience to model misspecification. Additional results indicate that the robust strategies maintain reliable performance on real market data and remain effective during periods of market change. Our findings establish a practical and effective framework for robust deep hedging under realistic market uncertainties.
