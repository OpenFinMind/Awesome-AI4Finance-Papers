# Insurance and Actuarial Science / 保险精算

Insurance underwriting, claims, reserves, actuarial prediction and insurance business decisions. / 承保、理赔、准备金、精算预测及保险业务决策。

10 Main long papers. Topic memberships can overlap.

[All topics](../ai_for_finance.md) · [Classification definitions](../finance_taxonomy.md) · [CSV](insurance.csv) · [Excel](../../finance_catalog.xlsx)

<!-- task-summary:start -->

## Research summary / 研究总结

**Insurance and Actuarial Science / 保险精算 · Main / Application**

2026-11-20 · 10 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 以保险合同、保费、索赔、准备金及寿命风险为对象。客户营销、保险销售对话与欺诈检测分别与金融服务或金融安全关联，不因使用保险数据就视为精算贡献。

**当前收录与方法。** 本页仅总结 Main / application 中的论文。当前较常见的子分类：Claim Frequency and Loss Severity / 索赔频率与损失严重度 (9)。已标注的方法：Optimization & Numerical Methods / 优化与数值方法 (4); Representation Learning / 表征学习 (2); Tabular Learning / 表格学习 (2); Multimodal Learning / 多模态学习 (1); Transformer / Transformer模型 (1)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 关注索赔分布、校准、选择偏差、长期风险及业务约束。 代表论文的摘要、金融关联证据及原文链接见 [1](../finance_notes/kdd-2017-30051c903823.md) · [2](../finance_notes/iclr-2026-wHuVdpnUFp.md) · [3](../finance_notes/iclr-2024-NialiwI2V6.md) · [4](../finance_notes/aaai-2021-16099.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 联合考察长尾赔付、风险选择和长期校准，检验模型在保单结构与人群变化下的适用性。

### English

**Problem and subdirections.** This task concerns insurance contracts, premiums, claims, reserves and longevity risk. Marketing, sales dialogue and fraud detection connect to services or safety; using insurance data alone does not establish an actuarial contribution.

**Current coverage and methods.** This page covers only Main / application. Frequent subcategories: Claim Frequency and Loss Severity / 索赔频率与损失严重度 (9). Recorded methods: Optimization & Numerical Methods / 优化与数值方法 (4); Representation Learning / 表征学习 (2); Tabular Learning / 表格学习 (2); Multimodal Learning / 多模态学习 (1); Transformer / Transformer模型 (1). Counts overlap and are not performance rankings.

**Data and evaluation.** Inspect claim distributions, calibration, selection bias, long-term risk and business constraints. Representative abstracts, financial evidence and original sources are linked at [1](../finance_notes/kdd-2017-30051c903823.md) · [2](../finance_notes/iclr-2026-wHuVdpnUFp.md) · [3](../finance_notes/iclr-2024-NialiwI2V6.md) · [4](../finance_notes/aaai-2021-16099.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Examine heavy-tailed claims, risk selection and long-term calibration, including changes in contract structure and insured populations.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. The Selective Labels Problem: Evaluating Algorithmic Predictions in the Presence of Unobservables](../finance_notes/kdd-2017-30051c903823.md) · KDD 2017 | 以 contraction 评价选择性标签下的预测<br>Contraction evaluates prediction with selective outcomes | 通用评价方法，保险只是应用领域之一<br>A general evaluation method with insurance among its domains |
| [2. xRFM: Accurate, scalable, and interpretable feature learning models for tabular data](../finance_notes/iclr-2026-wHuVdpnUFp.md) · ICLR 2026 | 研究主题：xRFM: Accurate, scalable, and interpretable feature learning models for tabular data<br>Research topic: xRFM: Accurate, scalable, and interpretable feature learning models for tabular data | 按原文的任务、数据和实验设置解释结果。<br>Interpret results within the original task, data and experimental setting. |
| [3. MOTOR: A Time-to-Event Foundation Model For Structured Medical Records](../finance_notes/iclr-2024-NialiwI2V6.md) · ICLR 2024 | 研究主题：MOTOR: A Time-to-Event Foundation Model For Structured Medical Records<br>Research topic: MOTOR: A Time-to-Event Foundation Model For Structured Medical Records | 按原文的任务、数据和实验设置解释结果。<br>Interpret results within the original task, data and experimental setting. |
| [4. Deep Contextual Clinical Prediction with Reverse Distillation](../finance_notes/aaai-2021-16099.md) · AAAI 2021 | 研究主题：Deep Contextual Clinical Prediction with Reverse Distillation<br>Research topic: Deep Contextual Clinical Prediction with Reverse Distillation | 按原文的任务、数据和实验设置解释结果。<br>Interpret results within the original task, data and experimental setting. |

<!-- task-summary:end -->

## Subtopic statistics / 子方向统计

| Subtopic | Papers |
|---|---:|
| Insurance Pricing and Premium Setting / 保险定价与保费厘定 | 0 |
| Claim Frequency and Loss Severity / 索赔频率与损失严重度 | 9 |
| Reserves and Payout Prediction / 准备金与赔付预测 | 0 |
| Mortality, Longevity and Survival / 死亡率、长寿与生存分析 | 0 |
| Reinsurance and Risk Sharing / 再保险与风险分担 | 0 |
| Catastrophe Risk and Solvency / 巨灾风险与偿付能力 | 0 |

## Full paper list / 完整论文列表

| Year | Venue | Paper | Scope | Primary topic | Subtopics | Methods | Resources |
|---|---|---|---|---|---|---|---|
| 2026 | ICLR | [xRFM: Accurate, scalable, and interpretable feature learning models for tabular data](../finance_notes/iclr-2026-wHuVdpnUFp.md) | application | Insurance and Actuarial Science / 保险精算 | Claim Frequency and Loss Severity / 索赔频率与损失严重度 | Tabular Learning / 表格学习 | [PDF](../../pdfs/ICLR/2026/iclr-2026-wHuVdpnUFp__xRFM_Accurate_scalable_and_interpretable_feature_learning_models_for_tabular_data.pdf) |
| 2025 | ICLR | [TabReD: Analyzing Pitfalls and Filling the Gaps in Tabular Deep Learning Benchmarks](../finance_notes/iclr-2025-L14sqcrUC3.md) | application | Financial Risk / 金融风险 | Credit Risk and Default Prediction / 信用风险与违约预测; Claim Frequency and Loss Severity / 索赔频率与损失严重度 | Tabular Learning / 表格学习 | [PDF](../../pdfs/ICLR/2025/iclr-2025-L14sqcrUC3__TabReD_Analyzing_Pitfalls_and_Filling_the_Gaps_in_Tabular_Deep_Learning_Benchmarks.pdf) |
| 2024 | ICLR | [MOTOR: A Time-to-Event Foundation Model For Structured Medical Records](../finance_notes/iclr-2024-NialiwI2V6.md) | application | Insurance and Actuarial Science / 保险精算 | Claim Frequency and Loss Severity / 索赔频率与损失严重度 | Uncertainty & Robustness / 不确定性与鲁棒性; Representation Learning / 表征学习 | [PDF](../../pdfs/ICLR/2024/iclr-2024-NialiwI2V6__MOTOR_A_Time_to_Event_Foundation_Model_For_Structured_Medical_Records.pdf) |
| 2021 | AAAI | [Deep Contextual Clinical Prediction with Reverse Distillation](../finance_notes/aaai-2021-16099.md) | application | Insurance and Actuarial Science / 保险精算 | Claim Frequency and Loss Severity / 索赔频率与损失严重度 | Transformer / Transformer模型; Representation Learning / 表征学习 | [PDF](../../pdfs/AAAI/2021/aaai-2021-16099__Deep_Contextual_Clinical_Prediction_with_Reverse_Distillation.pdf) |
| 2021 | AAAI | [Fairness in Forecasting and Learning Linear Dynamical Systems](../finance_notes/aaai-2021-17328.md) | application | Time Series / 时间序列 | General Sequence Forecasting / 通用序列预测; Claim Frequency and Loss Severity / 索赔频率与损失严重度; Financial Model and Agent Safety / 金融模型及智能体安全 | Fairness & Recourse / 公平性与算法追索; Optimization & Numerical Methods / 优化与数值方法 | [PDF](../../pdfs/AAAI/2021/aaai-2021-17328__Fairness_in_Forecasting_and_Learning_Linear_Dynamical_Systems.pdf) |
| 2021 | ICML | [Feature Clustering for Support Identification in Extreme Regions](../finance_notes/icml-2021-10013.md) | application | Financial Risk / 金融风险 | Market Risk and Tail Losses / 市场风险与尾部损失; Claim Frequency and Loss Severity / 索赔频率与损失严重度 | Optimization & Numerical Methods / 优化与数值方法 | [PDF](../../pdfs/ICML/2021/icml-2021-10013__Feature_Clustering_for_Support_Identification_in_Extreme_Regions.pdf) |
| 2021 | NeurIPS | [Optimal Best-Arm Identification Methods for Tail-Risk Measures](../finance_notes/neurips-2021-4wVlNqBJXg.md) | application | Financial Risk / 金融风险 | Market Risk and Tail Losses / 市场风险与尾部损失; Claim Frequency and Loss Severity / 索赔频率与损失严重度 | Reinforcement Learning / 强化学习; Optimization & Numerical Methods / 优化与数值方法 | [PDF](../../pdfs/NeurIPS/2021/neurips-2021-4wVlNqBJXg__Optimal_Best_Arm_Identification_Methods_for_Tail_Risk_Measures.pdf) |
| 2019 | EMNLP | [Multi-Domain Goal-Oriented Dialogues (MultiDoGO): Strategies toward Curating and Annotating Large Scale Dialogue Data](../finance_notes/D19-1460.md) | application | Financial Risk / 金融风险 | Claim Frequency and Loss Severity / 索赔频率与损失严重度; Credit Risk and Default Prediction / 信用风险与违约预测; Lending, Payment and Banking Workflows / 贷款、支付及银行业务流程 | Multimodal Learning / 多模态学习 | [PDF](../../pdfs/EMNLP/2019/D19-1460__Multi_Domain_Goal_Oriented_Dialogues_MultiDoGO_Strategies_toward_Curating_and_Annotating_Large_Scale_Dial.pdf) |
| 2017 | ICML | [StingyCD: Safely Avoiding Wasteful Updates in Coordinate Descent](../finance_notes/icml-2017-764.md) | application | Insurance and Actuarial Science / 保险精算 | Claim Frequency and Loss Severity / 索赔频率与损失严重度 | Optimization & Numerical Methods / 优化与数值方法 | [PDF](../../pdfs/ICML/2017/icml-2017-764__StingyCD_Safely_Avoiding_Wasteful_Updates_in_Coordinate_Descent.pdf) |
| 2017 | KDD | [The Selective Labels Problem: Evaluating Algorithmic Predictions in the Presence of Unobservables](../finance_notes/kdd-2017-30051c903823.md) | application | Insurance and Actuarial Science / 保险精算 |  |  | [Online](https://doi.org/10.1145/3097983.3098066) |
