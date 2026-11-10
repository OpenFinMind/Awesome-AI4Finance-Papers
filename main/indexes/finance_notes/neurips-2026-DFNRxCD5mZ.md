# Sketching the Readout of Large Language Models for Scalable Data Attribution and Valuation

NeurIPS 2026 · main · application

通用方法在金融任务、数据或明确案例上开展应用验证。 主题：Financial Safety & Compliance / 金融安全与合规。

- 官方论文页：https://openreview.net/forum?id=DFNRxCD5mZ
- 摘要来源：https://neurips.cc/virtual/2026/poster/154483
- 本地 PDF：[打开](../../pdfs/NeurIPS/2026/neurips-2026-DFNRxCD5mZ__Sketching_the_Readout_of_Large_Language_Models_for_Scalable_Data_Attribution_and_Valuation.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_review
- 主方向：Financial Safety & Compliance / 金融安全与合规
- 细分方向：Adversarial Robustness in Finance / 金融应用中的攻击与防御
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Language Models；language models；LLM；LLMs
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

We validate RISE on three tasks: Howdy backdoor data detection, Finance-Medical domain separation, and Brain Rot high-quality data selection.

## 原始摘要

Data attribution and valuation are critical for understanding data-model synergy for Large Language Models (LLMs), yet existing gradient-based methods suffer from scalability challenges on LLMs. Inspired by human cognition, where decision making relies on a focused readout of relevant memories rather than replaying all pathways, we introduce **RISE (Readout Influence Sketching Estimator)**. Instead of computing and indexing gradients across the entire LLM, RISE focuses on influence hotspots at the output layer, where influence signals concentrate, and the gradient admits a decomposed outer-product form. This enables a dual-channel representation combining a lexical residual channel (RH) and a semantic projected-error channel (GH). Applying CountSketch projections to these channels achieves strong compression while maintaining accurate attribution. Across the OLMo (1B–32B) and Pythia (14M–6.9B) families, RISE reduces index storage by up to 112$\times$ compared to RapidIn and scales to 32B parameters LLM, where gradient-based baselines such as RapidIn and ZO-Inf become memory-infeasible. We evaluate RISE on two paradigms: (1) retrospective attribution, retrieving influential training examples for specific predictions, and (2) prospective valuation, scoring candidate data utility zero-shot. We validate RISE on three tasks: Howdy backdoor data detection, Finance-Medical domain separation, and Brain Rot high-quality data selection. In a closed-loop Brain Rot study, continued pretraining on RISE-selected data yields consistent downstream improvements. Overall, RISE provides a practical and scalable primitive for influence analysis and training-data selection in modern large language models.
