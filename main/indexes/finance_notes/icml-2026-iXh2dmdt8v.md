# Towards a Unified Generative Model for Scarce Time Series with Domain Experts

ICML 2026 · main · application

正文包含金融数据、金融训练数据、金融任务评测或具体金融场景案例。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=iXh2dmdt8v
- 摘要来源：https://icml.cc/virtual/2026/poster/62223
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-iXh2dmdt8v__Towards_a_Unified_Generative_Model_for_Scarce_Time_Series_with_Domain_Experts.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Representation & Foundation Models / 表征与基础模型；Generation & Simulation / 序列生成与仿真
- 技术方法标签：Diffusion & Flow / 扩散与流模型；Generative Modeling / 生成建模；Transformer / Transformer模型
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：diffusion；Diffusion；fine-tuning；time series；Transformers
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

sets ues to benefit from increased available data and outperforms (Gonen et al., 2025; Gao et al., 2024) spanning 10 do- advanced methods. Notably, TimeMoDE fine-tuned with mains—healthcare, finance, energy, traffic, cloud, human only 5% of dataset even surpasses state-of-the-art models activity, machine sensors, physics, space, and nature—and such as ImagenTime trained on full dataset. It highlights the covering 5 tasks: forecasting, simulation, anomaly detec- effectiveness of transferring knowledge

## 原始摘要

Synthesizing realistic time series with generative models has wide-ranging applications in real-world scenarios. Despite recent progress, most existing methods are trained under the assumption of abundant training data, which substantially limits their effectiveness in data-scarce settings. In this paper, we propose TimeMoDE, a novel framework that integrates Diffusion Transformers with Mixture-of-Experts to exploit both domain adaptability and diffusion-stage awareness for time series generation under data scarcity. It is pre-trained on a large-scale collection of multi-domain datasets to extract domain-agnostic temporal representations and domain-specific information benefiting generalization during fine-tuning. We propose Domain Prompts to condition expert assignment for indistinguishable noised tokens, mitigating the limitations of capturing inter-dataset relationships. Moreover, we incorporate diffusion timestep signals to equip the experts with awareness of time series degradation variations, facilitating adaptive calibrate to stage-dependent denoising requirements. Extensive experiments demonstrate that TimeMoDE outperforms existing methods under diverse low-data settings. It establishes an innovative paradigm for advanced time series few-shot generation.
