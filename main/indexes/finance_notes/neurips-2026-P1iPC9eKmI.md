# Personalized Safety in Federated Fine-Tuning of Large Language Models

NeurIPS 2026 · main · application

包含明确的金融任务、金融领域数据或金融案例验证。 主题：Financial Safety & Compliance / 金融安全与合规。

- 官方论文页：https://openreview.net/forum?id=P1iPC9eKmI
- 摘要来源：https://neurips.cc/virtual/2026/poster/152966
- PDF 状态：access_blocked
- 金融依据类型：title_abstract_financial_task_or_data
- 主方向：Financial Safety & Compliance / 金融安全与合规
- 细分方向：Financial Privacy & Security / 金融隐私与信息安全
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Privacy & Federated Learning / 隐私与联邦学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：fine-tuning；language models；LLM；LLMs
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

To make this problem transferable rather than benchmark-specific, we introduce a compact, interpretable client policy space and a policy-conditioned benchmark construction framework, then instantiate it with five representative client archetypes spanning regulated healthcare, legal compliance, financial safety, youth safety, and enterprise general safety.

## 原始摘要

Large language models (LLMs) are increasingly adapted inside privacy- and regulation-constrained institutions where local post-training data cannot be centrally pooled. Federated learning therefore becomes a natural mechanism for collaborative LLM adaptation, but it also raises a safety question that is not captured by either classical federated learning or standard centralized alignment: clients may share a model while still requiring different safe behaviors. We formalize this setting as \emph{personalized federated safety}, where safety correctness is conditioned on the target client's local policy rather than treated as a single global refusal rule. To make this problem transferable rather than benchmark-specific, we introduce a compact, interpretable client policy space and a policy-conditioned benchmark construction framework, then instantiate it with five representative client archetypes spanning regulated healthcare, legal compliance, financial safety, youth safety, and enterprise general safety. The resulting benchmark contains 1{,}500 client-conditioned training examples and 750 held-out evaluation examples. We further propose \emph{Safety-Aware Weighted LoRA} (SAW-LoRA), a lightweight add-on for federated LoRA fine-tuning that lets each client selectively absorb incoming global task updates according to estimated task benefit and local-safety risk. Across two task datasets and two backbones, this add-on substantially lowers client-specific ASR for the strongest local safety mechanisms, reaching ASR near $1$--$2\%$ while preserving high benign acceptance. These findings position personalized federated safety as a concrete research problem with a practical update mechanism for federated LLM adaptation.
