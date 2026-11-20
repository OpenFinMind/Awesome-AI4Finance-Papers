# Feature-based Learning for Diverse and Privacy-Preserving Counterfactual Explanations

KDD 2023 · Research Track · Main · application · long

- Official paper: https://doi.org/10.1145/3580305.3599343
- Research Track: https://kdd.org/kdd2023/wp-content/uploads/2023/08/toc.html
- Primary task: Financial Safety & Compliance / 金融安全与合规
- Tasks: Financial Safety & Compliance / 金融安全与合规; Credit & Financial Risk / 信贷与金融风险
- Subtopics: Privacy and Sensitive Information Protection / 隐私与敏感信息保护
- Methods: Fairness & Recourse / 公平性与算法追索; Privacy & Federated Learning / 隐私与联邦学习
- Financial evidence source: https://arxiv.org/pdf/2209.13446
- Long-paper evidence: regular Research full-paper track ([format policy](https://kdd.org/kdd2023/call-for-research-track-papers/)).

## Financial evidence

by the development of F1-score in measuring Precision against Recall. For metrics used in privacy analysis, refer 4 EXPERIMENTAL SETUP to Section 5.2. We experiment with 4 popular real-word datasets: German Credit Evaluation setup. We consider a general setting of binary clas- [10], Adult Income [24] Graduate Admission [1] and Student Perforsification where a counterfactual outcome 𝑦 ′ is opposite to the mance [7]. For each dataset, we select a fixed subset of immutable original outcome 𝑦, whether 𝑦 has label 1 or 0. From each method, features based on our domain knowledge and suggestions from we generate a set of 100 counterfactual explanations. During gen- [52]. We reserve the privacy analysis for German Credit and Adult eration, most methods, including ours, require multiple iterations Income datase

## Abstract

Interpretable machine learning seeks to understand the reasoning process of complex black-box systems that are long notorious for lack of explainability. One flourishing approach is through counterfactual explanations, which provide suggestions on what a user can do to alter an outcome. Not only must a counterfactual example counter the original prediction from the black-box classifier but it should also satisfy various constraints for practical applications. Diversity is one of the critical constraints that however remains less discussed. While diverse counterfactuals are ideal, it is computationally challenging to simultaneously address some other constraints. Furthermore, there is a growing privacy concern over the released counterfactual data. To this end, we propose a feature-based learning framework that effectively handles the counterfactual constraints and contributes itself to the limited pool of private explanation models. We demonstrate the flexibility and effectiveness of our method in generating diverse counterfactuals of actionability and plausibility. Our counterfactual engine is more efficient than counterparts of the same capacity while yielding the lowest re-identification risks.

[PDF](../../pdfs/KDD/2023/kdd-2023-6ccdebc76b46__Feature-based_Learning_for_Diverse_and_Privacy-Preserving_Counterfactual_Explanations.pdf)

Version: `arxiv` · SHA-256: `7c2d3912e1293ae839ad917d992a93e2c11cbf668d9ebde9997e33de5fd604b8`

## Classification / 分类

- Primary task / 主方向: Financial Safety / 金融安全
- Primary subcategory / 主要子分类: Privacy and Sensitive Information Protection / 隐私与敏感信息保护
- Related tasks / 关联方向: Financial Safety / 金融安全
- Subcategories / 子分类: Privacy and Sensitive Information Protection / 隐私与敏感信息保护
- Methods / 技术方法: Fairness & Recourse / 公平性与算法追索; Privacy & Federated Learning / 隐私与联邦学习
- Review status / 核对状态: `inherited_evidence_mapping`
- [Definitions / 分类定义](../finance_taxonomy.md) · [Evidence / 分类依据](../../checks/finance_taxonomy/assignments.json)
