# Time Series Generation Under Data Scarcity: A Unified Generative Modeling Approach

NeurIPS 2025 · main · application

正文包含金融数据、金融训练数据、金融任务评测或具体金融场景案例。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=p324ryBKTc
- 摘要来源：https://neurips.cc/virtual/2025/poster/115993
- 本地 PDF：[打开](../../pdfs/NeurIPS/2025/neurips-2025-p324ryBKTc__Time_Series_Generation_Under_Data_Scarcity_A_Unified_Generative_Modeling_Approach.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Representation & Foundation Models / 表征与基础模型；Generation & Simulation / 序列生成与仿真
- 技术方法标签：Diffusion & Flow / 扩散与流模型；Generative Modeling / 生成建模；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：diffusion；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/azencot-group/ImagenFew.

## 纳入依据

, encouraging the learning of transferable representations that are useful in data-scarce settings. Specifi- cally, we utilize the datasets: Stocks, Energy [6], ETTh1 [68], Exchange [35], MSL [27], SMAP [27], PSM [1], SMD [57], ECG5000 [21], NonInvasiveFetalECGThorax1 [53], SelfRegulationSCP2 [2], Blink [11], ElectricDevices [37], Trace [52], FordB [15], UWaveGestureLibrary [40], EMOPain [18], Chinatown [15], and SharePriceIncrease [42]. These datasets combine commonly used collections from various tasks in UniTS [20] with datasets from generative modeling research [44, 67]. In our approach, all of these datasets are jointly employed during the pre-training phase, encompassing approximately 300,000 time series in total. During pre-train

## 原始摘要

Generative modeling of time series is a central challenge in time series analysis, particularly under data-scarce conditions. Despite recent advances in generative modeling, a comprehensive understanding of how state-of-the-art generative models perform under limited supervision remains lacking. In this work, we conduct the first large-scale study evaluating leading generative models in data-scarce settings, revealing a substantial performance gap between full-data and data-scarce regimes. To close this gap, we propose a unified diffusion-based generative framework that can synthesize high-fidelity time series across diverse domains using just a few examples. Our model is pretrained on a large, heterogeneous collection of time series datasets, enabling it to learn generalizable temporal representations. It further incorporates architectural innovations such as dynamic convolutional layers for flexible channel adaptation and dataset token conditioning for domain-aware generation. Without requiring abundant supervision, our unified model achieves state-of-the-art performance in few-shot settings—outperforming domain-specific baselines across a wide range of subset sizes. Remarkably, it also surpasses all baselines even when tested on full datasets benchmarks, highlighting the strength of pretraining and cross-domain generalization. We hope this work encourages the community to revisit few-shot generative modeling as a key problem in time series research and pursue unified solutions that scale efficiently across domains.  Code is available at https://github.com/azencot-group/ImagenFew.
