# Online Time Series Forecasting with Theoretical Guarantees

NeurIPS 2025 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：Exchange benchmark (currency series)。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=0XCZWAo7wN
- 摘要来源：https://neurips.cc/virtual/2025/poster/120310
- 本地 PDF：[打开](../../pdfs/NeurIPS/2025/neurips-2025-0XCZWAo7wN__Online_Time_Series_Forecasting_with_Theoretical_Guarantees.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测
- 技术方法标签：Generative Modeling / 生成建模；Causal Learning / 因果学习；Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：causal；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

1 0.013 0.013 0.012 0.009 0.017 0.015 0.031 0.017 0.113 0.010 Exchange 24 0.039 0.037 0.129 0.102 0.047 0.030 0.060 0.042 0.116 0.035 48 0.043 0.042 0.267 0.195 0.062 0.039 0.065 0.051 0.168 0.040 Finally, the total loss of the proposed method can be summarized as follows: Ltotal = Ly + αLr − β(L

## 原始摘要

This paper is concerned with online time series forecasting, where unknown distribution shifts occur over time, i.e., latent variables influence the mapping from historical to future observations. To develop an automated way of online time series forecasting, we propose a Theoretical framework for Online Time-series forecasting (TOT in short) with theoretical guarantees. Specifically, we prove that supplying a forecaster with latent variables tightens the Bayes risk—the benefit endures under estimation uncertainty of latent variables and grows as the latent variables achieve a more precise identifiability. To better introduce latent variables into online forecasting algorithms, we further propose to identify latent variables with minimal adjacent observations. Based on these results, we devise a model-agnostic blueprint by employing a temporal decoder to match the distribution of observed variables and two independent noise estimators to model the causal inference of latent variables and mixing procedures of observed variables, respectively. Experiment results on synthetic data support our theoretical claims. Moreover, plug-in implementations built on several baselines yield general improvement across multiple benchmarks, highlighting the effectiveness in real-world applications.
