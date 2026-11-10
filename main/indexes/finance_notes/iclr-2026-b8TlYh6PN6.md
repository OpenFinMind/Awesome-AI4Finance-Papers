# Distributional Equivalence in Linear Non-Gaussian Latent-Variable Cyclic Causal Models: Characterization and Learning

ICLR 2026 · main · application

正文包含金融领域的数据、模型、任务或独立金融评测。 主题：Financial QA & Reasoning / 金融问答与数值推理。

- 官方论文页：https://openreview.net/forum?id=b8TlYh6PN6
- 摘要来源：https://iclr.cc/virtual/2026/poster/10008640
- 本地 PDF：[打开](../../pdfs/ICLR/2026/iclr-2026-b8TlYh6PN6__Distributional_Equivalence_in_Linear_Non_Gaussian_Latent_Variable_Cyclic_Causal_Models_Characterization_a.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_data_model_or_task
- 主方向：Financial QA & Reasoning / 金融问答与数值推理
- 细分方向：Knowledge & Conversational QA / 知识与对话问答
- 技术方法标签：Causal Learning / 因果学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Causal；causal
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

roperties, Sun Hung Kai Properties, Wharf Holdings), 3 on utilities (CLP Holdings, HK & China Gas, HK Electric), and 3 on commerce (Hutchison, Swire Pacific ’A’, Cathay Pacific Airways). All of them were constituents of Hang Seng Index (HSI), and they were almost the largest companies of the Hong Kong stock market at the time. By applying glvLiNG on this dataset, we recovered an equivalence class of causal graphs containing 2 latent variables. The presentation (see Appendix C.3) of this equivalence class is shown in Figure 8. Here is a summary: the class consists of 19,008

## 原始摘要

Causal discovery with latent variables is a fundamental task. Yet most existing methods rely on strong structural assumptions, such as enforcing specific indicator patterns for latents or restricting how they can interact with others. We argue that a core obstacle to a general, structural-assumption-free approach is the lack of an equivalence characterization: without knowing what can be identified, one generally cannot design methods for how to identify it. In this work, we aim to close this gap for linear non-Gaussian models. We establish the graphical criterion for when two graphs with arbitrary latent structure and cycles are distributionally equivalent, that is, they induce the same observed distribution set. Key to our approach is a new tool, edge rank constraints, which fills a missing piece in the toolbox for latent-variable causal discovery in even broader settings. We further provide a procedure to traverse the whole equivalence class and develop an algorithm to recover models from data up to such equivalence. To our knowledge, this is the first equivalence characterization with latent variables in any parametric setting without structural assumptions, and hence the first structural-assumption-free discovery method. Code and an interactive demo are available at https://equiv.cc.
