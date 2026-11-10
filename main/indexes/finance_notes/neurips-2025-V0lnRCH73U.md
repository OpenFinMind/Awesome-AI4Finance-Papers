# Breaking the Gradient Barrier: Unveiling Large Language Models for Strategic Classification

NeurIPS 2025 · main · application

通用方法在金融任务、数据或明确案例上开展应用验证。 主题：Financial Models & Benchmarks / 金融模型与评测资源。

- 官方论文页：https://openreview.net/forum?id=V0lnRCH73U
- 摘要来源：https://neurips.cc/virtual/2025/poster/117729
- 本地 PDF：[打开](../../pdfs/NeurIPS/2025/neurips-2025-V0lnRCH73U__Breaking_the_Gradient_Barrier_Unveiling_Large_Language_Models_for_Strategic_Classification.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_review
- 主方向：Financial Models & Benchmarks / 金融模型与评测资源
- 细分方向：Financial Pretraining & Adaptation / 金融预训练与领域适配
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Generative Modeling / 生成建模；Transformer / Transformer模型；Fairness & Recourse / 公平性与算法追索；Uncertainty & Robustness / 不确定性与鲁棒性；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：fine-tuning；language models；LLMs；optimization
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

However, existing SC methods, which are largely based on linear models or shallow neural networks, face significant limitations in terms of scalability and capacity when applied to real-world datasets with significantly increasing scale, especially in financial services and the internet sector. / We validate our approach through experiments with a collection of pre-trained LLMs on real-world and synthetic datasets in financial and internet domains, demonstrating that our GLIM exhibits both robustness and efficiency, and offering an effective solution for large-scale SC tasks.

## 原始摘要

Strategic classification (SC) explores how individuals or entities modify their features strategically to achieve favorable classification outcomes. However, existing SC methods, which are largely based on linear models or shallow neural networks, face significant limitations in terms of scalability and capacity when applied to real-world datasets with significantly increasing scale, especially in financial services and the internet sector.  In this paper, we investigate how to leverage large language models to design a more scalable and efficient SC framework, especially in the case of growing individuals engaged with decision-making processes. Specifically, we introduce GLIM, a gradient-free SC method grounded in in-context learning.  During the feed-forward process of self-attention, GLIM implicitly simulates the typical bi-level optimization process of SC, including both the feature manipulation and decision rule optimization.  Without fine-tuning the LLMs, our proposed GLIM enjoys the advantage of cost-effective adaptation in dynamic strategic environments. Theoretically, we prove GLIM can support pre-trained LLMs to adapt to a broad range of strategic manipulations. We validate our approach through experiments with a collection of pre-trained LLMs on real-world and synthetic datasets in financial and internet domains, demonstrating that our GLIM exhibits both robustness and efficiency, and offering an effective solution for large-scale SC tasks.
