# UDora: A Unified Red Teaming Framework against LLM Agents by Dynamically Hijacking Their Own Reasoning

ICML 2025 · main · application

正文包含明确金融数据、金融任务或金融案例；金融应用可属于通用方法的一个实验。 主题：Trading & Microstructure / 交易与市场微观结构；Financial Agents / 金融Agent与决策。

- 官方论文页：https://openreview.net/forum?id=pRmxQHgjb1
- 摘要来源：https://icml.cc/virtual/2025/poster/44008
- 本地 PDF：[打开](../../pdfs/ICML/2025/icml-2025-pRmxQHgjb1__UDora_A_Unified_Red_Teaming_Framework_against_LLM_Agents_by_Dynamically_Hijacking_Their_Own_Reasoning.pdf)；版本：publisher_version
- 金融依据类型：fulltext_financial_data_or_task
- 主方向：Financial Agents / 金融Agent与决策
- 细分方向：Trading & Execution / 交易策略与执行；Investment & Financial Research Agents / 投研与金融决策Agent
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Uncertainty & Robustness / 不确定性与鲁棒性；Optimization & Numerical Methods / 优化与数值方法
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Language Model；LLM；optimization
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：https://github.com/AI-secure/UDora.

## 纳入依据

oken probability distri- and AgentHarm—covering a range of scenarios includ- bution—given the current instruction augmented with ing online shopping, financial tasks, and general agent an initialized adversarial string. manipulation. Our approach ooutperforms all existing (2) Identify Positions for Inserting Noise: We then auto- baselines, and successfully attack a real-world agent. matically pinpoint several optimal positions in the agent’s current reasoning where we can insert some 2. Related Work “noise” (e.g., the name of a target item or a malicious Adversarial Attacks on LLMs. Attacking language mod- tool). Here, the response serve

## 原始摘要

Large Language Model (LLM) agents equipped with external tools have become increasingly powerful for complex tasks such as web shopping, automated email replies, and financial trading. However, these advancements amplify the risks of adversarial attacks, especially when agents can access sensitive external functionalities. Nevertheless, manipulating LLM agents into performing targeted malicious actions or invoking specific tools remains challenging, as these agents extensively reason or plan before executing final actions. In this work, we present UDora, a unified red teaming framework designed for LLM agents that dynamically hijacks the agent's reasoning processes to compel malicious behavior. Specifically, UDora first generates the model’s reasoning trace for the given task, then automatically identifies optimal points within this trace to insert targeted perturbations. The resulting perturbed reasoning is then used as a surrogate response for optimization. By iteratively applying this process, the LLM agent will then be induced to undertake designated malicious actions or to invoke specific malicious tools. Our approach demonstrates superior effectiveness compared to existing methods across three LLM agent datasets. The code is available at https://github.com/AI-secure/UDora.
