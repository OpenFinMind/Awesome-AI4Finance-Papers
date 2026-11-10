# Flow Matching with Gaussian Process Priors for Probabilistic Time Series Forecasting

ICLR 2025 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：Exchange benchmark (currency series)。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=uxVBbSlKQ4
- 摘要来源：https://iclr.cc/virtual/2025/poster/27944
- 本地 PDF：[打开](../../pdfs/ICLR/2025/iclr-2025-uxVBbSlKQ4__Flow_Matching_with_Gaussian_Process_Priors_for_Probabilistic_Time_Series_Forecasting.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；Probabilistic Forecasting & Calibration / 概率预测与校准
- 技术方法标签：Diffusion & Flow / 扩散与流模型；Generative Modeling / 生成建模
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：diffusion；Gaussian processes；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

ts for different generative models and prior distributions. Best scores in bold, second best underlined. Method NFE(↓) Electr. Exchange KDDCup M4 (H) Solar Traffic UberTLC Wiki2000 TimeVAE 1 3.201±0.08 0.034±0.005 39.975±13.239 7.071±0.096 7.537±0.092 9.626±0.241 79.35±16.065 218.764±2.021 TSDiff 100 3.112±0.32 0.057±0.035 29.556±1.445 6.095±0.292 5.422±1.173 7.228±0.128 67.281±6.992 214.981±20.16 Isotropi

## 原始摘要

Recent advancements in generative modeling, particularly diffusion models, have opened new directions for time series modeling, achieving state-of-the-art performance in forecasting and synthesis. However, the reliance of diffusion-based models on a simple, fixed prior complicates the generative process since the data and prior distributions differ significantly. We introduce TSFlow, a conditional flow matching (CFM) model for time series combining Gaussian processes, optimal transport paths, and data-dependent prior distributions. By incorporating (conditional) Gaussian processes, TSFlow aligns the prior distribution more closely with the temporal structure of the data, enhancing both unconditional and conditional generation. Furthermore, we propose conditional prior sampling to enable probabilistic forecasting with an unconditionally trained model. In our experimental evaluation on eight real-world datasets, we demonstrate the generative capabilities of TSFlow, producing high-quality unconditional samples. Finally, we show that both conditionally and unconditionally trained models achieve competitive results across multiple forecasting benchmarks.
