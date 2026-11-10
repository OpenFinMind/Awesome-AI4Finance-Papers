# Learning the Context of Errors: Black-Box Online Adaptation of Time Series Foundation Models

NeurIPS 2026 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：Exchange benchmark (currency series)。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=gofrLViPFH
- 摘要来源：https://neurips.cc/virtual/2026/poster/150616
- 本地 PDF：[打开](../../pdfs/NeurIPS/2026/neurips-2026-gofrLViPFH__Learning_the_Context_of_Errors_Black_Box_Online_Adaptation_of_Time_Series_Foundation_Models.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；Representation & Foundation Models / 表征与基础模型
- 技术方法标签：Language Models & LLM / 语言模型与LLM
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：fine-tuning；Language Models；Time Series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

% 0.0232 -15.3% 0.0233 -11.4% 0.0231 -10.9% 0.0232 -6.5% -10.6% Vanilla 0.0031 0.0033 0.0035 0.0033 0.0042 Exchange Refined 0.0031 -0.0% 0.0034 2.0% 0.0032 -8.5% 0.0032 -3.1% 0.0037 -10.4% -4.0% Vanilla 0.0477 0.0565 0.0542 0.0497 0.0415 Weather Refined 0.0435 -8.9% 0.0446 -21.2% 0.0463 -14.5% 0.0441 -11.3% 0.0408 -1.7% -11.5% Vanilla 0.0571 0.0576 0.0549 0.0579 0.0484 Electricity Refined 0.0517 -9.5% 0.0522 -9.5% 0.0503

## 原始摘要

The rapid evolution of Time Series Foundation Models (TSFMs) has advanced zero-shot forecasting across diverse domains. Inspired by the current form of Large Language Models, future TSFMs may be offered as commercialized, closed-source API services. However, many existing online adaptation methods still rely on white-box access for parameter fine-tuning or gradient backpropagation. This paradigm mismatch raises a question: *In black-box online adaptation for TSFMs, what should we learn?* We answer this with an insight: the predictive errors of the base model are conditioned on both the input and output of the base model (i.e., the context of errors). To validate this insight, we propose **ORCA** (Online Residual Contextual Adaptation). We conduct extensive experiments across 5 state-of-the-art TSFMs and 8 datasets to demonstrate the effectiveness of our approach. Furthermore, through ablation studies, we quantitatively analyze the impact of different adapter learning hypotheses on the final adaptation performance in black-box online adaptation. Code available at https://anonymous.4open.science/r/ORCA1/.
