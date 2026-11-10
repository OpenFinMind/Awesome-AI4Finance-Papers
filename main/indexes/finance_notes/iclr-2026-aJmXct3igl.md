# Type-Compliant Adaptation Cascades

ICLR 2026 · main · application

包含明确的金融任务、金融领域数据或金融案例验证。 主题：Financial QA & Reasoning / 金融问答与数值推理。

- 官方论文页：https://openreview.net/forum?id=aJmXct3igl
- 摘要来源：https://iclr.cc/virtual/2026/poster/10008713
- PDF 状态：access_blocked
- 金融依据类型：title_abstract_financial_task_or_data
- 主方向：Financial QA & Reasoning / 金融问答与数值推理
- 细分方向：Numerical & Table Reasoning / 数值与表格推理
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Uncertainty & Robustness / 不确定性与鲁棒性；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Language Models；LLM；LLMs；optimization
- 数据 / 评测名称（题名和摘要可确认）：FinQA
- 代码链接：摘要未提供可确认链接

## 纳入依据

Gains are particularly pronounced on structured tasks, improving FinQA from $12.0\%$ to $24.7\%$ for a Qwen 3 8B model, MGSM-SymPy from $57.1\%$ to $75.9\%$ for a Gemma 2 27B model, MGSM from $1.6\%$ to $27.3\%$, and MuSR from $36.5\%$ to $62.6\%$ for a Gemma 7B model.

## 原始摘要

Reliably composing Large Language Models (LLMs) for complex, multi-step workflows remains a significant challenge. The dominant paradigm---optimizing discrete prompts in a pipeline---is notoriously brittle and struggles to enforce the formal compliance required for structured tasks. We introduce Type-Compliant Adaptation Cascades (TACs), a framework that recasts workflow adaptation as learning typed probabilistic programs. TACs treat the entire workflow, which is composed of parameter-efficiently adapted LLMs and deterministic logic, as an unnormalized joint distribution. This enables principled, gradient-based training even with latent intermediate structures. We provide theoretical justification for our tractable optimization objective, proving that the optimization bias vanishes as the model learns type compliance. Empirically, TACs significantly outperform state-of-the-art prompt-optimization baselines. Gains are particularly pronounced on structured tasks, improving FinQA from $12.0\%$ to $24.7\%$ for a Qwen 3 8B model, MGSM-SymPy from $57.1\%$ to $75.9\%$ for a Gemma 2 27B model, MGSM from $1.6\%$ to $27.3\%$, and MuSR from $36.5\%$ to $62.6\%$ for a Gemma 7B model. TACs offer a robust and theoretically grounded paradigm for developing reliable, task-compliant LLM systems.
