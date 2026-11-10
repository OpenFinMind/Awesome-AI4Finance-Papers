# Win Fast or Lose Slow: Balancing Speed and Accuracy in Latency-Sensitive Decisions of LLMs

NeurIPS 2025 · main · core

以金融任务或金融数据为核心研究对象。 主题：Trading & Microstructure / 交易与市场微观结构。

- 官方论文页：https://openreview.net/forum?id=Fcs90Rwm8j
- 摘要来源：https://neurips.cc/virtual/2025/poster/119027
- 本地 PDF：[打开](../../pdfs/NeurIPS/2025/neurips-2025-Fcs90Rwm8j__Win_Fast_or_Lose_Slow_Balancing_Speed_and_Accuracy_in_Latency_Sensitive_Decisions_of_LLMs.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_review
- 主方向：Trading & Microstructure / 交易与市场微观结构
- 细分方向：Trading & Execution / 交易策略与执行
- 技术方法标签：Language Models & LLM / 语言模型与LLM
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：language models；LLM；LLMs
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

However, many real-world applications, such as high-frequency trading and real-time competitive gaming, require decisions under strict latency constraints, where faster responses directly translate into higher rewards. / To support our investigation, we introduce two new benchmarks: HFTBench, a high-frequency trading simulation, and StreetFighter, a competitive gaming platform. / Our method achieves the best performance on both benchmarks, improving win rate by up to 80% in Street Fighter and boosting daily yield by up to 26.52% in trading,  underscoring the need for latency-aware evaluation and deployment strategies for LLM-based agents.

## 原始摘要

Large language models (LLMs) have shown remarkable performance across diverse reasoning and generation tasks, and are increasingly deployed as agents in dynamic environments such as code generation and recommendation systems. However, many real-world applications, such as high-frequency trading and real-time competitive gaming, require decisions under strict latency constraints, where faster responses directly translate into higher rewards. Despite the importance of this latency–quality trade-off, it remains underexplored in the context of LLM-based agents. In this work, we present the first systematic study of this trade-off in real-time decision-making tasks. To support our investigation, we introduce two new benchmarks: HFTBench, a high-frequency trading simulation, and StreetFighter, a competitive gaming platform. Our analysis reveals that optimal latency–quality balance varies by task, and that sacrificing quality for lower latency can significantly enhance downstream performance. To address this, we propose FPX, an adaptive framework that dynamically selects model size and quantization level based on real-time demands. Our method achieves the best performance on both benchmarks, improving win rate by up to 80% in Street Fighter and boosting daily yield by up to 26.52% in trading,  underscoring the need for latency-aware evaluation and deployment strategies for LLM-based agents. These results demonstrate the critical importance of latency-aware evaluation and deployment strategies for real-world LLM-based agents.
