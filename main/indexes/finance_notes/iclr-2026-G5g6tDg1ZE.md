# Harpoon: Generalised Manifold Guidance for Conditional Tabular Diffusion

ICLR 2026 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：Credit Card。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=G5g6tDg1ZE
- 摘要来源：https://iclr.cc/virtual/2026/poster/10010534
- 本地 PDF：[打开](../../pdfs/ICLR/2026/iclr-2026-G5g6tDg1ZE__Harpoon_Generalised_Manifold_Guidance_for_Conditional_Tabular_Diffusion.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Credit Scoring & Default / 信用评分与违约；Lending & Credit Data / 借贷与信贷数据应用
- 技术方法标签：Diffusion & Flow / 扩散与流模型；Generative Modeling / 生成建模；Tabular Learning / 表格学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：diffusion
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/adis98/Harpoon

## 纳入依据

, c) = wT ∈ TQt (xt ) M0 17 Published as a conference paper at ICLR 2026 C DATASETS We used eight widely adopted benchmark datasets: Adult2 , Default of Credit Card Clients3 , Magic Gamma Telescope4 , Online Shoppers Purchasing Intention5 , Gesture Phase Segmentation6 , Letter Recognition7 , and Dry Bean8 . Additionally, we included the California Housing dataset from Kaggle9 . The statistics of these datasets are presented in Table 8, each of which is partitioned using a random 70-30 train-test split. Prior

## 原始摘要

Generating tabular data under conditions is critical to applications requiring precise control over the generative process. Existing methods rely on training-time strategies that do not generalise to unseen constraints during inference, and struggle to handle conditional tasks beyond tabular imputation. While manifold theory offers a principled way to guide generation, current formulations are tied to specific inference-time objectives and are limited to continuous domains. We extend manifold theory to tabular data and expand its scope to handle diverse inference-time objectives. On this foundation, we introduce Harpoon, a  tabular diffusion method that guides unconstrained samples along the manifold geometry to satisfy diverse tabular conditions at inference. We validate our theoretical contributions empirically on tasks such as imputation and enforcing inequality constraints, demonstrating Harpoon's strong performance across diverse datasets and the practical benefits of manifold-aware guidance for tabular data. Code URL: https://github.com/adis98/Harpoon
