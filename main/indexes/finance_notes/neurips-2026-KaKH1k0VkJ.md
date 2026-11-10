# RiSE: Residual Subspace Expert for Generalizable Text-Centric Image Forgery Localization

NeurIPS 2026 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：SROIE。 主题：Document AI / 票据、财报与图表理解。

- 官方论文页：https://openreview.net/forum?id=KaKH1k0VkJ
- 摘要来源：https://neurips.cc/Downloads/2026
- 本地 PDF：[打开](../../pdfs/NeurIPS/2026/neurips-2026-KaKH1k0VkJ__RiSE_Residual_Subspace_Expert_for_Generalizable_Text_Centric_Image_Forgery_Localization.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Document AI / 票据、财报与图表理解
- 细分方向：Receipts, Invoices & OCR / 票据发票与OCR
- 技术方法标签：Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Fine-Tuning
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

0 2000 4000 6000 8000 10000 Training Step T-SROIE OSTF TPIC-13 RTM (a) (b) Figure 2: More residual experts improve (a) training optimization and (b) cross-domain localization. RiSE-x denotes the RiSE with x residua

## 原始摘要

As AI-assisted image editing becomes increasingly prevalent, Text-Centric Image Forgery Localization (TFL) is essential for protecting trust in financial and legal records. However, we observe that existing TFL detectors predominantly rely on Full-Parameter Fine-Tuning (FPFT) and fail to generalize to unseen forgery types because FPFT can induce low-rank feature collapse and overfit training artifacts. Meanwhile, prior detectors capture diverse forgery traces with a single unified representation, making subtle traces entangled and difficult to learn. To address these challenges, we propose RiSE, a Residual Subspace Expert model that preserves pre-trained priors by freezing principal SVD components and adapting only the residual subspaces with a ViT-only segmentor to avoid feature collapse. RiSE introduces forgery-aware residual experts, where each expert is trained independently on a training subset with a particular forgery type, and we show that cross-domain localization performance improves consistently as more experts are added. At inference, we introduce Latent Perturbation Confidence (LPC), which selects the most confident expert by analytically computing the latent-perturbed output. LPC enables efficient confidence estimation with a single forward pass, avoiding repeated forward passes on perturbed samples and improving expert selection. By training on synthetic forgery data, RiSE with 1 expert outperforms state-of-the-art methods on real-world forgery images by 20.4\% while reducing training steps by $10\times$. Scaling the number of experts to 9 yields a 35.8\% gain. RiSE also remains effective with DCT feature fusion, even when the majority of the parameters is frozen with RGB-only pretraining. The code is in the supplementary material.
