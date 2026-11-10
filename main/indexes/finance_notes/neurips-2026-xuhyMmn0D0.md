# Market Regime Council for Dynamic Credit Assignment in Multi-Agent LLM  Decision Systems

NeurIPS 2026 · main · core

研究金融业务、金融市场或金融系统中的具体问题。 主题：Portfolio & Investment / 投资组合与投资管理；Trading & Microstructure / 交易与市场微观结构；Financial Agents / 金融Agent与决策。

- 官方论文页：https://openreview.net/forum?id=xuhyMmn0D0
- 摘要来源：https://neurips.cc/Downloads/2026
- 本地 PDF：[打开](../../pdfs/NeurIPS/2026/neurips-2026-xuhyMmn0D0__Market_Regime_Council_for_Dynamic_Credit_Assignment_in_Multi_Agent_LLM_Decision_Systems.pdf)；版本：arxiv_author_version
- 金融依据类型：title_abstract_financial_task_or_data
- 主方向：Portfolio & Investment / 投资组合与投资管理
- 细分方向：Portfolio Selection & Optimization / 组合选择与优化；Trading & Execution / 交易策略与执行；Investment & Financial Research Agents / 投研与金融决策Agent
- 技术方法标签：Language Models & LLM / 语言模型与LLM；Causal Learning / 因果学习
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：Bayesian；causal；LLM；Multi-agent；multi-agent
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

Multi-agent LLM decision systems for portfolio management still lack a principled way to assign credit across specialist agents, remain vulnerable to cold-start dominance under regime shifts, and offer limited transparency into how final allocations are formed.

## 原始摘要

Multi-agent LLM decision systems for portfolio management still lack a principled way to assign credit across specialist agents, remain vulnerable to cold-start dominance under regime shifts, and offer limited transparency into how final allocations are formed.  We propose Market Regime Council (MRC), a cooperative multi-agent decision system that computes exact Shapley credits across all single, pairwise, and Grand-coalition outputs for online agent weighting. Instantiated with $N{=}3$ specialist agents, at each trading period, MRC recomputes coalition-based Shapley weights from exponentially weighted performance histories, uses a Bayesian adaptive mixture to stabilize early periods, applies regime-dependent multipliers to adjust agent authority, and records each rebalance through a five-layer causal trace. Over 1,037 trading days across 13 crypto assets and five seeds, MRC achieves a Sharpe ratio of 1.51 and a cumulative return of 440.1\%, ranking first on CR, SR, and IR among active baselines and attaining the lowest MDD among active methods. Ablation results show that the gains come from Shapley-weighted integration across coalition outputs rather than from any single stage in isolation. Code and demo data are included in the supplementary material.
