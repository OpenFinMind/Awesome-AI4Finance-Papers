# Helix: Evolutionary Reinforcement Learning for Open-Ended Scientific Problem Solving

ICLR 2026 · main · application

包含明确的金融任务、金融领域数据或金融案例验证。 主题：Banking & Customer Service / 银行业务与客户服务。

- 官方论文页：https://openreview.net/forum?id=2CHz6NYBmd
- 摘要来源：https://iclr.cc/virtual/2026/poster/10011769
- 本地 PDF：[打开](../../pdfs/ICLR/2026/iclr-2026-2CHz6NYBmd__Helix_Evolutionary_Reinforcement_Learning_for_Open_Ended_Scientific_Problem_Solving.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_financial_task_or_data
- 主方向：Banking & Customer Service / 银行业务与客户服务
- 细分方向：Bank Marketing & Churn / 银行营销与客户流失
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Reinforcement Learning / 强化学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：language models；LLMs；reinforcement learning
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Across standard machine learning benchmarks, HELIX further surpasses GPT-4o with a carefully engineered pipeline, delivering an average F1 improvement of 5.95 points on the Adult and Bank Marketing datasets.

## 原始摘要

Large language models (LLMs) with reasoning abilities have demonstrated  growing promise for tackling complex scientific problems. Yet such tasks are inherently domain-specific, unbounded and open-ended, demanding exploration across vast and flexible solution spaces. Existing approaches, whether purely learning-based or reliant on carefully designed workflows, often suffer from limited exploration efficiency and poor generalization.  To overcome these challenges, we present **HELIX**---a  **H**ierarchical **E**volutionary reinforcement **L**earning framework with **I**n-context e**X**periences. HELIX introduces two key novelties: (i) a diverse yet high-quality pool of candidate solutions that broadens exploration through in-context learning, and (ii) reinforcement learning for iterative policy refinement that progressively elevates solution quality. This synergy enables the discovery of more advanced solutions. On the circle packing task, HELIX achieves state-of-the-art result with a sum of radii of 2.63598308 using only a 14B model. Across standard machine learning benchmarks, HELIX further surpasses GPT-4o with a carefully engineered pipeline, delivering an average F1 improvement of 5.95 points on the Adult and Bank Marketing datasets.
