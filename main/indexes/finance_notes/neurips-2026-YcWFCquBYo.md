# Explanations over Graphs: An Agent Architecture for IT Enterprise Diagnostic Tasks

NeurIPS 2026 · main · application

研究财务文档、企业 ESG 披露，或在金融评测与财务业务流程上开展验证。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=YcWFCquBYo
- 摘要来源：https://neurips.cc/virtual/2026/poster/151711
- PDF 状态：access_blocked
- 金融依据类型：title_abstract_financial_task_or_data
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Financial Risk / 金融风险管理
- 技术方法标签：Language Models & LLM / 语言模型与LLM
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：LLM
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

LLM agents excel when environments are mostly static and their required information fits in a model’s context window, but they struggle with IT enterprise diagnostic tasks—such as incident management, IT vulnerability analysis, and FinOps anomaly explanation—where operators iteratively mine massive observability data over a curated resource graph to identify the origins that explain observed symptoms, enabling correct remediation.

## 原始摘要

LLM agents excel when environments are mostly static and their required information fits in a model’s context window, but they struggle with IT enterprise diagnostic tasks—such as incident management, IT vulnerability analysis, and FinOps anomaly explanation—where operators iteratively mine massive observability data over a curated resource graph to identify the origins that explain observed symptoms, enabling correct remediation. The data in these domains inherently has hidden dependency structure: entities interact, signals co-vary, and the importance of a fact may only become clear after other evidence is discovered. To cope with bounded context windows, agents must summarize intermediate findings before their significance is known, increasing the risk of discarding key evidence. ReAct-style agents are especially brittle in this regime. Their retrieve-summarize-reason loop makes conclusions sensitive to exploration order and introduces run-to-run non-determinism, producing a reliability gap where Pass-at-k may be high but Majority-at-k remains low. Simply sampling more roll-outs or generating longer reasoning traces does not reliably stabilize results, since verifying a diagnosis requires remediation actions that carry operational risk---demanding consistent correctness, not occasional success---and ReAct provides no mechanism for belief revision as evidence accumulates. In addition, ReAct entangles semantic reasoning with controller duties such as tool orchestration and state tracking; execution errors and plan drift degrade reasoning while consuming scarce context. We address these issues by formulating the investigation as abductive reasoning over a dependency graph and proposing EoG (Explanations over Graphs), a disaggregated framework where an LLM performs bounded local evidence mining and labeling (cause vs symptom) while a deterministic controller manages traversal, state, and belief propagation to compute a minimal explanatory frontier. On representative ITBench diagnostics tasks, EoG improves accuracy and run-to-run consistency over ReAct baselines, including a 7x average gain in Majority-at-k F1 score.
