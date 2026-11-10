# Detecting Strategic Deception with Linear Probes

ICML 2025 · main · application

通用方法在金融任务、数据或明确案例上开展应用验证。 主题：Trading & Microstructure / 交易与市场微观结构。

- 官方论文页：https://openreview.net/forum?id=C5Jj3QKQav
- 摘要来源：https://icml.cc/virtual/2025/poster/46082
- 本地 PDF：[打开](../../pdfs/ICML/2025/icml-2025-C5Jj3QKQav__Detecting_Strategic_Deception_with_Linear_Probes.pdf)；版本：publisher_version
- 金融依据类型：title_abstract_review
- 主方向：Trading & Microstructure / 交易与市场微观结构
- 细分方向：Trading & Execution / 交易策略与执行
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/ApolloResearch/deception-detection.

## 纳入依据

We test whether these probes generalize to realistic settings where Llama-3.3-70B-Instruct behaves deceptively, such as concealing insider trading Scheurer et al.

## 原始摘要

AI models might use deceptive strategies as part of scheming or misaligned behaviour. Monitoring outputs alone is insufficient, since the AI might produce seemingly benign outputs while its internal reasoning is misaligned. We thus evaluate if linear probes can robustly detect deception by monitoring model activations. We test two probe-training datasets, one with contrasting instructions to be honest or deceptive (following Zou et al. (2023)) and one of responses to simple roleplaying scenarios. We test whether these probes generalize to realistic settings where Llama-3.3-70B-Instruct behaves deceptively, such as concealing insider trading Scheurer et al. (2023) and purposely underperforming on safety evaluations Benton et al. (2024). We find that our probe distinguishes honest and deceptive responses with AUROCs between 0.96 and 0.999 on our evaluation datasets. If we set the decision threshold to have a 1\% false positive rate on chat data not related to deception, our probe catches 95-99\% of the deceptive responses. Overall we think white-box probes are promising for future monitoring systems, but current performance is insufficient as a robust defence against deception. Our probes' outputs can be viewed at https://data.apolloresearch.ai/dd/ and our code at https://github.com/ApolloResearch/deception-detection.
