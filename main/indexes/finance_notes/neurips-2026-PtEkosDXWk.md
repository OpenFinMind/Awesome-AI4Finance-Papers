# Crowded in B-Space: Calibrating Shared Directions for LoRA Merging

NeurIPS 2026 · main · application

通用方法在金融任务、数据或明确案例上开展应用验证。 主题：Financial QA & Reasoning / 金融问答与数值推理。

- 官方论文页：https://openreview.net/forum?id=PtEkosDXWk
- 摘要来源：https://neurips.cc/virtual/2026/poster/152853
- 本地 PDF：[打开](../../pdfs/NeurIPS/2026/neurips-2026-PtEkosDXWk__Crowded_in_B_Space_Calibrating_Shared_Directions_for_LoRA_Merging.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_review
- 主方向：Financial QA & Reasoning / 金融问答与数值推理
- 细分方向：Numerical & Table Reasoning / 数值与表格推理
- 技术方法标签：Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Across eight different benchmarks from math, coding, finance, and medical domains, Pico improves average accuracy by 3.4-8.3 points over the corresponding base method and achieves the best overall average performance.

## 原始摘要

Merging separately trained LoRA adapters is a practical alternative to joint multi-task training, but it often hurts performance. Existing methods usually treat the LoRA update $\Delta W = BA$ as a single object and do not distinguish the two LoRA matrices. We show that the main source of LoRA merge interference comes from the output-side matrix $B$. Across tasks, $B$ repeatedly uses a small set of shared directions, while $A$ remains much more task-specific. As a result, the merged adapter overemphasizes these shared directions, and task-specific information is lost. We propose Pico (Pre-merge interference calibration in output-space), a data-free method that calibrates $B$ before merge by downscaling over-shared directions and then rescaling the merged update. Pico plugs directly into existing merging methods such as Task Arithmetic, TIES, and TSV-M. Across eight different benchmarks from math, coding, finance, and medical domains, Pico improves average accuracy by 3.4-8.3 points over the corresponding base method and achieves the best overall average performance. Pico also enables merged adapters to outperform the LoRA trained with all task data. These results show that LoRA merging works better when the two LoRA matrices are treated separately.
