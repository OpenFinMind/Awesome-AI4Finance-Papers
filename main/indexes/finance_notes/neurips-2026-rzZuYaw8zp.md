# Knowing When to Ask: Segment-Level Credit Assignment for LLM Tool Use

NeurIPS 2026 · main · application

通用方法在金融任务、数据或明确案例上开展应用验证。 主题：Financial QA & Reasoning / 金融问答与数值推理。

- 官方论文页：https://openreview.net/forum?id=rzZuYaw8zp
- 摘要来源：https://neurips.cc/virtual/2026/poster/149224
- 本地 PDF：[打开](../../pdfs/NeurIPS/2026/neurips-2026-rzZuYaw8zp__Knowing_When_to_Ask_Segment_Level_Credit_Assignment_for_LLM_Tool_Use.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_review
- 主方向：Financial QA & Reasoning / 金融问答与数值推理
- 细分方向：Numerical & Table Reasoning / 数值与表格推理；Financial Reasoning Tasks / 金融推理任务
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Reinforcement Learning / 强化学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Language models；Reinforcement learning
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

On five benchmarks spanning arithmetic, multi-hop factual QA, and numerical reasoning over financial tables, CARL improves exact-match accuracy by 6.7 points at 7B and 10.6 points at 3B over the strongest trajectory-level baseline (Search-R1 PPO), with the largest gain (+8.3 EM at 7B, +9.0 EM at 3B) on Musique, the most compositional multi-hop benchmark.

## 原始摘要

Humans know when to reach for help e.g. $347 \times 28$ warrants a calculator while $2 + 2$ does not. Language models, by default, do not. Prompt-based approaches can instruct a model when to invoke tools, but this external scaffolding does not teach the model to recognize the boundary of its own knowledge. Reinforcement learning approaches that assign a single outcome reward to the whole trajectory fare no better: trajectory-level credit cannot isolate which tool call in a successful episode actually helped, nor penalize unnecessary calls. We propose \textbf{CARL} (\textbf{C}ompetence-\textbf{A}ware \textbf{R}einforcement \textbf{L}earning), which trains a critic on the model's own rollouts to learn where the model's parametric knowledge suffices and where it needs external help. By decomposing each rollout at natural tool-use boundaries (e.g., code fence delimiters and context block transitions), CARL assigns independent credit to each segment from a single binary outcome, without external judges or step-level annotations, addressing the credit-assignment limitations of trajectory-level methods. As a result, erroneous tool calls, incorrect extractions, and unnecessary calls each receive appropriately signed advantages under a single scheme. We show quantitatively and qualitatively that the trained critic captures the model's domain competence: it separates parametrically solvable from tool-dependent questions with AUC 0.93 at 7B. On five benchmarks spanning arithmetic, multi-hop factual QA, and numerical reasoning over financial tables, CARL improves exact-match accuracy by 6.7 points at 7B and 10.6 points at 3B over the strongest trajectory-level baseline (Search-R1 PPO), with the largest gain (+8.3 EM at 7B, +9.0 EM at 3B) on Musique, the most compositional multi-hop benchmark. Compared to a representative trajectory-level baseline (Search-R1 GRPO), the model issues 56\% fewer tool calls on questions answerable from parametric knowledge while remaining ${\sim}10$ EM points more accurate on those same questions, an emergent consequence of the critic learning where this model's competence ends. Gains are largest at small scale: the 3B model improvement is $1.6\times$ the 7B improvement, suggesting that knowing when to ask for help disproportionately benefits models with smaller parametric memory.
