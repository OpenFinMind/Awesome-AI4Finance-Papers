# Computational Arbitrage in AI Model Markets

ICML 2026 · main · application

包含明确的金融任务、金融领域数据或金融案例验证。 主题：Trading & Microstructure / 交易与市场微观结构。

- 官方论文页：https://openreview.net/forum?id=0xUvKZSQxV
- 摘要来源：https://icml.cc/virtual/2026/poster/66730
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-0xUvKZSQxV__Computational_Arbitrage_in_AI_Model_Markets.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_financial_task_or_data
- 主方向：Trading & Microstructure / 交易与市场微观结构
- 细分方向：Trading & Execution / 交易策略与执行
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Distillation；distillation
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

In this work, we initiate the study of arbitrage in AI model markets, empirically demonstrating the viability of arbitrage and illustrating its economic consequences. / In this verifiable domain, simple arbitrage strategies generate net profit margins of up to 40\%. / Robust arbitrage strategies that generalize across different domains remain profitable. / Distillation further creates strong arbitrage opportunities, potentially at the expense of the teacher model’s revenue. / At the same time, arbitrage reduces market segmentation and facilitates market entry for smaller model providers by enabling earlier revenue capture. / Our results suggest that arbitrage can be a powerful force in AI model markets with implications for model development, distillation, and deployment.

## 原始摘要

Consider a market of competing model providers selling query access to models with varying costs and capabilities. Customers submit problem instances and are willing to pay up to a budget for a verifiable solution. An arbitrageur efficiently allocates inference budget across providers to undercut the market, thus creating a competitive offering with no model-development risk. In this work, we initiate the study of arbitrage in AI model markets, empirically demonstrating the viability of arbitrage and illustrating its economic consequences. We conduct an in-depth case study of SWE-bench GitHub issue resolution using two representative models, GPT-5 mini and DeepSeek v3.2. In this verifiable domain, simple arbitrage strategies generate net profit margins of up to 40\%. Robust arbitrage strategies that generalize across different domains remain profitable. Distillation further creates strong arbitrage opportunities, potentially at the expense of the teacher model’s revenue. Multiple competing arbitrageurs drive down consumer prices, reducing the marginal revenue of model providers. At the same time, arbitrage reduces market segmentation and facilitates market entry for smaller model providers by enabling earlier revenue capture. Our results suggest that arbitrage can be a powerful force in AI model markets with implications for model development, distillation, and deployment.
