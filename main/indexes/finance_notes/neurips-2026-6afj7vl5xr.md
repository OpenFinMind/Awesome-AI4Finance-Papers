# PE-SHAP: Causally Interpretable Path-Wise Shapley Explanations

NeurIPS 2026 · main · application

包含明确的金融任务、金融领域数据或金融案例验证。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=6afj7vl5xr
- 摘要来源：https://neurips.cc/Downloads/2026
- PDF 状态：access_blocked
- 金融依据类型：title_abstract_financial_task_or_data
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Credit Scoring & Default / 信用评分与违约
- 技术方法标签：Causal Learning / 因果学习；Fairness & Recourse / 公平性与算法追索
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：causal
- 数据 / 评测名称（题名和摘要可确认）：German Credit
- 代码链接：摘要未提供可确认链接

## 纳入依据

We validate PE-SHAP analytically and through Monte-Carlo experiments on synthetic SCMs with known path effects, and demonstrate it on real-world fairness case studies using the German Credit and COMPAS datasets.

## 原始摘要

Shapley value-based explanations are widely used to attribute model predictions, but standard variants capture associative rather than causal relationships. Recent causally informed Shapley methods add a path-wise decomposition, but suffer from two key limitations: they assign zero attribution to chain-mediated paths, and their per-path values do not align with classical mediation estimands.  We propose PE-SHAP, a Shapley-inspired path-wise decomposition built on the portion-eliminated effect. Per-mediator values sum to the total mediated effect at every sample, aggregate to the Natural Indirect Effect at the population level, and match the Path-Specific Effect under additive separability. These are properties prior Shapley-based path-wise methods do not provide. We validate PE-SHAP analytically and through Monte-Carlo experiments on synthetic SCMs with known path effects, and demonstrate it on real-world fairness case studies using the German Credit and COMPAS datasets.
