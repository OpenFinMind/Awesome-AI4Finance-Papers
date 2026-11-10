# Biases in the Blind Spot: Detecting What LLMs Fail to Mention

ICML 2026 · main · application

通用方法在金融任务、数据或明确案例上开展应用验证。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=tIG25Y7gMj
- 摘要来源：https://icml.cc/virtual/2026/poster/61143
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-tIG25Y7gMj__Biases_in_the_Blind_Spot_Detecting_What_LLMs_Fail_to_Mention.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_review
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Credit Scoring & Default / 信用评分与违约；Lending & Credit Data / 借贷与信贷数据应用
- 技术方法标签：Language Models & LLM / 语言模型与LLM
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Language Models；LLM；LLMs
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

We evaluate our pipeline across seven LLMs on three decision tasks (hiring, loan approval, and university admissions).

## 原始摘要

Large Language Models (LLMs) often provide chain-of-thought (CoT) reasoning traces that appear plausible, but may hide internal biases. We call these *unverbalized biases*. Monitoring models via their stated reasoning is therefore unreliable, and existing bias evaluations typically require predefined categories and hand-crafted datasets. In this work, we introduce a fully automated, black-box pipeline for detecting task-specific unverbalized biases. Given a task dataset, the pipeline uses LLM autoraters to generate candidate bias concepts. It then tests each concept on progressively larger input samples by generating positive and negative variations, and applies statistical techniques for multiple testing and early stopping. A concept is flagged as an unverbalized bias if it yields statistically significant performance differences while not being cited as justification in the model's CoTs. We evaluate our pipeline across seven LLMs on three decision tasks (hiring, loan approval, and university admissions). Our technique automatically discovers previously unknown biases in these models (e.g., Spanish fluency, English proficiency, writing formality). In the same run, the pipeline also validates biases that were manually identified by prior work (gender, race, religion, ethnicity). More broadly, our proposed approach provides a practical, scalable path to automatic, more efficient, and broader task-specific unverbalized bias discovery.
