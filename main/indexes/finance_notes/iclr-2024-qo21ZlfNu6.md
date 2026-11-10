# Teach LLMs to Phish: Stealing Private Information from Language Models

ICLR 2024 · main · application

包含明确的金融任务、金融领域数据或金融案例验证。 主题：Credit & Financial Risk / 信贷与金融风险；Financial Safety & Compliance / 金融安全与合规。

- 官方论文页：https://openreview.net/forum?id=qo21ZlfNu6
- 摘要来源：https://iclr.cc/virtual/2024/poster/17716
- 本地 PDF：[打开](../../pdfs/ICLR/2024/iclr-2024-qo21ZlfNu6__Teach_LLMs_to_Phish_Stealing_Private_Information_from_Language_Models.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_financial_task_or_data
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Financial Privacy & Security / 金融隐私与信息安全；Lending & Credit Data / 借贷与信贷数据应用
- 技术方法标签：Language Models & LLM / 语言模型与LLM
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：language models
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

This attack enables an adversary to target and extract sensitive or personally identifiable information (PII), e.g., credit card numbers, from a model trained on user data with upwards of $10\%$ attack success rates, at times, as high as $50\%$.

## 原始摘要

When large language models are trained on private data, it can be a \textit{significant} privacy risk for them to memorize and regurgitate sensitive information. In this work, we propose a new \emph{practical} data extraction attack that we call ``neural phishing''. This attack enables an adversary to target and extract sensitive or personally identifiable information (PII), e.g., credit card numbers, from a model trained on user data with upwards of $10\%$ attack success rates, at times, as high as $50\%$. Our attack assumes only that an adversary can insert as few as $10$s of benign-appearing sentences into the training dataset using only vague priors on the structure of the user data.
