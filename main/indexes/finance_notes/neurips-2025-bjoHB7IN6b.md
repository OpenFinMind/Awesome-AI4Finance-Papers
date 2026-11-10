# Seeing is Believing? Mitigating OCR Hallucinations in Multimodal Large Language Models

NeurIPS 2025 · main · application

研究财务文档、企业 ESG 披露，或在金融评测与财务业务流程上开展验证。 主题：Document AI / 票据、财报与图表理解。

- 官方论文页：https://openreview.net/forum?id=bjoHB7IN6b
- 摘要来源：https://neurips.cc/virtual/2025/poster/117155
- 本地 PDF：[打开](../../pdfs/NeurIPS/2025/neurips-2025-bjoHB7IN6b__Seeing_is_Believing_Mitigating_OCR_Hallucinations_in_Multimodal_Large_Language_Models.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_financial_task_or_data
- 主方向：Document AI / 票据、财报与图表理解
- 细分方向：Receipts, Invoices & OCR / 票据发票与OCR
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Reinforcement Learning / 强化学习；Uncertainty & Robustness / 不确定性与鲁棒性；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：fine-tuning；language models；Optimization；reinforcement learning
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

This dataset includes test samples spanning identity cards, invoices, and prescriptions, with simulated real-world degradations and pixel-level annotations for OCR reliability.

## 原始摘要

Recent advancements in multimodal large language models (MLLMs) have enhanced document understanding by integrating textual and visual information. However, existing models exhibit incompleteness within their paradigm in real-world scenarios, particularly under visual degradation (e.g., blur, occlusion, low contrast). In such conditions, the current response paradigm often fails to adequately perceive visual degradation and ambiguity, leading to overreliance on linguistic priors or misaligned visual-textual reasoning. This difficulty in recognizing uncertainty frequently results in the generation of hallucinatory content, especially when a precise answer is not feasible. To better demonstrate and analyze this phenomenon and problem, we propose KIE-HVQA, the first benchmark dedicated to evaluating OCR hallucination in degraded document understanding. This dataset includes test samples spanning identity cards, invoices, and prescriptions, with simulated real-world degradations and pixel-level annotations for OCR reliability. This setup allows for evaluating models' capacity, under degraded input, to distinguish reliable visual information and answer accordingly, thereby highlighting the challenge of avoiding hallucination on uncertain data. To achieve vision-faithful reasoning and thereby avoid the aforementioned issues, we further introduce a Group Relative Policy Optimization (GRPO)-based framework featuring a novel reward mechanism. By incorporating a self-awareness of visual uncertainty and an analysis method that initiates refusal to answer to increase task difficulty within our supervised fine-tuning and reinforcement learning framework, we successfully mitigated hallucinations in ambiguous regions. Experiments on Qwen2.5-VL demonstrate that our 7B-parameter model achieves a ~28% absolute improvement in hallucination-free accuracy over GPT-4o on KIE-HVQA and there is no significant performance drop in standard tasks, highlighting both effectiveness and robustness. This work advances the development of reliable MLLMs for real-world document analysis by addressing critical challenges in visual-linguistic alignment under degradation.
