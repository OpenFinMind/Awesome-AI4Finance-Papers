# Test-Time Scaling in the Wild: Why Exploitation, Not Exploration, Is the Bottleneck

NeurIPS 2026 · main · application

通用方法在金融任务、数据或明确案例上开展应用验证。 主题：Financial Models & Benchmarks / 金融模型与评测资源。

- 官方论文页：https://openreview.net/forum?id=M2vIH3TuCs
- 摘要来源：https://neurips.cc/virtual/2026/poster/153345
- 本地 PDF：[打开](../../pdfs/NeurIPS/2026/neurips-2026-M2vIH3TuCs__Test_Time_Scaling_in_the_Wild_Why_Exploitation_Not_Exploration_Is_the_Bottleneck.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_review
- 主方向：Financial Models & Benchmarks / 金融模型与评测资源
- 细分方向：Cross-Task Financial Evaluation / 跨任务金融综合评测
- 技术方法标签：Language Models & LLM / 语言模型与LLM
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：language model
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

We conduct the first compute-normalised comparison of five TTS families across five open-ended generation benchmarks spanning medicine, law, finance, general chat, and creative writing — grounded in a unified framework that decomposes the effectiveness of each method's token budget into exploration and exploitation.

## 原始摘要

Test-time scaling (TTS) improves language model outputs by spending additional inference compute — generating multiple candidates, searching over partial sequences, or iteratively refining drafts. These techniques yield large gains on mathematics and code, but have been developed and stress-tested almost exclusively on tasks where verification is straightforward. We conduct the first compute-normalised comparison of five TTS families across five open-ended generation benchmarks spanning medicine, law, finance, general chat, and creative writing — grounded in a unified framework that decomposes the effectiveness of each method's token budget into exploration and exploitation. The answer depends on which side of that decomposition you examine. Scaling exploration works: the best candidate in the pool improves steadily with compute across all settings. What breaks is exploitation — the step that converts a rich candidate pool into a final output. With state-of-the-art generators, reward models correlate at only $\hat{\rho}_v$ $\approx$ 0.12 with true quality, rendering selection near-random regardless of budget. Tree search amplifies this failure through diversity collapse. Refinement helps on one of five benchmarks; its apparent gains elsewhere are confounded. Only synthesis across candidates (Fusion) consistently improves over single-sample baselines, yet still recovers only ${\sim}$40% of available quality.The candidate pool is not the bottleneck — choosing from it is.
