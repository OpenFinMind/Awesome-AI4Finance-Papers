# AMARIS: Merging Generalist and Specialist LLMs via Adaptive Subspace Inheritance

NeurIPS 2026 · main · application

以金融市场为研究对象，或包含明确的金融领域数据和应用评测。 主题：Financial Models & Benchmarks / 金融模型与评测资源。

- 官方论文页：https://openreview.net/forum?id=CkmAPV0HiB
- 摘要来源：https://neurips.cc/Downloads/2026
- PDF 状态：access_blocked
- 金融依据类型：title_abstract_financial_task_or_data
- 主方向：Financial Models & Benchmarks / 金融模型与评测资源
- 细分方向：Financial Pretraining & Adaptation / 金融预训练与领域适配
- 技术方法标签：Language Models & LLM / 语言模型与LLM
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：language models；LLMs
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

We evaluate AMARIS on Qwen3-based merges (8B and 32B) across finance, instruction-following, and multilingual SEA specialization. / In our evaluated settings, AMARIS reaches Pareto operating points that are competitive with strong training-free baselines, including 98.37\% specialist retention with 95.76\% core retention (finance), 103.49\% core retention with 90.28\% specialist retention (instruction following), and 93.69\% specialist retention with 99.77\% core retention (SEA).

## 原始摘要

Domain specialization of large language models (LLMs) often improves target-domain performance but degrades broad capabilities. Model merging is an attractive training-free alternative, yet common parameter-space strategies (for example, interpolation and sparsified averaging) provide limited control over task-specific interference. We introduce Adaptive Model Alignment via Ranked Inherited Subspaces (AMARIS), a covariance-driven framework that transfers specialist updates only along selected activation directions. AMARIS formulates merging as budgeted subspace inheritance: it maximizes specialist activation capture while constraining base-activation deviation, then builds a low-rank projection gate from ranked generalized eigendirections under an explicit preservation budget. This yields a single static merged checkpoint that concentrates transfer in high-utility, low-interference directions. We evaluate AMARIS on Qwen3-based merges (8B and 32B) across finance, instruction-following, and multilingual SEA specialization. In our evaluated settings, AMARIS reaches Pareto operating points that are competitive with strong training-free baselines, including 98.37\% specialist retention with 95.76\% core retention (finance), 103.49\% core retention with 90.28\% specialist retention (instruction following), and 93.69\% specialist retention with 99.77\% core retention (SEA). These results support subspace-constrained merging as a practical route to compositional capability integration without additional training.
