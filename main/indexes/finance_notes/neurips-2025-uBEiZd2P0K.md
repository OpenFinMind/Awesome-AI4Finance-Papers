# Conformal Risk Training: End-to-End Optimization of Conformal Risk Control

NeurIPS 2025 · main · application

通用方法在金融任务、数据或明确案例上开展应用验证。 主题：Credit & Financial Risk / 信贷与金融风险；Financial IR & RAG / 金融检索与RAG。

- 官方论文页：https://openreview.net/forum?id=uBEiZd2P0K
- 摘要来源：https://neurips.cc/virtual/2025/poster/115522
- 本地 PDF：[打开](../../pdfs/NeurIPS/2025/neurips-2025-uBEiZd2P0K__Conformal_Risk_Training_End_to_End_Optimization_of_Conformal_Risk_Control.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_review
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Financial Risk / 金融风险管理；Financial RAG & Long Documents / 金融RAG与长文档
- 技术方法标签：Uncertainty & Robustness / 不确定性与鲁棒性；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：conformal
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Our method achieves provable risk guarantees while demonstrating significantly improved average-case performance over post-hoc approaches on applications to controlling classifiers' false negative rate and controlling financial risk in battery storage operation.

## 原始摘要

While deep learning models often achieve high predictive accuracy, their predictions typically do not come with any provable guarantees on risk or reliability, which are critical for deployment in high-stakes applications. The framework of conformal risk control (CRC) provides a distribution-free, finite-sample method for controlling the expected value of any bounded monotone loss function and can be conveniently applied post-hoc to any pre-trained deep learning model. However, many real-world applications are sensitive to tail risks, as opposed to just expected loss. In this work, we develop a method for controlling the general class of Optimized Certainty-Equivalent (OCE) risks, a broad class of risk measures which includes as special cases the expected loss (generalizing the original CRC method) and common tail risks like the conditional value-at-risk (CVaR). Furthermore, standard post-hoc CRC can degrade average-case performance due to its lack of feedback to the model. To address this, we introduce "conformal risk training," an end-to-end approach that differentiates through conformal OCE risk control _during model training or fine-tuning_. Our method achieves provable risk guarantees while demonstrating significantly improved average-case performance over post-hoc approaches on applications to controlling classifiers' false negative rate and controlling financial risk in battery storage operation.
