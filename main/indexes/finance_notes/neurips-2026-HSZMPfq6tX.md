# ForecastCompass: Guiding Agentic Forecasting with Adaptive Factor Memory

NeurIPS 2026 · main · application

正文包含金融数据、金融训练数据、金融任务评测或具体金融场景案例。 主题：Financial Agents / 金融Agent与决策。

- 官方论文页：https://openreview.net/forum?id=HSZMPfq6tX
- 摘要来源：https://neurips.cc/virtual/2026/poster/153936
- 本地 PDF：[打开](../../pdfs/NeurIPS/2026/neurips-2026-HSZMPfq6tX__ForecastCompass_Guiding_Agentic_Forecasting_with_Adaptive_Factor_Memory.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Financial Agents / 金融Agent与决策
- 细分方向：Investment & Financial Research Agents / 投研与金融决策Agent
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Uncertainty & Robustness / 不确定性与鲁棒性；Retrieval & RAG / 检索与RAG
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：retrieval
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

, 2025]. Both datasets contain time-evolving forecasting questions across a broad range of domains, such as sports, technology, and finance. For each dataset, we select the latest five weeks of data to construct, update, and evaluate memory. This setting reflects the dynamic nature of agentic forecasting, where memory is built from recent resolved questions and revised as new weekly outcomes become available. The detailed data statistics is in the Appendix A.1. We follow a chronological evaluation protocol: memory is constructed only from previously resolved questions and is used to forecast future unresolved questions. This prevents post-resolution information from leaking into the current forecast. Evaluation metrics. We use Brier score [Glenn et

## 原始摘要

Agentic forecasting is important for decision-making in dynamic environments, but it remains challenging because agents must reason from incomplete, time-limited evidence and produce calibrated probabilities before outcomes are resolved. Memory provides a natural mechanism for transferring experience from resolved forecasts to future prediction tasks. However, existing agent-memory methods are not tailored to forecasting, as they typically store past interactions, reflections, or factual associations without explicitly representing reusable predictive factors or calibration knowledge.  We propose ForecastCompass(FoCo), an adaptive factor-based memory framework for agentic forecasting. FoCo organizes forecasting experience with a hierarchical forecasting-task taxonomy, enabling retrieval task-relevant forecasting knowledge. It maintains two complementary memory components: factor memory, which captures reusable predictive dimensions, and reasoning memory, which encodes probability updating, uncertainty handling, and calibration principles. Using retrospective analyses as learning signals, FoCo iteratively revises memory through a verbalized memory-revision procedure, enabling the agent to accumulate transferable forecasting knowledge over time. Experiments on Prophet Arena and FutureX with GPT-5-mini and Gemini-2.5-Flash show that FoCo improves both probabilistic accuracy and calibration.
