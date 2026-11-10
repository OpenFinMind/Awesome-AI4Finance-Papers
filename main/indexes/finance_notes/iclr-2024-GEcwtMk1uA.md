# Identifying the Risks of LM Agents with an LM-Emulated Sandbox

ICLR 2024 · main · application

正文包含金融数据、金融训练数据、金融任务评测或具体金融场景案例。 主题：Financial Agents / 金融Agent与决策；Financial Safety & Compliance / 金融安全与合规。

- 官方论文页：https://openreview.net/forum?id=GEcwtMk1uA
- 摘要来源：https://iclr.cc/virtual/2024/poster/19037
- 本地 PDF：[打开](../../pdfs/ICLR/2024/iclr-2024-GEcwtMk1uA__Identifying_the_Risks_of_LM_Agents_with_an_LM_Emulated_Sandbox.pdf)；版本：arxiv_author_version
- 金融依据类型：fulltext_financial_case_or_formal_model
- 主方向：Financial Safety & Compliance / 金融安全与合规
- 细分方向：Investment & Financial Research Agents / 投研与金融决策Agent；Financial Privacy & Security / 金融隐私与信息安全
- 技术方法标签：Language Models & LLM / 语言模型与LLM
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Language Model
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

(e.g., GPT-4) Agent Action - emu. tool exec. & states Send the annual financial report to Alice … - adv. emu. for red-teaming Evaluator

## 原始摘要

Recent advances in Language Model (LM) agents and tool use, exemplified by applications like ChatGPT Plugins, enable a rich set of capabilities but also amplify potential risks—such as leaking private data or causing financial losses. Identifying these risks is labor-intensive, necessitating implementing the tools, setting up the environment for each test scenario manually, and finding risky cases. As tools and agents become more complex, the high cost of testing these agents will make it increasingly difficult to find high-stakes, long-tail risks. To address these challenges, we introduce ToolEmu: a framework that uses an LM to emulate tool execution and enables scalable testing of LM agents against a diverse range of tools and scenarios. Alongside the emulator, we develop an LM-based automatic safety evaluator that examines agent failures and quantifies associated risks. We test both the tool emulator and evaluator through human evaluation and find that 68.8% of failures identified with ToolEmu would be valid real-world agent failures. Using our curated initial benchmark consisting of 36 high-stakes toolkits and 144 test cases, we provide a quantitative risk analysis of current LM agents and identify numerous failures with potentially severe outcomes. Notably, even the safest LM agent exhibits such failures 23.9% of the time according to our evaluator, underscoring the need to develop safer LM agents for real-world deployment.
