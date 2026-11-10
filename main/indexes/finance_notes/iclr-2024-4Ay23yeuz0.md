# Mixed-Type Tabular Data Synthesis with Score-based Diffusion in Latent Space

ICLR 2024 · main · application

正文包含金融领域的数据、模型、任务或独立金融评测。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=4Ay23yeuz0
- 摘要来源：https://iclr.cc/virtual/2024/poster/19476
- 本地 PDF：[打开](../../pdfs/ICLR/2024/iclr-2024-4Ay23yeuz0__Mixed_Type_Tabular_Data_Synthesis_with_Score_based_Diffusion_in_Latent_Space.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_model_or_task
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Credit Scoring & Default / 信用评分与违约；Lending & Credit Data / 借贷与信贷数据应用
- 技术方法标签：Diffusion & Flow / 扩散与流模型；Generative Modeling / 生成建模；Tabular Learning / 表格学习；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：diffusion；variational
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/amazon-science/tabsyn.

## 纳入依据

Census Income" dataset contains the demographic and employment- related features people. The task is to predict whether an individual’s income exceeds 50, 000. • Default3 : The "Default of Credit Card Clients Dataset" dataset contains information on default payments, demographic factors, credit data, history of payment, and bill statements of credit card clients in Taiwan from April 2005 to September 2005. The task is to predict whether the client will default payment next month. • Shoppers4 : The "Onli

## 原始摘要

Recent advances in tabular data generation have greatly enhanced synthetic data quality. However, extending diffusion models to tabular data is challenging due to the intricately varied distributions and a blend of data types of tabular data. This paper introduces TabSyn, a methodology that synthesizes tabular data by leveraging a diffusion model within a variational autoencoder (VAE) crafted latent space. The key advantages of the proposed Tabsyn include (1) Generality: the ability to handle a broad spectrum of data types by converting them into a single unified space and explicitly capturing inter-column relations; (2) Quality: optimizing the distribution of latent embeddings to enhance the subsequent training of diffusion models, which helps generate high-quality synthetic data; (3) Speed: much fewer number of reverse steps and faster synthesis speed than existing diffusion-based methods. Extensive experiments on six datasets with five metrics demonstrate that Tabsyn outperforms existing methods. Specifically, it reduces the error rates by 86% and 67% for column-wise distribution and pair-wise column correlation estimations compared with the most competitive baselines. The code has been made available at https://github.com/amazon-science/tabsyn.
