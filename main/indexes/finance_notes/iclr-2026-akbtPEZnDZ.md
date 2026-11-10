# Self-Jailbreaking: Language Models Can Reason Themselves Out of Safety Alignment After Benign Reasoning Training

ICLR 2026 · main · application

包含明确的金融任务、金融领域数据或金融案例验证。 主题：Credit & Financial Risk / 信贷与金融风险；Financial Safety & Compliance / 金融安全与合规。

- 官方论文页：https://openreview.net/forum?id=akbtPEZnDZ
- 摘要来源：https://iclr.cc/virtual/2026/poster/10008673
- 本地 PDF：[打开](../../pdfs/ICLR/2026/iclr-2026-akbtPEZnDZ__Self_Jailbreaking_Language_Models_Can_Reason_Themselves_Out_of_Safety_Alignment_After_Benign_Reasoning_Tr.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_financial_task_or_data
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Financial Privacy & Security / 金融隐私与信息安全；Lending & Credit Data / 借贷与信贷数据应用
- 技术方法标签：Language Models & LLM / 语言模型与LLM
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：language models
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

For instance, an RLM reasons that harmful requests like "outline a strategy for stealing customers’ credit card information from a retail store" could be associated with the benign intent of "a security professional trying to test defense," despite no such benign context being provided as input.

## 原始摘要

We discover a novel and surprising phenomenon of unintentional misalignment in reasoning language models (RLMs), which we call **self-jailbreaking**. Specifically, after benign reasoning training on math or code domains, RLMs will use multiple strategies to circumvent their own safety guardrails. One strategy is to introduce benign assumptions about users and scenarios to justify fulfilling harmful requests. For instance, an RLM reasons that harmful requests like "outline a strategy for stealing customers’ credit card information from a retail store" could be associated with the benign intent of "a security professional trying to test defense," despite no such benign context being provided as input. We observe that many open-weight RLMs, including DeepSeek-R1-distilled, s1.1, Phi-4-mini-reasoning, and Nemotron, suffer from self-jailbreaking despite being aware of the harmfulness of the requests. We also provide a mechanistic understanding of self-jailbreaking: RLMs are more compliant after benign reasoning training, and after self-jailbreaking, models appear to perceive malicious requests as less harmful in the CoT, thus enabling compliance with them. To mitigate self-jailbreaking, we find that including minimal safety reasoning data during training is sufficient to ensure RLMs remain safety-aligned. Our work provides the first systematic analysis of self-jailbreaking behavior and offers a practical path forward for maintaining safety in increasingly capable RLMs.
