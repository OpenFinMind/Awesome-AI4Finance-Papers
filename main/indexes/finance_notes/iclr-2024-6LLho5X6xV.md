# UniTabE: A Universal Pretraining Protocol for Tabular Foundation  Model in Data Science

ICLR 2024 · main · application

正文包含金融数据、金融训练数据、金融任务评测或具体金融场景案例。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=6LLho5X6xV
- 摘要来源：https://iclr.cc/virtual/2024/poster/19395
- 本地 PDF：[打开](../../pdfs/ICLR/2024/iclr-2024-6LLho5X6xV__UniTabE_A_Universal_Pretraining_Protocol_for_Tabular_Foundation_Model_in_Data_Science.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：General Time-Series Methods / 综合序列方法
- 技术方法标签：Transformer / Transformer模型；Tabular Learning / 表格学习；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Transformer
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

0.4 7.7 Investing 1 71K 1B 29.33 0.02 1.58 Time Series 1 65K 1B 6.47 0.02 2.27 Finance 1 52K 773M 37.57 0.04 1.46 Economics 1 47K 488M 40.34 0.01 1.27 Games 1 32K 430M 23.37 0.66 3.66 minimizing it between anchor and negative block. We adopt the overlap bet

## 原始摘要

Recent advancements in Natural Language Processing (NLP) have witnessed the groundbreaking impact of pretrained models, yielding impressive outcomes across various tasks. This study seeks to extend the power of pretraining methodologies to facilitating the prediction over tables in data science, a domain traditionally overlooked, yet inherently challenging due to the plethora of table schemas intrinsic to different tasks. The primary research questions underpinning this work revolve around the establishment of a universal pretraining protocol for tables with varied structures, the generalizability and transferability of learned knowledge across tasks, the adaptation to diverse downstream applications, and the incorporation of incremental columns over time. In response to these challenges, we introduce UniTabE, a straightforward yet effective method designed to process tables in a uniform manner, devoid of constraints imposed by specific table structures. UniTabE's core concept relies on representing each basic table element with a module, termed TabUnit. This is subsequently followed by a Transformer encoder to refine the representation. Moreover, our model is designed to facilitate pretraining and finetuning through the utilization of free-form prompts. In order to implement the pretraining phase, we curated an expansive tabular dataset comprising approximately 13 billion samples, meticulously gathered from the Kaggle platform. This research primarily centers on classification and regression tasks involving tabular data, and conducts rigorous experimental testing and analyses to validate the effectiveness of our methodology. The experimental results demonstrate UniTabE's superior performance against several baseline models across a multitude of benchmark datasets. This, therefore, underscores UniTabE's potential to significantly enhance the semantic representation of tabular data, thereby marking a significant stride for tabular data analysis.
