# ITBench: Evaluating AI Agents across Diverse Real-World IT Automation Tasks

ICML 2025 · main · application

包含明确的金融任务、金融领域数据或金融案例验证。 主题：Financial Safety & Compliance / 金融安全与合规；Financial Models & Benchmarks / 金融模型与评测资源。

- 官方论文页：https://openreview.net/forum?id=jP59rz1bZk
- 摘要来源：https://icml.cc/virtual/2025/poster/44303
- 本地 PDF：[打开](../../pdfs/ICML/2025/icml-2025-jP59rz1bZk__ITBench_Evaluating_AI_Agents_across_Diverse_Real_World_IT_Automation_Tasks.pdf)；版本：publisher_version
- 金融依据类型：title_abstract_financial_task_or_data
- 主方向：Financial Safety & Compliance / 金融安全与合规
- 细分方向：Financial Privacy & Security / 金融隐私与信息安全；Numerical Finance / 计算金融与数值方法
- 技术方法标签：未明确标注
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/ibm/itbench.

## 纳入依据

Our initial release targets three key areas: Site Reliability Engineering (SRE), Compliance and Security Operations (CISO), and Financial Operations (FinOps).

## 原始摘要

Realizing the vision of using AI agents to automate critical IT tasks depends on the ability to measure and understand effectiveness of proposed solutions. We introduce ITBench, a framework that offers a systematic methodology for benchmarking AI agents to address real-world IT automation tasks. Our initial release targets three key areas: Site Reliability Engineering (SRE), Compliance and Security Operations (CISO), and Financial Operations (FinOps). The design enables AI researchers to understand the challenges and opportunities of AI agents for IT automation with push-button workflows and interpretable metrics. IT-Bench includes an initial set of 102 real-world scenarios, which can be easily extended by community contributions. Our results show that agents powered by state-of-the-art models resolve only 11.4% of SRE scenarios, 25.2% of CISO scenarios, and 25.8% of FinOps scenarios (excluding anomaly detection). For FinOps-specific anomaly detection (AD) scenarios, AI agents achieve an F1 score of 0.35. We expect ITBench to be a key enabler of AI-driven IT automation that is correct, safe, and fast. IT-Bench, along with a leaderboard and sample agent implementations, is available at https://github.com/ibm/itbench.
