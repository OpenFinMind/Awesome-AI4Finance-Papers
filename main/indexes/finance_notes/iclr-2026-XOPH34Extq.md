# TabStruct: Measuring Structural Fidelity of Tabular Data

ICLR 2026 · main · application

实验使用汇率、宏观金融、信用评估或财务文档等金融相关基准。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=XOPH34Extq
- 摘要来源：https://iclr.cc/virtual/2026/poster/10008974
- 本地 PDF：[打开](../../pdfs/ICLR/2026/iclr-2026-XOPH34Extq__TabStruct_Measuring_Structural_Fidelity_of_Tabular_Data.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_benchmark
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Credit Scoring & Default / 信用评分与违约
- 技术方法标签：Generative Modeling / 生成建模；Causal Learning / 因果学习；Tabular Learning / 表格学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：causal
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/SilenceX12138/TabStruct.

## 纳入依据

,132 3,430 Characters Images OpenML 1459 10,218 8 1277.25 7 1 10 600 1,416 Credit-g Economics OpenML 46378 1,000 21 47.62 7 14 2 300 700 Electricity Economics OpenML 151 45,312 9 5034.67 7 2 2 19,237 26,075 Higgs Physics OpenML 4532 98,050 29 3381.03

## 原始摘要

Evaluating tabular generators remains a challenging problem, as the unique causal structural prior of heterogeneous tabular data does not lend itself to intuitive human inspection. Recent work has introduced structural fidelity as a tabular-specific evaluation dimension to assess whether synthetic data complies with the causal structures of real data. However, existing benchmarks often neglect the interplay between structural fidelity and conventional evaluation dimensions, thus failing to provide a holistic understanding of model performance. Moreover, they are typically limited to toy datasets, as quantifying existing structural fidelity metrics requires access to ground-truth causal structures, which are rarely available for real-world datasets. In this paper, we propose a novel evaluation framework that jointly considers structural fidelity and conventional evaluation dimensions. We introduce a new evaluation metric, global utility, which enables the assessment of structural fidelity even in the absence of ground-truth causal structures. In addition, we present TabStruct, a comprehensive evaluation benchmark offering large-scale quantitative analysis on 13 tabular generators from nine distinct categories, across 29 datasets. Our results demonstrate that global utility provides a task-independent, domain-agnostic lens for tabular generator performance. We release the TabStruct benchmark suite, including all datasets, evaluation pipelines, and raw results. Code is available at https://github.com/SilenceX12138/TabStruct.
