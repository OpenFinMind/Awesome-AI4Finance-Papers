# PAAC: Privacy-Aware Agentic Device-Cloud Collaboration

NeurIPS 2026 · main · application

包含明确的金融任务、金融领域数据或金融案例验证。 主题：Financial QA & Reasoning / 金融问答与数值推理。

- 官方论文页：https://openreview.net/forum?id=pkgQ4KB4Se
- 摘要来源：https://neurips.cc/Downloads/2026
- 本地 PDF：[打开](../../pdfs/NeurIPS/2026/neurips-2026-pkgQ4KB4Se__PAAC_Privacy_Aware_Agentic_Device_Cloud_Collaboration.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_financial_task_or_data
- 主方向：Financial QA & Reasoning / 金融问答与数值推理
- 细分方向：Numerical & Table Reasoning / 数值与表格推理
- 技术方法标签：Language Models & LLM / 语言模型与LLM
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：language model；LLM
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

We find consistent improvements on 17 additional benchmarks spanning 10 domains, including math, science, and finance.

## 原始摘要

Large language model (LLM) agents face a structural tension: cloud agents provide strong reasoning but expose user data, while on-device agents preserve privacy at the cost of overall capability. Existing device-cloud designs treat this boundary as a compute split rather than a trust boundary suited to agentic workloads, and existing sanitizers force a choice between policy flexibility and the structural fidelity tool calls require. In this work, we develop PAAC, a privacy-aware agentic framework that aligns planner--executor decomposition with the device-cloud boundary so that role specialization itself becomes the privacy mechanism. The cloud agent reasons over typed placeholder tokens that preserve each sensitive value's reasoning role while discarding its content, while the on-device agent identifies sensitive spans and distills each step's execution outcome into compact key findings. Sanitization confines the on-device LLM to proposing which spans to mask, while a deterministic registry performs all substitution and reversal, keeping actions directly executable on device. On three agentic benchmarks under strict privacy settings, PAAC dominates the Pareto frontier of privacy and accuracy, improving average accuracy by 15-36\% and reducing average leakage by 2-6$\times$ over state-of-the-art device-cloud baselines, with the largest margins on privacy targets outside fixed entity taxonomies. We find consistent improvements on 17 additional benchmarks spanning 10 domains, including math, science, and finance.
