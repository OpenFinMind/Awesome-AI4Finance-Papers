# Strengthening LLMs for Tabular Prediction with Structural Priors

NeurIPS 2026 · main · application

正文包含金融数据、金融训练数据、金融任务评测或具体金融场景案例。 主题：Credit & Financial Risk / 信贷与金融风险；Banking & Customer Service / 银行业务与客户服务。

- 官方论文页：https://openreview.net/forum?id=pTunYUdPGz
- 摘要来源：https://neurips.cc/virtual/2026/poster/149527
- 本地 PDF：[打开](../../pdfs/NeurIPS/2026/neurips-2026-pTunYUdPGz__Strengthening_LLMs_for_Tabular_Prediction_with_Structural_Priors.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Banking Dialogue & Intent / 银行对话与意图；Bank Marketing & Churn / 银行营销与客户流失；Lending & Credit Data / 借贷与信贷数据应用
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Reinforcement Learning / 强化学习；Tabular Learning / 表格学习；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：language models；LLM；LLMs；Optimization；optimization；reinforcement learning
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

in our experiments. n tio me via na bre set Ab ata set ll d ta Da Fu 1000 1000_Cameras_Dataset AAPL AAPL_stock_price_2021_2022 AVIDa AVIDa_SARS_CoV_2 Amazo Amazon_employee_access_seed_0_nrows_2000_nclasses_10_ncols_100_stratify_True Bank Bank_Customer_Churn Bosto Boston_house_price_data CPMP CPMP_2015_runtime_regression Carpe CarpenterFdaData Click Click_prediction_small_seed_0_nrows_2000_nclasses_10_ncols_100_stratify_True Emplo Employee Fraud Fraud_Detection_Updated Goodr Goodreads_Computer_Books HMEQ HMEQ_Data Lisbo Lisbon_House_Prices Loan Loan_Predication Continued on next page 18 (continued) n tio me via na bre et Ab tas set da ta ll Da Fu MIP MIP_2016_regression Mammo Mammographic_Mass_Data_Set Marke Marketing_Campaign

## 原始摘要

Tabular prediction has long been dominated by gradient-boosted decision trees and specialized deep tabular models, while large language models (LLMs) remain difficult to make competitive despite their cross-task adaptability and transparent reasoning traces. Existing LLM-for-tabular methods mainly adapt tables into textual inputs, but often fail to capture key structural properties of tabular data. In this work, we propose Permutation Relative Policy Optimization (PRPO), a reinforcement learning post-training method that strengthens LLMs for tabular prediction by injecting column-permutation invariance as a structural prior. By constructing label-preserving column permutations and estimating advantages both within and across them, PRPO converts sparse outcome rewards into denser and more stable optimization signals. Extensive experiments on 139 OpenML datasets show that our 8B model reaches a genuinely competitive regime against strong specialized tabular baselines. It achieves strong fully supervised performance, dominates cross-dataset zero-shot settings, and performs on par with 32-shot strong baselines. Moreover, it substantially outperforms much larger general-purpose and reasoning LLMs, including up to a 53.17% improvement over DeepSeek-R1 (685B). These results show that structural-prior RL post-training is an effective route for making LLMs competitive in tabular prediction.
