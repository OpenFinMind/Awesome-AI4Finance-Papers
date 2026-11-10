# AutoBencher: Towards Declarative Benchmark Construction

ICLR 2025 · main · application

包含明确的金融任务、金融领域数据或金融案例验证。 主题：Fraud & AML / 欺诈检测与反洗钱；Blockchain & Digital Assets / 区块链与数字资产。

- 官方论文页：https://openreview.net/forum?id=ymt4crbbXh
- 摘要来源：https://iclr.cc/virtual/2025/poster/27700
- 本地 PDF：[打开](../../pdfs/ICLR/2025/iclr-2025-ymt4crbbXh__AutoBencher_Towards_Declarative_Benchmark_Construction.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_financial_task_or_data
- 主方向：Fraud & AML / 欺诈检测与反洗钱
- 细分方向：Scams & Financial Misinformation / 诈骗与金融虚假信息；Crypto & Blockchain Transactions / 加密资产与链上交易
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：language model；language models；optimization
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

On the novelty ends, AutoBencher also helps identify specific gaps not captured by existing benchmarks: e.g., Gemini-Pro has knowledge gaps on Permian Extinction and Fordism while GPT-4o fails to decline harmful requests about cryptocurrency scams.

## 原始摘要

We present AutoBencher, a declarative framework for automatic benchmark construction, and use it to scalably discover novel insights and vulnerabilities of existing language models. Concretely, given a few desiderata of benchmarks (e.g., question difficulty, topic salience), we operationalize each desideratum and cast benchmark creation as an optimization problem. Specifically, we experiment with two settings with different optimization objectives: (i) for capability evaluation, we declare the goal of finding a salient, difficult dataset that induces novel performance patterns; (ii) for safety evaluation, we declare the goal of finding a dataset of unsafe prompts that existing LMs fail to decline. To tackle this optimization problem, we use a language model to iteratively propose and refine dataset descriptions, which are then used to generate topic-specific questions and answers. These descriptions are optimized to improve the declared desiderata. We use AutoBencher (powered by GPT-4) to create datasets for math, multilinguality, knowledge, and safety. The scalability of AutoBencher allows it to test fine-grained categories and tail knowledge, creating datasets that elicit 22% more model errors (i.e., difficulty) than existing benchmarks. On the novelty ends, AutoBencher also helps identify specific gaps not captured by existing benchmarks: e.g., Gemini-Pro has knowledge gaps on Permian Extinction and Fordism while GPT-4o fails to decline harmful requests about cryptocurrency scams.
