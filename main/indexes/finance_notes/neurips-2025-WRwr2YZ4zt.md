# TimeXL: Explainable Multi-modal Time Series Prediction with LLM-in-the-Loop

NeurIPS 2025 · main · application

正文包含金融数据、金融训练数据、金融任务评测或具体金融场景案例。 主题：Time Series / 时间序列。

- 官方论文页：https://openreview.net/forum?id=WRwr2YZ4zt
- 摘要来源：https://neurips.cc/virtual/2025/poster/117594
- 本地 PDF：[打开](../../pdfs/NeurIPS/2025/neurips-2025-WRwr2YZ4zt__TimeXL_Explainable_Multi_modal_Time_Series_Prediction_with_LLM_in_the_Loop.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Time Series / 时间序列
- 细分方向：Forecasting / 序列预测；Generation & Simulation / 序列生成与仿真；Causality & Dynamics / 序列因果与动力学
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Multimodal Learning / 多模态学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Language Models；LLM；LLMs；Time series；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

AUROC (AUC) for TimeXL and state-of-the-art baselines on multi- modal time series datasets. Weather Finance Healthcare (TP) Healthcare (MT) Datasets → Methods ↓ F1 AUC F1 AUC F1 AUC F1 AUC DLinear [75] 0.540 0.660 0.255 0.485 0.393 0.500 0.419 0.388 Autoformer [76] 0.546 0.590 0.565 0.747 0.774 0.918 0.683 0.825 Crossformer [77] 0.500 0.594 0.571 0.775 0.924 0.984 0.737 0.913 TimesNet [78] 0.494 0.594 0.538 0.756 0.794 0.867 0.765 0.944 iTransformer [79] 0.541 0.650 0.600 0.783 0.861 0.931 0.791 0.963 TSMixer [80] 0.488 0.534 0.465 0.689 0.770 0.797 0.808 0.931 TimeMixer [81] 0.577 0.658 0.571 0.776 0.822 0.887 0.824 0.935 FreTS [82] 0.623 0.688 0.546 0.737 0.887 0.950 0.751 0.762 PatchTST [5] 0.592 0.675 0.604 0.795 0.841 0.934

## 原始摘要

Time series analysis provides essential insights for real-world system dynamics and informs downstream decision-making, yet most existing methods often overlook the rich contextual signals present in auxiliary modalities. To bridge this gap, we introduce TimeXL, a multi-modal prediction framework that integrates a prototype-based time series encoder with three collaborating Large Language Models (LLMs) to deliver more accurate predictions and interpretable explanations. First, a multi-modal prototype-based encoder processes both time series and textual inputs to generate preliminary forecasts alongside case-based rationales. These outputs then feed into a prediction LLM, which refines the forecasts by reasoning over the encoder's predictions and explanations. Next, a reflection LLM compares the predicted values against the ground truth, identifying textual inconsistencies or noise. Guided by this feedback, a refinement LLM iteratively enhances text quality and triggers encoder retraining. This closed-loop workflow---prediction, critique (reflect), and refinement---continuously boosts the framework's performance and interpretability. Empirical evaluations on four real-world datasets demonstrate that TimeXL achieves up to 8.9\% improvement in AUC and produces human-centric, multi-modal explanations, highlighting the power of LLM-driven reasoning for time series prediction.
