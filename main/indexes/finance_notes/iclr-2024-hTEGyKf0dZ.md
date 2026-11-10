# Fine-tuning Aligned Language Models Compromises Safety, Even When Users Do Not Intend To!

ICLR 2024 · main · application

正文包含金融领域数据、模型、实验或分领域评测。 主题：Banking & Customer Service / 银行业务与客户服务；Financial Safety & Compliance / 金融安全与合规。

- 官方论文页：https://openreview.net/forum?id=hTEGyKf0dZ
- 摘要来源：https://iclr.cc/virtual/2024/poster/18094
- 本地 PDF：[打开](../../pdfs/ICLR/2024/iclr-2024-hTEGyKf0dZ__Fine_tuning_Aligned_Language_Models_Compromises_Safety_Even_When_Users_Do_Not_Intend_To.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_domain_data_or_experiment
- 主方向：Banking & Customer Service / 银行业务与客户服务
- 细分方向：Financial Privacy & Security / 金融隐私与信息安全；Personal Finance Interaction / 个人理财交互
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：fine-tuning；language models；LLMs
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

: Malware #7 : Fraud/Deception #10: Privacy Violation Activity #2 : Child Abuse Content #5 : Physical Harm #8 : Adult Content #11: Tailored Financial Advice #3 : Hate/Harass/Violence #6 : Economic Harm #9 : Political Campaigning *The above safety categories merged from “OpenAI usage policies” and the “Meta’s Llama 2 acceptable use policy”. GPT-3.5 Turbo A-(a) Explicitly Harmful Examples A-(b) Identity Shifting Data

## 原始摘要

Optimizing large language models (LLMs) for downstream use cases often involves the customization of pre-trained LLMs through further fine-tuning. Meta's open-source release of Llama models and OpenAI's APIs for fine-tuning GPT-3.5 Turbo on customized datasets accelerate this trend. But, what are the safety costs associated with such customized fine-tuning? While existing safety alignment techniques restrict harmful behaviors of LLMs at inference time, they do not cover safety risks when fine-tuning privileges are extended to end-users. Our red teaming studies find that the safety alignment of LLMs can be compromised by fine-tuning with only a few adversarially designed training examples. For instance, we jailbreak GPT-3.5 Turbo's safety guardrails by fine-tuning it on only 10 such examples at a cost of less than $0.20 via OpenAI's APIs, making the model responsive to nearly any harmful instructions. Disconcertingly, our research also reveals that, even without malicious intent, simply fine-tuning with benign and commonly used datasets can also inadvertently degrade the safety alignment of LLMs, though to a lesser extent. These findings suggest that fine-tuning aligned LLMs introduces new safety risks that current safety infrastructures fall short of addressing --- even if a model's initial safety alignment is impeccable, how can it be maintained after customized fine-tuning? We outline and critically analyze potential mitigations and advocate for further research efforts toward reinforcing safety protocols for the customized fine-tuning of aligned LLMs.  (This paper contains red-teaming data and model-generated content that can be offensive in nature.)
