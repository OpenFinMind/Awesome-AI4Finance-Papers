# KDD Research Track screening / KDD Research Track 筛查

This addition covers the official **2017–2026 KDD Research Track** lists, including both 2026 cycles. Research papers enter `main/`; KDD has no Findings collection here. Short papers, Applied Data Science / ADS, Datasets & Benchmarks, workshops, demos, tutorials and invited entries are outside this addition.

本次覆盖 **2017–2026 年 KDD Research Track** 官方名单，2026 年包含两个周期。收录论文进入 `main/`，不向 Findings 添加 KDD 条目；短文、ADS、Datasets & Benchmarks、研讨会、演示、教程及邀请项目均不在范围内。

| Year / 年份 | Official Research records / 官方条目 | Admitted / 收录 | Track and format evidence / 类别与篇幅依据 |
|---|---:|---:|---|
| 2017 | 130 | 3 | [Research list](https://www.kdd.org/kdd2017/accepted-papers) · [CFP](https://www.kdd.org/kdd2017/announcements/view/kdd-2017-call-for-research-papers) |
| 2018 | 181 | 4 | [Research list](https://www.kdd.org/kdd2018/accepted-papers) · [CFP](https://www.kdd.org/kdd2018/calls/view/kdd-2018-call-for-research-papers) |
| 2019 | 174 | 4 | [Research list](https://www.kdd.org/kdd2019/proceedings) · [CFP](https://www.kdd.org/kdd2019/calls/view/kdd-2019-call-for-research-papers) |
| 2020 | 217 | 5 | [Research list](https://www.kdd.org/kdd2020/proceedings/) · [CFP](https://www.kdd.org/kdd2020/calls/view/kdd-2020-call-for-research-papers) |
| 2021 | 239 | 14 | [Research list](https://www.kdd.org/kdd2021/accepted-papers/toc.html) · [CFP](https://www.kdd.org/calls/view/call-for-research-track-papers-kdd-2021) |
| 2022 | 253 | 10 | [Research list](https://www.kdd.org/kdd2022/toc.html) · [CFP](https://www.kdd.org/kdd2022/cfpResearch.html) |
| 2023 | 313 | 9 | [Research list](https://kdd.org/kdd2023/wp-content/uploads/2023/08/toc.html) · [CFP](https://kdd.org/kdd2023/call-for-research-track-papers/) |
| 2024 | 411 | 20 | [Research list](https://kdd.org/kdd2024/research-track-papers/) · [CFP](https://kdd.org/kdd2024/research-track-call-for-papers/) |
| 2025 | 552 | 28 | [Research list](https://kdd.org/kdd2025/research-track-papers-2/) · [CFP](https://kdd.org/kdd2025/research-track-call-for-papers/) |
| 2026 | 785 | 37 | [Research list](https://kdd2026.kdd.org/papers/) · [CFP](https://kdd2026.kdd.org/research-track-call-for-papers/) |
| Total / 合计 | 3255 | 134 | |

## Sources and paper length / 来源与长文依据

The [source manifest](source_manifest.json) records retrieval URLs, timestamps and SHA-256 for every compressed source. [Official Research records](records.json) are parsed independently of awards and presentation format. For mixed proceedings, only the explicitly marked Research section is parsed; for 2026, only `track == rtp` in both cycle lists is retained. Crossref, OpenAlex and Semantic Scholar supplement DOI, abstract and author-PDF locations; they do not establish track membership.

[来源清单](source_manifest.json)记录全部缓存的 URL、时间和 SHA-256。混合论文集中仅解析明确的 Research 栏，2026 年仅保留两个周期中 `track == rtp` 的条目。Crossref、OpenAlex 和 Semantic Scholar 只补充 DOI、摘要和作者公开 PDF 地址，不用于认定发表轨道。

Long-paper eligibility uses the regular Research full-paper track and the corresponding year's official call for papers, preserved separately for each year. It is not inferred from the total number of PDF pages. Per-paper [admission evidence](admitted_records.json) links both the official Research list and its format policy.

长文属性依据常规 Research full-paper track 及逐年官方征稿格式要求，保留对应缓存，不以含附录和参考文献的 PDF 总页数推断。逐篇[收录依据](admitted_records.json)同时记录 Research 名单及篇幅政策。

## Financial screening / 金融筛查

All 3,255 Research records are inventoried; 3,209 have abstracts and 3,208 have resolved DOIs. The versioned queries in [collect_kdd.py](../../../scripts/collect_kdd.py) retrieve direct financial terms and adjacent methods, including forecasting, tabular learning, fairness and anomaly detection. Records initially missing abstracts also enter the targeted queue. Query matches produce candidates, not admissions.

全部 3,255 条 Research 记录进入台账，其中 3,209 条具备摘要，3,208 条匹配 DOI。候选检索包含直接金融线索及预测、表格学习、公平性、异常检测等邻近方法；初始缺失摘要的记录也进入候选队列。命中查询不等于正式收录。

The [candidate queue](candidate_queue.json) contains 852 records. Accessible original author/publisher PDFs were inspected for 404 candidates; [inspection results](fulltext_results.json) preserve source URLs, identity checks, excerpts and hashes. Title-token overlap is checked before a PDF can be copied. The [reviewed admissions](review_decisions.json) require a direct financial research task (`core`) or substantive financial data, experiments, modeling or business cases (`application`). General forecasting and fairness papers qualify only with actual financial evidence. Dataset identity can be established using benchmark-author documentation, with that additional evidence preserved in the decision.

[候选队列](candidate_queue.json)包含 852 篇，其中 404 篇取得公开原文并检查，[正文检查记录](fulltext_results.json)保留地址、题名身份检查、片段和哈希。[人工复核的收录决定](review_decisions.json)区分金融核心研究和包含实质金融数据、实验、建模或业务案例的通用方法；金融基准的领域身份另由基准作者文档核实并记录。

There are **134 admissions: 43 core and 91 application**, with 96 local PDFs and 38 metadata-only records linked to official papers. Funding, affiliations, passing examples, citations, advertising ROI, memory banks, credit assignment and nonfinancial meanings of trading/alpha are insufficient. A financial dataset mentioned only in related work is insufficient. Main-body evidence is preferred; explicitly reviewed experimental appendix tables are also valid evidence, with benchmark mapping recorded where needed.

本次收录 **134 篇：金融核心研究 43 篇、金融应用 91 篇**，其中 96 篇有本地 PDF，其余 38 篇保留元数据和官方论文链接。资助、单位、背景举例、引用文献、广告 ROI、memory bank、credit assignment 以及非金融含义的 trading/alpha 均不足以单独支持收录；仅在相关工作提及金融基准也不满足要求。优先采用主体证据，明确复核的附录实验表亦可作为依据。

This is corpus-wide metadata screening with targeted full-text inspection, not a claim that every source paper has been read in full or that all financial applications have been recovered. Unavailable full texts and negative queries do not prove irrelevance. Author manuscripts can differ from publisher versions. The [combined inventory](../screening_inventory.csv.gz) records unconfirmed and unavailable candidates separately from admissions.

这是全量元数据筛查与定向正文复核，不代表已逐篇通读全部来源或保证零遗漏。未取得正文或查询未命中不能证明论文不相关；作者稿可能与出版版本不同。[总台账](../screening_inventory.csv.gz)分别记录收录、未确认和待正文核查状态。

## Reproduction and validation / 复现与验证

The preserved sources and explicit decisions are the reproducible inputs. [apply_kdd_update.py](../../../scripts/apply_kdd_update.py) applies reviewed admissions; [build_kdd_audit.py](../../../scripts/build_kdd_audit.py) builds this audit. Existing Main and Findings CSV, JSONL and financial assignments are bound to [baseline hashes](baseline_record_hashes.json).

保留的来源与明确收录决定构成可复现输入。应用脚本只导入已复核条目；[原记录哈希](baseline_record_hashes.json)用于逐项确认历史 Main / Findings 元数据和金融分类未被改动。

[verify_kdd.py](../../../scripts/verify_kdd.py) reparses official Research sources, checks per-year policy links, preserved hashes, decisions, PDF identity and catalog assignments, and verifies the complete KDD inventory. Results: [KDD validation](validation.json), [all-track validation](../validation.json).
