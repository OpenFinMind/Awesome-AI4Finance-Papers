# From Token to Token Pair: Efficient Prompt Compression for Large Language Models in Clinical Prediction

ICML 2026 · main · application

通用方法在金融任务、数据或明确案例上开展应用验证。 主题：Financial Models & Benchmarks / 金融模型与评测资源。

- 官方论文页：https://openreview.net/forum?id=SRGpmDQjJM
- 摘要来源：https://icml.cc/virtual/2026/poster/63934
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-SRGpmDQjJM__From_Token_to_Token_Pair_Efficient_Prompt_Compression_for_Large_Language_Models_in_Clinical_Prediction.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_review
- 主方向：Financial Models & Benchmarks / 金融模型与评测资源
- 细分方向：Cross-Task Financial Evaluation / 跨任务金融综合评测
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Uncertainty & Robustness / 不确定性与鲁棒性；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：language models；LLM；LLMs
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Furthermore, MedTPE demonstrates robustness across different input context lengths and generalisability to scientific and financial domains and different languages.

## 原始摘要

By processing electronic health records (EHRs) as natural language sequences, large language models (LLMs) have shown potential in clinical prediction tasks such as mortality prediction and phenotyping. However, longitudinal or highly frequent EHRs often yield excessively long token sequences that result in high computational costs and even reduced performance. Existing solutions either add modules for compression or remove less important tokens, which introduce additional inference latency or risk losing clinical information. To achieve lossless compression of token sequences without additional cost or loss of performance, we propose Medical Token-Pair Encoding (MedTPE), a layered method that extends standard tokenisation for EHR sequences. MedTPE merges frequently co-occurring medical token pairs into composite tokens, providing lossless compression while preserving the computational complexity through a dependency-aware replacement strategy. Only the embeddings of the newly introduced tokens of merely 0.5-1.0\% of the LLM’s parameters are fine-tuned via self-supervised learning. Experiments on real-world datasets for two clinical scenarios demonstrate that MedTPE reduces input token length by up to 31\% and inference latency by 34-63\%, while maintaining or even improving both predictive performance and output format compliance across multiple LLMs and four clinical prediction tasks. Furthermore, MedTPE demonstrates robustness across different input context lengths and generalisability to scientific and financial domains and different languages. The code is available in the GitHub repository.

## Classification / 分类

- Primary task / 主方向: Financial Models / 金融模型
- Primary subcategory / 主要子分类: Financial Model Adaptation, Compression and Deployment / 金融模型适配、压缩与高效部署
- Related tasks / 关联方向: Financial Models / 金融模型; Financial Evaluation / 金融评测
- Subcategories / 子分类: Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Financial Model Adaptation, Compression and Deployment / 金融模型适配、压缩与高效部署; Financial Understanding and Multimodal Evaluation / 金融理解及多模态评测
- Methods / 技术方法: Language Models & LLM / 语言模型与LLM; Uncertainty & Robustness / 不确定性与鲁棒性; Representation Learning / 表征学习
- Review status / 核对状态: `inherited_evidence_mapping`
- [Definitions / 分类定义](../finance_taxonomy.md) · [Evidence / 分类依据](../../checks/finance_taxonomy/assignments.json)
