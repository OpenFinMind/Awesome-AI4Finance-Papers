# GS-Fuse: Granger-Supervised Gated Fusion and Multi-Granularity Alignment for Event-Driven Financial Forecasting

KDD 2026 · Research Track · Main · core · long

- Official paper: https://doi.org/10.1145/3770855.3817927
- Research Track: https://kdd2026.kdd.org/papers/
- Primary task: Market Prediction / 股价、收益与波动率预测
- Tasks: Market Prediction / 股价、收益与波动率预测
- Subtopics: Stock Price and Return Prediction / 股票价格与收益预测
- Methods: Language Models & LLM / 语言模型与LLM; Causal Learning / 因果学习
- Financial evidence source: https://openalex.org/W7162791679
- Long-paper evidence: regular Research full-paper track ([format policy](https://kdd2026.kdd.org/research-track-call-for-papers/)).

## Financial evidence

Accurately forecasting the impact of salient financial events on markets is critical for investors and policymakers. Extensive experiments on real-world financial datasets show that GS-Fuse consistently outperforms state-of-the-art time-series and multimodal baselines across multiple assets and forecasting horizons.

## Abstract

Accurately forecasting the impact of salient financial events on markets is critical for investors and policymakers. However, existing multimodal time-series models typically fuse text and prices symmetrically, without an explicit way to decide when event text is truly predictive, and thus struggle to exploit the directional event-to-price structure and the heterogeneous roles of textual and price signals. In this work, we propose GS-Fuse, a multimodal event-based forecasting framework that employs (i) a Granger-supervised, causal-aware gated fusion module, which learns to open toward event text only when it provides incremental predictive value beyond historical prices, and (ii) a multi-granularity alignment mechanism that jointly aligns high-level event representations and fine-grained textual cues with future market trajectories. Built as a flexible, plug-and-play adapter on top of off-the-shelf large language models and time-series foundation models, GS-Fuse can be instantiated across diverse backbones and market settings. Extensive experiments on real-world financial datasets show that GS-Fuse consistently outperforms state-of-the-art time-series and multimodal baselines across multiple assets and forecasting horizons.

[PDF](../../pdfs/KDD/2026/kdd-2026-9b8ecdc7bdc5__GS-Fuse_Granger-Supervised_Gated_Fusion_and_Multi-Granularity_Alignment_for_Event-Driven_Financial_F.pdf)

Version: `arxiv` · SHA-256: `b644126c474131bea30276c05e3ac494cc05d178de71f168c260358e9cedb8b6`

## Classification / 分类

- Primary task / 主方向: Valuation Prediction / 估值预测
- Primary subcategory / 主要子分类: Stock Price and Return Prediction / 股票价格与收益预测
- Related tasks / 关联方向: Valuation Prediction / 估值预测
- Subcategories / 子分类: Stock Price and Return Prediction / 股票价格与收益预测
- Methods / 技术方法: Language Models & LLM / 语言模型与LLM; Causal Learning / 因果学习
- Review status / 核对状态: `inherited_evidence_mapping`
- [Definitions / 分类定义](../finance_taxonomy.md) · [Evidence / 分类依据](../../checks/finance_taxonomy/assignments.json)
