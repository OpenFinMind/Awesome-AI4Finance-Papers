# ElliCE: Efficient and Provably Robust Algorithmic Recourse via the Rashomon Sets

NeurIPS 2025 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：FICO。 主题：Credit & Financial Risk / 信贷与金融风险；Fraud & AML / 欺诈检测与反洗钱。

- 官方论文页：https://openreview.net/forum?id=GNDgQie8W4
- 摘要来源：https://neurips.cc/virtual/2025/poster/118970
- 本地 PDF：[打开](../../pdfs/NeurIPS/2025/neurips-2025-GNDgQie8W4__ElliCE_Efficient_and_Provably_Robust_Algorithmic_Recourse_via_the_Rashomon_Sets.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Credit Scoring & Default / 信用评分与违约；Lending & Credit Data / 借贷与信贷数据应用；Banknote Authentication / 钞票真伪识别
- 技术方法标签：Fairness & Recourse / 公平性与算法追索；Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

her methods that produce robust counterfactuals. Please see Appendix B for additional details and results. Datasets. We consider nine datasets from high-stakes decision domains such as lending (Aus- tralian Credit [53], FICO [20], German Credit [27], Banknote [44]), healthcare (Parkinson’s [60], Diabetes [58]), and recidivism (COMPAS [2]), as well as benchmark datasets (Wine Quality [13], Extended Iris [3]). Please see Table 3 for detailed dataset descriptions and preprocessing notes. We used datasets with predominantly categorical features (FICO, Australian Credit, C

## 原始摘要

Machine learning models now influence decisions that directly affect people’s lives, making it important to understand not only their predictions, but also how individuals could act to obtain better results. Algorithmic recourse provides actionable input modifications to achieve more favorable outcomes, typically relying on counterfactual explanations to suggest such changes. However, when the Rashomon set - the set of near-optimal models - is large, standard counterfactual explanations can become unreliable, as a recourse action valid for one model may fail under another. We introduce ElliCE, a novel framework for robust algorithmic recourse that optimizes counterfactuals over an ellipsoidal approximation of the Rashomon set. The resulting explanations are provably valid over this ellipsoid, with theoretical guarantees on uniqueness, stability, and alignment with key feature directions. Empirically, ElliCE generates counterfactuals that are not only more robust but also more flexible, adapting to user-specified features constraints  while being substantially faster than existing baselines. This provides a principled and practical solution for reliable recourse under model uncertainty, ensuring stable recommendations for users even as models evolve.
