# UniDoc: Unified Pretraining Framework for Document Understanding

NeurIPS 2021 · main · application

正文包含金融数据、金融任务或金融领域评测。 主题：Document AI / 票据、财报与图表理解。

- 官方论文页：https://openreview.net/forum?id=UMcd6l1msUK
- 摘要来源：https://neurips.cc/virtual/2021/poster/28496
- 本地 PDF：[打开](../../pdfs/NeurIPS/2021/neurips-2021-UMcd6l1msUK__UniDoc_Unified_Pretraining_Framework_for_Document_Understanding.pdf)；版本：publisher_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Document AI / 票据、财报与图表理解
- 细分方向：Receipts, Invoices & OCR / 票据发票与OCR
- 技术方法标签：Transformer / Transformer模型；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Transformer
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

7 3 7 results into text regions. We think document RVL-CDIP [8] Misc 400K 7 7 7 3 image pretraining should be treated differently CORD [7] Receipt 1K 3 3 3 7 than sequence-based pretraining in NLP, since FUNSD [27] Form 0.2K 3 3 3 7 the words in the document (2D) are arranged PubLayNet [28] Article 347K 3 3 7 7 according to spatial layouts, while the words in NLP corpora are sequential (1D). Considering the special characteristics of d

## 原始摘要

Document intelligence automates the extraction of information from documents and supports many business applications. Recent self-supervised learning methods on large-scale unlabeled document datasets have opened up promising directions towards reducing annotation efforts by training models with self-supervised objectives. However, most of the existing document pretraining methods are still language-dominated. We present UDoc, a new unified pretraining framework for document understanding. UDoc is designed to support most document understanding tasks, extending the Transformer to take multimodal embeddings as input. Each input element is composed of words and visual features from a semantic region of the input document image. An important feature of UDoc is that it learns a generic representation by making use of three self-supervised losses, encouraging the representation to model sentences, learn similarities, and align modalities. Extensive empirical analysis demonstrates that the pretraining procedure learns better joint representations and leads to improvements in downstream tasks.
