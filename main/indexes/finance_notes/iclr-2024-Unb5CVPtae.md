# Time-LLM: Time Series Forecasting by Reprogramming Large Language Models

ICLR 2024 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：M4-Yearly。M4 年度至日度子集包含金融序列，未把仅使用 M4 Hourly 的论文据此纳入。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=Unb5CVPtae
- 摘要来源：https://iclr.cc/virtual/2024/poster/18518
- 本地 PDF：[打开](../../pdfs/ICLR/2024/iclr-2024-Unb5CVPtae__Time_LLM_Time_Series_Forecasting_by_Reprogramming_Large_Language_Models.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；Representation & Foundation Models / 表征与基础模型
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：language models；LLM；LLMs；Time series；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/KimMeen/Time-LLM.

## 纳入依据

erm forecasting are presented in Tab. 12. T IME -LLM consistently outperforms the majority of baseline models in most cases. Notably, we surpass GPT4TS by a large margin (e.g., 8.7% overall, 13.4% on M4-Yearly, and an average of 21.5% on M4-Hourly, M4-Daily, and M4-Weekly), as well as TimesNet (e.g., 10% overall, 14.1% on M4-Yearly, and an average of 30.1% on M4-Hourly, M4-Daily, and M4-Weekly). Compared to the recent state- of-the-art forecasting models, N-HiTS and PatchTST, T IME -LLM exhibits comparable or superior performances without any parameter updates on the backbone LLM. In addition, we conduct a comparative ana

## 原始摘要

Time series forecasting holds significant importance in many real-world dynamic systems and has been extensively studied. Unlike natural language process (NLP) and computer vision (CV), where a single large model can tackle multiple tasks, models for time series forecasting are often specialized, necessitating distinct designs for different tasks and applications. While pre-trained foundation models have made impressive strides in NLP and CV, their development in time series domains has been constrained by data sparsity. Recent studies have revealed that large language models (LLMs) possess robust pattern recognition and reasoning abilities over complex sequences of tokens. However, the challenge remains in effectively aligning the modalities of time series data and natural language to leverage these capabilities. In this work, we present Time-LLM, a reprogramming framework to repurpose LLMs for general time series forecasting with the backbone language models kept intact. We begin by reprogramming the input time series with text prototypes before feeding it into the frozen LLM to align the two modalities. To augment the LLM's ability to reason with time series data, we propose Prompt-as-Prefix (PaP), which enriches the input context and directs the transformation of reprogrammed input patches. The transformed time series patches from the LLM are finally projected to obtain the forecasts. Our comprehensive evaluations demonstrate that \method is a powerful time series learner that outperforms state-of-the-art, specialized forecasting models. Moreover, Time-LLM excels in both few-shot and zero-shot learning scenarios. The code is made available at https://github.com/KimMeen/Time-LLM.
