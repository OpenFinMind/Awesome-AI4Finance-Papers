# T1: One-to-One Channel-Head Binding for Multivariate Time-Series Imputation

ICLR 2026 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：Exchange benchmark (currency series)。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=IAnIlFsPEW
- 摘要来源：https://iclr.cc/virtual/2026/poster/10010327
- 本地 PDF：[打开](../../pdfs/ICLR/2026/iclr-2026-IAnIlFsPEW__T1_One_to_One_Channel_Head_Binding_for_Multivariate_Time_Series_Imputation.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Imputation & Irregular Series / 缺失与不规则序列
- 技术方法标签：Transformer / Transformer模型；Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Time series；time series；Transformer
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/Oppenheimerdinger/T1.

## 纳入依据

.093 0.044 0.143 0.056 0.166 0.048 0.147 0.059 0.171 0.038 0.133 0.094 0.220 0.080 0.175 0.060 0.154 0.082 0.155 0.076 0.176 0.049 0.149 Exchange 0.002 0.018 0.002 0.023 0.009 0.062 0.004 0.034 0.003 0.032 0.003 0.027 0.005 0.044 0.031 0.070 0.180 0.344 0.007 0.054 0.115 0.249 0.031 0.026 Illness 0.038 0.102 0.238 0.291 0.260 0.350 0.205 0.283 0.583 0.458 0.130 0.223 0.345 0.392 0.636 0.505 0.614 0.495 586.936 9.057 0.426 0.399 0.067 0.122 Electricity 0.043 0.131 0.071 0.172 0.121 0.253 0.090 0.199 0.105 0.225 0.089 0.208 0.191 0.33

## 原始摘要

Imputing missing values in multivariate time series remains challenging, especially under diverse missing patterns and heavy missingness. Existing methods suffer from suboptimal performance as corrupted temporal features hinder effective cross-variable information transfer, amplifying reconstruction errors. Robust imputation requires both extracting temporal patterns from sparse observations within each variable and selectively transferring information across variables—yet current approaches excel at one while compromising the other. We introduce T1 (Time series imputation with 1-to-1 channel-head binding), a CNN-Transformer hybrid architecture that achieves robust imputation through Channel-Head Binding—a mechanism creating one-to-one correspondence between CNN channels and attention heads. This design enables selective information transfer: when missingness corrupts certain temporal patterns, their corresponding attention pathways adaptively down-weight based on remaining observable patterns while preserving reliable cross-variable connections through unaffected channels. Experiments on 11 benchmark datasets demonstrate that T1 achieves state-of-the-art performance, reducing MSE by 46% on average compared to the second-best baseline, with particularly strong gains under extreme sparsity (70% missing ratio). The model generalizes to unseen missing patterns without retraining and uses a consistent hyperparameter configuration across all datasets. The code is available at https://github.com/Oppenheimerdinger/T1.
