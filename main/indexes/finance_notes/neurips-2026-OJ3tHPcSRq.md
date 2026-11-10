# Partially Performative Prediction

NeurIPS 2026 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：credit card。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=OJ3tHPcSRq
- 摘要来源：https://neurips.cc/Downloads/2026
- 本地 PDF：[打开](../../pdfs/NeurIPS/2026/neurips-2026-OJ3tHPcSRq__Partially_Performative_Prediction.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Financial Risk / 金融风险管理；Lending & Credit Data / 借贷与信贷数据应用
- 技术方法标签：Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

rticular the processed version from [29]. The dataset contains demographic and socioeconomic features xi ∈ R16 , including age, education, and credit history, and labels yi indicating whether a person defaulted on their credit card payment, for 30, 000 individuals. The learner aims to predict the individuals’ creditworthiness by minimizing a regularized logistic loss over an ℓ2 ball in d = 17 dimensions (one dimension corresponding to the intercept), after standardizing the features. The performative feedback is modeled as coming from strategic responses: an individual i res

## 原始摘要

Performative prediction studies feedback loops that arise when predictive models are deployed in consequential domains. In these settings, model updates can shape the population whose patterns they aim to predict, inducing a distribution shift that is *endogenous* to the learning system. This perspective departs from classical treatments of distribution shift, where shifts are typically modeled as *exogenous* changes in the data-generating process. Yet, in practice, distribution shift is rarely one or the other. Predictive models may influence future data through the decisions they support, while the world itself continues to drift for reasons beyond the learner’s control. We study *partially performative prediction*, a framework that captures both endogenous and exogenous sources of distribution shift. The framework generalizes performative prediction by allowing the data distribution to evolve both in response to the deployed model and according to an external, time-varying process. We extend the central notions of performative stability and performative optimality to this setting by defining online analogues that measure performance relative to the evolving partially performative environment. We analyze practical learning heuristics, including repeated retraining, and characterize when they successfully adapt to partially performative environments.
