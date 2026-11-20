# Cost-efficient Collaboration between On-device and Cloud Language Models

ICML 2025 · main · application

通用方法在金融任务、数据或明确案例上开展应用验证。 主题：Financial Models & Benchmarks / 金融模型与评测资源。

- 官方论文页：https://openreview.net/forum?id=qGDlzt3dKz
- 摘要来源：https://icml.cc/virtual/2025/poster/43949
- 本地 PDF：[打开](../../pdfs/ICML/2025/icml-2025-qGDlzt3dKz__Cost_efficient_Collaboration_between_On_device_and_Cloud_Language_Models.pdf)；版本：publisher_version
- 金融依据类型：title_abstract_review
- 主方向：Financial Models & Benchmarks / 金融模型与评测资源
- 细分方向：Cross-Task Financial Evaluation / 跨任务金融综合评测
- 技术方法标签：Language Models & LLM / 语言模型与LLM
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：language model
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

We investigate an emerging setup in which a small, on-device language model (LM) with access to local data collaborates with a frontier, cloud-hosted LM to solve real-world tasks involving financial, medical, and scientific reasoning over long documents.

## 原始摘要

We investigate an emerging setup in which a small, on-device language model (LM) with access to local data collaborates with a frontier, cloud-hosted LM to solve real-world tasks involving financial, medical, and scientific reasoning over long documents. *Can a local-remote collaboration reduce cloud inference costs while preserving quality?*First, we consider a naïve collaboration protocol, coined MINION, where the local and remote models simply chat back and forth. Because only the local model ingests the full context, this protocol reduces cloud costs by 30.4x, but recovers only 87% of the performance of the frontier model.We identify two key limitations of this protocol: the local model struggles to (1) follow the remote model's multi-step instructions and (2) reason over long contexts. Motivated by these observations, we propose MINIONS, a protocol in which the remote model decomposes the task into easier subtasks over shorter chunks of the document, that are executed locally in parallel. MINIONS reduces costs by 5.7× on average while recovering 97.9% of the remote-only performance. Our analysis reveals several key design choices that influence the trade-off between cost and performance in local-remote systems.

## Classification / 分类

- Primary task / 主方向: Financial Question Answering / 金融问答
- Primary subcategory / 主要子分类: Multi-Document and Multi-Hop QA / 多文档与多跳问答
- Related tasks / 关联方向: Financial Question Answering / 金融问答; Financial Evaluation / 金融评测
- Subcategories / 子分类: Multi-Document and Multi-Hop QA / 多文档与多跳问答; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Financial Understanding and Multimodal Evaluation / 金融理解及多模态评测
- Methods / 技术方法: Language Models & LLM / 语言模型与LLM
- Review status / 核对状态: `contribution_evidence_review`
- [Definitions / 分类定义](../finance_taxonomy.md) · [Evidence / 分类依据](../../checks/finance_taxonomy/assignments.json)
