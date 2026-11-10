# Contributing / 维护说明

Use the matching publication-track directory: `main/` or `findings/`. Each has independent catalogs, notes, classifications, exports and PDFs. `local_path` is relative to that track directory. Keep source evidence and review decisions in `checks/track_screening/`.

按发表类别分别维护 `main/` 与 `findings/`。两边的清单、笔记、分类、导出和 PDF 独立存储；`local_path` 相对于所属类别目录。来源和复核决定保存在 `checks/track_screening/`。

## Admission / 收录

- Cover the six named conferences in the README, within 2017–2026. Findings applies only to ACL and EMNLP.
- Verify the main/Findings track and long-paper eligibility separately. Keep official volume/program evidence, or auditable regular-full-paper/content-boundary evidence. Total PDF page count is insufficient. Keep unresolved types outside the admitted catalogs.
- Review specific financial tasks, datasets, experiments, business cases, modeling or domain reviews. Neither oral presentation nor an award is required.
- Record `core` or `application` separately from one primary financial task, additional task labels, subtopics and technical methods. Preserve excerpts supporting inclusion and classification; keyword matches alone are insufficient.
- Name PDF versions correctly, and record byte count and SHA-256. Retain official paper links when no local PDF is available.

仅收录六会范围内已核验的 Main / Findings 长文；具体会议和年份以 README 为准。独立核验发表类别、长文属性和金融相关性。不以口头报告、获奖状态或 PDF 总页数代替收录依据。金融核心研究与金融应用分别标注，金融任务、子方向和技术方法保持独立；未确认的论文留在待核验清单。

## Rebuild and verify / 重新生成与验证

```bash
python -m pip install -r scripts/requirements.txt
python scripts/build_collection.py
python scripts/verify_tracks.py
git diff --check
```

The CSV/JSONL and classification assignments within each track are the curated inputs. `build_collection.py` rebuilds both tracks' Excel/BibTeX exports, task/subtopic/method views, venue/year indexes and bilingual READMEs without changing admission decisions. `verify_tracks.py` checks export consistency, PDF hashes, track separation, long-paper evidence, source inventory coverage and local links.

各类别的 CSV、JSONL 及分类记录是维护输入；构建脚本不更改收录决定。验证覆盖导出一致性、PDF 哈希、类别隔离、长文证据、来源台账和本地链接。

## Reproducible screening / 可复核筛查

`screen_tracks.py prepare <source-library>` captures official ACL Anthology Findings XML from a local source cache. `screen_tracks.py download` inspects the documented metadata candidates and records without abstracts. Financial review decisions are saved explicitly in `checks/track_screening/findings_review_decisions.json`, and reviewed taxonomy corrections in `findings_taxonomy_overrides.json`.

`apply_scope_revision.py` recreates this scope migration from the preserved original Main baseline and reviewed Findings inputs. It requires the temporary candidate PDF cache when admitted PDFs are not already present. It is a migration tool, not a routine command for future additions. `build_screening_inventory.py` rebuilds the source-level screening ledger. The previous AAAI import scripts are historical tooling; their historical reports are retained under `main/checks/aaai_expansion/`.

筛查脚本保留全部官方来源条目及候选记录，金融收录和分类修订另存为明确决定。迁移脚本用于复现本轮范围调整，不应在新增未来论文后直接覆盖新的清单。AAAI 首次导入审计作为历史来源保留。

PDF copyrights remain with the authors and publishers. / PDF 版权归作者与出版方。
