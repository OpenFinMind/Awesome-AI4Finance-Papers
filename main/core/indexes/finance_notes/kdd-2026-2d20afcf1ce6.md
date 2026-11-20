# Disentangled Dual-Granularity Learning for Market-Adaptive Stock Return Forecasting under Non-Stationary Environments

KDD 2026 · Research Track · Main · core · long

- Official paper: https://doi.org/10.1145/3770855.3817765
- Research Track: https://kdd2026.kdd.org/papers/
- Primary task: Market Prediction / 股价、收益与波动率预测
- Tasks: Market Prediction / 股价、收益与波动率预测
- Subtopics: Stock Price and Return Prediction / 股票价格与收益预测; Earnings, Revenue and Fundamental Prediction / 盈利、营收与基本面预测
- Methods:
- Financial evidence source: https://openalex.org/W7197004068
- Long-paper evidence: regular Research full-paper track ([format policy](https://kdd2026.kdd.org/research-track-call-for-papers/)).

## Financial evidence

Deep learning has emerged as a prominent paradigm in stock return forecasting, demonstrating remarkable capabilities in extracting non-linear patterns from historical stock data. However, existing approaches often process stock features as a monolithic input with fixed temporal receptive fields. Extensive experiments confirm that DDGL-Net outperforms state-of-the-art baselines on real-world stock datasets, validating the effectiveness of disentangled modeling and regime-aware adaptation.

## Abstract

Deep learning has emerged as a prominent paradigm in stock return forecasting, demonstrating remarkable capabilities in extracting non-linear patterns from historical stock data. However, existing approaches often process stock features as a monolithic input with fixed temporal receptive fields. This structural inflexibility fails to distinguish transient microstructure fluctuations and persistent long-term trends, resulting in entangled representations that impede adaptation to non-stationary environments. To address these issues, we propose the Disentangled Dual-Granularity Learning Network (DDGL-Net) to decouple and integrate diverse temporal signals. Specifically, we first construct a Disentangled Dual-Granularity Encoder (DDGE) to isolate fine-grained short-term and coarse-grained long-term features via parallel streams. To fuse dual-granularity temporal representations, we introduce a Market-Adaptive Contextual Modulator (MACM) as a regime-aware filter, which leverages global market context to dynamically reweight granularity contributions. Recognizing that input modulation alone is insufficient for the non-stationary latent-to-return mapping, we devise a Hybrid Residual Mixture of Experts (HR-MoE) predictor to decompose forecasts into stable consensus and adaptive residuals, ensuring resilient performance across shifting regimes. Extensive experiments confirm that DDGL-Net outperforms state-of-the-art baselines on real-world stock datasets, validating the effectiveness of disentangled modeling and regime-aware adaptation.

## Classification / 分类

- Primary task / 主方向: Valuation Prediction / 估值预测
- Primary subcategory / 主要子分类: Stock Price and Return Prediction / 股票价格与收益预测
- Related tasks / 关联方向: Valuation Prediction / 估值预测
- Subcategories / 子分类: Stock Price and Return Prediction / 股票价格与收益预测; Earnings, Revenue and Fundamental Prediction / 盈利、营收与基本面预测
- Methods / 技术方法: Not labeled / 暂未标注
- Review status / 核对状态: `inherited_evidence_mapping`
- [Definitions / 分类定义](../finance_taxonomy.md) · [Evidence / 分类依据](../../checks/finance_taxonomy/assignments.json)
