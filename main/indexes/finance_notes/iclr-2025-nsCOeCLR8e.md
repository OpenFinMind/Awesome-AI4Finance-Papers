# DynFrs: An Efficient Framework for Machine Unlearning in Random Forest

ICLR 2025 · main · application

正文包含金融数据、金融训练数据、金融任务评测或具体金融场景案例。 主题：Banking & Customer Service / 银行业务与客户服务。

- 官方论文页：https://openreview.net/forum?id=nsCOeCLR8e
- 摘要来源：https://iclr.cc/virtual/2025/poster/28390
- 本地 PDF：[打开](../../pdfs/ICLR/2025/iclr-2025-nsCOeCLR8e__DynFrs_An_Efficient_Framework_for_Machine_Unlearning_in_Random_Forest.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Banking & Customer Service / 银行业务与客户服务
- 细分方向：Banking Data Applications / 银行业务数据应用
- 技术方法标签：Privacy & Federated Learning / 隐私与联邦学习；Tabular Learning / 表格学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

±.000 .7911±.001 .7934±.002 Adult .8628±.001 .8428±.001 .8637±.000 .8503±.000 .8633±.001 .8650±.001 Bank .9420±.000 .9350±.000 .9414±.001 .9436±.000 .9417±.000 .9436±.000 Heart .7344±.001 .7195±.001 .7342±.001 .7301±.000 .7358±.002 .7366±.000 Diabetes .6443±.001 .6190±.000 .6435±.001 .6462±.000 .6453±.001 .6470±.002 NoShow .7361±.001 .7170±.000 .7387±.000 .7269±.000 .7335±.001 .7356±.000 Synthetic .9451±.000 / .9441±.000 .9309±.000 .9424±.000 .9454±.000 Higgs .7441±.000 / .7434±.000 .7255±.000 .7431±.000 .7475±.000 Effect of q on Predictive Accuracy Unlearning v.s. Retraining .866 .86 Accuracy Accuracy .863 .84 Adult .860 .82 Unlearned DYNFRS .857 Adult .80 Retrained DYNFRS .854 .648 .65 .64 Accuracy Accuracy .645 .642 .

## 原始摘要

Random Forests are widely recognized for establishing efficacy in classification and regression tasks, standing out in various domains such as medical diagnosis, finance, and personalized recommendations. These domains, however, are inherently sensitive to privacy concerns, as personal and confidential data are involved. With increasing demand for the right to be forgotten, particularly under regulations such as GDPR and CCPA, the ability to perform machine unlearning has become crucial for Random Forests. However, insufficient attention was paid to this topic, and existing approaches face difficulties in being applied to real-world scenarios. Addressing this gap, we propose the DynFrs framework designed to enable efficient machine unlearning in Random Forests while preserving predictive accuracy. Dynfrs leverages subsampling method Occ(q) and a lazy tag strategy Lzy, and is still adaptable to any Random Forest variant. In essence, Occ(q) ensures that each sample in the training set occurs only in a proportion of trees so that the impact of deleting samples is limited, and Lzy delays the reconstruction of a tree node until necessary, thereby avoiding unnecessary modifications on tree structures. In experiments, applying Dynfrs on Extremely Randomized Trees yields substantial improvements, achieving orders of magnitude faster unlearning performance and better predictive accuracy than existing machine unlearning methods for Random Forests.
