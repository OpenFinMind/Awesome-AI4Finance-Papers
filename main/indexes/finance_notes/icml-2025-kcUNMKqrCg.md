# Conditional Diffusion Model with Nonlinear Data Transformation for Time Series Forecasting

ICML 2025 · main · application

实验使用汇率、宏观金融、信用评估或财务文档等金融相关基准。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=kcUNMKqrCg
- 摘要来源：https://icml.cc/virtual/2025/poster/44243
- 本地 PDF：[打开](../../pdfs/ICML/2025/icml-2025-kcUNMKqrCg__Conditional_Diffusion_Model_with_Nonlinear_Data_Transformation_for_Time_Series_Forecasting.pdf)；版本：publisher_version
- 金融依据类型：fulltext_financial_benchmark
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测
- 技术方法标签：Diffusion & Flow / 扩散与流模型；Generative Modeling / 生成建模
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：diffusion；Diffusion；time series；variational
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

tricity. Results of all baselines are from (Shen et al., 2024) Method NorPool Caiso Traffic Electricity Weather Exchange ETTh1 ETTm1 Wind Rank Ours 0.531(1) 0.094(1) 0.374(2) 0.145(1) 0.296(1) 0.016(1) 0.405(1) 0.340(2) 0.988(5) 1.7 mr-Diff 0.645(3) 0.127(4) 0.474(7) 0.155(4) 0.296(1) 0.016(1) 0.411(4) 0.340(2) 0.881(1) 3.0 TimeDiff 0.665(5) 0.136(7) 0.564(8) 0.193(6) 0.311(3) 0.018(7)

## 原始摘要

Time-series forecasting finds application across domains such as finance, climate science, and energy systems. We introduce the Conditional Diffusion  with Nonlinear Data Transformation Model (CN-Diff), a generative framework that employs novel nonlinear transformations and learnable conditions in the forward process for time series forecasting. A new loss formulation for training is proposed, along with a detailed derivation of both forward and reverse process. The new additions improve the diffusion model's capacity to capture complex time series patterns, thus simplifying the reverse process. Our novel condition facilitates learning an efficient prior distribution. This also reduces the gap between the true negative log-likelihood and its variational approximation. CN-Diff is shown to perform better than other leading time series models on nine real-world datasets. Ablation studies are conducted to elucidate the role of each component of CN-Diff.
