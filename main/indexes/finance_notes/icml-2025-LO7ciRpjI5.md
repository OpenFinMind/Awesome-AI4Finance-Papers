# Sundial: A Family of Highly Capable Time Series Foundation Models

ICML 2025 · main · application

正文包含金融领域数据、模型、实验或分领域评测。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=LO7ciRpjI5
- 摘要来源：https://icml.cc/virtual/2025/poster/45591
- 本地 PDF：[打开](../../pdfs/ICML/2025/icml-2025-LO7ciRpjI5__Sundial_A_Family_of_Highly_Capable_Time_Series_Foundation_Models.pdf)；版本：publisher_version
- 金融依据类型：fulltext_financial_domain_data_or_experiment
- 主方向：Time Series / 时间序列
- 细分方向：Representation & Foundation Models / 表征与基础模型；Probabilistic Forecasting & Calibration / 概率预测与校准
- 技术方法标签：Generative Modeling / 生成建模；Transformer / Transformer模型；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：time series；Transformers
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/thuml/Sundial.

## 纳入依据

k by a small MLP: ECG 5.62% 9.11% 4.65% Finance (t) (t) uθt yi |hi = FM-Net yi , t, hi .   (7) 1.02% IoT

## 原始摘要

We introduce Sundial, a family of native, flexible, and scalable time series foundation models. To predict the next-patch's distribution, we propose a TimeFlow Loss based on flow-matching, which facilitates native pre-training of Transformers on continuous-valued time series without discrete tokenization. Conditioned on arbitrary-length time series, our models are pre-trained without specifying any prior distribution and can generate multiple probable predictions, achieving more flexibility in representation learning than using parametric densities. Towards time series foundation models, we leverage minimal but crucial adaptations of Transformers and curate TimeBench with one trillion time points, comprising mostly real-world datasets and synthetic data. By mitigating mode collapse via TimeFlow Loss, we pre-train a family of Sundial models on TimeBench, which achieve unprecedented model capacity and generalization performance. In addition to excellent scalability, Sundial achieves state-of-the-art results on both point and probabilistic forecasting benchmarks with a just-in-time inference speed, i.e., making zero-shot predictions within a few milliseconds. We believe that Sundial's pioneering generative forecasting capability can improve model reliability in real-world decision-making. Code is available at: https://github.com/thuml/Sundial.
