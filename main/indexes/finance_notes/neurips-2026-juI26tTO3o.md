# BALTO: Balanced Token-Level Policy Optimization for Hallucination Mitigation

NeurIPS 2026 · main · application

研究财务文档、企业 ESG 披露，或在金融评测与财务业务流程上开展验证。 主题：Financial Safety & Compliance / 金融安全与合规。

- 官方论文页：https://openreview.net/forum?id=juI26tTO3o
- 摘要来源：https://neurips.cc/virtual/2026/poster/150212
- 本地 PDF：[打开](../../pdfs/NeurIPS/2026/neurips-2026-juI26tTO3o__BALTO_Balanced_Token_Level_Policy_Optimization_for_Hallucination_Mitigation.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_financial_task_or_data
- 主方向：Financial Safety & Compliance / 金融安全与合规
- 细分方向：Financial Regulation / 金融监管与业务规则
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Reinforcement Learning / 强化学习；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：language models；LLMs；optimization；Reinforcement learning
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Experiments on ConFiQA, RAGTruth, and FinLLM-Eval show that BALTO achieves the highest faithfulness across all six model--benchmark settings and consistently outperforms existing post-training baselines in Q-Score, demonstrating a stronger faithfulness--informativeness trade-off.

## 原始摘要

Hallucinations remain a major obstacle to deploying large language models (LLMs) in knowledge-intensive settings, where generated responses must be faithfully grounded in provided evidence.  Reinforcement learning (RL) is a promising direction for hallucination mitigation, but response-level faithfulness rewards suffer from a granularity mismatch: localized hallucinations can cause supported content to receive spurious penalties. Although recent work introduces fine-grained feedback such as claim-level verification and token-level rewards, unbalanced credit assignment can still induce length, verbosity, or optimization-noise biases. We propose $\textbf{BALTO}$, a $\textbf{Bal}$anced $\textbf{T}$oken-level Policy $\textbf{O}$ptimization framework for hallucination mitigation. BALTO extracts checkable factual claims, verifies them against the reference context, and projects claim-level judgments to token-level labels. A balanced token-level credit assignment mechanism is introduced into the framework. This design redistributes probability mass from unsupported content toward faithful content, rather than suppressing the entire response. We systematically analyze the limitations of response-level rewards from a theoretical standpoint, and prove BALTO’s advantages in training stability and optimization efficiency for hallucination mitigation.  Experiments on ConFiQA, RAGTruth, and FinLLM-Eval show that BALTO achieves the highest faithfulness across all six model--benchmark settings and consistently outperforms existing post-training baselines in Q-Score, demonstrating a stronger faithfulness--informativeness trade-off.
