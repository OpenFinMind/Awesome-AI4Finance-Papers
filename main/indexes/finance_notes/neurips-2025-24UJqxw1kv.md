# Forecasting in Offline Reinforcement Learning for Non-stationary Environments

NeurIPS 2025 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：Exchange Rate。 主题：Time Series / 时间序列；Market Prediction / 股价、收益与波动率预测。

- 官方论文页：https://openreview.net/forum?id=24UJqxw1kv
- 摘要来源：https://neurips.cc/virtual/2025/poster/120177
- 本地 PDF：[打开](../../pdfs/NeurIPS/2025/neurips-2025-24UJqxw1kv__Forecasting_in_Offline_Reinforcement_Learning_for_Non_stationary_Environments.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Market Prediction / 股价、收益与波动率预测
- 细分方向：Forecasting / 序列预测；Representation & Foundation Models / 表征与基础模型；Generation & Simulation / 序列生成与仿真；FX & Crypto Forecasts / 汇率与加密资产预测
- 技术方法标签：Reinforcement Learning / 强化学习；Diffusion & Flow / 扩散与流模型；Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：diffusion；Reinforcement Learning
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Forecast Mean Figure 18: Zero-shot forecasting results with Lag-Llama [10] for first 2 time-series in univariate time-series datasets: real-data-A (Australian-electricity-demand), real-data-E (Exchange Rate), real-data-B (Electricity), real-data-C (Electricity Hourly),real-data-D (Electricity Nips). In all datasets, F ORL outperforms the DQL+L AG-s̄ baseline. F ORL achieves its greatest impact on moderately challenging forecasts (a 56.5% error reduction on real-data-D). Its behavior at the extremes further demonstrates its robustness: • F ORL still refines the best forecast by 10.2% (real-data-C)

## 原始摘要

Offline Reinforcement Learning (RL) provides a promising avenue for training policies from pre-collected datasets when gathering additional interaction data is infeasible. However, existing offline RL methods often assume stationarity or only consider synthetic perturbations at test time—assumptions that often fail in real-world scenarios characterized by abrupt, time-varying offsets. These offsets can lead to partial observability, causing agents to misperceive their true state and degrade performance. To overcome this challenge, we introduce Forecasting in Non-stationary Offline RL (FORL), a framework that unifies (i) conditional diffusion-based candidate state generation, trained without presupposing any specific form of future non-stationarity, and (ii) zero-shot time-series foundation models. FORL targets environments prone to unexpected, potentially non-Markovian offsets, requiring robust agent performance from the onset of each episode. Empirical evaluations on offline RL benchmarks, augmented with real-world time-series data to simulate realistic non-stationarity, demonstrate that FORL consistently improves performance compared to competitive baselines. By integrating zero-shot forecasting with the agent’s experience we aim to bridge the gap between offline RL and the complexity of real-world, non-stationary environments.
