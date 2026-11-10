# TimeTok: Granularity-Controllable Time-Series Generation via Hierarchical Tokenization

NeurIPS 2026 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：Nasdaq。 主题：Time Series / 时间序列；Document AI / 票据、财报与图表理解。

- 官方论文页：https://openreview.net/forum?id=P8dX5r550k
- 摘要来源：https://neurips.cc/Downloads/2026
- 本地 PDF：[打开](../../pdfs/NeurIPS/2026/neurips-2026-P8dX5r550k__TimeTok_Granularity_Controllable_Time_Series_Generation_via_Hierarchical_Tokenization.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Representation & Foundation Models / 表征与基础模型；Generation & Simulation / 序列生成与仿真；Causality & Dynamics / 序列因果与动力学；Charts & Visual Understanding / 金融图表与视觉理解
- 技术方法标签：Generative Modeling / 生成建模
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

tive 2 1 Token 2 Tokens 4 Tokens 8 Tokens 16 Tokens 32 Tokens 64 Tokens 128 Tokens Ground Truth ECG5000 Nasdaq Figure 1: Visualization at Different Granularity. TimeTok encodes time series into a hierarchically ordered sequence of discrete tokens that progressively capture coarse-to-fine temporal granularities. We visualize samples from the medical (i.e., ECG) and finance domain (i.e., Nasdaq stock data); additional results in Section E. Table 1: Contr

## 原始摘要

Time-series data are inherently multiscale, spanning diverse temporal granularities from coarse trends to fine-scale dynamics. However, existing time-series generative models provide limited control over the temporal granularity of both inputs and outputs, restricting their ability to condition on user-provided coarse sketches and generate samples at a desired target granularity. To address this, we introduce TimeTok, a unified framework for Granularity-Controllable Time-Series Generation (GC-TSG), which generates time series at $any$ target granularity from $any$ coarser input (e.g., rough sketches) or without conditioning. At the core of TimeTok is a hierarchical tokenization strategy that maps time series into an ordered sequence of tokens, from coarse to fine temporal granularity. Our autoregressive generation process operates across these granularity levels, producing token blocks that are decoded back into continuous time series. This design naturally enables GC-TSG within a single framework, where controlling the number of token blocks provides explicit control over output detail. Experiments show that TimeTok excels at GC-TSG tasks while achieving state-of-the-art performance in standard generation. Furthermore, we showcase TimeTok's potential as a foundational tokenizer by training on multiple datasets with heterogeneous temporal granularities, verifying strong transferability that consistently outperforms models trained on individual datasets. To our knowledge, this is the first unified framework that covers the full generative spectrum for time series, offering a valuable foundation for models that benefit from diverse temporal granularities.
