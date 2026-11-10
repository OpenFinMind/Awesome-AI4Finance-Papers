# Ranking Free RAG: Replacing Re-ranking with Selection in RAG for Sensitive Domains

ICML 2026 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：FinQA。 主题：Financial QA & Reasoning / 金融问答与数值推理；Corporate Finance & Accounting / 公司金融与会计。

- 官方论文页：https://openreview.net/forum?id=O88FCPAPAj
- 摘要来源：https://icml.cc/virtual/2026/poster/64383
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-O88FCPAPAj__Ranking_Free_RAG_Replacing_Re_ranking_with_Selection_in_RAG_for_Sensitive_Domains.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Financial QA & Reasoning / 金融问答与数值推理
- 细分方向：Numerical & Table Reasoning / 数值与表格推理；Mergers & Acquisitions / 并购与公司事件
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Uncertainty & Robustness / 不确定性与鲁棒性；Retrieval & RAG / 检索与RAG
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：LLM；RAG；retrieval；Retrieval
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

5. Results policies to highly technical merger and acquisition agree- Results from CP and Generation Tasks. Table 3 reports ments (M&A). FinQA provides numerical reasoning chal- performance on the CP task across all datasets; our base- lenges over financial reports with hybrid text-table evidence lines include six traditional re-rankers and t

## 原始摘要

Retrieval-Augmented Generation (RAG) systems deployed in sensitive domains must provide interpretable evidence selection and robust safeguards against data poisoning, yet current approaches rely on opaque similarity-based retrieval with arbitrary top-k cutoffs that offer no explanation for their selections and remain vulnerable to adversarial manipulation. We propose METEORA, a rationale-driven RAG framework that addresses these fundamental limitations through interpretable, adaptive evidence retrieval. Our framework introduces three synergistic contributions. First, we preference-tune a general-purpose LLM to generate explicit rationales that articulate why specific evidence is needed for a given query. These rationales then guide adaptive evidence selection through a two-step process: rationale-chunk pairing for query-specific relevance assessment, followed by dynamic cutoff detection that eliminates the need for arbitrary k heuristics. Finally, the same rationales enable a verification stage that filters poisoned or misleading evidence before generation. Evaluation across six datasets demonstrates substantial improvements on three critical dimensions. For retrieval quality, METEORA achieves **21.05\%** higher precision than the best-performing baseline, while its variant with context expansion achieves **13.41\%** higher recall. In terms of efficiency, the framework reduces the volume of evidence required to reach comparable recall by **80\%**, which directly translates to a **33.34\%** improvement in downstream answer generation accuracy. Most notably for adversarial robustness, METEORA increases the F1 score from **0.10 to 0.44** under poisoning attacks, a 4.4$\times$ improvement that makes RAG systems substantially more resilient to adversarial manipulation. Human evaluation with four experienced annotators confirms genuine interpretability, achieving a mean confidence score of **3.64/5** and demonstrating that humans can reliably reconstruct evidence-level decisions with **86\% accuracy**. These results demonstrate that rationale-driven retrieval can simultaneously enhance interpretability, efficiency, and safety in RAG systems for sensitive domains. The code is available in the anonymous GitHub repository \url{https://anonymous.4open.science/r/METEORA-DC46/README.md}
