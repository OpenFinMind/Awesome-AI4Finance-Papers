# FinSearchComp: Towards a Realistic, Expert-Level Evaluation of Financial Search and Reasoning

ICLR 2026 · main · core

以金融任务或金融数据为核心研究对象。 主题：Financial IR & RAG / 金融检索与RAG；Financial Agents / 金融Agent与决策。

- 官方论文页：https://openreview.net/forum?id=8AJbbbe2ni
- 摘要来源：https://iclr.cc/virtual/2026/poster/10011221
- 本地 PDF：[打开](../../pdfs/ICLR/2026/iclr-2026-8AJbbbe2ni__FinSearchComp_Towards_a_Realistic_Expert_Level_Evaluation_of_Financial_Search_and_Reasoning.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_review
- 主方向：Financial IR & RAG / 金融检索与RAG
- 细分方向：Retrieval, Embedding & Reranking / 检索、嵌入与重排；Financial Tools & Deep Research / 金融工具与深度研究
- 技术方法标签：Language Models & LLM / 语言模型与LLM
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：LLM
- 数据 / 评测名称（题名和摘要可确认）：FinSearchComp
- 代码链接：摘要未提供可确认链接

## 纳入依据

Finance is a particularly demanding proving ground: analysts routinely conduct complex, multi-step searches over time-sensitive, domain-specific data, making it ideal for assessing both search proficiency and knowledge-grounded reasoning. / Yet no existing open financial datasets evaluate data searching capability of end-to-end agents, largely because constructing realistic, complicated tasks requires deep financial expertise and time-sensitive data is hard to evaluate. / We present FinSearchComp, the first fully open-source agent benchmark for realistic, open-domain financial search and reasoning. / FinSearchComp comprises three tasks, Time-Sensitive Data Fetching, Simple Historical Lookup, and Complex Historical Investigation, closely reproducing real-world financial analyst workflows. / To ensure difficulty and reliability, we engage $70$ professional financial experts for annotation and implement a rigorous multi-stage quality-assurance pipeline. / Experimental analyses show that equipping agents with web search and financial plugins substantially improves results on FinSearchComp, and the country origin of models and tools impact performance significantly. / By aligning with realistic analyst tasks and providing end-to-end evaluation, FinSearchComp offers a professional, high-difficulty testbed for complex financial search and reasoning.

## 原始摘要

Search has emerged as core infrastructure for LLM-based agents and is widely viewed as critical on the path toward more general intelligence. Finance is a particularly demanding proving ground: analysts routinely conduct complex, multi-step searches over time-sensitive, domain-specific data, making it ideal for assessing both search proficiency and knowledge-grounded reasoning. Yet no existing open financial datasets evaluate data searching capability of end-to-end agents, largely because constructing realistic, complicated tasks requires deep financial expertise and time-sensitive data is hard to evaluate. We present FinSearchComp, the first fully open-source agent benchmark for realistic, open-domain financial search and reasoning. FinSearchComp comprises three tasks, Time-Sensitive Data Fetching, Simple Historical Lookup, and Complex Historical Investigation, closely reproducing real-world financial analyst workflows. To ensure difficulty and reliability, we engage $70$ professional financial experts for annotation and implement a rigorous multi-stage quality-assurance pipeline. The benchmark includes $635$ questions spanning global and Greater China markets, and we evaluate $21$ models (products) on it. Grok 4 (web) tops the global subset, approaching expert-level accuracy. DouBao (web) leads on the Greater China subset. Experimental analyses show that equipping agents with web search and financial plugins substantially improves results on FinSearchComp, and the country origin of models and tools impact performance significantly. By aligning with realistic analyst tasks and providing end-to-end evaluation, FinSearchComp offers a professional, high-difficulty testbed for complex financial search and reasoning.
