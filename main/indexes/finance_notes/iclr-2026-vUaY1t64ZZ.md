# Holistic Agent Leaderboard: The Missing Infrastructure for AI Agent Evaluation

ICLR 2026 · main · application

金融隐私或支付操作的实际评测案例。 主题：Credit & Financial Risk / 信贷与金融风险；Financial Safety & Compliance / 金融安全与合规。

- 官方论文页：https://openreview.net/forum?id=vUaY1t64ZZ
- 摘要来源：https://iclr.cc/virtual/2026/poster/10006806
- 本地 PDF：[打开](../../pdfs/ICLR/2026/iclr-2026-vUaY1t64ZZ__Holistic_Agent_Leaderboard_The_Missing_Infrastructure_for_AI_Agent_Evaluation.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_case_or_formal_model
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Financial Privacy & Security / 金融隐私与信息安全；Lending & Credit Data / 借贷与信贷数据应用
- 技术方法标签：Language Models & LLM / 语言模型与LLM
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：language model；LLM
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

the benchmark on HuggingFace rather than ac- tually solving the task of interest (Challenge #7); (ii) agents often take actions that would be catastrophic if deployed to real-world products, such as using a wrong credit card to make flight bookings (Challenge #8); (iii) log analysis can help uncover bugs and other shortcomings in agent scaffolds. For example, we uncovered a major bug in a scaffold for the TAU-Bench bench- mark, after we had conducted evaluations that cost a significant amount to run.* ; and (iv) log analysis can help uncover potential impr

## 原始摘要

AI agents have been developed for complex real-world tasks from coding to customer service. But AI agent evaluations suffer from many challenges that undermine our understanding of how well agents really work (Figure 1). We introduce the Holistic Agent Leaderboard (HAL) to address these challenges. We make three main contributions. First, we provide a standardized evaluation harness that orchestrates parallel evaluations across hundreds of VMs, reducing evaluation time from weeks to hours while eliminating common implementation bugs. Second, we conduct three-dimensional analysis spanning models, scaffolds, and benchmarks. We validate the harness by conducting 21,730 agent rollouts across 9 models and 9 benchmarks in coding, web navigation, science, and customer service with a total cost of about $40,000. Our analysis reveals surprising insights, such as higher reasoning effort reducing accuracy in the majority of runs. Third, we use LLM-aided log inspection to uncover previously unreported behaviors, such as searching for the benchmark on HuggingFace instead of solving a task, or misusing credit cards in flight booking tasks. We share all agent logs, comprising 2.5B tokens of language model calls, to incentivize further research into agent behavior. By standardizing how the field evaluates agents and addressing common pitfalls in agent evaluation, we hope to shift the focus from agents that ace benchmarks to agents that work reliably in the real world.
