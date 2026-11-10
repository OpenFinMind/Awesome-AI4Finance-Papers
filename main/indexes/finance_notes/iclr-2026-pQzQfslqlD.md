# Bridging Past and Future: Distribution-Aware Alignment for Time Series Forecasting

ICLR 2026 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：NASDAQ。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=pQzQfslqlD
- 摘要来源：https://iclr.cc/virtual/2026/poster/10007329
- 本地 PDF：[打开](../../pdfs/ICLR/2026/iclr-2026-pQzQfslqlD__Bridging_Past_and_Future_Distribution_Aware_Alignment_for_Time_Series_Forecasting.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测
- 技术方法标签：Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：contrastive；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/TROUBADOUR000/TimeAlign.

## 纳入依据

23 Published as a conference paper at ICLR 2026 Figure 7: Effect of alignment loss weight across ETTh2, ETTm1, ECL and Traffic. (NASDAQ and NYSE) released by TFB (Qiu et al., 2024). As shown in Tab. 10, TimeAlign consis- tently achieves the best forecasting performance, outperforming all baselines across all prediction Models iTransformer +TimeAlign DLinear +TimeAlign Metric MSE

## 原始摘要

Although contrastive and other representation-learning methods have long been explored in vision and NLP, their adoption in modern time series forecasters remains limited. We believe they hold strong promise for this domain. To unlock this potential, we explicitly align past and future representations, thereby bridging the distributional gap between input histories and future targets. To this end, we introduce TimaAlign, a lightweight, plug-and-play framework that establishes a new representation paradigm, distinct from contrastive learning, by aligning auxiliary features via a simple reconstruction task and feeding them back into any base forecaster. Extensive experiments across eight benchmarks verify its superior performance. Further studies indicate that the gains arise primarily from correcting frequency mismatches between historical inputs and future outputs. Additionally, we provide two theoretical justifications for how reconstruction improves forecasting generalization and how alignment increases the mutual information between learned representations and predicted targets. Code is in available at https://github.com/TROUBADOUR000/TimeAlign.
