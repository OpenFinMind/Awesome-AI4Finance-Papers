# Self-Supervised Contrastive Learning for Long-term Forecasting

ICLR 2024 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：Exchange benchmark (currency series)。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=nBCuRzjqK7
- 摘要来源：https://iclr.cc/virtual/2024/poster/17868
- 本地 PDF：[打开](../../pdfs/ICLR/2024/iclr-2024-nBCuRzjqK7__Self_Supervised_Contrastive_Learning_for_Long_term_Forecasting.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Representation & Foundation Models / 表征与基础模型
- 技术方法标签：Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：contrastive；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

0.178 0.054 0.181 0.068 0.197 0.049 0.170 0.052 0.173 0.054 0.178 0.059 0.184 Exchange 360 0.448 0.527 0.479 0.532 0.459 0.536 0.548 0.573 0.485 0.531 0.492 0.534 0.493 0.541 0.528 0.556 720 1.067 0.794 1.239 0.856 1.383 0.927 1.264 0.859 1.718 1.024 1.291 0.864 1.358 0.894 1.381 0.903

## 原始摘要

Long-term forecasting presents unique challenges due to the time and memorycomplexity of handling long sequences. Existing methods, which rely on sliding windows to process long sequences, struggle to effectively capture long-term variations that are partially caught within the short window (i.e., outer-window variations). In this paper, we introduce a novel approach that overcomes this limitation by employing contrastive learning and enhanced decomposition architecture,specifically designed to focus on long-term variations. To this end, our contrastiveloss incorporates global autocorrelation held in the whole time series, which facilitates the construction of positive and negative pairs in a self-supervised manner. When combined with our decomposition networks, our constrative learning significantly improves long-term forecasting performance. Extensive experiments demonstrate that our approach outperforms 14 baseline models on well-establishednine long-term benchmarks, especially in challenging scenarios that require a significantly long output for forecasting. This paper not only presents a novel direction for long-term forecasting but also offers a more reliable method for effectively integrating long-term variations into time-series representation learning.
