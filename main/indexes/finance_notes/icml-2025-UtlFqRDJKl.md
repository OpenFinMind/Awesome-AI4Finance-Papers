# TabSDS: a Lightweight, Fully Non-Parametric, and Model Free Approach for Generating Synthetic Tabular Data

ICML 2025 · main · application

正文包含明确金融数据、金融任务或金融案例；金融应用可属于通用方法的一个实验。 主题：Banking & Customer Service / 银行业务与客户服务。

- 官方论文页：https://openreview.net/forum?id=UtlFqRDJKl
- 摘要来源：https://icml.cc/virtual/2025/poster/45094
- 本地 PDF：[打开](../../pdfs/ICML/2025/icml-2025-UtlFqRDJKl__TabSDS_a_Lightweight_Fully_Non_Parametric_and_Model_Free_Approach_for_Generating_Synthetic_Tabular_Data.pdf)；版本：publisher_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Banking & Customer Service / 银行业务与客户服务
- 细分方向：Bank Marketing & Churn / 银行营销与客户流失
- 技术方法标签：Generative Modeling / 生成建模；Uncertainty & Robustness / 不确定性与鲁棒性；Tabular Learning / 表格学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

9 (0.005) (0.006) (0.005) (0.018) (0.018) (0.012) tions the figure only report results for the Abalone (AB) and DI 0.611 0.621 0.625 0.561 0.579 0.616 Bank marketing (BM) datasets. The complete results for (0.005) (0.003) (0.004) (0.023) (0.031) (0.005) EL 0.836 0.889 0.889 0.821 0.806 0.657 all datasets are presented in Figures 24 and 25 in Appendix (0.003) (0.003) (0.005) (0.010) (0.023) (0.024) G.6.) In addition to

## 原始摘要

The development of deep generative models for tabular data is currently a very active research area in machine learning. These models, however, tend to be computationally heavy and require careful tuning of multiple model parameters. In this paper, we propose TabSDS - a lightweight, non-parametric, and model free alternative to tabular deep generative models which leverages rank and data shuffling transformations for generating synthetic data which closely approximates the joint probability distribution of the real data. We evaluate TabSDS against multiple baselines implemented in the Synthcity Python library across several datasets. TabSDS showed very competitive performance against all baselines (including TabDDPM - a strong baseline model for tabular data generation). Importantly, the execution time of TabSDS is orders of magnitude faster than the deep generative baselines, and also considerably faster than other computationally efficient baselines such as adversarial random forests.
