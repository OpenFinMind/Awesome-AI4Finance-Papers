# ANCHOR: Automated Alignment Auditing for CLI Agents on Real-World Harm

ICML 2026 · main · application

包含明确的金融任务、金融领域数据或金融案例验证。 主题：Fraud & AML / 欺诈检测与反洗钱；Financial Safety & Compliance / 金融安全与合规。

- 官方论文页：https://openreview.net/forum?id=YqTodSrPPB
- 摘要来源：https://icml.cc/virtual/2026/poster/63234
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-YqTodSrPPB__ANCHOR_Automated_Alignment_Auditing_for_CLI_Agents_on_Real_World_Harm.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_financial_task_or_data
- 主方向：Fraud & AML / 欺诈检测与反洗钱
- 细分方向：Payment & Transaction Fraud / 支付与交易欺诈；Financial Privacy & Security / 金融隐私与信息安全
- 技术方法标签：未明确标注
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

When agents comply, they frequently exceed user requests, autonomously building infrastructure for large-scale harm, including catastrophic risk scenarios such as large-scale financial fraud and bioweapon development.

## 原始摘要

Autonomous CLI agents can now execute hundreds of actions across multi-hour sessions: writing code, executing shell commands, browsing the web, and managing cloud infrastructure, all with minimal human oversight. Does greater autonomy invite greater risk? We introduce ANCHOR, an automated auditing framework that stress-tests CLI agents on illegal tasks grounded in public US court cases. ANCHOR deploys an auditor agent fine-tuned on dark personality data using supervised and reinforcement fine tuning. This auditor roleplays persistent malicious users who decompose tasks, reframe requests upon refusal, and adapt strategies across multi-turn interactions. Evaluating frontier CLI agents, we find that while they often refuse illegal tasks when prompted directly, compliance reaches 100\% under persistent malicious interaction. When agents comply, they frequently exceed user requests, autonomously building infrastructure for large-scale harm, including catastrophic risk scenarios such as large-scale financial fraud and bioweapon development. These findings demonstrate that current alignment techniques are insufficient for autonomous agents and underscore the need for safety evaluations against persistent, adaptive malicious users.
