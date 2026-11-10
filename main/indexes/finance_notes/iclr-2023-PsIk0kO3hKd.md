# Spatio-temporal point processes with deep non-stationary kernels

ICLR 2023 · main · application

正文包含金融数据、金融训练数据、金融任务评测或具体金融场景案例。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=PsIk0kO3hKd
- 摘要来源：https://iclr.cc/virtual/2023/poster/11011
- 本地 PDF：[打开](../../pdfs/ICLR/2023/iclr-2023-PsIk0kO3hKd__Spatio_temporal_point_processes_with_deep_non_stationary_kernels.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Causality & Dynamics / 序列因果与动力学；Financial Stochastic Processes / 金融随机过程
- 技术方法标签：未明确标注
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

first use two popular data sets containing time-stamped events with categorical marks to demonstrate the robustness of DNSK+Barrier in marked STPPs (refer to Appendix B for detailed definition and kernel modeling): (i) Financial Transactions. (Du et al., 2016). This data set contains transaction records of a stock in one day with time unit milliseconds and the action (mark) of each 9 Table 3: Results of real data sets with time and categorical marks. We compare the testing log- likelihood (Testing `, higher the better),

## 原始摘要

Point process data are becoming ubiquitous in modern applications, such as social networks, health care, and finance. Despite the powerful expressiveness of the popular recurrent neural network (RNN) models for point process data, they may not successfully capture sophisticated non-stationary dependencies in the data due to their recurrent structures. Another popular type of deep model for point process data is based on representing the influence kernel (rather than the intensity function) by neural networks. We take the latter approach and develop a new deep non-stationary influence kernel that can model non-stationary spatio-temporal point processes. The main idea is to approximate the influence kernel with a novel and general low-rank decomposition, enabling efficient representation through deep neural networks and computational efficiency and better performance. We also take a new approach to maintain the non-negativity constraint of the conditional intensity by introducing a log-barrier penalty. We demonstrate our proposed method's good performance and computational efficiency compared with the state-of-the-art on simulated and real data.
