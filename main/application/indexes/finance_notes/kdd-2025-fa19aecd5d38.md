# $Hi-PNG:$ Efficient Interval-Filtering ANNS via Hierarchical Interval Partition Navigating Graph

KDD 2025 · Research Track · Main · application · long

- Official paper: https://doi.org/10.1145/3711896.3736997
- Research Track: https://kdd.org/kdd2025/research-track-papers-2/
- Primary task: Financial IR & RAG / 金融检索与RAG
- Tasks: Financial IR & RAG / 金融检索与RAG
- Subtopics: Financial Semantic Matching and Ranking / 金融语义匹配与排序
- Methods: Generative Modeling / 生成建模; Retrieval & RAG / 检索与RAG
- Financial evidence source: https://openalex.org/W4412877223
- Long-paper evidence: regular Research full-paper track ([format policy](https://kdd.org/kdd2025/research-track-call-for-papers/)).

## Financial evidence

gnificant speedups.We provide a theoretical analysis of the search space, demonstrating the superiority of our approach.Extensive experiments on eight datasets, including commonly used benchmarks and real-world stock price data, show that Hi-PNG outperforms four state-of-the-art graph-based ANNS baselines, achieving up to 15× acceleration while maintaining high precision.These results highlight Hi-PNG's effectiveness in solving the IF-ANNS problem.All codes and data generation are available at https://github.com/PUITAR/Hi-PNG.git.

## Abstract

Approximate nearest neighbor search (ANNS) is widely used to retrieve similar vectors from high-dimensional data.However, many real-world applications require additional interval filtering based on numerical constraints, such as stock price ranges.In this paper, we introduce interval-filtering ANNS (IF-ANNS), a novel yet general retrieval task where both base and query vectors are associated with numerical intervals.The goal is to retrieve nearest neighbors whose intervals are fully contained within the query interval.To efficiently address this problem, we propose Hierarchical Interval Partitioning Navigating Graph (Hi-PNG), a framework that hierarchically partitions the interval space to efficiently locate the search space, eliminating unnecessary computations and achieving significant speedups.We provide a theoretical analysis of the search space, demonstrating the superiority of our approach.Extensive experiments on eight datasets, including commonly used benchmarks and real-world stock price data, show that Hi-PNG outperforms four state-of-the-art graph-based ANNS baselines, achieving up to 15× acceleration while maintaining high precision.These results highlight Hi-PNG's effectiveness in solving the IF-ANNS problem.All codes and data generation are available at https://github.com/PUITAR/Hi-PNG.git.

## Classification / 分类

- Primary task / 主方向: Financial Retrieval / 金融检索
- Primary subcategory / 主要子分类: Financial Semantic Matching and Ranking / 金融语义匹配与排序
- Related tasks / 关联方向: Financial Retrieval / 金融检索
- Subcategories / 子分类: Financial Semantic Matching and Ranking / 金融语义匹配与排序
- Methods / 技术方法: Generative Modeling / 生成建模; Retrieval & RAG / 检索与RAG
- Review status / 核对状态: `contribution_evidence_review`
- [Definitions / 分类定义](../finance_taxonomy.md) · [Evidence / 分类依据](../../checks/finance_taxonomy/assignments.json)
