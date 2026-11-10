# MOTOR: A Time-to-Event Foundation Model For Structured Medical Records

ICLR 2024 · main · application

正文包含金融数据、金融训练数据、金融任务评测或具体金融场景案例。本篇使用健康保险理赔记录开展医疗事件预测，属于保险数据应用。 主题：Insurance & Actuarial / 保险与精算。

- 官方论文页：https://openreview.net/forum?id=NialiwI2V6
- 摘要来源：https://iclr.cc/virtual/2024/poster/18777
- 本地 PDF：[打开](../../pdfs/ICLR/2024/iclr-2024-NialiwI2V6__MOTOR_A_Time_to_Event_Foundation_Model_For_Structured_Medical_Records.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Insurance & Actuarial / 保险与精算
- 细分方向：Insurance & Claims / 承保与理赔
- 技术方法标签：Uncertainty & Robustness / 不确定性与鲁棒性；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

to PhysioNet. (2) We prohibit medical decision making, diagnoses, and other non-research use cases of MOTOR in our DUA and can revoke model access for violations. (3) We do not release our MERATIVE models pretrained on insurance claims data, which may be easier for entities to obtain commercially vs. longitudinal EHR data. Reproducibility Statement The code necessary for reproducing the experiments in this paper can be found in the supplemental materials as a zip file. Our hyperparameter search grids can be found in Appendix A. To aid reproducibility we have performed evaluat

## 原始摘要

We present a self-supervised, time-to-event (TTE) foundation model called MOTOR (Many Outcome Time Oriented Representations) which is pretrained on timestamped sequences of events in electronic health records (EHR) and health insurance claims. TTE models are used for estimating the probability distribution of the time until a specific event occurs, which is an important task in medical settings. TTE models provide many advantages over classification using fixed time horizons, including naturally handling censored observations, but are challenging to train with limited labeled data. MOTOR addresses this challenge by pretraining on up to 55M patient records (9B clinical events). We evaluate MOTOR's transfer learning performance on 19 tasks, across 3 patient databases (a private EHR system, MIMIC-IV, and Merative claims data). Task-specific models adapted from MOTOR improve time-dependent C statistics by 4.6\% over state-of-the-art, improve label efficiency by up to 95\%, and are more robust to temporal distributional shifts. We further evaluate cross-site portability by adapting our MOTOR foundation model for six prediction tasks on the MIMIC-IV dataset, where it outperforms all baselines. MOTOR is the first foundation model for medical TTE predictions and we release a 143M parameter pretrained model for research use at https://huggingface.co/StanfordShahLab/motor-t-base.
