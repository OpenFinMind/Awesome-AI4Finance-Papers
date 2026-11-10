# TARFVAE: Efficient One-Step Generative Time Series Forecasting via TARFLOW based VAE

NeurIPS 2025 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：Exchange benchmark (currency series)。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=3hnqwOq7iT
- 摘要来源：https://neurips.cc/virtual/2025/poster/120017
- 本地 PDF：[打开](../../pdfs/NeurIPS/2025/neurips-2025-3hnqwOq7iT__TARFVAE_Efficient_One_Step_Generative_Time_Series_Forecasting_via_TARFLOW_based_VAE.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；Representation & Foundation Models / 表征与基础模型；Generation & Simulation / 序列生成与仿真
- 技术方法标签：Generative Modeling / 生成建模；Transformer / Transformer模型
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Time series；time series；Transformer；variational
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/Gavine77/TARFVAE.

## 纳入依据

0.206 0.166 0.316 0.088 0.205 0.256 0.367 0.094 0.218 0.088 0.218 0.148 0.278 Exchange 192 0.172 0.294 0.182 0.305 0.182 0.304 0.177 0.299 0.279 0.402 0.176 0.299 0.470 0.509 0.184 0.307 0.176 0.315 0.271 0.315 336 0.340 0.423 0.310 0.403 0.363 0.438 0.331 0.417 0.477 0.548 0.301 0.397 1.268

## 原始摘要

Time series data is ubiquitous, with forecasting applications spanning from finance to healthcare. Beyond popular deterministic methods, generative models are gaining attention due to advancements in areas like image synthesis and video generation, as well as their inherent ability to provide probabilistic predictions. However, existing generative approaches mostly involve recurrent generative operations or repeated denoising steps, making the prediction laborious, particularly for long-term forecasting. Most of them only conduct experiments for relatively short-term forecasting, with limited comparison to deterministic methods in long-term forecasting, leaving their practical advantages unclear. This paper presents TARFVAE, a novel generative framework that combines the Transformer-based autoregressive flow (TARFLOW) and variational autoencoder (VAE) for efficient one-step generative time series forecasting. Inspired by the rethinking that complex architectures for extracting time series representations might not be necessary, we add a flow module, TARFLOW, to VAE to promote spontaneous learning of latent variables that benefit predictions. TARFLOW enhances VAE's posterior estimation by breaking the Gaussian assumption, thereby enabling a more informative latent space. TARFVAE uses only the forward process of TARFLOW, avoiding autoregressive inverse operations and thus ensuring fast generation. During generation, it samples from the prior latent space and directly generates full-horizon forecasts via the VAE decoder. With simple MLP modules, TARFVAE achieves superior performance over state-of-the-art deterministic and generative models across different forecast horizons on benchmark datasets while maintaining efficient prediction speed, demonstrating its effectiveness as an efficient and powerful solution for generative time series forecasting. Our code is available at https://github.com/Gavine77/TARFVAE.
