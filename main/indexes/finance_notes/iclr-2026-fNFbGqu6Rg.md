# Towards Multimodal Time Series Anomaly Detection with Semantic Alignment and Condensed Interaction

ICLR 2026 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：NASDAQ。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=fNFbGqu6Rg
- 摘要来源：https://iclr.cc/virtual/2026/poster/10008243
- 本地 PDF：[打开](../../pdfs/ICLR/2026/iclr-2026-fNFbGqu6Rg__Towards_Multimodal_Time_Series_Anomaly_Detection_with_Semantic_Alignment_and_Condensed_Interaction.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Anomaly Detection / 序列异常检测
- 技术方法标签：Multimodal Learning / 多模态学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Time series；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/decisionintelligence/MindTS.

## 纳入依据

m Yahoo EWJ 1 9.96 2658 2009.11.16 - 2020.6.9 Finance and news information collected from various financial MDT 1 11.17 2732 2009.8.6 - 2020.6.12 news websites such as NASDAQ, Bloomberg, and others. A.2 BASELINES We extensively compare MindTS against 19 baselines, including (1) LLM-based methods: LLMMixer (LMixer) (Kowsher et al., 2024), UniTime (UTime) (Liu et al., 2024c), GPT4TS 17 Published as a conference paper at ICLR 202

## 原始摘要

Time series anomaly detection plays a critical role in many dynamic systems. Despite its importance, previous approaches have primarily relied on unimodal numerical data, overlooking the importance of complementary information from other modalities. In this paper, we propose a novel multimodal time series anomaly detection model (MindTS) that focuses on addressing two key challenges: (1) how to achieve semantically consistent alignment across heterogeneous multimodal data, and (2) how to filter out redundant modality information to enhance cross-modal interaction effectively. To address the first challenge, we propose Fine-grained Time-text Semantic Alignment. It integrates exogenous and endogenous text information through cross-view text fusion and a multimodal alignment mechanism, achieving semantically consistent alignment between time and text modalities. For the second challenge, we introduce Content Condenser Reconstruction, which filters redundant information within the aligned text modality and performs cross-modal reconstruction to enable interaction. Extensive experiments on six real-world multimodal datasets demonstrate that the proposed MindTS achieves competitive or superior results compared to existing methods. The code is available at: https://github.com/decisionintelligence/MindTS.
