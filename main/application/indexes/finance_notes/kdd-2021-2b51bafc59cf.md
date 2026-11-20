# Fast and Accurate Partial Fourier Transform for Time Series Data

KDD 2021 · Research Track · Main · application · long

- Official paper: https://doi.org/10.1145/3447548.3467293
- Research Track: https://www.kdd.org/kdd2021/accepted-papers/toc.html
- Primary task: Time Series / 时间序列
- Tasks: Time Series / 时间序列
- Subtopics: Anomaly and Change-Point Detection / 异常检测与变点识别
- Methods:
- Financial evidence source: https://www.kdd.org/kdd2021/accepted-papers/toc.html
- Long-paper evidence: regular Research full-paper track ([format policy](https://www.kdd.org/calls/view/call-for-research-track-papers-kdd-2021)).

## Financial evidence

up for sufficiently small output sizes without sacrificing accuracy. In addition, we demonstrate the accuracy and efficacy of PFT on real-world anomaly detection, with interpretations of anomalies in stock price data.

## Abstract

Given a time-series vector, how can we efficiently detect anomalies? A widely used method is to use Fast Fourier transform (FFT) to compute Fourier coefficients, take first few coefficients while discarding the remaining small coefficients, and reconstruct the original time series to find points with large errors. Despite the pervasive use, the method requires to compute all of the Fourier coefficients which can be cumbersome if the input length is large or when we need to perform many FFT operations. In this paper, we propose Partial Fourier Transform (PFT), an efficient and accurate algorithm for computing only a part of Fourier coefficients. PFT approximates a part of twiddle factors (trigonometric constants) using polynomials, thereby reducing the computational complexity due to the mixture of many twiddle factors. We derive the asymptotic time complexity of PFT with respect to input and output sizes, and tolerance. We also show that PFT provides an option to set an arbitrary approximation error bound, which is useful especially when the fast evaluation is of utmost importance. Experimental results show that PFT outperforms the current state-of-the-art algorithms, with an order of magnitude of speedup for sufficiently small output sizes without sacrificing accuracy. In addition, we demonstrate the accuracy and efficacy of PFT on real-world anomaly detection, with interpretations of anomalies in stock price data.

## Classification / 分类

- Primary task / 主方向: Time Series / 时间序列
- Primary subcategory / 主要子分类: Anomaly and Change-Point Detection / 异常检测与变点识别
- Related tasks / 关联方向: Time Series / 时间序列
- Subcategories / 子分类: Anomaly and Change-Point Detection / 异常检测与变点识别
- Methods / 技术方法: Not labeled / 暂未标注
- Review status / 核对状态: `inherited_evidence_mapping`
- [Definitions / 分类定义](../finance_taxonomy.md) · [Evidence / 分类依据](../../checks/finance_taxonomy/assignments.json)
