# GT-GAN: General Purpose Time Series Synthesis with Generative Adversarial Networks

NeurIPS 2022 · main · application

正文包含金融数据、金融任务或金融领域评测。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=ez6VHWvuXEx
- 摘要来源：https://neurips.cc/virtual/2022/poster/54370
- 本地 PDF：[打开](../../pdfs/NeurIPS/2022/neurips-2022-ez6VHWvuXEx__GT_GAN_General_Purpose_Time_Series_Synthesis_with_Generative_Adversarial_Networks.pdf)；版本：publisher_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Generation & Simulation / 序列生成与仿真；Imputation & Irregular Series / 缺失与不规则序列
- 技术方法标签：Generative Modeling / 生成建模；Uncertainty & Robustness / 不确定性与鲁棒性；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Time series；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

phases independently. For each feature, i ∈ {1, ..., 5}, xi (t) = sin(2πfi t + θi ), wherefi ∼ U[0, 1] and θi ∼ U[−π, π]. MuJoCo is multivariate physics simulation time series data with 14 features. Stocks is the Google stock price data from 2004 to 2019. Each observation represents one day and has 6 features. Energy is a UCI appliance energy prediction dataset with 28 values. To create the challenging irregular environments, 30, 50, 70% of observations from each time series sample {(ti , xreal i )}N

## 原始摘要

Time series synthesis is an important research topic in the field of deep learning, which can be used for data augmentation. Time series data types can be broadly classified into regular or irregular. However, there are no existing generative models that show good performance for both types without any model changes. Therefore, we present a general purpose model capable of synthesizing regular and irregular time series data. To our knowledge, we are the first designing a general purpose time series synthesis model, which is one of the most challenging settings for time series synthesis. To this end, we design a generative adversarial network-based method, where many related techniques are carefully integrated into a single framework, ranging from neural ordinary/controlled differential equations to continuous time-flow processes. Our method outperforms all existing methods.
