# Mining Useful General Data for Low-Resource Domain Adaptation

ICML 2026 · main · application

通用方法在金融任务、数据或明确案例上开展应用验证。 主题：Financial Models & Benchmarks / 金融模型与评测资源。

- 官方论文页：https://openreview.net/forum?id=y1AV6cX8dX
- 摘要来源：https://icml.cc/virtual/2026/poster/60654
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-y1AV6cX8dX__Mining_Useful_General_Data_for_Low_Resource_Domain_Adaptation.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_review
- 主方向：Financial Models & Benchmarks / 金融模型与评测资源
- 细分方向：Financial Pretraining & Adaptation / 金融预训练与领域适配
- 技术方法标签：Language Models & LLM / 语言模型与LLM
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：fine-tuning；language models；LLMs
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Extensive experiments across medical, financial, legal, and psychological domains demonstrate that NTK-Selector consistently outperforms domain-only fine-tuning and existing data selection baselines.

## 原始摘要

Adapting large language models (LLMs) to low-resource domains remains challenging due to the scarcity of domain-specific data. While in-domain data is limited, there exists a vast amount of general-domain data that shares similar question–answer formats and reasoning patterns with domain tasks. This observation raises an important question: can useful general-domain data be mined to improve low-resource domain adaptation? Our initial findings show that general-domain chain-of-thought data contains useful auxiliary signals for domain adaptation, even without careful selection. This observation motivates a new paradigm for domain adaptation beyond exclusive reliance on domain-specific data. To systematically identify the most beneficial general-domain samples, we propose NTK-Selector, motivated by the Neural Tangent Kernel’s ability to capture alignment in training dynamics. Since directly applying NTK to pretrained LLMs is impractical, we introduce a Jacobian-free NTK approximation and empirically demonstrate stable NTK-like behavior during fine-tuning. Extensive experiments across medical, financial, legal, and psychological domains demonstrate that NTK-Selector consistently outperforms domain-only fine-tuning and existing data selection baselines. In particular, NTK-Selector achieves gains of +8.7 and +5.1 points on Llama3-8B-Instruct and Qwen3-8B, respectively, compared to only +0.8 and +0.9 points from domain-only fine-tuning.
