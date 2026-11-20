# Financial Models / 金融模型

Financial domain pretraining, adaptation and reusable foundation models; generic time-series pretraining stays time series. / 金融领域预训练、适配与可复用基础模型；通用序列预训练仍归时间序列。

22 Main long papers. Topic memberships can overlap.

[All topics](../ai_for_finance.md) · [Classification definitions](../finance_taxonomy.md) · [CSV](financial_models.csv) · [Excel](../../finance_catalog.xlsx)

<!-- task-summary:start -->

## Research summary / 研究总结

**Financial Models / 金融模型 · Main / Application**

2026-11-20 · 22 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 关注可复用的金融领域模型及其预训练、后训练和适配。金融是通用适配方法的实验领域时归 Application；只在单个任务中调用 LLM 不构成金融模型贡献。

**当前收录与方法。** 本页仅总结 Main / application 中的论文。当前较常见的子分类：Financial Foundation Models and Domain Pretraining / 金融基础模型与领域预训练 (17); Financial Instruction Tuning and Post-Training / 金融指令微调与后训练 (8); Financial Model Adaptation, Compression and Deployment / 金融模型适配、压缩与高效部署 (5); Financial Representation Models / 金融专用表示模型 (2); Financial Multimodal Models / 金融多模态模型 (1)。已标注的方法：Language Models & LLM / 语言模型与LLM (20); Representation Learning / 表征学习 (6); Optimization & Numerical Methods / 优化与数值方法 (4); Uncertainty & Robustness / 不确定性与鲁棒性 (4); Retrieval & RAG / 检索与RAG (3)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 检查预训练数据、时间污染、跨任务迁移、模型规模和计算预算。 代表论文的摘要、金融关联证据及原文链接见 [1](../finance_notes/aaai-2026-40722.md) · [2](../finance_notes/2026.acl-long.645.md) · [3](../finance_notes/2026.acl-long.996.md) · [4](../finance_notes/2026.acl-long.2201.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 核对金融语料时间边界、能力保持和跨任务迁移，分离模型规模、数据、训练预算及检索的贡献。

### English

**Problem and subdirections.** This task concerns reusable financial models and their pretraining, post-training and adaptation. Finance as one domain of a general adaptation method belongs to Application; calling an LLM for one task is insufficient.

**Current coverage and methods.** This page covers only Main / application. Frequent subcategories: Financial Foundation Models and Domain Pretraining / 金融基础模型与领域预训练 (17); Financial Instruction Tuning and Post-Training / 金融指令微调与后训练 (8); Financial Model Adaptation, Compression and Deployment / 金融模型适配、压缩与高效部署 (5); Financial Representation Models / 金融专用表示模型 (2); Financial Multimodal Models / 金融多模态模型 (1). Recorded methods: Language Models & LLM / 语言模型与LLM (20); Representation Learning / 表征学习 (6); Optimization & Numerical Methods / 优化与数值方法 (4); Uncertainty & Robustness / 不确定性与鲁棒性 (4); Retrieval & RAG / 检索与RAG (3). Counts overlap and are not performance rankings.

**Data and evaluation.** Audit pretraining data, temporal contamination, cross-task transfer, model size and compute budget. Representative abstracts, financial evidence and original sources are linked at [1](../finance_notes/aaai-2026-40722.md) · [2](../finance_notes/2026.acl-long.645.md) · [3](../finance_notes/2026.acl-long.996.md) · [4](../finance_notes/2026.acl-long.2201.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Audit financial-corpus time boundaries, capability retention and cross-task transfer, separating scale, data, training budget and retrieval effects.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. RCP-Merging: Merging Long Chain-of-Thought Models with Domain-Specific Models by Considering Reasoning Capability as Prior](../finance_notes/aaai-2026-40722.md) · AAAI 2026 | 研究主题：RCP-Merging: Merging Long Chain-of-Thought Models with Domain-Specific Models by Considering Reasoning Capability as Prior<br>Research topic: RCP-Merging: Merging Long Chain-of-Thought Models with Domain-Specific Models by Considering Reasoning Capability as Prior | 按原文的任务、数据和实验设置解释结果。<br>Interpret results within the original task, data and experimental setting. |
| [2. Map of Encoders – Mapping Sentence Encoders using Quantum Relative Entropy](../finance_notes/2026.acl-long.645.md) · ACL 2026 | 研究主题：Map of Encoders – Mapping Sentence Encoders using Quantum Relative Entropy<br>Research topic: Map of Encoders – Mapping Sentence Encoders using Quantum Relative Entropy | 按原文的任务、数据和实验设置解释结果。<br>Interpret results within the original task, data and experimental setting. |
| [3. Nirvana: A Specialized Generalist Model With Task-Aware Memory Mechanism](../finance_notes/2026.acl-long.996.md) · ACL 2026 | 研究主题：Nirvana: A Specialized Generalist Model With Task-Aware Memory Mechanism<br>Research topic: Nirvana: A Specialized Generalist Model With Task-Aware Memory Mechanism | 按原文的任务、数据和实验设置解释结果。<br>Interpret results within the original task, data and experimental setting. |
| [4. ReasonAny: Incorporating Reasoning Capability to Any Model via Simple and Effective Model Merging](../finance_notes/2026.acl-long.2201.md) · ACL 2026 | 研究主题：ReasonAny: Incorporating Reasoning Capability to Any Model via Simple and Effective Model Merging<br>Research topic: ReasonAny: Incorporating Reasoning Capability to Any Model via Simple and Effective Model Merging | 按原文的任务、数据和实验设置解释结果。<br>Interpret results within the original task, data and experimental setting. |

<!-- task-summary:end -->

## Subtopic statistics / 子方向统计

| Subtopic | Papers |
|---|---:|
| Financial Foundation Models and Domain Pretraining / 金融基础模型与领域预训练 | 17 |
| Financial Instruction Tuning and Post-Training / 金融指令微调与后训练 | 8 |
| Financial Representation Models / 金融专用表示模型 | 2 |
| Financial Multimodal Models / 金融多模态模型 | 1 |
| Financial Time-Series Foundation Models / 金融时序基础模型 | 0 |
| Financial Model Adaptation, Compression and Deployment / 金融模型适配、压缩与高效部署 | 5 |

## Full paper list / 完整论文列表

| Year | Venue | Paper | Scope | Primary topic | Subtopics | Methods | Resources |
|---|---|---|---|---|---|---|---|
| 2026 | AAAI | [RCP-Merging: Merging Long Chain-of-Thought Models with Domain-Specific Models by Considering Reasoning Capability as Prior](../finance_notes/aaai-2026-40722.md) | application | Financial Models / 金融模型 | Financial Foundation Models and Domain Pretraining / 金融基础模型与领域预训练 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/AAAI/2026/aaai-2026-40722__RCP_Merging_Merging_Long_Chain_of_Thought_Models_with_Domain_Specific_Models_by_Considering_Reasoning_Capability_as_Prior.pdf) |
| 2026 | ACL | [Map of Encoders – Mapping Sentence Encoders using Quantum Relative Entropy](../finance_notes/2026.acl-long.645.md) | application | Financial Models / 金融模型 | Financial Foundation Models and Domain Pretraining / 金融基础模型与领域预训练 | Retrieval & RAG / 检索与RAG; Representation Learning / 表征学习 | [PDF](../../pdfs/ACL/2026/2026.acl-long.645__Map_of_Encoders_Mapping_Sentence_Encoders_using_Quantum_Relative_Entropy.pdf) |
| 2026 | ACL | [Nirvana: A Specialized Generalist Model With Task-Aware Memory Mechanism](../finance_notes/2026.acl-long.996.md) | application | Financial Models / 金融模型 | Financial Foundation Models and Domain Pretraining / 金融基础模型与领域预训练 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/ACL/2026/2026.acl-long.996__Nirvana_A_Specialized_Generalist_Model_With_Task_Aware_Memory_Mechanism.pdf) |
| 2026 | ACL | [ReasonAny: Incorporating Reasoning Capability to Any Model via Simple and Effective Model Merging](../finance_notes/2026.acl-long.2201.md) | application | Financial Models / 金融模型 | Financial Foundation Models and Domain Pretraining / 金融基础模型与领域预训练 | Uncertainty & Robustness / 不确定性与鲁棒性 | [PDF](../../pdfs/ACL/2026/2026.acl-long.2201__ReasonAny_Incorporating_Reasoning_Capability_to_Any_Model_via_Simple_and_Effective_Model_Merging.pdf) |
| 2026 | ICLR | [GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning](../finance_notes/iclr-2026-RQm2KQTM5r.md) | application | Financial Models / 金融模型 | Financial Foundation Models and Domain Pretraining / 金融基础模型与领域预训练 | Language Models & LLM / 语言模型与LLM; Reinforcement Learning / 强化学习; Optimization & Numerical Methods / 优化与数值方法 | [PDF](../../pdfs/ICLR/2026/iclr-2026-RQm2KQTM5r__GEPA_Reflective_Prompt_Evolution_Can_Outperform_Reinforcement_Learning.pdf) |
| 2026 | ICLR | [GradPruner: Gradient-guided Layer Pruning Enabling Efficient Fine-Tuning and Inference for LLMs](../finance_notes/iclr-2026-bxzJorqyYM.md) | application | Financial Models / 金融模型 | Financial Foundation Models and Domain Pretraining / 金融基础模型与领域预训练; Financial Instruction Tuning and Post-Training / 金融指令微调与后训练; Financial Model Adaptation, Compression and Deployment / 金融模型适配、压缩与高效部署 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/ICLR/2026/iclr-2026-bxzJorqyYM__GradPruner_Gradient_guided_Layer_Pruning_Enabling_Efficient_Fine_Tuning_and_Inference_for_LLMs.pdf) |
| 2026 | ICLR | [LLM DNA: Tracing Model Evolution via Functional Representations](../finance_notes/iclr-2026-2026-Oral--8961-f474c16f.md) | application | Financial Models / 金融模型 | Financial Foundation Models and Domain Pretraining / 金融基础模型与领域预训练; Financial Representation Models / 金融专用表示模型 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/ICLR/2026/iclr-2026-2026-Oral--8961-f474c16f__LLM_DNA_Tracing_Model_Evolution_via_Functional_Representations.pdf) |
| 2026 | ICLR | [Semi-Supervised Preference Optimization with Limited Feedback](../finance_notes/iclr-2026-2026-Oral--710-b9dc3169.md) | application | Financial Models / 金融模型 | Financial Instruction Tuning and Post-Training / 金融指令微调与后训练 | Language Models & LLM / 语言模型与LLM; Optimization & Numerical Methods / 优化与数值方法 | [PDF](../../pdfs/ICLR/2026/iclr-2026-2026-Oral--710-b9dc3169__Semi_Supervised_Preference_Optimization_with_Limited_Feedback.pdf) |
| 2026 | ICML | [From Token to Token Pair: Efficient Prompt Compression for Large Language Models in Clinical Prediction](../finance_notes/icml-2026-SRGpmDQjJM.md) | application | Financial Models / 金融模型 | Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Financial Model Adaptation, Compression and Deployment / 金融模型适配、压缩与高效部署; Financial Understanding and Multimodal Evaluation / 金融理解及多模态评测 | Language Models & LLM / 语言模型与LLM; Uncertainty & Robustness / 不确定性与鲁棒性; Representation Learning / 表征学习 | [PDF](../../pdfs/ICML/2026/icml-2026-SRGpmDQjJM__From_Token_to_Token_Pair_Efficient_Prompt_Compression_for_Large_Language_Models_in_Clinical_Prediction.pdf) |
| 2026 | ICML | [Mining Useful General Data for Low-Resource Domain Adaptation](../finance_notes/icml-2026-y1AV6cX8dX.md) | application | Financial Models / 金融模型 | Financial Foundation Models and Domain Pretraining / 金融基础模型与领域预训练; Financial Instruction Tuning and Post-Training / 金融指令微调与后训练 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/ICML/2026/icml-2026-y1AV6cX8dX__Mining_Useful_General_Data_for_Low_Resource_Domain_Adaptation.pdf) |
| 2026 | NeurIPS | [AMARIS: Merging Generalist and Specialist LLMs via Adaptive Subspace Inheritance](../finance_notes/neurips-2026-CkmAPV0HiB.md) | application | Financial Models / 金融模型 | Financial Foundation Models and Domain Pretraining / 金融基础模型与领域预训练; Financial Instruction Tuning and Post-Training / 金融指令微调与后训练 | Language Models & LLM / 语言模型与LLM | [Online](https://openreview.net/forum?id=CkmAPV0HiB) |
| 2025 | ACL | [TrimLLM: Progressive Layer Dropping for Domain-Specific LLMs](../finance_notes/2025.acl-long.33.md) | application | Financial Models / 金融模型 | Financial Foundation Models and Domain Pretraining / 金融基础模型与领域预训练 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/ACL/2025/2025.acl-long.33__TrimLLM_Progressive_Layer_Dropping_for_Domain_Specific_LLMs.pdf) |
| 2025 | EMNLP | [CBP-Tuning: Efficient Local Customization for Black-box Large Language Models](../finance_notes/2025.emnlp-main.991.md) | application | Financial Models / 金融模型 | Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Financial Model Adaptation, Compression and Deployment / 金融模型适配、压缩与高效部署; Financial Understanding and Multimodal Evaluation / 金融理解及多模态评测 | Language Models & LLM / 语言模型与LLM; Optimization & Numerical Methods / 优化与数值方法 | [PDF](../../pdfs/EMNLP/2025/2025.emnlp-main.991__CBP_Tuning_Efficient_Local_Customization_for_Black_box_Large_Language_Models.pdf) |
| 2025 | EMNLP | [VersaTune: An Efficient Data Composition Framework for Training Multi-Capability LLMs](../finance_notes/2025.emnlp-main.337.md) | application | Financial Models / 金融模型 | Financial Foundation Models and Domain Pretraining / 金融基础模型与领域预训练; Financial Model Adaptation, Compression and Deployment / 金融模型适配、压缩与高效部署 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/EMNLP/2025/2025.emnlp-main.337__VersaTune_An_Efficient_Data_Composition_Framework_for_Training_Multi_Capability_LLMs.pdf) |
| 2025 | ICLR | [REEF: Representation Encoding Fingerprints for Large Language Models](../finance_notes/iclr-2025-SnDmPkOJ0T.md) | application | Financial Models / 金融模型 | Financial Foundation Models and Domain Pretraining / 金融基础模型与领域预训练; Financial Representation Models / 金融专用表示模型 | Language Models & LLM / 语言模型与LLM; Uncertainty & Robustness / 不确定性与鲁棒性 | [PDF](../../pdfs/ICLR/2025/iclr-2025-SnDmPkOJ0T__REEF_Representation_Encoding_Fingerprints_for_Large_Language_Models.pdf) |
| 2025 | ICLR | [Teaching LLMs How to Learn with Contextual Fine-Tuning](../finance_notes/iclr-2025-FS2nukC2jv.md) | application | Financial Models / 金融模型 | Financial Foundation Models and Domain Pretraining / 金融基础模型与领域预训练; Financial Instruction Tuning and Post-Training / 金融指令微调与后训练 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/ICLR/2025/iclr-2025-FS2nukC2jv__Teaching_LLMs_How_to_Learn_with_Contextual_Fine_Tuning.pdf) |
| 2025 | NeurIPS | [Breaking the Gradient Barrier: Unveiling Large Language Models for Strategic Classification](../finance_notes/neurips-2025-V0lnRCH73U.md) | application | Financial Models / 金融模型 | Financial Foundation Models and Domain Pretraining / 金融基础模型与领域预训练 | Language Models & LLM / 语言模型与LLM; Generative Modeling / 生成建模; Transformer / Transformer模型; Fairness & Recourse / 公平性与算法追索; Uncertainty & Robustness / 不确定性与鲁棒性; Optimization & Numerical Methods / 优化与数值方法 | [PDF](../../pdfs/NeurIPS/2025/neurips-2025-V0lnRCH73U__Breaking_the_Gradient_Barrier_Unveiling_Large_Language_Models_for_Strategic_Classification.pdf) |
| 2025 | NeurIPS | [Memory Decoder: A Pretrained, Plug-and-Play Memory for Large Language Models](../finance_notes/neurips-2025-ARJpQtLXfe.md) | application | Financial Models / 金融模型 | Financial Foundation Models and Domain Pretraining / 金融基础模型与领域预训练 | Language Models & LLM / 语言模型与LLM; Transformer / Transformer模型; Retrieval & RAG / 检索与RAG; Representation Learning / 表征学习 | [PDF](../../pdfs/NeurIPS/2025/neurips-2025-ARJpQtLXfe__Memory_Decoder_A_Pretrained_Plug_and_Play_Memory_for_Large_Language_Models.pdf) |
| 2024 | ACL | [IndicLLMSuite: A Blueprint for Creating Pre-training and Fine-Tuning Datasets for Indian Languages](../finance_notes/2024.acl-long.843.md) | application | Financial Models / 金融模型 | Financial Foundation Models and Domain Pretraining / 金融基础模型与领域预训练; Financial Instruction Tuning and Post-Training / 金融指令微调与后训练 | Language Models & LLM / 语言模型与LLM; Generative Modeling / 生成建模; Representation Learning / 表征学习 | [PDF](../../pdfs/ACL/2024/2024.acl-long.843__IndicLLMSuite_A_Blueprint_for_Creating_Pre_training_and_Fine_Tuning_Datasets_for_Indian_Languages.pdf) |
| 2024 | ICLR | [Adapting Large Language Models via Reading Comprehension](../finance_notes/iclr-2024-y886UXPEZ0.md) | application | Financial Models / 金融模型 | Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Financial Instruction Tuning and Post-Training / 金融指令微调与后训练; Financial Understanding and Multimodal Evaluation / 金融理解及多模态评测 | Language Models & LLM / 语言模型与LLM; Representation Learning / 表征学习 | [Online](https://openreview.net/forum?id=y886UXPEZ0) |
| 2023 | NeurIPS | [Interactive Multi-fidelity Learning for Cost-effective Adaptation of Language Model with Sparse Human Supervision](../finance_notes/neurips-2023-71465.md) | application | Financial Models / 金融模型 | Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Financial Instruction Tuning and Post-Training / 金融指令微调与后训练; Financial Multimodal Models / 金融多模态模型; Financial Understanding and Multimodal Evaluation / 金融理解及多模态评测 | Language Models & LLM / 语言模型与LLM; Retrieval & RAG / 检索与RAG | [PDF](../../pdfs/NeurIPS/2023/neurips-2023-71465__Interactive_Multi_fidelity_Learning_for_Cost_effective_Adaptation_of_Language_Model_with_Sparse_Human_Sup.pdf) |
| 2022 | ACL | [Domain Knowledge Transferring for Pre-trained Language Model via Calibrated Activation Boundary Distillation](../finance_notes/2022.acl-long.116.md) | application | Financial Models / 金融模型 | Financial Foundation Models and Domain Pretraining / 金融基础模型与领域预训练; Financial Model Adaptation, Compression and Deployment / 金融模型适配、压缩与高效部署 | Language Models & LLM / 语言模型与LLM; Representation Learning / 表征学习 | [PDF](../../pdfs/ACL/2022/2022.acl-long.116__Domain_Knowledge_Transferring_for_Pre_trained_Language_Model_via_Calibrated_Activation_Boundary_Distillat.pdf) |
