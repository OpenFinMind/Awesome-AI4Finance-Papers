# Findings selection evidence / Findings 筛选依据

This directory contains only verified long papers from ACL / EMNLP Findings. The screening input is the complete set of 13,578 official records in the cached 2020–2026 ACL / EMNLP Findings volumes. NAACL, EACL and AACL Findings are outside the six-conference scope requested for this repository.

本目录仅收录 ACL / EMNLP Findings 中已核验的长文。筛查入口为缓存的 2020–2026 年官方论文集全部 13,578 条记录；NAACL、EACL 与 AACL 不在本仓库六会范围内。

Every record is screened through its available title and abstract, independently of the Main list, awards or presentation format. The 988 records with financial signals or no abstract are additionally inspected in their publisher PDFs. Admission decisions require substantive financial tasks, data, experiments, business cases, modeling or a domain review. Funding, affiliations, reference-only hits and nonfinancial word senses do not establish admission. Full text outside this candidate queue has not been systematically reviewed, so omissions remain possible.

所有记录独立进行题名和可用摘要筛查，不从 Main 清单、获奖清单或 Oral 清单推导。含金融线索或无摘要的 988 篇另行核查出版 PDF。仅背景、资助、作者单位、参考文献和非金融词义命中不构成收录依据。候选队列之外的正文未系统复核，仍可能漏收。

Long-paper eligibility is established separately. Where official paper-type labels are absent, the audit retains substantive content beyond the five-page final short-paper content limit, before explicit references, limitations or other back matter. This is a content-based inference under the official formatting policy, not an official publisher type label and not a total-page-count heuristic. Short and unverified cases stay outside the admitted catalog.

长文属性单独核验。没有官方类型标签的混合卷，记录出版正文中超出短文五页正文上限的实质内容，以及参考文献、局限性等后置章节边界。这是依据官方格式规则进行的正文复核推断，不冒充出版方的类型标签，也不使用 PDF 总页数推断。短文和未核验记录不进入正式清单。

- [Full screening audit / 完整审计](../../checks/track_screening/README.md)
- [Pending long-paper verification / 待核验长文属性](pending_length_verification.json)
- [Classification schema / 分类定义](finance_taxonomy/schema.json)
- [Assignments and evidence / 分类与证据](finance_taxonomy/assignments.json)
- [Reviewed taxonomy corrections / 分类修订](finance_taxonomy/manual_overrides.json)
- [Missing local PDFs / 未下载 PDF](missing_pdfs.csv)
- [Current validation / 当前验证](validation.json)
