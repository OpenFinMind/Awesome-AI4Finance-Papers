# ELASTIC: Numerical Reasoning with Adaptive Symbolic Compiler

NeurIPS 2022 · main · application

通用方法在金融任务、数据或明确案例上开展应用验证。 主题：Financial QA & Reasoning / 金融问答与数值推理。

- 官方论文页：https://openreview.net/forum?id=gd7ZI0X7Q-h
- 摘要来源：https://neurips.cc/virtual/2022/poster/54779
- 本地 PDF：[打开](../../pdfs/NeurIPS/2022/neurips-2022-gd7ZI0X7Q-h__ELASTIC_Numerical_Reasoning_with_Adaptive_Symbolic_Compiler.pdf)；版本：publisher_version
- 金融依据类型：title_abstract_review
- 主方向：Financial QA & Reasoning / 金融问答与数值推理
- 细分方向：Numerical & Table Reasoning / 数值与表格推理
- 技术方法标签：Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：FinQA
- 代码链接：摘要未提供可确认链接

## 纳入依据

Experiments show that ELASTIC achieves 68.96 and 65.21 of execution accuracy and program accuracy on the FinQA dataset and 83.00 program accuracy on the MathQA dataset, outperforming previous state-of-the-art models significantly.

## 原始摘要

Numerical reasoning over text is a challenging task of Artificial Intelligence (AI), requiring reading comprehension and numerical reasoning abilities. Previous approaches use numerical reasoning programs to represent the reasoning process. However, most works do not separate the generation of operators and operands, which are key components of a numerical reasoning program, thus limiting their ability to generate such programs for complicated tasks. In this paper, we introduce the numEricaL reASoning with adapTive symbolIc Compiler (ELASTIC) model, which is constituted of the RoBERTa as the Encoder and a Compiler with four modules: Reasoning Manager, Operator Generator, Operands Generator, and Memory Register. ELASTIC is robust when conducting complicated reasoning. Also, it is domain agnostic by supporting the expansion of diverse operators without caring about the number of operands it contains. Experiments show that ELASTIC achieves 68.96 and 65.21 of execution accuracy and program accuracy on the FinQA dataset and 83.00 program accuracy on the MathQA dataset, outperforming previous state-of-the-art models significantly.
