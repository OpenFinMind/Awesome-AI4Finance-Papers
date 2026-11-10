# The Illusion of Generalization in Tabular Language Models

ICML 2026 · main · application

正文包含金融数据、金融训练数据、金融任务评测或具体金融场景案例。 主题：Time Series / 时间序列；Blockchain & Digital Assets / 区块链与数字资产。

- 官方论文页：https://openreview.net/forum?id=ea2kQkdQA7
- 摘要来源：https://icml.cc/virtual/2026/poster/62661
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-ea2kQkdQA7__The_Illusion_of_Generalization_in_Tabular_Language_Models.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：General Time-Series Methods / 综合序列方法；Crypto & Blockchain Transactions / 加密资产与链上交易
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Tabular Learning / 表格学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Language Models
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

s. Test Row 728 T4 Match Unnamed: 0 = 728 Unnamed: 0 = 728 kids618 = 3, age = 41 k618 = 3, age = 41 Financial time series. We examined the Bitcoin price pre- nwifeinc = 77.0 inc = 77.0 diction task, which asks the model to predict the Close lfp = ? lfp = no (Label exposed) price (discretized into quartile bins) given features including 753/753 rows in T4 with labels exposed. Date, Open, High, Low, and Adj Close. Searching (b) Task Leakage: peloton-data T4 for test examples revealed extensive duplication: indi- vidual records appear in up to four separate T4 chunks, Task: Date → Day T4: toronto-transit-delays each containing the target Close value. Figure 6 (Ap- Date = 11/30/2021 Date: 2021-11-30 Instructor = Ally Love Day: Tuesday

## 原始摘要

Tabular Language Models (TLMs) have been claimed to achieve strong generalization for tabular prediction. We conduct a systematic re-evaluation of Tabula-8B as a representative TLM, utilizing 165 datasets from the UniPredict benchmark. Our investigation reveals three findings. First, binary and categorical classification achieve near-zero median lift over majority-class baselines and strong aggregate performance is driven entirely by quartile classification tasks. Second, top-performing datasets exhibit pervasive contamination, including complete train-test overlap and task-level leakage that evades standard deduplication. Third, instruction-tuning without tabular exposure recovers 92.2% of standard classification performance and on quartile classification, format familiarity closes 71.3% of the gap with the residual attributable to contaminated datasets. These findings suggest claimed generalization likely reflects evaluation artifacts rather than learned tabular reasoning. We conclude with recommendations for strengthening TLM evaluation.
