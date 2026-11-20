# Time Series / 时间序列

Forecast, represent, generate or reconstruct financial sequences; a specific asset-value target belongs to valuation prediction. / 金融序列预测、表征、生成与重建；明确的资产价值目标归估值预测。

7 Findings long papers. Topic memberships can overlap.

[All topics](../ai_for_finance.md) · [Classification definitions](../finance_taxonomy.md) · [CSV](time_series.csv) · [Excel](../../finance_catalog.xlsx)

<!-- task-summary:start -->

## Research summary / 研究总结

**Time Series / 时间序列 · Findings / Core**

2026-11-20 · 7 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 关注金融序列的时间结构、变量依赖、表示、补全与生成。通用序列方法的金融实验与专门的金融建模分别保存在 Application 和 Core；明确以资产价值为目标的预测另见估值预测。

**当前收录与方法。** 本页仅总结 Findings / core 中的论文。当前较常见的子分类：General Sequence Forecasting / 通用序列预测 (6); Sequence Representation and Pattern Discovery / 序列表示与模式发现 (2); Sequence Generation and Augmentation / 序列生成与数据增强 (1)。已标注的方法：Language Models & LLM / 语言模型与LLM (5); Causal Learning / 因果学习 (2); Tabular Learning / 表格学习 (1); Representation Learning / 表征学习 (1); Uncertainty & Robustness / 不确定性与鲁棒性 (1)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 使用严格时间切分，分别报告预测误差、概率校准及合成质量。 代表论文的摘要、金融关联证据及原文链接见 [1](../finance_notes/2025.findings-acl.149.md) · [2](../finance_notes/2026.findings-acl.1799.md) · [3](../finance_notes/2026.findings-acl.32.md) · [4](../finance_notes/2024.findings-acl.58.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 研究跨频率、缺失和状态变化下的稳定性，避免将单一预测误差改善直接解释为投资收益。

### English

**Problem and subdirections.** This task concerns temporal structure, variable dependence, representation, reconstruction and generation. General sequence methods with financial experiments and finance-specific modeling are separated into Application and Core. Explicit asset-value targets also belong to valuation prediction.

**Current coverage and methods.** This page covers only Findings / core. Frequent subcategories: General Sequence Forecasting / 通用序列预测 (6); Sequence Representation and Pattern Discovery / 序列表示与模式发现 (2); Sequence Generation and Augmentation / 序列生成与数据增强 (1). Recorded methods: Language Models & LLM / 语言模型与LLM (5); Causal Learning / 因果学习 (2); Tabular Learning / 表格学习 (1); Representation Learning / 表征学习 (1); Uncertainty & Robustness / 不确定性与鲁棒性 (1). Counts overlap and are not performance rankings.

**Data and evaluation.** Use chronological splits and separate forecast error, probabilistic calibration and synthesis quality. Representative abstracts, financial evidence and original sources are linked at [1](../finance_notes/2025.findings-acl.149.md) · [2](../finance_notes/2026.findings-acl.1799.md) · [3](../finance_notes/2026.findings-acl.32.md) · [4](../finance_notes/2024.findings-acl.58.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Study stability across frequencies, missingness and regime changes without translating a forecast-error gain directly into investment profit.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. Stories that (are) Move(d by) Markets: A Causal Exploration of Market Shocks and Semantic Shifts across Different Partisan Groups](../finance_notes/2025.findings-acl.149.md) · ACL 2025 | 分析党派叙事语义与市场冲击关系<br>Analyze partisan narrative semantics and market shocks | 因果解释需保留原识别设定<br>Causal interpretation depends on the original identification design |
| [2. Do LLM Agents Really Mimic Humans? Diagnosing and Aligning Microeconomic Behaviors in Macro-ABMs](../finance_notes/2026.findings-acl.1799.md) · ACL 2026 | 用人类调查校准微观行为并检查宏观仿真<br>Calibrate micro behavior against surveys and test macro simulation | 特定人群校准不证明总体代表性<br>Calibration to a population does not establish universal representativeness |
| [3. Op-Fed: Opinion, Stance, and Monetary Policy Annotations on FOMC Transcripts Using Active Learning](../finance_notes/2026.findings-acl.32.md) · ACL 2026 | 主动学习和上下文标注货币政策立场<br>Active learning and context annotate monetary-policy stance | 意见识别与紧缩/宽松立场不同<br>Opinion detection differs from tightening/easing stance |
| [4. EconNLI: Evaluating Large Language Models on Economics Reasoning](../finance_notes/2024.findings-acl.58.md) · ACL 2024 | 以经济事件前提—后果评价推理<br>Evaluate premise–consequence reasoning for economic events | 文本因果标签不是政策效果估计<br>Textual causal labels are not policy-effect estimates |

<!-- task-summary:end -->

## Subtopic statistics / 子方向统计

| Subtopic | Papers |
|---|---:|
| General Sequence Forecasting / 通用序列预测 | 6 |
| Sequence Representation and Pattern Discovery / 序列表示与模式发现 | 2 |
| Imputation and Sequence Reconstruction / 缺失值填补与序列重建 | 0 |
| Sequence Generation and Augmentation / 序列生成与数据增强 | 1 |
| Anomaly and Change-Point Detection / 异常检测与变点识别 | 0 |
| Multivariate Relations and Cross-Frequency Modeling / 多变量关联与跨频率建模 | 0 |

## Full paper list / 完整论文列表

| Year | Venue | Paper | Scope | Primary topic | Subtopics | Methods | Resources |
|---|---|---|---|---|---|---|---|
| 2026 | ACL | [Do LLM Agents Really Mimic Humans? Diagnosing and Aligning Microeconomic Behaviors in Macro-ABMs](../finance_notes/2026.findings-acl.1799.md) | core | Financial Decision Making / 金融决策 | General Sequence Forecasting / 通用序列预测; Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策 | Language Models & LLM / 语言模型与LLM; Causal Learning / 因果学习 | [PDF](../../pdfs/ACL/2026/2026.findings-acl.1799.pdf) |
| 2026 | ACL | [From Heard to Lived Opinions: Simulating Opinion Dynamics with Grounded LLM Agents in Economic Environments](../finance_notes/2026.findings-acl.580.md) | core | Financial Decision Making / 金融决策 | Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策; Sequence Representation and Pattern Discovery / 序列表示与模式发现; Sequence Generation and Augmentation / 序列生成与数据增强 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/ACL/2026/2026.findings-acl.580.pdf) |
| 2026 | ACL | [Op-Fed: Opinion, Stance, and Monetary Policy Annotations on FOMC Transcripts Using Active Learning](../finance_notes/2026.findings-acl.32.md) | core | Financial Evaluation / 金融评测 | General Sequence Forecasting / 通用序列预测; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Report and Earnings-Call Tone / 财报及电话会议语调; Financial Stance and Opinion Detection / 金融立场与观点识别; Report and Disclosure Understanding / 财报与公告理解 | Language Models & LLM / 语言模型与LLM; Uncertainty & Robustness / 不确定性与鲁棒性 | [PDF](../../pdfs/ACL/2026/2026.findings-acl.32.pdf) |
| 2026 | EMNLP | [Scaling Multi-Agent Systems with Prospect-State Propagation](../finance_notes/2026.findings-emnlp.1585.md) | core | Financial Decision Making / 金融决策 | General Sequence Forecasting / 通用序列预测; Financial Agents and Multi-Agent Decisions / 金融智能体与多主体决策 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/EMNLP/2026/2026.findings-emnlp.1585.pdf) |
| 2025 | ACL | [Stories that (are) Move(d by) Markets: A Causal Exploration of Market Shocks and Semantic Shifts across Different Partisan Groups](../finance_notes/2025.findings-acl.149.md) | core | Time Series / 时间序列 | General Sequence Forecasting / 通用序列预测; Sequence Representation and Pattern Discovery / 序列表示与模式发现 | Causal Learning / 因果学习; Representation Learning / 表征学习 | [PDF](../../pdfs/ACL/2025/2025.findings-acl.149.pdf) |
| 2024 | ACL | [EconNLI: Evaluating Large Language Models on Economics Reasoning](../finance_notes/2024.findings-acl.58.md) | core | Financial Evaluation / 金融评测 | General Sequence Forecasting / 通用序列预测; Numerical Calculation and Program Reasoning / 数值计算与程序推理; Financial Datasets and Task Benchmarks / 金融数据集与任务基准; Financial Understanding and Multimodal Evaluation / 金融理解及多模态评测; Evaluation Protocols and Metrics / 评测协议与指标 | Language Models & LLM / 语言模型与LLM | [PDF](../../pdfs/ACL/2024/2024.findings-acl.58.pdf) |
| 2024 | EMNLP | [Financial Forecasting from Textual and Tabular Time Series](../finance_notes/2024.findings-emnlp.486.md) | core | Valuation Prediction / 估值预测 | Stock Price and Return Prediction / 股票价格与收益预测; General Sequence Forecasting / 通用序列预测 | Tabular Learning / 表格学习 | [PDF](../../pdfs/EMNLP/2024/2024.findings-emnlp.486.pdf) |
