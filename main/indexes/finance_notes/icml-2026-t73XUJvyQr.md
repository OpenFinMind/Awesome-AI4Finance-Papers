# Latent Laplace Diffusion for Irregular Multivariate Time Series

ICML 2026 · main · application

正文包含金融数据、金融训练数据、金融任务评测或具体金融场景案例。 主题：Time Series / 时间序列；Trading & Microstructure / 交易与市场微观结构。

- 官方论文页：https://openreview.net/forum?id=t73XUJvyQr
- 摘要来源：https://icml.cc/virtual/2026/poster/61165
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-t73XUJvyQr__Latent_Laplace_Diffusion_for_Irregular_Multivariate_Time_Series.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；Imputation & Irregular Series / 缺失与不规则序列；Trading & Execution / 交易策略与执行
- 技术方法标签：Diffusion & Flow / 扩散与流模型；Generative Modeling / 生成建模
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Diffusion；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

orology features include temperature, dew point, sea-level pressure, wind speed, and precipitation. We construct the finance datasets (Crypto and US Equity) from Google Finance daily market data. Crypto spans 2019-01-01 to 2024-12-31 with the top 118 (volume and market cap) most actively traded currencies selected; US Equity spans 2017-01-01 to 2024-12-31 with the top 222 (volume and market cap) most actively traded equities selected from NYSE and NASDAQ. Finance features include open, high, low, close, volume, daily returns (percent; adjacent trading days), gapped returns, a market index feature, 20-day rolling close, high–low ratio, dividends, and sinusoidal calendar features (day-of-week, day-of-month, month-of-year). Table 9. Dataset stati

## 原始摘要

Irregular multivariate time series pose a fundamental trade-off for long-horizon forecasting: discrete methods can distort temporal structure via re-gridding, while continuous-time models often rely on sequential numerical solvers that are prone to drift. To bridge this gap, we present the Latent Laplace Diffusion (LLapDiff), a generative framework that models the target as a low-dimensional latent trajectory, enabling horizon-wide generation without step-by-step integration over physical time. We guide the reverse process using a stable modal parameterization motivated by stochastic port-Hamiltonian dynamics, and parameterize its mean evolution in the Laplace domain via learnable complex-conjugate poles, allowing for direct evaluation over irregular timestamps. Moreover, we link continuous dynamics to irregular observations through renewal-averaging analysis, which maps sampling gaps to effective event-domain poles and theoretically motivates a gap-aware history summarizer for conditioning. Extensive experiments demonstrate that LLapDiff consistently outperforms baselines in long-horizon forecasting, and its continuous-time generative nature also supports missing-value imputation by querying the same model at historical timestamps.
