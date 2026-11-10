# Once-for-All: Scalable Simultaneous Forecasting via Equilibrium State Estimation

ICML 2026 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：exchange rates。 主题：Market Prediction / 股价、收益与波动率预测。

- 官方论文页：https://openreview.net/forum?id=mZd4u9d7pQ
- 摘要来源：https://icml.cc/virtual/2026/poster/61831
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-mZd4u9d7pQ__Once_for_All_Scalable_Simultaneous_Forecasting_via_Equilibrium_State_Estimation.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Market Prediction / 股价、收益与波动率预测
- 细分方向：FX & Crypto Forecasts / 汇率与加密资产预测
- 技术方法标签：Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

t red background. commonly used as a benchmark in prediction studies. Here, we use 16 exchange rates relative to the USD, representing Models RMSE MAE Cost (mins) 16 non-USD currencies from the G20, which comprises ESE – 0.248 0.228 0.23 the world’s most significant economies. These currencies No ESE 0.249 0.243 0.09 exhibit mutual influence, while the impact of economie

## 原始摘要

We introduce Equilibrium State Estimation (ESE), a novel paradigm for simultaneous prediction, where multiple interacting systems require separate yet coordinated forecasts. Such scenarios often arise in real-world such as economics and healthcare modeling.  Unlike existing approaches that predict one system at a time, ESE forecasts all systems in a single pass.  It first estimates the equilibrium state across systems, then generates holistic forecasts based on the difference between the current state and the estimated equilibrium.  Extensive experiments on synthetic and real-world datasets, including currency exchange and COVID-19 spread modeling, demonstrate that ESE is at least as accurate as state-of-the-art (SOTA) methods while being significantly faster.  In addition, ESE integrates seamlessly with conventional predictors, combining their accuracy with its exceptional efficiency and delivering a 10–70× speedup. With linear-time complexity, ESE scales far better than SOTA methods as the number of systems increases. Moreover, it remains accurate under diverse perturbations, establishing ESE as a fast, generalizable, robust, and scalable multi-prediction method.
