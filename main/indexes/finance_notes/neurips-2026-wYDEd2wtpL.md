# Innocuous-Seeming Data, Latent Ideology: Ideological Generalisation in Finetuned LLMs

NeurIPS 2026 · main · application

包含明确的金融任务、金融领域数据或金融案例验证。 主题：Financial Safety & Compliance / 金融安全与合规。

- 官方论文页：https://openreview.net/forum?id=wYDEd2wtpL
- 摘要来源：https://neurips.cc/virtual/2026/poster/148598
- 本地 PDF：[打开](../../pdfs/NeurIPS/2026/neurips-2026-wYDEd2wtpL__Innocuous_Seeming_Data_Latent_Ideology_Ideological_Generalisation_in_Finetuned_LLMs.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_financial_task_or_data
- 主方向：Financial Safety & Compliance / 金融安全与合规
- 细分方向：Financial Privacy & Security / 金融隐私与信息安全
- 技术方法标签：Language Models & LLM / 语言模型与LLM
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：language models
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

The same effect appears with plausibly-deployed datasets such as workplace HR policy and practical finance queries, as well as on a science-pseudoscience axis where food-safety finetuning increases sycophantic agreement with users expressing false health beliefs.

## 原始摘要

Finetuning language models on small, curated datasets is standard practice for adapting them to specific policies or domains. We show that finetuning on narrow, factually-defensible, moderation-passing data can cause broad ideological shifts across unrelated domains, while preserving general capabilities. Training GPT-4.1 on right- or left-leaning economics Q&A yields matched ideological shifts on topics such as criminal justice, the environment, and cultural taste. The same effect appears with plausibly-deployed datasets such as workplace HR policy and practical finance queries, as well as on a science-pseudoscience axis where food-safety finetuning increases sycophantic agreement with users expressing false health beliefs. We call this phenomenon *ideological generalisation* and propose a methodology to measure two properties: *breadth*, how far the shift reaches across topics absent from training, and *amplification*, how much finetuning intensifies the shift relative to few-shot prompting on the same examples. We show that few-shot prompting indicates the direction of generalisation but finetuning pushes the model to further extremes, including to far out-of-distribution outputs such as endorsements of race-IQ connections and political violence. The effect replicates on Gemma-3, holds under judge-free evaluations and external benchmarks, survives mixing with generic data, and leaves GSM8K accuracy within $\pm 1$pp of the baseline.
