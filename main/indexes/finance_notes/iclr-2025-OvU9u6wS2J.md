# An Online Learning Theory of Trading-Volume Maximization

ICLR 2025 · main · core

以金融任务或金融数据为核心研究对象。 主题：Trading & Microstructure / 交易与市场微观结构。

- 官方论文页：https://openreview.net/forum?id=OvU9u6wS2J
- 摘要来源：https://iclr.cc/virtual/2025/poster/29793
- PDF 状态：access_blocked
- 金融依据类型：title_abstract_review
- 主方向：Trading & Microstructure / 交易与市场微观结构
- 细分方向：Trading & Execution / 交易策略与执行；Order Books & Market Impact / 订单簿与市场冲击
- 技术方法标签：未明确标注
- 分类说明：[打开](../finance_taxonomy.md)；逐条分类依据见 [分类记录](../../checks/finance_taxonomy/assignments.json)
- 方法关键词（来自摘要）：摘要未明确列出
- 数据 / 评测名称（题名和摘要可确认）：摘要未明确列出，具体金融依据见下文正文摘录
- 代码链接：摘要未提供可确认链接

## 纳入依据

We explore brokerage between traders in an online learning framework.At any round $t$, two traders meet to exchange an asset, provided the exchange is mutually beneficial.The broker proposes a trading price, and each trader tries to sell their asset or buy the asset from the other party, depending on whether the price is higher or lower than their private valuations.A trade happens if one trader is willing to sell and the other is willing to buy at the proposed price.Previous work provided guidance to a broker aiming at enhancing traders' total earnings by maximizing the *gain from trade*, defined as the sum of the traders' net utilities after each interaction.This classical notion of reward can be highly unfair to traders with small profit margins, and far from the real-life utility of the broker.For these reasons, we investigate how the broker should behave to maximize the trading volume, i.e., the *total number of trades*.We model the traders' valuations as an i.i.d.

## 原始摘要

We explore brokerage between traders in an online learning framework.At any round $t$, two traders meet to exchange an asset, provided the exchange is mutually beneficial.The broker proposes a trading price, and each trader tries to sell their asset or buy the asset from the other party, depending on whether the price is higher or lower than their private valuations.A trade happens if one trader is willing to sell and the other is willing to buy at the proposed price.Previous work provided guidance to a broker aiming at enhancing traders' total earnings by maximizing the *gain from trade*, defined as the sum of the traders' net utilities after each interaction.This classical notion of reward can be highly unfair to traders with small profit margins, and far from the real-life utility of the broker.For these reasons, we investigate how the broker should behave to maximize the trading volume, i.e., the *total number of trades*.We model the traders' valuations as an i.i.d. process with an unknown distribution.If the traders' valuations are revealed after each interaction (full-feedback), and the traders' valuations cumulative distribution function (cdf) is continuous, we provide an algorithm achieving logarithmic regret and show its optimality up to constants.If only their willingness to sell or buy at the proposed price is revealed after each interaction ($2$-bit feedback), we provide an algorithm achieving poly-logarithmic regret when the traders' valuations cdf is Lipschitz and show its near-optimality.We complement our results by analyzing the implications of dropping the regularity assumptions on the unknown traders' valuations cdf. If we drop the continuous cdf assumption, the regret rate degrades to $\Theta(\sqrt{T})$ in the full-feedback case, where $T$ is the time horizon. If we drop the Lipschitz cdf assumption, learning becomes impossible in the $2$-bit feedback case.
