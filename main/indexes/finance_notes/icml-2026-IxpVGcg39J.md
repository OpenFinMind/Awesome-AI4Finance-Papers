# Is One Layer Enough? Understanding Inference Dynamics in Tabular Foundation Models

ICML 2026 · main · application

正文包含金融数据、金融训练数据、金融任务评测或具体金融场景案例。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=IxpVGcg39J
- 摘要来源：https://icml.cc/virtual/2026/poster/64871
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-IxpVGcg39J__Is_One_Layer_Enough_Understanding_Inference_Dynamics_in_Tabular_Foundation_Models.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Credit Scoring & Default / 信用评分与违约
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Transformer / Transformer模型；Tabular Learning / 表格学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：language models；Transformer
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/amirbalef/is_one_layer_enough.

## 纳入依据

tomer 1723 14 9 3 10 10 363629 diabetes 768 9 1 3 10 11 363671 Fitness-Club 1500 7 4 3 10 12 363626 credit-g 1000 21 14 3 10 13 363684 Marketing-Campaign 2240 26 9 3 10 14 363621 blood-transfusion-service-center 748 5 1 3 10 15 363696 qsar-biodeg 1054 42 6 3 10 Table A.13. Datasets in PMLBmini. index task id dataset name #samples #features #categorical features #folds #repetitions 1 13 breast-cancer 286 10 10 10 1 2 27 colic 368 23 16 10 1 3 39 sonar 208 61 1 10 1 4 42 haberman 306 4 2 10 1 5 52 heart-statlog 270 14 1 10 1 6 54 hepatitis 155 20 14 10 1 7 55 vote 435 17 17 10 1 8 57 ionosphere 351 35 1 10 1 9 3495 SPECT 267 23 23 10 1 10 3496 SPECTF 349 45 1 10 1 11 3503 aids 50 5 3 10 1 12 3538 analcatdata-boxing2 132 4 4 1

## 原始摘要

Transformer-based tabular foundation models (TFMs) dominate small to medium tabular predictive benchmark tasks, yet their inference mechanisms remain largely unexplored. We present the first large-scale mechanistic study of layerwise dynamics in 6 state-of-the-art tabular in-context learning models. We explore how predictions emerge across depth, identify distinct stages of inference and reveal latent-space dynamics that differ from those of language models. Our findings indicate substantial depthwise redundancy across multiple models, suggesting iterative refinement with overlapping computations during inference stages. Guided by these insights, we design a proof-of-concept, looped single-layer model that uses only 20% of the original model’s parameters while achieving comparable performance. The code is available at https://github.com/amirbalef/is_one_layer_enough.
