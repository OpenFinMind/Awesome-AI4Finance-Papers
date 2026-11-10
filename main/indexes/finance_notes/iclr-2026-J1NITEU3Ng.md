# ATEX-CF: Attack-Informed Counterfactual Explanations for Graph Neural Networks

ICLR 2026 · main · application

正文包含金融数据、金融训练数据、金融任务评测或具体金融场景案例。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=J1NITEU3Ng
- 摘要来源：https://iclr.cc/virtual/2026/poster/10010240
- 本地 PDF：[打开](../../pdfs/ICLR/2026/iclr-2026-J1NITEU3Ng__ATEX_CF_Attack_Informed_Counterfactual_Explanations_for_Graph_Neural_Networks.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_case_or_formal_model
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Credit Scoring & Default / 信用评分与违约；Lending & Credit Data / 借贷与信贷数据应用
- 技术方法标签：Graph Learning / 图学习；Fairness & Recourse / 公平性与算法追索；Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：graph neural networks
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

strate the limitations Alice Alice of existing counterfactual methods, consider a scenario from the Loan-Decision dataset 6 6 4 (Ma et al., 2025). Loan approval is granted when both conditions are met: income > 5 and degree > 3. Applicant Alice has 4 3 5 4 3 5 income 6 (satisfies condition) but degree 3 (fails). The model predicts rejection. Classi- Figure 1: Illustration of counterfactual limitations cal deletion-based counterfactual methods fail in the Loan Decision dataset. here–removing edges further reduces degree. Unconstrained edge additions (e.g., linking to a billionaire) succeed but can be implausible. Our method ATEX-CF identifies a feasible peer connection that serves as an actionable update and flips the prediction. Wh

## 原始摘要

Counterfactual explanations offer an intuitive way to interpret graph neural networks (GNNs) by identifying minimal changes that alter a model’s prediction, thereby answering “what must differ for a different outcome?”. In this work, we propose a novel framework, ATEX-CF that unifies adversarial attack techniques with counterfactual explanation generation—a connection made feasible by theirshared goal of flipping a node’s prediction, yet differing in perturbation strategy:adversarial attacks often rely on edge additions, while counterfactual methods typically use deletions. Unlike traditional approaches that treat explanation and attack separately, our method efficiently integrates both edge additions and deletions, grounded in theory, leveraging adversarial insights to explore impactful counterfactuals. In addition, by jointly optimizing fidelity, sparsity, and plausibility under a constrained perturbation budget, our method produces instance-level explanations that are both informative and realistic. Experiments on synthetic and real-world node classification benchmarks demonstrate that ATEX-CF generates faithful, concise, and plausible explanations, highlighting the effectiveness of integrating adversarial insights into counterfactual reasoning for GNNs.
