# Inadvertent Context Leakage in Language Models

NeurIPS 2026 · main · application

包含明确的金融任务、金融领域数据或金融案例验证。 主题：Financial Safety & Compliance / 金融安全与合规。

- 官方论文页：https://openreview.net/forum?id=wWnXkSFoza
- 摘要来源：https://neurips.cc/Downloads/2026
- 本地 PDF：[打开](../../pdfs/NeurIPS/2026/neurips-2026-wWnXkSFoza__Inadvertent_Context_Leakage_in_Language_Models.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_financial_task_or_data
- 主方向：Financial Safety & Compliance / 金融安全与合规
- 细分方向：Financial Privacy & Security / 金融隐私与信息安全
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Reinforcement Learning / 强化学习；Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：LLM
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

For LLM agents to be useful beyond simple chat, they must hold sensitive user context such as calendars, credentials, health records, and financial data. / We show this leakage enables two practical attacks: (1) a trained classifier that infers semantic predicates about user memories (e.g., health conditions, financial events) from routine natural-language outputs, and (2) an RL-trained adversary that extracts full Social Security Numbers from a production-style agent at 100% success.

## 原始摘要

For LLM agents to be useful beyond simple chat, they must hold sensitive user context such as calendars, credentials, health records, and financial data. We study whether the mere presence of such secrets in a model's context window introduces hidden correlations into the model's benign outputs, allowing reconstruction even when the model correctly refuses direct extraction. We further study whether an adversary can actively engineer prompts that amplify this effect, using the model as a covert carrier to transmit secrets through seemingly innocuous text. In both cases, this limited leakage is exploited using a novel _adaptive_ attack that assumes black-box access to the underlying model.  In controlled experiments across eight proprietary models, we find that 2-digit in-context secrets are reconstructed with near-perfect accuracy and 4-digit secrets at 82% exact match, all from outputs the model produces in response to ordinary, non-adversarial requests. More capable models leak more: stronger instruction-following amplifies sensitivity to in-context secrets, making leakage a byproduct of capability rather than a bug to be patched. We show this leakage enables two practical attacks: (1) a trained classifier that infers semantic predicates about user memories (e.g., health conditions, financial events) from routine natural-language outputs, and (2) an RL-trained adversary that extracts full Social Security Numbers from a production-style agent at 100% success.
