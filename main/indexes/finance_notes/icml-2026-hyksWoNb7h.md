# DRL-STAF: A Deep Reinforcement Learning Framework for State-Aware Forecasting of Complex Multivariate Hidden Markov Processes

ICML 2026 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：Exchange benchmark (currency series)。 主题：Time Series / 时间序列；Market Prediction / 股价、收益与波动率预测。

- 官方论文页：https://openreview.net/forum?id=hyksWoNb7h
- 摘要来源：https://icml.cc/virtual/2026/poster/62284
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-hyksWoNb7h__DRL_STAF_A_Deep_Reinforcement_Learning_Framework_for_State_Aware_Forecasting_of_Complex_Multivariate_Hidd.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；FX & Crypto Forecasts / 汇率与加密资产预测
- 技术方法标签：Reinforcement Learning / 强化学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：reinforcement learning
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

n real-world datasets. SMachine dataset Exchange dataset Traffic dataset Models Accuracy Precision Recall F1 MAE MSE MAE MSE MAE MSE Parallel HMM 76.37% 55.86% 90.95% 69.21% 0.0563 0.0056 8.6701 294.0451 5.5411 59.5501 Parallel HSMM

## 原始摘要

Forecasting multivariate hidden Markov processes is challenging due to nonlinear and nonstationary observations, latent state transitions, and cross-sequence dependencies. While deep learning methods achieve strong predictive accuracy, they typically lack explicit state modeling, whereas Hidden Markov Models (HMMs) provide interpretable latent states but struggle with complex nonlinear emissions and scalability. To address these limitations, we propose DRL-STAF, a **D**eep **R**einforcement **L**earning based **ST**ate-**A**ware **F**orecasting framework that jointly predicts next-step observations and estimates the corresponding hidden states for complex multivariate hidden Markov processes. Specifically, DRL-STAF models complex nonlinear emissions using deep neural networks and estimates discrete hidden states using reinforcement learning, reducing the reliance on predefined transition structures and enabling flexible adaptation to diverse temporal dynamics. In particular, DRL-STAF mitigates the state-space explosion encountered by typical multivariate HMM-based methods. Extensive experiments demonstrate that DRL-STAF outperforms HMM variants, standalone deep learning models, and existing DL-HMM hybrids in most cases, while also providing reliable hidden-state estimates.
