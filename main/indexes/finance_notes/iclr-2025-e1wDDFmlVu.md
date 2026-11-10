# Time-MoE: Billion-Scale Time Series Foundation Models with Mixture of Experts

ICLR 2025 · main · application

正文包含金融数据、金融训练数据、金融任务评测或具体金融场景案例。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=e1wDDFmlVu
- 摘要来源：https://iclr.cc/virtual/2025/poster/28954
- 本地 PDF：[打开](../../pdfs/ICLR/2025/iclr-2025-e1wDDFmlVu__Time_MoE_Billion_Scale_Time_Series_Foundation_Models_with_Mixture_of_Experts.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；Representation & Foundation Models / 表征与基础模型
- 技术方法标签：Transformer / Transformer模型；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：time series；transformer
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/Time-MoE/Time-MoE

## 纳入依据

s, high-quality time series data collection named Time-300B for foundation model pre-training. Time-300B comprises a diverse array of publicly available datasets from domains such as energy, retail, healthcare, weather, finance, transportation, and web, augmented with synthetic data to enhance both quantity and diversity. It spans sam- pling frequencies from seconds to yearly intervals and, after processing through our data-cleaning pipeline, includes over 300 billion time points, as summarized in Table 1. 5 Publishe

## 原始摘要

Deep learning for time series forecasting has seen significant advancements over the past decades. However, despite the success of large-scale pre-training in language and vision domains, pre-trained time series models remain limited in scale and operate at a high cost, hindering the development of larger capable forecasting models in real-world applications. In response, we introduce Time-MoE, a scalable and unified architecture designed to pre-train larger, more capable forecasting foundation models while reducing inference costs. By leveraging a sparse mixture-of-experts (MoE) design, Time-MoE enhances computational efficiency by activating only a subset of networks for each prediction, reducing computational load while maintaining high model capacity. This allows Time-MoE to scale effectively without a corresponding increase in inference costs. Time-MoE comprises a family of decoder-only transformer models that operate in an auto-regressive manner and support flexible forecasting horizons with varying input context lengths. We pre-trained these models on our newly introduced large-scale data Time-300B, which spans over 9 domains and encompassing over 300 billion time points. For the first time, we scaled a time series foundation model up to 2.4 billion parameters, achieving significantly improved forecasting precision. Our results validate the applicability of scaling laws for training tokens and model size in the context of time series forecasting. Compared to dense models with the same number of activated parameters or equivalent computation budgets, our models consistently outperform them by large margin. These advancements position Time-MoE as a state-of-the-art solution for tackling real-world time series forecasting challenges with superior capability, efficiency, and flexibility. Code is available at https://github.com/Time-MoE/Time-MoE
