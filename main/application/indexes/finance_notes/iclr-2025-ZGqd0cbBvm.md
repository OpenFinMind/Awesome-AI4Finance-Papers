# InsightBench: Evaluating Business Analytics Agents Through Multi-Step Insight Generation

ICLR 2025 · main · application

以金融任务或金融数据为核心研究对象。 主题：Financial Agents / 金融Agent与决策。

- 官方论文页：https://openreview.net/forum?id=ZGqd0cbBvm
- 摘要来源：https://iclr.cc/virtual/2025/poster/29227
- 本地 PDF：[打开](../../pdfs/ICLR/2025/iclr-2025-ZGqd0cbBvm__InsightBench_Evaluating_Business_Analytics_Agents_Through_Multi_Step_Insight_Generation.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_review
- 主方向：Financial Agents / 金融Agent与决策
- 细分方向：Investment & Financial Research Agents / 投研与金融决策Agent
- 技术方法标签：Language Models & LLM / 语言模型与LLM
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：LLMs
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/ServiceNow/insight-bench.

## 纳入依据

First, it consists of 100 datasets representing diverse business use cases such as finance and incident management, each accompanied by a carefully curated set of insights planted in the datasets.

## 原始摘要

Data analytics is essential for extracting valuable insights from data that can assist organizations in making effective decisions. We introduce InsightBench, a benchmark dataset with three key features. First, it consists of 100 datasets representing diverse business use cases such as finance and incident management, each accompanied by a carefully curated set of insights planted in the datasets. Second, unlike existing benchmarks focusing on answering single queries, InsightBench evaluates agents based on their ability to perform end-to-end data analytics, including formulating questions, interpreting answers, and generating a summary of insights and actionable steps. Third, we conducted comprehensive quality assurance to ensure that each dataset in the benchmark had clear goals and included relevant and meaningful questions and analysis. Furthermore, we implement a two-way evaluation mechanism using LLaMA-3 as an effective, open-source evaluator to assess agents’ ability to extract insights. We also propose AgentPoirot, our baseline data analysis agent capable of performing end-to-end data analytics. Our evaluation on InsightBench shows that AgentPoirot outperforms existing approaches (such as Pandas Agent) that focus on resolving single queries. We also compare the performance of open- and closed-source LLMs and various evaluation strategies. Overall, this benchmark serves as a testbed to motivate further development in comprehensive automated data analytics and can be accessed here: https://github.com/ServiceNow/insight-bench.

## Classification / 分类

- Primary task / 主方向: Financial Evaluation / 金融评测
- Primary subcategory / 主要子分类: Financial Datasets and Task Benchmarks / 金融数据集与任务基准
- Related tasks / 关联方向: Financial Evaluation / 金融评测; Financial Decision Making / 金融决策
- Subcategories / 子分类: Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Financial Knowledge and Professional Evaluation / 金融知识与专业能力评测; Financial Decision and Agent Evaluation / 金融决策与智能体评测
- Methods / 技术方法: Language Models & LLM / 语言模型与LLM
- Review status / 核对状态: `contribution_abstract_review`
- [Definitions / 分类定义](../finance_taxonomy.md) · [Evidence / 分类依据](../../checks/finance_taxonomy/assignments.json)
