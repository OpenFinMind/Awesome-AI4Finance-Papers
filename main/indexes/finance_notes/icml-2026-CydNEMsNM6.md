# Learning the ESG Geometry with Domain Aware Language Models

ICML 2026 · main · core

以金融任务或金融数据为核心研究对象。 主题：Time Series / 时间序列；Financial NLP / 金融文本、情感与事件；ESG & Sustainable Finance / ESG与可持续金融。

- 官方论文页：https://openreview.net/forum?id=CydNEMsNM6
- 摘要来源：https://icml.cc/virtual/2026/poster/65502
- PDF 状态：access_blocked
- 金融依据类型：title_abstract_review
- 主方向：ESG & Sustainable Finance / ESG与可持续金融
- 细分方向：Representation & Foundation Models / 表征与基础模型；Sentiment & Stance / 情感与立场；ESG Disclosure & Greenwashing / ESG披露与漂绿
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Multimodal Learning / 多模态学习；Representation Learning / 表征学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：LLM；time series
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Current ESG solutions cannot model high-dimensional, multi-modal time series capturing the joint evolution of ESG risks, financial returns, news, and sentiment, even though this domain requires jointly reasoning over distinct numerical signals where both numerical proximity and semantic type must be preserved. / Trained on ESG, returns, news, and sentiment, the domain-aware LLM learns a representation space that enables accurate ESG forecasting, trajectory-based grouping, and latent-space search for superior asset selection and downstream application like portfolio rebalancing

## 原始摘要

Responsible investing aims to generate positive impact across Environment (E), Society (S), and Governance (G), and rating companies along these dimensions is now widespread, making ESG scores highly popular. Allocating retail capital with sustainability in mind could be transformational, yet it remains unclear how individual investors can do so in practice. Current ESG solutions cannot model high-dimensional, multi-modal time series capturing the joint evolution of ESG risks, financial returns, news, and sentiment, even though this domain requires jointly reasoning over distinct numerical signals where both numerical proximity and semantic type must be preserved. To bridge this gap, we introduce a novel domain-aware $\textbf{representation learning framework}$ that learns geometry-preserving representations for heterogeneous time series using value-aware tokens with block-wise $\textbf{orthogonal embeddings}$. To capture trajectory-level structure, we introduce $\textbf{FACET}$ tokens and train the model using a geometry-preserving loss. The resulting model jointly learns to forecast future values and to organize entities in a representation space that reflects their temporal evolution. Trained on ESG, returns, news, and sentiment, the domain-aware LLM learns a representation space that enables accurate ESG forecasting, trajectory-based grouping, and latent-space search for superior asset selection and downstream application like portfolio rebalancing
