# DAVE: A VLM Vision Encoder for Document Understanding and Web Agents

ICLR 2026 · main · application

正文包含金融数据、金融训练数据、金融任务评测或具体金融场景案例。 主题：ESG & Sustainable Finance / ESG与可持续金融。

- 官方论文页：https://openreview.net/forum?id=kgk0NqjsoW
- 摘要来源：https://iclr.cc/virtual/2026/poster/10007757
- 本地 PDF：[打开](../../pdfs/ICLR/2026/iclr-2026-kgk0NqjsoW__DAVE_A_VLM_Vision_Encoder_for_Document_Understanding_and_Web_Agents.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：ESG & Sustainable Finance / ESG与可持续金融
- 细分方向：ESG Disclosure & Greenwashing / ESG披露与漂绿
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Uncertainty & Robustness / 不确定性与鲁棒性；Multimodal Learning / 多模态学习；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：language models
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

20 million images for our self-supervised training. For document data, we sample 10 million PDF images from DocFM (Team et al., 2025), which contains 85 million document pages extracted from Common Crawl, Wikipedia, and ESG (Environmental, 6 Preprint. Under review. Mind2Web Model Cross-Task Cross-Website Cross-Domain Element Step Element Step

## 原始摘要

While Vision–language models (VLMs) have demonstrated remarkable performance across multi-modal tasks, their choice of vision encoders presents a fundamental weakness: their low-level features lack the robust structural and spatial information essential for document understanding and web agents. To bridge this gap, we introduce DAVE, a vision encoder purpose-built for VLMs and tailored for these tasks. Our training pipeline is designed to leverage abundant unlabeled data to bypass the need for costly large-scale annotations for document and web images. We begin with a self-supervised pretraining stage on unlabeled images, followed by a supervised autoregressive pretraining stage, where the model learns tasks like parsing and localization from limited, high-quality data. Within the supervised stage, we adopt two strategies to improve our encoder’s alignment with both general visual knowledge and diverse document and web agentic tasks: (i) We introduce a novel model-merging scheme, combining encoders trained with different text decoders to ensure broad compatibility with different web agentic architectures. (ii) We use ensemble training to fuse features from pretrained generalist encoders (e.g., SigLIP2) with our own document and web-specific representations. Extensive experiments on classic document tasks, VQAs, web localization, and agent-based benchmarks validate the effectiveness of our approach, establishing DAVE as a strong vision encoder for document and web applications.
