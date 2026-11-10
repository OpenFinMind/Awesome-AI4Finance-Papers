# HiPRAG: Hierarchical Process Rewards for Efficient Agentic Retrieval Augmented Generation

ICLR 2026 · main · application

正文包含金融数据、金融训练数据、金融任务评测或具体金融场景案例。 主题：Financial IR & RAG / 金融检索与RAG。

- 官方论文页：https://openreview.net/forum?id=Gt4v9WBPzm
- 摘要来源：https://iclr.cc/virtual/2026/poster/10010451
- 本地 PDF：[打开](../../pdfs/ICLR/2026/iclr-2026-Gt4v9WBPzm__HiPRAG_Hierarchical_Process_Rewards_for_Efficient_Agentic_Retrieval_Augmented_Generation.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_case_or_formal_model
- 主方向：Financial IR & RAG / 金融检索与RAG
- 细分方向：Retrieval, Embedding & Reranking / 检索、嵌入与重排
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Reinforcement Learning / 强化学习；Retrieval & RAG / 检索与RAG
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Language Models；LLMs；RAG；Reinforcement Learning；Retrieval
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

8, 2025. to find the stock price. Today is </think> Saturday, July 19, 2025, so I need the <search> AMD stock price closing July closing price from Friday, July 18, 18 2025 </search> 2025. </reasoning> <information> <search> AMD stock price closing July On Friday, July 18, 2025, the stock 18 2025 </search> for Advanced Micro Devices, Inc. <context> AMD (Advanced Micro Devices, (ticker: AMD) closed at a price of Inc.) closed at $175.40 on Friday, $175.40 per share. July 18, 2025. </context> </information> <conclusion> $175.40 </conclusion> <think> </step> I have all the necessary information. </think> The company is AMD, the CEO is Dr. <answer> Lisa Su, and the closing stock price Dr. Lisa Su and $175.40. was $175.40. I can no

## 原始摘要

Agentic Retrieval-Augmented Generation (RAG) is a powerful technique for incorporating external information that Large Language Models (LLMs) lack, enabling better problem solving and question answering. However, suboptimal search behaviors exist widely, such as over-search (retrieving information already known) and under-search (failing to search when necessary), which leads to unnecessary overhead and unreliable outputs. Current training methods, which typically rely on outcome-based rewards in a Reinforcement Learning (RL) framework, lack the fine-grained control needed to address these inefficiencies. To overcome this, we introduce $\textbf{Hi}$erarchical $\textbf{P}$rocess Rewards for Efficient agentic $\textbf{RAG}$ (HiPRAG), a novel training methodology that incorporates a fine-grained, knowledge-grounded process reward into the RL training. Our approach evaluates the necessity of each search decision on-the-fly by decomposing the agent's reasoning trajectory into discrete, parsable steps. We then apply a hierarchical reward function that provides an additional bonus based on the proportion of optimal search and non-search steps, on top of commonly used outcome and format rewards. Experiments on the Qwen2.5 and Llama-3.2 models across seven diverse QA benchmarks show that our method achieves average accuracies of 65.4\% (3B) and 67.2\% (7B), outperforming strong agentic RAG baselines. This is accomplished while dramatically improving search efficiency, reducing the over-search rate from over 27\% in baselines from previous work to just 2.3\% and concurrently lowering the under-search rate. These results demonstrate the efficacy of optimizing the reasoning process itself, not just the final outcome. Further experiments and analysis demonstrate that HiPRAG shows good generalizability across a wide range of RL algorithms, model families, sizes, and types. This work demonstrates the importance and potential of fine-grained control through RL, for improving the efficiency and optimality of reasoning for search agents.
