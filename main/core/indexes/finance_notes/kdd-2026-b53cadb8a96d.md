# Bayesian Robust Financial Trading with Adversarial Synthetic Market Data

KDD 2026 · Research Track · Main · core · long

- Official paper: https://doi.org/10.1145/3770854.3780175
- Research Track: https://kdd2026.kdd.org/papers/
- Primary task: Trading & Microstructure / 交易与市场微观结构
- Tasks: Trading & Microstructure / 交易与市场微观结构
- Subtopics: Trading Strategies and Buy/Sell Decisions / 交易策略与买卖决策
- Methods: Generative Modeling / 生成建模; Uncertainty & Robustness / 不确定性与鲁棒性
- Financial evidence source: https://openalex.org/W7161812513
- Long-paper evidence: regular Research full-paper track ([format policy](https://kdd2026.kdd.org/research-track-call-for-papers/)).

## Financial evidence

Algorithmic trading relies on machine learning models to make trading decisions. On the policy side, to learn robust policy against market fluctuations, we cast the trading process as a two-player zero-sum Bayesian Markov game, wherein an adversarial agent simulates shifting regimes by perturbing macroeconomic indicators in the macro-conditioned generator, while the trading agent—guided by a quantile belief network—maintains and updates its belief over hidden market states. The trading agent seeks a Robust Perfect Bayesian Equilibrium via Bayesian neural fictitious self-play, stabilizing learning under adversarial market perturbations. Extensive experiments on 9 financial instruments demonstrate that our framework outperforms 9 state-of-the-art baselines. In extreme events like the COVID pandemic, our method shows improved profitability and risk management, offering a reliable solution for trading under uncertain and rapidly shifting market dynamics.

## Abstract

Algorithmic trading relies on machine learning models to make trading decisions. Despite strong in-sample performance, these models often degrade when confronted with evolving real-world market regimes, which can shift dramatically due to macroeconomic changes—e.g., monetary policy updates or unanticipated fluctuations in participant behavior. We identify two core challenges that perpetuate this mismatch: (1) insufficient robustness in existing policy against uncertainties in high-level market fluctuations, and (2) the absence of a realistic and diverse simulation environment for training, leading to policy overfitting. To address these issues, we propose a Bayesian Robust Framework that systematically integrates a macro-conditioned generative model with robust policy learning. On the data side, to generate realistic and diverse data, we propose a macro-conditioned GAN-based generator that leverages macroeconomic indicators as primary control variables, synthesizing data with faithful temporal, cross-instrument, and macro correlations. On the policy side, to learn robust policy against market fluctuations, we cast the trading process as a two-player zero-sum Bayesian Markov game, wherein an adversarial agent simulates shifting regimes by perturbing macroeconomic indicators in the macro-conditioned generator, while the trading agent—guided by a quantile belief network—maintains and updates its belief over hidden market states. The trading agent seeks a Robust Perfect Bayesian Equilibrium via Bayesian neural fictitious self-play, stabilizing learning under adversarial market perturbations. Extensive experiments on 9 financial instruments demonstrate that our framework outperforms 9 state-of-the-art baselines. In extreme events like the COVID pandemic, our method shows improved profitability and risk management, offering a reliable solution for trading under uncertain and rapidly shifting market dynamics.

[PDF](../../pdfs/KDD/2026/kdd-2026-b53cadb8a96d__Bayesian_Robust_Financial_Trading_with_Adversarial_Synthetic_Market_Data.pdf)

Version: `arxiv` · SHA-256: `d9e8e90399ac93bc93efc4331ac7576920b6b5120ee86c0e4263528f0bb33a82`

## Classification / 分类

- Primary task / 主方向: Financial Decision Making / 金融决策
- Primary subcategory / 主要子分类: Trading Strategies and Buy/Sell Decisions / 交易策略与买卖决策
- Related tasks / 关联方向: Financial Decision Making / 金融决策
- Subcategories / 子分类: Trading Strategies and Buy/Sell Decisions / 交易策略与买卖决策
- Methods / 技术方法: Generative Modeling / 生成建模; Uncertainty & Robustness / 不确定性与鲁棒性
- Review status / 核对状态: `inherited_evidence_mapping`
- [Definitions / 分类定义](../finance_taxonomy.md) · [Evidence / 分类依据](../../checks/finance_taxonomy/assignments.json)
