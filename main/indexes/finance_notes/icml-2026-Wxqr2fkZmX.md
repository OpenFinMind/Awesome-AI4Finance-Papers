# Building Social World Model with Large Language Models

ICML 2026 · main · application

包含明确的金融任务、金融领域数据或金融案例验证。 主题：Time Series / 时间序列；Trading & Microstructure / 交易与市场微观结构；Blockchain & Digital Assets / 区块链与数字资产。

- 官方论文页：https://openreview.net/forum?id=Wxqr2fkZmX
- 摘要来源：https://icml.cc/virtual/2026/poster/63462
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-Wxqr2fkZmX__Building_Social_World_Model_with_Large_Language_Models.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_financial_task_or_data
- 主方向：Blockchain & Digital Assets / 区块链与数字资产
- 细分方向：Representation & Foundation Models / 表征与基础模型；Prediction Markets / 预测市场；Crypto & Blockchain Transactions / 加密资产与链上交易
- 技术方法标签：Language Models & LLM / 语言模型与LLM
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：LLMs
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

SWM-bench includes over 12k data points for social belief prediction tasks spanning diverse domains such as politics, finance, and cryptocurrency.

## 原始摘要

Understanding and predicting how social beliefs evolve in response to events -- from policy changes to scientific breakthroughs -- remains a fundamental challenge in social science. Given LLMs' commonsense knowledge and social intelligence, we ask: Can LLMs model the dynamics of social beliefs following social events? In this work, we introduce the concept of the Social World Model (SWM), a general framework designed to capture how social beliefs evolve in response to major events. SWM learns state-transition functions for social beliefs by mining temporal patterns in social data and optimizing the evidence lower bound, without the need for explicit human annotations linking events to belief shifts, or for expensive census data. To evaluate SWM, we introduce a benchmark, SWM-bench, derived from real-world prediction markets, specifically Kalshi and Polymarket. SWM-bench includes over 12k data points for social belief prediction tasks spanning diverse domains such as politics, finance, and cryptocurrency. Our experimental results show that SWM significantly outperforms time-series foundation models, achieving state-of-the-art results on Kalshi data and demonstrating competitive performance on Polymarket data, while offering interpretable insights into the underlying mechanisms of social belief dynamics.
