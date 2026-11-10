# MarketSim: Simulating Stock Markets with Large-Scale Generative Agents

ICML 2026 · main · core

以金融任务或金融数据为核心研究对象。 主题：Trading & Microstructure / 交易与市场微观结构。

- 官方论文页：https://openreview.net/forum?id=EzpJxPDqXB
- 摘要来源：https://icml.cc/virtual/2026/poster/65297
- PDF 状态：access_blocked
- 金融依据类型：title_abstract_review
- 主方向：Trading & Microstructure / 交易与市场微观结构
- 细分方向：Market Simulation / 金融市场仿真
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Generative Modeling / 生成建模
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：LLM；multi-agent
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Stock markets are one of the most complex systems in the modern world, where prices emerge from billions of decentralized interactions among heterogeneous participants in an ever-evolving information landscape. / To this end, we propose MarketSim, a large-scale stock market simulation framework with generative agents. / To evaluate our proposed MarketSim, we develop a comprehensive benchmark that includes stocks from 8 GICS sectors and 3 representative real-world scenarios, along with 5 stylized facts for market complexity and 5 price-related statistical metrics.

## 原始摘要

Stock markets are one of the most complex systems in the modern world, where prices emerge from billions of decentralized interactions among heterogeneous participants in an ever-evolving information landscape. While high-fidelity simulation is important for understanding market dynamics, existing approaches face a persistent trade-off between structural and behavioral fidelity. To this end, we propose MarketSim, a large-scale stock market simulation framework with generative agents. MarketSim introduces a hierarchical multi-agent architecture that decouples strategic reasoning from high-frequency execution, enabling LLM agents to operate in a nanosecond-resolution, NASDAQ-like continuous double auction market. Building on this, we simulate over 15,000 heterogeneous market participants whose interactions shape and are shaped by an evolving market environment grounded in more than 12k real-world news articles, policy documents, and earnings reports. To evaluate our proposed MarketSim, we develop a comprehensive benchmark that includes stocks from 8 GICS sectors and 3 representative real-world scenarios, along with 5 stylized facts for market complexity and 5 price-related statistical metrics. Extensive experiments demonstrate that MarketSim not only captures key complexity properties of real-world markets, but also outperforms state-of-the-art baselines in tracking high-frequency price dynamics with an average MAPE of 3.48%, providing a scalable testbed for market analysis.
