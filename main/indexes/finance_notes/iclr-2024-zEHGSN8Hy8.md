# SetCSE: Set Operations using Contrastive Learning of Sentence Embeddings

ICLR 2024 · main · application

通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：Financial PhraseBank。 主题：Financial NLP / 金融文本、情感与事件；Banking & Customer Service / 银行业务与客户服务。

- 官方论文页：https://openreview.net/forum?id=zEHGSN8Hy8
- 摘要来源：https://iclr.cc/virtual/2024/poster/17387
- 本地 PDF：[打开](../../pdfs/ICLR/2024/iclr-2024-zEHGSN8Hy8__SetCSE_Set_Operations_using_Contrastive_Learning_of_Sentence_Embeddings.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Banking & Customer Service / 银行业务与客户服务
- 细分方向：Sentiment & Stance / 情感与立场；Banking Dialogue & Intent / 银行对话与意图
- 技术方法标签：Retrieval & RAG / 检索与RAG；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：contrastive；retrieval
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

6: Form (A, ⪯) and rank sentences in A in descending order To cover a diverse range of semantics, we employee the following datasets in this section: AG News Title and Description (AGT and AGD) (Zhang et al., 2015), Financial PhraseBank (FPB) (Malo et al., 2014), Banking77 (Casanueva et al., 2020), and Facebook Multilingual Task Oriented Dataset (FMTOD) (Schuster et al., 2018). We consider an extensive list of models for generating sentence embeddings, including encoder-only Transformer models such as BERT (Devlin et al., 2018) and RoBERTa (Liu et al., 2019b), their fine-tuned ve

## 原始摘要

Taking inspiration from Set Theory, we introduce SetCSE, an innovative information retrieval framework. SetCSE employs sets to represent complex semantics and incorporates well-defined operations for structured information querying under the provided context. Within this framework, we introduce an inter-set contrastive learning objective to enhance comprehension of sentence embedding models concerning the given semantics. Furthermore, we present a suite of operations, including SetCSE intersection, difference, and operation series, that leverage sentence embeddings of the enhanced model for complex sentence retrieval tasks. Throughout this paper, we demonstrate that SetCSE adheres to the conventions of human language expressions regarding compounded semantics, provides a significant enhancement in the discriminatory capability of underlying sentence embedding models, and enables numerous information retrieval tasks involving convoluted and intricate prompts which cannot be achieved using existing querying methods.
