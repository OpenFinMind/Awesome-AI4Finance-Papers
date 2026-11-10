# ProCTI: Prototype-Refined Global Conditioning for Diffusion-Based Time Series Imputation

NeurIPS 2026 · main · application

正文包含金融数据、金融训练数据、金融任务评测或具体金融场景案例。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=qJv71MIpc5
- 摘要来源：https://neurips.cc/virtual/2026/poster/149404
- 本地 PDF：[打开](../../pdfs/NeurIPS/2026/neurips-2026-qJv71MIpc5__ProCTI_Prototype_Refined_Global_Conditioning_for_Diffusion_Based_Time_Series_Imputation.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Imputation & Irregular Series / 缺失与不规则序列
- 技术方法标签：Diffusion & Flow / 扩散与流模型；Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：diffusion；Time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

ataset is from the weather station of the Max Planck Institute for Biogeochemistry, comprising 14 meteorological attributes recorded between January 1st 2009 and December 31st 2016. The Stock [2] dataset reflects Google stock price data from 2004 to 2019, with each record representing a new day. Finally, the Gait [4] dataset comprises gait data collected using IMU sensors from 744 users during walks on level ground. We provide further details about dataset preparation for our experiments in Appendix A.3. Baselines We evaluate ProCTI against a diverse set of baselines. We con

## 原始摘要

Time series imputation has progressed from statistical and deep learning approaches to diffusion-based models, which have shown strong recent performance. Existing diffusion-based methods typically condition the reverse process using local contextual information from the current or neighbouring windows. Meanwhile, global dataset-level structure often remains implicit, limiting performance when local observations are sparse, noisy, or unrepresentative. To address this issue, we propose ProCTI, a diffusion-imputation framework that augments local conditioning with retrieved global dataset-level priors through learned prototypes. A hybrid conditioning mechanism integrates this global context with local signals during reverse diffusion, enabling more accurate reconstruction under varying missingness scenarios. Experiments across multiple benchmark datasets show that ProCTI outperforms strong baselines overall under random missingness, while remaining competitive under attribute-wise missingness. We further introduce a theoretical framework that distinguishes between local and global conditioning in diffusion-based imputation, showing that combining both can reduce conditional uncertainty and improve imputation quality.
