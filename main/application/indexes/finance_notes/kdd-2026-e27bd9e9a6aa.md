# Parallel Complex Diffusion for Scalable Time Series Generation

KDD 2026 · Research Track · Main · application · long

- Official paper: https://doi.org/10.1145/3770855.3817791
- Research Track: https://kdd2026.kdd.org/papers/
- Primary task: Time Series / 时间序列
- Tasks: Time Series / 时间序列
- Subtopics: Sequence Generation and Augmentation / 序列生成与数据增强
- Methods: Diffusion & Flow / 扩散与流模型; Generative Modeling / 生成建模
- Financial evidence source: https://arxiv.org/pdf/2602.17706
- Long-paper evidence: regular Research full-paper track ([format policy](https://kdd2026.kdd.org/research-track-call-for-papers/)).

## Financial evidence

le unitarity ensures stability, the Hermitian Symmetry of real- Datasets. For the conditional task, we employ ETTh1 & ETTm1 [24], valued signals enables significant state-space compression. ECL [19], Exchange [9], and Air Quality [3]. For the uncondiFor any real vector x ∈ R𝐿 , its spectrum satisfies X𝑘 = X̄𝐿−𝑘 . tional task, we synthesize multivariate series on ETTh1, Stocks [3], By discarding the redundant negative frequencies, we define the Sines [22], and Air Quality (Details in Table 2). Compressed Frequency State: 6.2 Experimental Setting X̃ = [X0, . . . , X𝐾 ] ⊤ ∈ C𝐾 , where 𝐾 = ⌊𝐿/2⌋. (24) Evaluation Metrics. We evaluate unconditional generation using This reduction halves the modeling dimensionality. However, to four metrics: (1) Discriminative Score [21]: classification accuracy maintain

## Abstract

Diffusion models learn data distributions indirectly through denoising, making the difficulty of generative modeling closely tied to the dependency structure of data. For time series, strong temporal dependence forces the noise / score estimator to recover highly entangled cross-time relationships, leading to the curse of entanglement. We mitigate this burden by changing the topology of the diffusion space: the Discrete Fourier Transform (DFT) decomposes temporal dependencies into spectral modes, diagonalizing second-order dependency structure and better aligning the data manifold with isotropic Gaussian noise and homogeneous diffusion dynamics. However, existing frequency-aware diffusion methods mainly use the DFT to design estimator blocks under temporal DDPM/SDE frameworks, while frequency-native diffusion paths face a mathematical barrier from complex-valued dynamics. We propose PaCoDi (Parallel Complex Diffusion), a frequency-native diffusion framework that constructs the diffusion path in the spectral domain while replacing the complex-valued estimator with parallel real-valued estimators for real and imaginary components. Theoretically, we prove the statistical orthogonality of spectral Gaussian noise, establish quadrature forward transitions and conditional reverse factorization, and extend discrete PaCoDi to continuous-time spectral SDEs through a Spectral Wiener Process. We further introduce a Mean Field Theory approximation with an Interactive Correction Branch to handle marginal coupling, and exploit Hermitian symmetry to reduce 50% attention FLOPs without information loss. Extensive experiments on unconditional and conditional time series generation demonstrate superior generative quality and computational efficiency against 5 SOTA baselines in 5 benchmarks, respectively. Code is available at https://github.com/RongyaoCai/PaCoDi. Full proofs are available at https://arxiv.org/abs/2602.17706.

[PDF](../../pdfs/KDD/2026/kdd-2026-e27bd9e9a6aa__Parallel_Complex_Diffusion_for_Scalable_Time_Series_Generation.pdf)

Version: `arxiv` · SHA-256: `d86e5f63e0a5f366c2b3c629a4d572df8d7628f4a71c40d1599cde5b4393fcda`

## Classification / 分类

- Primary task / 主方向: Time Series / 时间序列
- Primary subcategory / 主要子分类: Sequence Generation and Augmentation / 序列生成与数据增强
- Related tasks / 关联方向: Time Series / 时间序列
- Subcategories / 子分类: Sequence Generation and Augmentation / 序列生成与数据增强
- Methods / 技术方法: Diffusion & Flow / 扩散与流模型; Generative Modeling / 生成建模
- Review status / 核对状态: `inherited_evidence_mapping`
- [Definitions / 分类定义](../finance_taxonomy.md) · [Evidence / 分类依据](../../checks/finance_taxonomy/assignments.json)
