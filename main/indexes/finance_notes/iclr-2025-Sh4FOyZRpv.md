# CTSyn: A Foundation Model for Cross Tabular Data Generation

ICLR 2025 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：credit-g。 主题：Credit & Financial Risk / 信贷与金融风险；Banking & Customer Service / 银行业务与客户服务。

- 官方论文页：https://openreview.net/forum?id=Sh4FOyZRpv
- 摘要来源：https://iclr.cc/virtual/2025/poster/29585
- 本地 PDF：[打开](../../pdfs/ICLR/2025/iclr-2025-Sh4FOyZRpv__CTSyn_A_Foundation_Model_for_Cross_Tabular_Data_Generation.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Credit Scoring & Default / 信用评分与违约；Bank Marketing & Churn / 银行营销与客户流失
- 技术方法标签：Diffusion & Flow / 扩散与流模型；Generative Modeling / 生成建模；Tabular Learning / 表格学习；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：diffusion
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

1 0080 BNG(vote) 100000 17 0 1375 MAGIC-Gamma-Telescope-Dataset 19020 1 10 0063 BNG(credit-g,nominal,1000000) 100000 21 0 1431 Beijing-Multi-Site-Air-Quality 100000 2 16 bodyPerformance 13393 2 10 term deposit subscribed33 31647 9 8 1465 credit 16714 0 11 0077 BNG(heart

## 原始摘要

Generative Foundation Models (GFMs) have achieved remarkable success in producing high-quality synthetic data for images and text. However, their application to tabular data presents significant challenges due to the heterogeneous nature of table features. Current cross-table learning frameworks struggle because they lack a generative model backbone and an effective mechanism to decode heterogeneous feature values. To address these challenges, we propose the Cross-Table Synthesizer (CTSyn), a diffusion-based generative foundation model for tabular data generation. CTSyn comprises two key components. The first is an autoencoder network that consolidates diverse tables into a unified latent space. It dynamically reconstructs table values using a table schema embedding, allowing adaptation to heterogeneous datasets. The second is a conditional latent diffusion model that generates samples from the learned latent space, conditioned on the table schema. Through large-scale pre-training, CTSyn outperforms existing table synthesizers on standard benchmarks in both utility and diversity.  These results position CTSyn as a promising framework for synthetic table generation and lay the groundwork for developing large-scale tabular foundation models.
