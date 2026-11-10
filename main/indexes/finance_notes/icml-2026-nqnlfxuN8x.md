# SEER: Transformer-based Robust Time Series Forecasting via Automated Patch Enhancement and Replacement

ICML 2026 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：NASDAQ。 主题：Time Series / 时间序列；Macro & Economic Forecasting / 宏观经济与预测。

- 官方论文页：https://openreview.net/forum?id=nqnlfxuN8x
- 摘要来源：https://icml.cc/virtual/2026/poster/61675
- 本地 PDF：[打开](../../pdfs/ICML/2026/icml-2026-nqnlfxuN8x__SEER_Transformer_based_Robust_Time_Series_Forecasting_via_Automated_Patch_Enhancement_and_Replacement.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；Imputation & Irregular Series / 缺失与不规则序列；Macro Indicators & Policy / 宏观指标与政策
- 技术方法标签：Transformer / Transformer模型；Causal Learning / 因果学习；Uncertainty & Robustness / 不确定性与鲁棒性；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：causal；Time series；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

White Noise Anomalies Missing Value Dataset ILI NASDAQ FRED-MD Wike2000 SMD PSM USHCN Activity Metrics mse mae mse mae mse mae mse mae mse mae mse

## 原始摘要

Time series forecasting is important in many fields that require accurate predictions for decision-making. Patching techniques, commonly used and effective in time series modeling, help capture temporal dependencies by dividing the data into patches. However, existing patch-based methods fail to dynamically select patches and typically use all patches during the prediction process. In real-world time series, there are often low-quality issues during data collection, such as missing values, distribution shifts, anomalies and white noise, which may cause some patches to contain low-quality information, negatively impacting the prediction results. To address this issue, this study proposes a robust time series forecasting framework called $\textbf{SEER}$. Firstly, we propose an $\textit{Augmented Embedding Module}$, which improves patch-wise representations using a Mixture-of-Experts~(MoE) architecture and obtains series-wise token representations through a channel-adaptive perception mechanism. Secondly, we introduce a $\textit{Learnable Patch Replacement Module}$, which enhances forecasting robustness and model accuracy through a two-stage process: 1) a dynamic filtering mechanism eliminates negative patch-wise tokens; 2) a replaced attention module substitutes the identified low-quality patches with global series-wise token, further refining their representations through a causal attention mechanism. Comprehensive experimental results demonstrate the SOTA performance of SEER.
