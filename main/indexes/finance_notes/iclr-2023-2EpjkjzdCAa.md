# Effectively Modeling Time Series with Simple Discrete State Spaces

ICLR 2023 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：M4 Quarterly。M4 年度至日度子集包含金融序列，未把仅使用 M4 Hourly 的论文据此纳入。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=2EpjkjzdCAa
- 摘要来源：https://iclr.cc/virtual/2023/poster/10874
- 本地 PDF：[打开](../../pdfs/ICLR/2023/iclr-2023-2EpjkjzdCAa__Effectively_Modeling_Time_Series_with_Simple_Discrete_State_Spaces.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；Representation & Foundation Models / 表征与基础模型
- 技术方法标签：Transformer / Transformer模型
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Time series；time series；Transformers
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

845.3 948.4 M3 Other 265.56 309.7 242.1 217.0 224.1 220.8 262.3 349.9 277.7 248.5 277.0 271.0 M4 Quarterly 718.2 732.8 673.2 672.7 674.3 710.0 711.9 714.2 700.3 684.7 697.0 739.1 M4 Monthly 1092.2 755.5 683.7 743.4 705.7 702.1 720.5 734.8 740.3 705.2 787.9 902.4 M4 Weekly 348.3 412.6 405.2 356.7 408.5 386.3 350.3 4

## 原始摘要

Time series modeling is a well-established problem, which often requires that methods (1) expressively represent complicated dependencies, (2) forecast long horizons, and (3) efficiently train over long sequences. State-space models (SSMs) are classical models for time series, and prior works combine SSMs with deep learning layers for efficient sequence modeling. However, we find fundamental limitations with these prior approaches, proving their SSM representations cannot express  autoregressive time series processes. We thus introduce SpaceTime, a new state-space time series architecture that improves all three criteria. For expressivity, we propose a new SSM parameterization based on the companion matrix---a canonical representation for discrete-time processes---which enables SpaceTime's SSM layers to learn desirable autoregressive processes. For long horizon forecasting, we introduce a "closed-loop" variation of the companion SSM, which enables SpaceTime to predict many future time-steps by generating its own layer-wise inputs. For efficient training and inference, we introduce an algorithm that reduces the memory and compute of a forward pass with the companion matrix. With sequence length $\ell$ and state-space size $d$, we go from $\tilde{O}(d \ell)$ naïvely to $\tilde{O}(d + \ell)$. In experiments, our contributions lead to state-of-the-art results on extensive and diverse benchmarks, with best or second-best AUROC on 6 / 7 ECG and speech time series classification, and best MSE on 14 / 16 Informer forecasting tasks. Furthermore, we find SpaceTime (1) fits AR($p$) processes that prior deep SSMs fail on, (2) forecasts notably more accurately on longer horizons than prior state-of-the-art, and (3) speeds up training on real-world ETTh1 data by 73% and 80% relative wall-clock time over Transformers and LSTMs.
