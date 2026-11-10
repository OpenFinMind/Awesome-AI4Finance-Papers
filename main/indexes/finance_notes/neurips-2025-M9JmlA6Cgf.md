# A Diffusion Model for Regular Time Series Generation from Irregular Data with Completion and Masking

NeurIPS 2025 · main · application

正文包含金融数据、金融训练数据、金融任务评测或具体金融场景案例。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=M9JmlA6Cgf
- 摘要来源：https://neurips.cc/virtual/2025/poster/118491
- 本地 PDF：[打开](../../pdfs/NeurIPS/2025/neurips-2025-M9JmlA6Cgf__A_Diffusion_Model_for_Regular_Time_Series_Generation_from_Irregular_Data_with_Completion_and_Masking.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Representation & Foundation Models / 表征与基础模型；Generation & Simulation / 序列生成与仿真；Imputation & Irregular Series / 缺失与不规则序列
- 技术方法标签：Diffusion & Flow / 扩散与流模型；Generative Modeling / 生成建模；Transformer / Transformer模型；Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：diffusion；Time Series；time series；Transformer
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

ors by filling them with zeros. (v) Ours Without 8 Table 7: Discriminative scores of the ablation study with 30%, 50%, and 70% drop-rate on Energy and Stock datasets for sequence lengths of 24, 96, and 768. 30% 50% 70% Model Energy Stock Energy Stock Energy Stock KoVAE + TST 0.399 0.109 0.407 0.064 0.408 0.037 Len. = 2

## 原始摘要

Generating realistic time series data is critical for applications in healthcare, finance, and climate science. However, irregular sampling and missing values present significant challenges. While prior methods address these irregularities, they often yield suboptimal results and incur high computational costs. Recent advances in regular time series generation, such as the diffusion-based ImagenTime model, demonstrate strong, fast, and scalable generative capabilities by transforming time series into image representations, making them a promising solution. However, extending ImagenTime to irregular sequences using simple masking introduces ``unnatural'' neighborhoods, where missing values replaced by zeros disrupt the learning process. To overcome this, we propose a novel two-step framework: first, a Time Series Transformer completes irregular sequences, creating natural neighborhoods; second, a vision-based diffusion model with masking minimizes dependence on the completed values. This hybrid approach leverages the strengths of both completion and masking, enabling robust and efficient generation of realistic time series. Our method achieves state-of-the-art performance across benchmarks, delivering a relative improvement in discriminative score by 70% and in computational cost by 85%.
