# LLM Meeting Decision Trees on Tabular Data

NeurIPS 2025 · main · application

正文包含金融数据、金融训练数据、金融任务评测或具体金融场景案例。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=SRDF3RV0KP
- 摘要来源：https://neurips.cc/virtual/2025/poster/117938
- 本地 PDF：[打开](../../pdfs/NeurIPS/2025/neurips-2025-SRDF3RV0KP__LLM_Meeting_Decision_Trees_on_Tabular_Data.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Credit Scoring & Default / 信用评分与违约
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Uncertainty & Robustness / 不确定性与鲁棒性；Tabular Learning / 表格学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：fine-tuning；Language Models；LLM；LLMs
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

iclass classification, and regression. Specifically, the tabular datasets include: Blood (BL) [54], Credit (CR) [55], Car [56], Bank (BA) [57], Adult (AD) [58], Jan- nis (JA) [11], Cpu_act (CP) [11], Credit_reg (CRR) [11], California_housing (CA) [59], House_16H (HO) [11], Fried (FR) [60], Diomand (DI) [61]. The dataset properties and data pre-processing details are summarized in Appendix A.1. Following previous studies [5], we use Accuracy (higher is better) to evaluate binary and multiclass classification tasks, Normalized Root Mean Squared Error (NRMSE) (lower is better) to evaluate the regression tasks. Baselines and implementation details. We conduct a comparative analysis between DeLTa and other prominent methods in

## 原始摘要

Tabular data have been playing a vital role in diverse real-world fields, including healthcare, finance, etc.  With the recent success of Large Language Models (LLMs), early explorations of extending LLMs to the domain of tabular data have been developed. Most of these LLM-based methods typically first serialize tabular data into natural language descriptions, and then tune LLMs or directly infer on these serialized data. However, these methods suffer from two key inherent issues: (i) data perspective: existing data serialization methods lack universal applicability for structured tabular data, and may pose privacy risks through direct textual exposure, and (ii) model perspective: LLM fine-tuning methods struggle with tabular data, and in-context learning scalability is bottle-necked by input length constraints (suitable for few-shot learning). This work explores a novel direction of integrating LLMs into tabular data through logical decision tree rules as intermediaries, proposing a decision tree enhancer with LLM-derived rule for tabular prediction, DeLTa. The proposed DeLTa avoids tabular data serialization, and can be applied to full data learning setting without LLM fine-tuning.  Specifically, we leverage the reasoning ability of LLMs to redesign an improved rule given a set of decision tree rules. Furthermore, we provide a calibration method for original decision trees via new generated rule by LLM, which approximates the error correction vector to steer the original decision tree predictions in the direction of ``errors'' reducing. Finally, extensive experiments on diverse tabular benchmarks show that our method achieves state-of-the-art performance.
