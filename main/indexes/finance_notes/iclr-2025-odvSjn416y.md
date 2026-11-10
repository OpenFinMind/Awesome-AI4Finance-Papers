# Promptriever: Instruction-Trained Retrievers Can Be Prompted Like Language Models

ICLR 2025 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：FiQA。 主题：Financial IR & RAG / 金融检索与RAG。

- 官方论文页：https://openreview.net/forum?id=odvSjn416y
- 摘要来源：https://iclr.cc/virtual/2025/poster/28345
- 本地 PDF：[打开](../../pdfs/ICLR/2025/iclr-2025-odvSjn416y__Promptriever_Instruction_Trained_Retrievers_Can_Be_Prompted_Like_Language_Models.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Financial IR & RAG / 金融检索与RAG
- 细分方向：Retrieval, Embedding & Reranking / 检索、嵌入与重排
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Uncertainty & Robustness / 不确定性与鲁棒性；Retrieval & RAG / 检索与RAG
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：language models；retrieval
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

3.5 45.0 45.2 45.2 Dataset has dev/train set FEVER 48.1 7.4 45.3 82.9 85.3 85.3 82.8 82.8 82.8 FiQA 25.1 16.9 21.9 45.0 41.8 42.7 45.9 46.6 46.6 HotpotQA 56.9 54.6 54.6 68.8 66.4 67.9 69.2 69.5 69.5 NFCorpus 32.1 18.0 23.5 36.0 34.2 35.0 36.5 36.9 36.9

## 原始摘要

Instruction-tuned language models (LM) are able to respond to imperative commands, providing a more natural user interface compared to their base counterparts. In this work, we present Promptriever, the first retrieval model able to be prompted like an LM. To train Promptriever, we curate and release a new instance-level instruction training set from MS MARCO, spanning nearly 500k instances. Promptriever not only achieves strong performance on standard retrieval tasks, but also follows instructions. We observe: (1) large gains (reaching SoTA) on following detailed relevance instructions (+14.3 p-MRR / +3.1 nDCG on FollowIR), (2) significantly increased robustness to lexical choices/phrasing in the query+instruction (+12.9 Robustness@10 on InstructIR), and (3) the ability to perform hyper-parameter search via prompting to reliably improve retrieval performance (+1.4 average increase on BEIR). Promptriever demonstrates that retrieval models can be controlled with prompts on a per-query basis, setting the stage for future work aligning LM prompting techniques with information retrieval.
