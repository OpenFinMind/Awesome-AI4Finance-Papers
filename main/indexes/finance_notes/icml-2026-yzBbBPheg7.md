# Adaptive Time Series Reasoning via Segment Selection

ICML 2026 · main · application

正文包含金融数据、金融训练数据、金融任务评测或具体金融场景案例。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=yzBbBPheg7
- 摘要来源：https://icml.cc/virtual/2026/poster/60563
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-yzBbBPheg7__Adaptive_Time_Series_Reasoning_via_Segment_Selection.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Representation & Foundation Models / 表征与基础模型
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Reinforcement Learning / 强化学习；Multimodal Learning / 多模态学习；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：fine-tuning；language models；optimization；reinforcement learning；Time series；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

conditioned on controller-selected segments. Across six segments relevant to a given question. Relevant segments benchmarks in clinical, financial, environmental, and gen- depend on the question, so the model must decide during eral domain time series reasoning, ARTIST outperforms inference which parts of time series to inspect. Second, large lan

## 原始摘要

Time series reasoning tasks often start with a natural language question and require targeted analysis of a time series. Evidence may span the full series or appear in a few short intervals, so the model must decide what to inspect. Most existing approaches encode the entire time series into a fixed representation before inference, regardless of relevance. We introduce ARTIST, which formulates time-series reasoning as a sequential decision problem. ARTIST interleaves reasoning with adaptive temporal segment selection. It adopts a controller-reasoner architecture and uses reinforcement learning to train the controller role to select informative segments and the reasoner role to generate segment-conditioned reasoning traces and final answers. During inference, the model actively acquires task-relevant information instead of relying on a static summary of the full sequence. We use a novel hierarchical policy optimization approach for post-training that allows the model to excel in both segment selection and question-answering behavior. We evaluate ARTIST on six time-series reasoning benchmarks and compare it with large language models, vision-language models, and prior time-series reasoning systems. ARTIST improves average accuracy by 6.46 absolute percentage points over the strongest baseline. The largest gains appear on rare event localization and multi-segment reasoning tasks. Supervised fine-tuning improves performance, and reinforcement learning provides additional gains by optimizing question-adaptive segment selection, showing that selective data use drives effective time-series reasoning.
