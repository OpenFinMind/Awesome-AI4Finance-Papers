# Statistical Guarantees in the Search for Less Discriminatory Algorithms

ICLR 2026 · main · application

包含明确的金融任务、金融领域数据或金融案例验证。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=n8FKO0DIl8
- 摘要来源：https://iclr.cc/virtual/2026/poster/10007506
- 本地 PDF：[打开](../../pdfs/ICLR/2026/iclr-2026-n8FKO0DIl8__Statistical_Guarantees_in_the_Search_for_Less_Discriminatory_Algorithms.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_financial_task_or_data
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Lending & Credit Data / 借贷与信贷数据应用
- 技术方法标签：未明确标注
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Recent scholarship argues that this doctrine has direct implications for algorithmic decision-making in high-stakes domains such as employment, lending, and housing, potentially obligating firms to search for “less discriminatory algorithms” (Black et al., 2024). / We also show how stronger distributional assumptions over the model space can yield tighter bounds, and we validate the approach on real-world credit and housing datasets.

## 原始摘要

U.S. discrimination law can impose liability on firms that fail to adopt a less discriminatory alternative (LDA), defined as a decision policy that achieves the same business objectives while reducing disparate impact on legally protected groups. Recent scholarship argues that this doctrine has direct implications for algorithmic decision-making in high-stakes domains such as employment, lending, and housing, potentially obligating firms to search for “less discriminatory algorithms” (Black et al., 2024). Regulators have at times encouraged proactive LDA searches, reinforcing the expectation of a good-faith effort to identify equally performant models with lower disparate impact. Model multiplicity makes such searches plausible: retraining with different random seeds can yield models with comparable predictive performance but materially different disparate impacts. Yet firms cannot retrain indefinitely, raising a central question: when is the search sufficient to demonstrate good faith? We formalize LDA search under multiplicity as an optimal stopping problem in which a developer seeks to produce evidence that further search is unlikely to yield meaningful improvements. Our main contribution is an adaptive stopping algorithm that provides a high-probability upper bound on the best disparate-impact gains attainable through continued retraining, enabling developers to certify (e.g., to a court) that additional search is unlikely to help. We also show how stronger distributional assumptions over the model space can yield tighter bounds, and we validate the approach on real-world credit and housing datasets.
