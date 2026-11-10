# Screening audit / 筛查审计

This audit separates **publication track**, **long-paper eligibility**, **financial inclusion**, and **financial-task classification**. Main and Findings are independent admitted collections. Awards and presentation format are not admission filters. The working date is 2026-11-10; the original five-venue Main literature snapshot is 2026-11-02.

本审计将**发表类别、长文属性、金融收录和金融任务分类**分别记录。Main 与 Findings 独立存储，不以获奖或报告形式作为收录门槛。本轮工作日期为 2026-11-10，原始五会 Main 文献快照为 2026-11-02。

## Source coverage / 来源覆盖

| Source / 来源 | Records / 条目 | Evidence / 依据 |
|---|---:|---|
| ICML, ICLR, ACL, EMNLP, NeurIPS Main | 85,756 | [Preserved metadata source and SHA-256](main_sources.json); [initial full-universe coverage](../../main/checks/initial_screening/coverage.csv) |
| AAAI publisher records within 2017–2026 volumes | 21,938 | [Publisher source manifest](../../main/checks/aaai_expansion/source_manifest.json); [track rules](../../main/checks/aaai_expansion/track_rules.json) |
| ACL / EMNLP Findings, 2020–2026 | 13,578 | [Official XML sources and SHA-256](findings_sources.json); [cached XML](../../findings/sources/) |
| Total inventoried records | 121,272 | [One disposition per record, CSV gzip](screening_inventory.csv.gz) |

The AAAI raw responses contain 22,308 unique DOI records. 370 belong to older volumes outside 2017–2026 despite later Crossref publication/deposit dates, so they are outside the in-scope inventory. The 21,938 retained AAAI publisher records include special and other tracks; admission separately requires main-track evidence. For mixed legacy volumes, the historical main-membership list verifies the reviewed candidate subset, not all noncandidate legacy articles. `other_or_unverified` in the inventory therefore does not imply every such article is outside Main.

AAAI 原始响应含 22,308 个唯一 DOI，其中 370 个属于 2017 年以前的卷次，仅 Crossref 发表或登记日期较晚，故不进入本轮年份范围。保留的 21,938 条出版社记录包含特殊轨道和其他项目；正式收录另需 Main 证据。早期混合卷的 Main 名单仅核验历史候选子集，不能把未核验条目全部认定为非 Main。

The original five-venue screening and its financial evidence are reused from the full Main universe, rather than from a best-paper or Oral list. This revision preserves that complete metadata source and rebuilds the source-level ledger. See [initial candidate dispositions](../../main/checks/initial_screening/all_candidate_dispositions.csv) and the [separate AAAI screening audit](../../main/checks/aaai_expansion/README.md). Existing financial fields and classifications for retained Main papers are unchanged; only long-paper scope fields and storage layout are added.

五会 Main 复用的是原全量论文集的独立金融筛查与证据，不是 Best / Oral 论文子集；本轮保留完整元数据来源并重新生成逐条台账。保留的 Main 论文原金融字段与分类不变，新增长文核验字段并迁移存储目录。

## Findings screening / Findings 筛查

1. Parse every record from the official ACL / EMNLP Findings XML volumes, 2020–2026. Keep only the two requested venue families; NAACL / EACL / AACL Findings are outside this six-conference scope.
2. Screen title and abstract for financial tasks, domain terms, or named financial benchmarks. The exact query is versioned in [screen_tracks.py](../../scripts/screen_tracks.py). This is candidate retrieval, not admission.
3. Inspect publisher PDFs for all metadata hits and all records without an abstract: **988 PDFs**. Missing-abstract records are therefore not silently dropped. Retain financial snippets before References and publisher-PDF hashes.
4. Review the financial task, actual experiments/data, business cases, modeling or domain survey. Ignore funding, affiliations, compute costs, background-only examples, references and nonfinancial meanings of words such as bank, credit or trading.
5. Establish long-paper eligibility independently. **207** financially relevant Findings records were confirmed; **187** have verified long-paper evidence and enter the catalog. **20** await long-paper verification.
6. Review the task taxonomy separately from methods. [Per-paper taxonomy corrections](findings_taxonomy_overrides.json) identify the actual financial task and remove labels produced by incidental mentions.

逐条解析 13,578 条官方记录；题名/摘要检索只产生候选。所有含金融线索或缺少摘要的 988 篇均核查出版正文，保留引用文献之前的证据和 PDF 哈希。另行复核金融相关性、长文属性及分类：金融相关性确认 207 篇，其中 187 篇具备长文证据进入正式清单，20 篇继续待核验。

- [Complete Findings records](findings_records.json)
- [All 988 full-text screening results](findings_fulltext_results.json)
- [Financial review decisions](findings_review_decisions.json)
- [Pending long-paper verification](../../findings/checks/pending_length_verification.json)
- [Aggregate screening summary](screening_summary.json)

The inventory records query results and review status; a negative query or an unconfirmed candidate is not proof of financial irrelevance. Full texts outside the candidate queue have not been systematically reviewed. Later papers, incomplete abstracts, undisclosed financial datasets and unavailable sources can still produce omissions. No ranking or completeness guarantee is implied.

台账区分检索结果与复核状态；未命中或未确认不代表已经证明不相关。候选队列之外的正文未系统复核，后续论文、摘要缺失和正文未披露于元数据的金融数据仍可能导致漏收。

## Long-paper evidence / 长文依据

- Official ACL Long Papers volumes establish long-paper status directly; Short Papers volumes establish exclusions.
- Where available, official EMNLP program tables provide explicit long/short labels. [Cached program evidence](length_sources/) and [per-record Main review](main_length_review.json) preserve these sources.
- ICML, ICLR, NeurIPS and AAAI admissions belong to verified regular full-paper main tracks; their separate position, datasets/benchmarks, evaluations and other special tracks are not admitted here.
- For mixed ACL / EMNLP Main or Findings volumes without official type labels, a conservative publisher-content inspection checks for substantial content on page six or later **before** explicit References, Limitations, Acknowledgments or other back matter. The audit saves the inspected content page, prose excerpt, boundary and PDF SHA-256. At least 160 extracted words are required. This is a documented inference from actual content under the [official ACL formatting policy](https://github.com/acl-org/acl-style-files/blob/master/formatting.md#paper-length), not a publisher-assigned type label. Total PDF page count is not used to label long papers.
- A failed extraction, short body or missing boundary remains unverified unless official short-paper evidence exists. We do not automatically turn every unverified record into a short paper.

长文优先采用官方卷名、官方程序表或常规 full-paper track 证据。混合卷无类型字段时，复核出版正文在第六页或更后页是否仍有实质内容，并要求位于参考文献、局限性、致谢等明确后置章节之前；保留页面、至少 160 个抽取词、片段、边界和 PDF 哈希。此项是依据正文的推断，不冒充出版方标签，也不以含附录和参考文献的 PDF 总页数推断长文。抽取失败或正文较短的记录继续待核验。

The original Main catalog had 1,338 papers. The current catalog retains **1,310**: 925 verified regular full-paper-track records, 159 official Long Papers volume records, 64 official program labels, and 162 publisher-content inspections. **13** known short papers are excluded; **14** records await type verification. One ACL 2019 Student Research Workshop paper was also removed from Main. See the [scope migration manifest](main_scope_migration.json). Original metadata is preserved in [CSV](finance_catalog.csv.baseline.gz) and [JSONL](finance_catalog.jsonl.baseline.gz) baselines; excluded PDFs and notes remain recoverable from Git commit `685f2131547bddf32a41f6900e713a76dd7b0a3d`.

原 Main 清单 1,338 篇，本轮保留 1,310 篇：常规 full-paper track 925 篇、官方 Long Papers 卷 159 篇、官方程序表 64 篇、出版正文复核 162 篇；13 篇已知短文移出，14 篇待核验；另移出一篇误归 Main 的 ACL 2019 学生研讨会论文。原始元数据保留压缩基线，移出记录的旧 PDF 与笔记仍可从上述 Git 提交恢复。

## Validation and maintenance / 验证与维护

[verify_tracks.py](../../scripts/verify_tracks.py) checks both catalogs, JSONL, Excel, topic CSVs, bibliography, classification labels, note IDs, PDF hashes and local links. It also verifies disjoint track identities, long-paper evidence, source XML hashes and complete Findings inventory coverage, plus preservation of retained Main financial fields. Results: [Main](../../main/checks/validation.json), [Findings](../../findings/checks/validation.json), [cross-track audit](validation.json).

验证覆盖两类清单及导出、分类、笔记、PDF 哈希和链接，并核对类别身份隔离、长文证据、来源哈希和全部 Findings 台账；保留的 Main 原金融字段也逐项核对。维护命令见 [CONTRIBUTING.md](../../CONTRIBUTING.md)。

## Explicit short-paper exclusion / 明确排除短文

Short papers are excluded from both Main and Findings, including their indexes, notes, PDFs and exports. The validator independently rejects explicit short-paper types, official Short Papers volumes and short-paper identifiers even if another field says long. Unverified lengths remain outside the admitted catalogs.

Main 和 Findings 均不收录短文，索引、笔记、PDF 和数据导出采用同一口径。验证器独立检查官方短文卷、短文 ID 和类型字段，避免被错误的 long 标签覆盖；长文属性未确认的论文不进入正式清单。

The [long-only recheck](long_only_recheck.json) records a second inspection of 355 historical content-boundary cases, supplemented by three subsequent boundary corrections. Six PDFs with late or corrupted text boundaries were also rendered and checked visually: all six have substantive main-body methods or results on PDF page six. One separate volume-identity error was found: P19-2046 belongs to the ACL 2019 Student Research Workshop, so it is excluded from Main. The current totals are Main 1,310 and Findings 187.

[长文复核记录](long_only_recheck.json)保留 355 篇历史正文边界记录及本次补充三篇的复查结果；对其中 6 篇文本边界异常的 PDF 另行查看了页面，均确认第六页仍为主体方法或实验结果，这 6 篇继续保留。另发现 P19-2046 属于 ACL 2019 学生研讨会，已从 Main 移出；现为 Main 1,310 篇、Findings 187 篇。

The historical five-venue metadata source also includes legacy auxiliary-volume entries. The current inventory labels these as outside Main rather than inheriting the historical track field. In particular, P17-2 and P18-2 are short-paper volumes, whereas P19-2 is the Student Research Workshop. Official source: [P19-2046](https://aclanthology.org/P19-2046/).

历史五会来源中夹有早期辅助卷条目，本轮台账依据出版卷名排除，避免沿用旧 track 字段。P17-2 / P18-2 为短文卷，P19-2 则为学生研讨会卷，不能混用编号规则。

The eight retained ACL 2019 papers were additionally matched against the official program’s **Long Papers (Main Conference)** section; their evidence now uses that explicit label. The validator checks this source independently, including its separate Short Papers and SRW sections.

保留的 8 篇 ACL 2019 论文另已逐篇匹配官方程序表的 Main Long Papers 栏，改用明确类型证据；验证器会独立核对该程序表，避免将 Main Short Papers 或 SRW 混入。

## Reconciled boundary corrections / 正文边界纠正

Three publisher PDFs were incorrectly deferred because a wrapped inline Appendix reference, a figure label, or a table column matched the automatic back-matter detector. [SHA-bound reviewed exceptions](length_overrides.json) confirm substantive main content on page six for all three. Main now contains 1,310 papers and Findings 187; prior recheck reports remain historical snapshots.

三篇出版 PDF 曾因正文中的换行 Appendix 引用、图标签或表格列名被误判为后置章节而暂缓。逐篇复核确认第六页仍有实质正文，修订与 PDF SHA-256 绑定。修正后 Main 1,310 篇、Findings 187 篇；此前的复查报告作为历史快照保留。

The three boundary corrections were also checked on rendered publisher PDF page six. The [current recheck](long_only_recheck.json) includes these observations and retains the [earlier recheck snapshot](long_only_recheck.before_reconciliation.json).

三处边界纠正均已查看出版 PDF 第六页图像，确认仍是方法、结果或领域综述正文。当前复查记录保留页面观察，旧版复查结果另存为历史快照。
