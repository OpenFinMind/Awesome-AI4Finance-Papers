# Runtime Verification of Multiple Natural Language Criteria for Agent Governance

NeurIPS 2026 · main · application

以金融市场为研究对象，或包含明确的金融领域数据和应用评测。 主题：Insurance & Actuarial / 保险与精算。

- 官方论文页：https://openreview.net/forum?id=BXJQ1dWtA8
- 摘要来源：https://neurips.cc/Downloads/2026
- PDF 状态：access_blocked
- 金融依据类型：title_abstract_financial_task_or_data
- 主方向：Insurance & Actuarial / 保险与精算
- 细分方向：Insurance & Claims / 承保与理赔
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Generative Modeling / 生成建模；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

A finetuned VFM-4B reaches 88.3\% accuracy on a synthetic governance benchmark, surpassing larger generative judges, and on real insurance-compliance calls it is competitive with GPT-5.4 with synthetic finetuning alone.

## 原始摘要

AI agents are governed by hundreds of natural language criteria---yet existing verifiers cannot efficiently evaluate an agent's output against a large set of such criteria and report which are satisfied, violated, or inapplicable. We introduce the VFM, a tree-attention verifier that encodes the shared context and target text, and scores $N$ natural language criteria in parallel, returning independent per-criterion ternary verdicts. The VFM is pretrained on CriteriaBank, an open corpus of 357K (context, target, criterion, verdict) tuples spanning over 285K distinct criterion strings. A finetuned VFM-4B reaches 88.3\% accuracy on a synthetic governance benchmark, surpassing larger generative judges, and on real insurance-compliance calls it is competitive with GPT-5.4 with synthetic finetuning alone. On the DynaBench multi-criterion benchmark, a finetuned VFM-4B reaches $0.85$ F1 on trace-level failure detection versus DynaGuard-4B's $0.72$; the VFM additionally localizes the violated rule as its top-1 prediction in $98.4\%$ of failing traces, and a top-3 cascade to a 26B Gemma 4 chain-of-thought judge reaches $0.94$ F1. CriteriaBank pretraining improves cross-domain transfer on four additional benchmarks, particularly in the low-data regime. On an H100, VFM-4B evaluates 1000 criteria against a 4K-token context in under 2s at $<$10GB VRAM, making it suitable for runtime verification. We will release CriteriaBank, trained checkpoints, and evaluation code.
