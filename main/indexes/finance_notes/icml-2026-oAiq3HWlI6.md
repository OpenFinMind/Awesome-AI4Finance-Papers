# Density-Guided Robust Counterfactual Explanations on Tabular Data under Model Multiplicity

ICML 2026 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：HELOC。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=oAiq3HWlI6
- 摘要来源：https://icml.cc/virtual/2026/poster/61642
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-oAiq3HWlI6__Density_Guided_Robust_Counterfactual_Explanations_on_Tabular_Data_under_Model_Multiplicity.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Credit Scoring & Default / 信用评分与违约
- 技术方法标签：Generative Modeling / 生成建模；Fairness & Recourse / 公平性与算法追索；Uncertainty & Robustness / 不确定性与鲁棒性；Tabular Learning / 表格学习；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Contrastive；distillation；optimization
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/G-AILab/DensityFlow}.

## 纳入依据

0.8579 (.001) black-box ensemble M. As shown in the results, Densi- Compas 7214 9 0.6753 (.003) tyFlow consistently achieves high validity while maintain- HELOC 10459 23 0.7106 (.002) Blood 748 4 0.7994 (.004) ing competitive costs. Specifically, on real-world tabular datasets such as Adult and Compas, our method

## 原始摘要

Counterfactual explanations (CEs) are essential for actionable recourse, yet their reliability is often compromised in low-density regions, where classifiers exhibit high variance. Unlike existing methods that rely on expensive ensemble intersections to define stability, we propose DensityFlow, a generative framework that constructs robust CEs by adhering to the high-confidence data manifold. Specifically, we model the counterfactual generation as continuous-time dynamics parameterized by Neural ODE, guided by a differentiable density score to actively avoid uncertain, low-density areas. This density score is learned via Noise Contrastive Estimation, effectively leveraging a $(K{+}1)$-way discriminator to estimate density ratios. For black-box settings, we introduce a local proxy distillation mechanism that aligns a lightweight surrogate with the target model strictly within the trajectory of CE generation, enabling efficient gradient-based optimization with minimal queries. Experiments demonstrate that \textit{DensityFlow} achieves superior validity under model multiplicity while significantly reducing query costs compared to ensemble-based baselines. Our implementation is available at \url{https://github.com/G-AILab/DensityFlow}.
