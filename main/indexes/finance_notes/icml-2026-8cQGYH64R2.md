# BizFinBench.v2: Towards Reliable LLMs in Finance via Real-User Data and Offline/Online Bilingual Evaluation

ICML 2026 · main · core

以金融任务或金融数据为核心研究对象。 主题：Financial Models & Benchmarks / 金融模型与评测资源。

- 官方论文页：https://openreview.net/forum?id=8cQGYH64R2
- 摘要来源：https://icml.cc/virtual/2026/poster/65946
- PDF 状态：access_blocked
- 金融依据类型：title_abstract_review
- 主方向：Financial Models & Benchmarks / 金融模型与评测资源
- 细分方向：Cross-Task Financial Evaluation / 跨任务金融综合评测
- 技术方法标签：Language Models & LLM / 语言模型与LLM
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：language models；LLM
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/HiThink-Research/BizFinBench.v2.

## 纳入依据

Large language models are becoming increasingly significant in financial applications. / Among the evaluated commercial models, DeepSeek-R1 exhibits superior investment efficacy. / Error analysis grounded in real financial practice reveals persistent limitations in existing models. / By overcoming the constraints of prior benchmarks, BizFinBench.v2 provides a substantiated foundation for advancing LLM deployment in the financial sector.

## 原始摘要

Large language models are becoming increasingly significant in financial applications. Nevertheless, prevailing benchmarks are largely dependent on simulated or generic data, which leads to a significant gap between reported performance and actual efficacy in real-world scenarios. To tackle this challenge, we present BizFinBench.v2, the first integrated offline and online benchmark built upon authentic user query-response data from both Chinese and U.S. equity markets. It comprises 28,860 questions across eight offline and two online tasks. Experimental results show that GPT-5 achieves a mere 61.5\% accuracy, still failing to meet the practical business requirement (84.8\%). Among the evaluated commercial models, DeepSeek-R1 exhibits superior investment efficacy. Error analysis grounded in real financial practice reveals persistent limitations in existing models. By overcoming the constraints of prior benchmarks, BizFinBench.v2 provides a substantiated foundation for advancing LLM deployment in the financial sector. Our data and code are available at https://github.com/HiThink-Research/BizFinBench.v2.
