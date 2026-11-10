# PlotCraft: Pushing the Limits of LLMs for Complex and Interactive Data Visualization

ICML 2026 · main · application

包含明确的金融任务、金融领域数据或金融案例验证。 主题：Document AI / 票据、财报与图表理解。

- 官方论文页：https://openreview.net/forum?id=RQJjbqIcz0
- 摘要来源：https://icml.cc/virtual/2026/poster/64044
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-RQJjbqIcz0__PlotCraft_Pushing_the_Limits_of_LLMs_for_Complex_and_Interactive_Data_Visualization.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_financial_task_or_data
- 主方向：Document AI / 票据、财报与图表理解
- 细分方向：Charts & Visual Understanding / 金融图表与视觉理解
- 技术方法标签：Language Models & LLM / 语言模型与LLM
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Language Models；LLMs
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

To address this gap, we introduce **PlotCraft**, a new benchmark featuring 1k challenging visualization tasks that cover a wide range of topics, such as finance, scientific research, and sociology.

## 原始摘要

Recent Large Language Models (LLMs) have demonstrated remarkable proficiency in code generation. However, their ability to create complex visualizations for scaled and structured data remains largely unevaluated and underdeveloped. To address this gap, we introduce **PlotCraft**, a new benchmark featuring 1k challenging visualization tasks that cover a wide range of topics, such as finance, scientific research, and sociology. The benchmark is structured around seven high-level visualization tasks and encompasses 48 distinct chart types. Crucially, it is the first to systematically evaluate both single-turn generation and multi-turn refinement across a diverse spectrum of task complexities. Our comprehensive evaluation of 23 leading LLMs on PlotCraft reveals obvious performance deficiencies in handling sophisticated visualization tasks. To bridge this performance gap, we develope **SynthVis-30K**, a large-scale, high-quality dataset of complex visualization code synthesized via a collaborative agent framework. Building upon this dataset, we develope **PlotCraftor**, a novel code generation model that achieves strong capabilities in complex data visualization with a remarkably small size. Across VisEval, PandasPlotBench, and our proposed PlotCraft, PlotCraftor shows performance comparable to that of leading proprietary approaches. Especially, on hard task, Our model achieves over 50\% performance improvement. We will release the benchmark, dataset, and code at \href{https://anonymous.4open.science/r/PlotCraft-E320}{PlotCraft anonymous repository}.
