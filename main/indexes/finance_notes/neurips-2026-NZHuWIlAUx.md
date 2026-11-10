# Stable Alpha: Adversarial Invariant Representation Learning for Nonlinear Asset Pricing  under Temporal Distribution Shifts

NeurIPS 2026 · main · core

以金融任务或金融数据为核心研究对象。 主题：Asset Pricing / 资产定价。

- 官方论文页：https://openreview.net/forum?id=NZHuWIlAUx
- 摘要来源：https://neurips.cc/Downloads/2026
- PDF 状态：access_blocked
- 金融依据类型：title_abstract_review
- 主方向：Asset Pricing / 资产定价
- 细分方向：Pricing Models & Risk Premia / 定价模型与风险溢价
- 技术方法标签：Causal Learning / 因果学习；Uncertainty & Robustness / 不确定性与鲁棒性；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

原清单未单列纳入摘录；保留的题名分类证据如下，详见分类记录。

Stable Alpha: Adversarial Invariant Representation Learning for Nonlinear Asset Pricing under Temporal Distribution Shifts

## 原始摘要

Deep learning has emerged as a powerful paradigm for constructing nonlinear asset pricing factor models. However, temporal distribution shifts such as bull-bear transitions and industry rotations undermine the generalization of models trained under the i.i.d. assumption. As a result, existing models tend to exploit environment-specific correlations that are highly predictive in-sample but unstable across market regimes. To address this challenge, we propose $\textit{\textbf{CASH}}$, a causality-inspired asset pricing factor framework designed to learn invariant and minimally sufficient representations under temporal distribution shifts. CASH formulates an information-theoretic adversarial learning objective that systematically discards transient market noise by optimizing against an adversary designed to exploit spurious correlations, thereby distilling invariant factor-return relationships. The resulting invariant representation is then integrated into a conditional factor pricing model via a dynamic factor exposure network. Experiments on real-world stock datasets across multiple markets demonstrate that CASH consistently outperforms state-of-the-art baselines in out-of-sample return prediction and exhibits superior robustness under pronounced temporal regime shifts.
