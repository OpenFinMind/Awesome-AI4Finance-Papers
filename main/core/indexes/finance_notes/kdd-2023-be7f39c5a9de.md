# Mastering Stock Markets with Efficient Mixture of Diversified Trading Experts

KDD 2023 · Research Track · Main · core · long

- Official paper: https://doi.org/10.1145/3580305.3599424
- Research Track: https://kdd.org/kdd2023/wp-content/uploads/2023/08/toc.html
- Primary task: Trading & Microstructure / 交易与市场微观结构
- Tasks: Trading & Microstructure / 交易与市场微观结构
- Subtopics: Trading Strategies and Buy/Sell Decisions / 交易策略与买卖决策
- Methods: Uncertainty & Robustness / 不确定性与鲁棒性
- Financial evidence source: https://kdd.org/kdd2023/wp-content/uploads/2023/08/toc.html
- Long-paper evidence: regular Research full-paper track ([format policy](https://kdd.org/kdd2023/call-for-research-track-papers/)).

## Financial evidence

Quantitative stock investment is a fundamental financial task that highly relies on accurate prediction of market status and profitable investment decision making. Despite recent advances in deep learning (DL) have shown stellar performance on capturing trading opportunities in the stochastic stock market, the performance of existing DL methods is unstable with sensitivity to network initialization and hyperparameter selection. One major limitation of existing works is that investment decisions are made based on one individual neural network predictor with high uncertainty, which is inconsistent with the workflow in real-world trading firms. To tackle this limitation, we propose AlphaMix, a novel three-stage mixture-of-experts (MoE) framework for quantitative investment to mimic the efficient bottom-up hierarchical trading strategy design workflow of successful trading companies. In Stage one, we introduce an efficient ensemble learning method, whose computational and memory costs are significantly lower comparing to traditional ensemble methods, to train multiple groups of trading experts with personalised market understanding and trading styles. In Stage two, we collect diversified investment suggestions through building a pool of trading experts utilizing hyperparameter level and initialization level diversity of neural networks for post hoc ensemble construction. In Stage three, we design three different mechanisms, namely as-needed router, with-replacement selection and integrated expert soup, to dynamically pick experts from the expert pool, which takes the responsibility of a portfolio manager. Through extensive experiments on US and Chinese stock markets, we demonstrate that AlphaMix significantly outperforms many state-of-the-art baselines in terms of 7 popular

## Abstract

Quantitative stock investment is a fundamental financial task that highly relies on accurate prediction of market status and profitable investment decision making. Despite recent advances in deep learning (DL) have shown stellar performance on capturing trading opportunities in the stochastic stock market, the performance of existing DL methods is unstable with sensitivity to network initialization and hyperparameter selection. One major limitation of existing works is that investment decisions are made based on one individual neural network predictor with high uncertainty, which is inconsistent with the workflow in real-world trading firms. To tackle this limitation, we propose AlphaMix, a novel three-stage mixture-of-experts (MoE) framework for quantitative investment to mimic the efficient bottom-up hierarchical trading strategy design workflow of successful trading companies. In Stage one, we introduce an efficient ensemble learning method, whose computational and memory costs are significantly lower comparing to traditional ensemble methods, to train multiple groups of trading experts with personalised market understanding and trading styles. In Stage two, we collect diversified investment suggestions through building a pool of trading experts utilizing hyperparameter level and initialization level diversity of neural networks for post hoc ensemble construction. In Stage three, we design three different mechanisms, namely as-needed router, with-replacement selection and integrated expert soup, to dynamically pick experts from the expert pool, which takes the responsibility of a portfolio manager. Through extensive experiments on US and Chinese stock markets, we demonstrate that AlphaMix significantly outperforms many state-of-the-art baselines in terms of 7 popular financial criteria.

## Classification / 分类

- Primary task / 主方向: Financial Decision Making / 金融决策
- Primary subcategory / 主要子分类: Trading Strategies and Buy/Sell Decisions / 交易策略与买卖决策
- Related tasks / 关联方向: Financial Decision Making / 金融决策
- Subcategories / 子分类: Trading Strategies and Buy/Sell Decisions / 交易策略与买卖决策
- Methods / 技术方法: Uncertainty & Robustness / 不确定性与鲁棒性
- Review status / 核对状态: `inherited_evidence_mapping`
- [Definitions / 分类定义](../finance_taxonomy.md) · [Evidence / 分类依据](../../checks/finance_taxonomy/assignments.json)
