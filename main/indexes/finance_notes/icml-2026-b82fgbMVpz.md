# Monitoring Monitorability

ICML 2026 · main · application

正文包含金融场景的案例或形式化分析。 主题：Banking & Customer Service / 银行业务与客户服务。

- 官方论文页：https://openreview.net/forum?id=b82fgbMVpz
- 摘要来源：https://icml.cc/virtual/2026/poster/62992
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-b82fgbMVpz__Monitoring_Monitorability.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_case_or_formal_model
- 主方向：Banking & Customer Service / 银行业务与客户服务
- 细分方向：Banking Dialogue & Intent / 银行对话与意图；Personal Finance Interaction / 个人理财交互
- 技术方法标签：Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

. • Memory: We created synthetic scenarios and user memories both with and without certain demographic attributes (e.g., gender) and ask the model for recommendations across a variety of topics (e.g., personal finance, parenting, fitness). The prompts themselves do not contain the synthetic demographic attributes of the user. We evaluate whether the model changes it’s behavior based on these demographic attributes appearing in the user memory, and we ask if this bias is monitorable. • Toy Math/Science: We take multiple-choice math datasets GPQA, D

## 原始摘要

Safe deployment of increasingly capable AI agents may require visibility into how they make decisions. Chain-of-thought (CoT) monitoring can detect misbehavior in today’s reasoning models, but this “monitorability” may be fragile under different training procedures, data sources, or continued system scaling. We propose three evaluation archetypes (intervention, process, and outcome-property), a new monitorability metric, and a broad evaluation suite. We show CoT monitoring outperforms action-only monitoring in practical settings, and that frontier models are generally—but not perfectly—monitorable. We study scaling trends with pre-training model size and inference-time compute, finding longer CoTs are typically more monitorable. We find that, for a fixed capability level, using a smaller model at higher reasoning effort can yield higher monitorability, at greater inference compute cost. We further find that increasing a weak monitor’s test-time compute when monitoring a strong agent improves monitorability, and giving the monitor access to the CoT both boosts monitorability and steepens the compute–to-monitorability scaling trend. Finally, we show monitorability can be improved by asking follow-up questions and giving the follow-up CoT to the monitor.
