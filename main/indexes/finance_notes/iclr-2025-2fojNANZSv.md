# Mixture of In-Context Prompters for Tabular PFNs

ICLR 2025 · main · application

正文包含金融数据、金融训练数据、金融任务评测或具体金融场景案例。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=2fojNANZSv
- 摘要来源：https://iclr.cc/virtual/2025/poster/31124
- 本地 PDF：[打开](../../pdfs/ICLR/2025/iclr-2025-2fojNANZSv__Mixture_of_In_Context_Prompters_for_Tabular_PFNs.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Credit Scoring & Default / 信用评分与违约
- 技术方法标签：Transformer / Transformer模型；Uncertainty & Robustness / 不确定性与鲁棒性；Tabular Learning / 表格学习；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：transformers
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

atasets ALL MixturePFN, CatBoost, ada-agnostic, australian, balance-scale, TabPFN*, XGBoost, colic, credit-approval, elevators, heart-h, ResNet, FTTransformer, jasmine, kc1, lymph, mfeat-fourier, mfeat-zernike, LightGBM, SAINT, monks-problems-2, phoneme, profb, NODE, MLP-rtdl, qsar-biodeg, socmob, speeddating, splice, vehicle RandomForest, TabNet, MLP, DecisionTree, LinearModel, STG, VIME, KNN, DANet, SVM Top-10 MixturePFN, CatBoost, ada-agnostic, artificial-characters, australian, TabPFN*, XGBoost, balance-scale, colic, credit-approval, elevators, ResNet, LightGBM, gesturephasesegmentationprocessed, heart-h, jasmine, SAINT, DANet, kc1, lymph, mfeat-fourier, mfeat-zernike, FTTransformer, SVM, monks-problems-2, phoneme, profb,

## 原始摘要

Recent benchmarks find In-Context Learning (ICL) outperforms both deep learning and tree-based algorithms on small tabular datasets. However, on larger datasets, ICL for tabular learning suffers in both efficiency and effectiveness. In terms of efficiency, transformers incur linear space and quadratic time complexity w.r.t. context size. In terms of effectiveness, contexts at inference encounter distribution shift compared to contexts from pretraining. We propose MixturePFN, which extends Sparse Mixture of Experts to the state-of-the-art ICL for tabular learning model. Specifically, MixturePFN finetunes a specialized ICL expert on each cluster of tabular data and routes new test samples to appropriate experts at inference. MixturePFN supports constant-size contexts by splitting large training datasets into more manageable clusters. MixturePFN addresses distribution shift by finetuning an expert on each training dataset cluster via bootstrapping. Extensive experimental results shows MixturePFN outperforms 19 baselines both in mean rank and as the Condorcet winner across 36 diverse tabular datasets under both accuracy and F1 score with statistical significance.
