# Learning Monotonic Probabilities with a Generative Cost Model

ICML 2025 · main · application

正文包含金融数据、金融任务或金融领域评测。 主题：Credit & Financial Risk / 信贷与金融风险。

- 官方论文页：https://openreview.net/forum?id=VWjkpro9gv
- 摘要来源：https://icml.cc/virtual/2025/poster/45065
- 本地 PDF：[打开](../../pdfs/ICML/2025/icml-2025-VWjkpro9gv__Learning_Monotonic_Probabilities_with_a_Generative_Cost_Model.pdf)；版本：publisher_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Credit Scoring & Default / 信用评分与违约；Lending & Credit Data / 借贷与信贷数据应用
- 技术方法标签：Generative Modeling / 生成建模
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/tyxaaron/GCM](https://github.com/tyxaaron/GCM

## 纳入依据

AS dataset (Larson et al., 2016), y1 (denoted y1 ≺r.v. y2 ) if and only if Pr(y1 ≻ t) < the Diabetes dataset (Teboul), the Blog Feedback dataset Pr(y2 ≻ t) for any vector t ∈ Rn . (Buza, 2014), the Loan Defaulter dataset and the Auto MPG dataset (Quinlan, 1993). In most tasks, our model outper- forms existing approaches. Further ablation studies and time complexity analysis are available in the appendix. epiF1 The main contributions of our paper are summarized as follows: • We introduce a universal technique t

## 原始摘要

In many machine learning tasks, it is often necessary for the relationship between input and output variables to be monotonic, including both strictly monotonic and implicitly monotonic relationships. Traditional methods for maintaining monotonicity mainly rely on construction or regularization techniques, whereas this paper shows that the issue of strict monotonic probability can be viewed as a partial order between an observable revenue variable and a latent cost variable. This perspective enables us to reformulate the monotonicity challenge into modeling the latent cost variable. To tackle this, we introduce a generative network for the latent cost variable, termed the Generative Cost Model (**GCM**), which inherently addresses the strict monotonic problem, and propose the Implicit Generative Cost Model (**IGCM**) to address the implicit monotonic problem. We further validate our approach with a numerical simulation of quantile regression and conduct multiple experiments on public datasets, showing that our method significantly outperforms existing monotonic modeling techniques. The code for our experiments can be found at [https://github.com/tyxaaron/GCM](https://github.com/tyxaaron/GCM).
