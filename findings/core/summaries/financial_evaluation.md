## Research summary / 研究总结

**Financial Evaluation / 金融评测 · Findings / Core**

2026-11-20 · 48 task memberships / 篇任务关联论文。

### 中文

**研究问题与子方向。** 主要贡献是数据集、基准、评测环境、协议或能力诊断。任务覆盖、数据构建和评测设计是研究对象；论文仅使用现有基准不会自动归到本类。

**当前收录与方法。** 本页仅总结 Findings / core 中的论文。当前较常见的子分类：Financial Datasets and Task Benchmarks / 金融数据集与任务基准 (48); Financial Understanding and Multimodal Evaluation / 金融理解及多模态评测 (17); Evaluation Protocols and Metrics / 评测协议与指标 (16); Reliability, Safety and Fairness Evaluation / 可靠性、安全与公平性评测 (13); Financial Decision and Agent Evaluation / 金融决策与智能体评测 (10)。已标注的方法：Language Models & LLM / 语言模型与LLM (41); Uncertainty & Robustness / 不确定性与鲁棒性 (14); Retrieval & RAG / 检索与RAG (8); Multimodal Learning / 多模态学习 (5); Tabular Learning / 表格学习 (4)。这些是多标签篇数，不能直接相加，也不表示性能排名。

**数据与评测。** 检查覆盖、污染、标注质量、评测预算与指标外推边界。 代表论文的摘要、金融关联证据及原文链接见 [1](../indexes/finance_notes/2026.findings-acl.138.md) · [2](../indexes/finance_notes/2026.findings-acl.1481.md) · [3](../indexes/finance_notes/2026.findings-acl.694.md) · [4](../indexes/finance_notes/2026.findings-acl.1934.md)；不同数据与指标不合并为统一数值结论。

**研究机会（编辑判断）。** 检查污染、标注、用户场景和预算敏感性，研究静态得分与实际金融工作表现之间的联系。

### English

**Problem and subdirections.** The main contribution is a dataset, benchmark, evaluation environment, protocol or capability audit. Coverage, construction and evaluation design are research objects; merely using an existing benchmark is insufficient.

**Current coverage and methods.** This page covers only Findings / core. Frequent subcategories: Financial Datasets and Task Benchmarks / 金融数据集与任务基准 (48); Financial Understanding and Multimodal Evaluation / 金融理解及多模态评测 (17); Evaluation Protocols and Metrics / 评测协议与指标 (16); Reliability, Safety and Fairness Evaluation / 可靠性、安全与公平性评测 (13); Financial Decision and Agent Evaluation / 金融决策与智能体评测 (10). Recorded methods: Language Models & LLM / 语言模型与LLM (41); Uncertainty & Robustness / 不确定性与鲁棒性 (14); Retrieval & RAG / 检索与RAG (8); Multimodal Learning / 多模态学习 (5); Tabular Learning / 表格学习 (4). Counts overlap and are not performance rankings.

**Data and evaluation.** Inspect coverage, contamination, annotation quality, evaluation budget and limits of metric extrapolation. Representative abstracts, financial evidence and original sources are linked at [1](../indexes/finance_notes/2026.findings-acl.138.md) · [2](../indexes/finance_notes/2026.findings-acl.1481.md) · [3](../indexes/finance_notes/2026.findings-acl.694.md) · [4](../indexes/finance_notes/2026.findings-acl.1934.md). Results from incompatible data or metrics are not pooled.

**Research opportunities (editorial).** Check contamination, annotation, user scenarios and budget sensitivity, and study the connection between static scores and financial work.

### Representative papers / 代表论文

| Paper / 论文 | Contribution / 研究内容 | Boundary / 适用边界 |
|---|---|---|
| [1. AlphaQT-Bench: Diagnosing the Gap between Financial Code Generation and Quantitative Reasoning in LLMs](../indexes/finance_notes/2026.findings-acl.138.md) · ACL 2026 | 分层诊断金融代码的执行与时间正确性<br>Layered diagnosis of financial-code execution and temporal correctness | 过程可靠性不直接代表因子盈利<br>Process reliability does not directly establish profitable factors |
| [2. Are Large Language Models Reliable Reviewers? A Benchmark for Error Detection in Financial Documents](../indexes/finance_notes/2026.findings-acl.1481.md) · ACL 2026 | 分复杂度测试财务文档错误识别<br>Test financial-document errors at different complexities | 文档新颖性依赖被测模型的截止时间<br>Document novelty depends on the evaluated model cutoff |
| [3. FinSafetyBench: Evaluating LLM Safety in Real-World Financial Scenarios](../indexes/finance_notes/2026.findings-acl.694.md) · ACL 2026 | 双语金融场景的安全拒答与红队评价<br>Bilingual financial safety/refusal and red-team evaluation | 拒答率需结合正常任务误拒理解<br>Interpret refusal alongside false refusals on legitimate tasks |
| [4. From Tasks to Teams: A Risk-First Evaluation Framework for Multi-Agent LLM Systems in Finance](../indexes/finance_notes/2026.findings-acl.1934.md) · ACL 2026 | 多层探针检查多 Agent 协作风险<br>Multilayer probes assess collaborative-agent risks | 代理评分仍需独立验证<br>Proxy risk scores still require independent validation |
