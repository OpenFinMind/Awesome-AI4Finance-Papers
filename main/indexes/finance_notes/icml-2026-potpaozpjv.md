# Reward Shaping Control Variates for Off-Policy Evaluation Under Sparse Rewards

ICML 2026 · main · application

通用方法在金融任务、数据或明确案例上开展应用验证。 主题：Trading & Microstructure / 交易与市场微观结构。

- 官方论文页：https://openreview.net/forum?id=potpaozpjv
- 摘要来源：https://icml.cc/virtual/2026/poster/61480
- PDF 状态：access_blocked
- 金融依据类型：title_abstract_review
- 主方向：Trading & Microstructure / 交易与市场微观结构
- 细分方向：Trading & Execution / 交易策略与执行
- 技术方法标签：Reinforcement Learning / 强化学习；Uncertainty & Robustness / 不确定性与鲁棒性
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：reinforcement learning
- 数据 / 评测名称（题名和摘要可确认）：DOW-30
- 代码链接：摘要未提供可确认链接

## 纳入依据

Empirically, we provide a systematic regime map across synthetic chains, a cancer simulator, 5 single-stock and 1 multi-stock DOW-30 trading environments and an ICU-sepsis benchmark showing that shaping-based OPE consistently outperforms DR in sparse-reward settings, while a hybrid estimator achieves state-of-the-art performance across sparse, noisy, and misspecified environments.

## 原始摘要

Off-policy evaluation (OPE) is essential for deploying reinforcement learning in safety-critical settings, yet existing estimators such as importance sampling and doubly robust (DR) often exhibit prohibitively high variance when rewards are sparse. In this work, we introduce Reward-Shaping Control Variates, a new family of unbiased estimators that leverage potential-based reward shaping to construct additional zero-mean control variates. We prove that shaped estimators always yields valid variance reduction, and that combining shaping-based and Q-based control variates strictly expands the variance-reduction subspace beyond DR and its minimax variant MRDR. Empirically, we provide a systematic regime map across synthetic chains, a cancer simulator, 5 single-stock and 1 multi-stock DOW-30 trading environments and an ICU-sepsis benchmark showing that shaping-based OPE consistently outperforms DR in sparse-reward settings, while a hybrid estimator achieves state-of-the-art performance across sparse, noisy, and misspecified environments. Our results highlight reward shaping as a powerful and interpretable tool for robust OPE, offering both theoretical guarantees and practical improvements in domains where standard estimators fail.
