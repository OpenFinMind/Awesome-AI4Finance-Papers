# Advancing Constrained Monotonic Neural Networks: Achieving Universal Approximation Beyond Bounded Activations

ICML 2025 · main · application

正文包含金融数据、金融任务或金融领域评测。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=RAa8muWVhW
- 摘要来源：https://icml.cc/virtual/2025/poster/45293
- 本地 PDF：[打开](../../pdfs/ICML/2025/icml-2025-RAa8muWVhW__Advancing_Constrained_Monotonic_Neural_Networks_Achieving_Universal_Approximation_Beyond_Bounded_Activati.pdf)；版本：publisher_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Credit Scoring & Default / 信用评分与违约；Lending & Credit Data / 借贷与信贷数据应用
- 技术方法标签：Uncertainty & Robustness / 不确定性与鲁棒性；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：optimization
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Beyond Bounded Activations Table 1. Test metrics across different datasets. The best-performing architecture per dataset is bolded. COMPAS Blog Feedback Loan Defaulter AutoMPG Heart Disease Method (Test Accuracy) (Test RMSE) (Test Accuracy) (Test MSE) (Test Accuracy) XGBoost 68.5% ± 0.1% 0.176 ± 0.005 63.7% ± 0.1% - - Certified 68.8% ± 0.2% 0.159

## 原始摘要

Imposing input-output constraints in multi-layer perceptrons (MLPs) plays a pivotal role in many real world applications. Monotonicity in particular is a common requirement in applications that need transparent and robust machine learning models. Conventional techniques for imposing monotonicity in MLPs by construction involve the use of non-negative weight constraints and bounded activation functions, which poses well known optimization challenges.  In this work, we generalize previous theoretical results, showing that MLPs with non-negative weight constraint and activations that saturate on alternating sides are universal approximators for monotonic functions.  Additionally, we show an equivalence between saturation side in the activations and sign of the weight constraint. This connection allows us to prove that MLPs with convex monotone activations and non-positive constrained weights also qualify as universal approximators, in contrast to their non-negative constrained counterparts.  This results provide theoretical grounding to the empirical effectiveness observed in previous works, while leading to possible architectural simplification.  Moreover, to further alleviate the optimization difficulties, we propose an alternative formulation that allows the network to adjust its activations according to the sign of the weights. This eliminates the requirement for weight reparameterization, easing initialization and improving training stability.  Experimental evaluation reinforce the validity of the theoretical results, showing that our novel approach compares favorably to traditional monotonic architectures.
