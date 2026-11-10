# Computer Use at the Edge of the Statistical Precipice

NeurIPS 2026 · main · application

正文包含金融领域数据、模型、实验或分领域评测。 主题：Banking & Customer Service / 银行业务与客户服务。

- 官方论文页：https://openreview.net/forum?id=We2oXEmu4W
- 摘要来源：https://neurips.cc/Downloads/2026
- 本地 PDF：[打开](../../pdfs/NeurIPS/2026/neurips-2026-We2oXEmu4W__Computer_Use_at_the_Edge_of_the_Statistical_Precipice.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_domain_data_or_experiment
- 主方向：Banking & Customer Service / 银行业务与客户服务
- 细分方向：Banking Dialogue & Intent / 银行对话与意图
- 技术方法标签：未明确标注
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

erarchical structure plugs directly into the evaluation methodology of Section 4. Fifteen apps across seven domains. The 15 applications span 7 real-world domains (Table 4, Appendix E): communication (Email, Messaging), financial services (Payment, Banking), shopping (E-Commerce, QwikShop, Auction), entertainment (Music, Video), on-demand services (Eats, Ryde), travel (Flight Booking, Transit), and smart living (Smart Home, Parking). Each application is a fully-featured React Native Android application, 6

## 原始摘要

Evaluating Computer Use Agents (CUAs) on interactive environments is fraught with methodological pitfalls that the field has yet to systematically address. We show that a 1MB replay script that blindly executes a recorded action sequence without ever observing the screen outperforms frontier models on prominent static benchmarks, and prove that its expected success rate is exactly equal to the source agent's pass@k in deterministic environments. We trace this and other failures to two root causes: non-principled environment design (static, unsandboxed, or unreliably verified environments) and non-principled evaluation methodology (naïve aggregation and misuse of pass@k for stateful UI interactions). To address the first, we propose PRISM, five design principles for CUA environments (privileged verification, realistic environments, integrity-checked configurations, sandboxed execution, and multifactorial variability) and instantiate them in DigiWorld, a benchmark of 15 realistic sandboxed mobile applications able to evaluate agents in over 3.2 million verified unique configurations. To address the second, we develop an aggregation framework pairing Wilson score intervals with hierarchical bootstrap, producing confidence intervals that correctly account for the nested structure of CUA benchmarks, as we empirically demonstrate. All together, we show that principled environment design and rigorous evaluation methodology are not optional refinements but prerequisites for meaningful CUA research.
