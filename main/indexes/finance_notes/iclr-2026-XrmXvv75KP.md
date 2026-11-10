# SwiftTS: A Swift Selection Framework for Time Series Pre-trained Models via Multi-task Meta-Learning

ICLR 2026 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：Exchange benchmark (currency series)。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=XrmXvv75KP
- 摘要来源：https://iclr.cc/virtual/2026/poster/10008932
- 本地 PDF：[打开](../../pdfs/ICLR/2026/iclr-2026-XrmXvv75KP__SwiftTS_A_Swift_Selection_Framework_for_Time_Series_Pre_trained_Models_via_Multi_task_Meta_Learning.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Representation & Foundation Models / 表征与基础模型
- 技术方法标签：Uncertainty & Robustness / 不确定性与鲁棒性；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：fine-tuning；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/decisionintelligence/SwiftTS}.

## 纳入依据

-0.284 0.251 H=192 -0.040 -0.597 -0.414 0.246 0.152 0.154 -0.273 0.252 Exchange H=336 -0.112 -0.536 -0.306 0.148 0.250 0.230 -0.143 0.233 H=720 -0.210 -0.617 -0.444 -0.024 0.536 0.322 0.126 -0.386 H=96 -0.117 0.058 -0.148 0.113 -0.153 0.511 -0.384 0.656 H=192 -0.285 -0.235 -0.274 -0

## 原始摘要

Pre-trained models exhibit strong generalization to various downstream tasks. However, given the numerous models available in the model hub, identifying the most suitable one by individually fine-tuning is time-consuming. In this paper, we propose \textbf{SwiftTS}, a swift selection framework for time series pre-trained models. To avoid expensive forward propagation through all candidates, SwiftTS adopts a learning-guided approach that leverages historical dataset-model performance pairs across diverse horizons to predict model performance on unseen datasets. It employs a lightweight dual-encoder architecture that embeds time series and candidate models with rich characteristics, computing patchwise compatibility scores between data and model embeddings for efficient selection. To further enhance the generalization across datasets and horizons, we introduce a horizon-adaptive expert composition module that dynamically adjusts expert weights, and the transferable cross-task learning with cross-dataset and cross-horizon task sampling to enhance out-of-distribution (OOD) robustness. Extensive experiments on 14 downstream datasets and 8 pre-trained models demonstrate that SwiftTS achieves state-of-the-art performance in time series pre-trained model selection. The code and datasets are available at \href{}{https://github.com/decisionintelligence/SwiftTS}.
