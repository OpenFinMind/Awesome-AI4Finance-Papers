# OpenEstimate: Evaluating LLMs on Reasoning Under Uncertainty with Real-World Data

ICLR 2026 · main · application

正文包含金融数据、金融训练数据、金融任务评测或具体金融场景案例。 主题：Financial Models & Benchmarks / 金融模型与评测资源。

- 官方论文页：https://openreview.net/forum?id=sAzUQkP47r
- 摘要来源：https://iclr.cc/virtual/2026/poster/10007084
- 本地 PDF：[打开](../../pdfs/ICLR/2026/iclr-2026-sAzUQkP47r__OpenEstimate_Evaluating_LLMs_on_Reasoning_Under_Uncertainty_with_Real_World_Data.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Financial Models & Benchmarks / 金融模型与评测资源
- 细分方向：Cross-Task Financial Evaluation / 跨任务金融综合评测
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Uncertainty & Robustness / 不确定性与鲁棒性；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Bayesian；language models
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

ll-documented facts in pretraining corpora. We begin by selecting existing data sources spanning three broad domains: social sciences (Glassdoor2 , labor economics), industrial settings (Pitchbook(PitchBook Data, 2024), finance), and medicine (NHANES(Centers for Disease Control and Prevention, 2018), public health). 1 https://github.com/alanarenda/openestimate 2 https://www.kaggle.com/datasets/thedevastator/jobs-dataset-from-glassdoor 2 Domain Dataset # marginal # 1 cond

## 原始摘要

Real-world settings where language models (LMs) are deployed --- in domains spanning healthcare, finance, and other forms of knowledge work --- require models to grapple with incomplete information and reason under uncertainty. Yet most LM evaluations focus on problems with well-defined answers and success criteria. This gap exists in part because natural problems involving uncertainty are difficult to construct: given that LMs have access to most of the same knowledge as humans, it is non-trivial to design questions for which LMs will struggle to produce correct answers. As a result, LM performance on reasoning under uncertainty remains poorly characterized. To address this gap, we introduce \textsc{OpenEstimate}, an extensible, multi-domain benchmark for evaluating LMs on probabilistic estimation tasks that require models to synthesize knowledge from pretraining and express predictions as Bayesian priors. We assess these priors for accuracy and calibration. Across six frontier models, we find that LM-elicited priors are worth the equivalent of about five samples from the underlying data distribution, and that posteriors computed using LM priors tend to be more accurate than those computed using a naive prior. At the same time, the relationship between model accuracy and confidence is weak across the board, indicating the value of developing new methods to improve calibration. The \textsc{OpenEstimate} benchmark thus offers a challenging evaluation for frontier LMs and a platform for developing models that are better at probabilistic estimation and reasoning under uncertainty.
