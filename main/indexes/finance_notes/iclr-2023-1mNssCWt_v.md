# STaSy: Score-based Tabular data Synthesis

ICLR 2023 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：credit card。 主题：Credit & Financial Risk / 信贷与金融风险；Fraud & AML / 欺诈检测与反洗钱。

- 官方论文页：https://openreview.net/forum?id=1mNssCWt_v
- 摘要来源：https://iclr.cc/virtual/2023/poster/11517
- 本地 PDF：[打开](../../pdfs/ICLR/2023/iclr-2023-1mNssCWt_v__STaSy_Score_based_Tabular_data_Synthesis.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Credit & Financial Risk / 信贷与金融风险
- 细分方向：Credit Scoring & Default / 信用评分与违约；Financial Risk / 金融风险管理；Payment & Transaction Fraud / 支付与交易欺诈；Scams & Financial Misinformation / 诈骗与金融虚假信息；Lending & Credit Data / 借贷与信贷数据应用
- 技术方法标签：Generative Modeling / 生成建模；Tabular Learning / 表格学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：fine-tuning
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

is a binary classification dataset collected from European cardholders for credit card fraud detection. • Default (Lichman, 2013) is a binary classification dataset describing the information on credit card clients in Taiwan regarding default payments. • HTRU (Lyon, 2017) is a binary classification dataset that describes a sample of pulsar candidates collected during the High Time Resolution Universe Survey. • Magic (Bock, 2007) is a binary classification dataset that simulates the registration of high-energy gamma par

## 原始摘要

Tabular data synthesis is a long-standing research topic in machine learning. Many different methods have been proposed over the past decades, ranging from statistical methods to deep generative methods. However, it has not always been successful due to the complicated nature of real-world tabular data. In this paper, we present a new model named $\textbf{S}$core-based $\textbf{Ta}$bular data $\textbf{Sy}$nthesis ($\texttt{STaSy}$) and its training strategy based on the paradigm of score-based generative modeling. Despite the fact that score-based generative models have resolved many issues in generative models, there still exists room for improvement in tabular data synthesis. Our proposed training strategy includes a self-paced learning technique and a fine-tuning strategy, which further increases the sampling quality and diversity by stabilizing the denoising score matching training. Furthermore, we also conduct rigorous experimental studies in terms of the generative task trilemma: sampling quality, diversity, and time. In our experiments with 15 benchmark tabular datasets and 7 baselines, our method outperforms existing methods in terms of task-dependant evaluations and diversity.
