#!/usr/bin/env python3
"""Prepare full-text evidence for AAAI metadata candidates; do not admit papers."""
import concurrent.futures
import json
import re
import subprocess
from pathlib import Path

import requests
from download_aaai_pdfs import identify

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'checks/aaai_expansion'
CACHE = Path('/tmp/ai4finance_aaai_pdf_review')
DISCOVERY = {}
BOUNDS = {2020: 7, 2021: 16, 2022: 10, 2023: 11, 2024: 18, 2025: 25, 2026: 43}
BENCHMARK = re.compile(
    r'exchange[ _-]?rates?|credit[ _-]?cards?|German[ _-]?Credit|T-Finance|TFinance|'
    r'DGraphFin|Elliptic|Bitcoin|Ethereum|Bytom|\bNN5\b|NASDAQ|NYSE|S\s*&\s*P\s*500|Dow[ -]?Jones|'
    r'FRED-MD|FICO|LendingClub|FinQA|FiQA|TAT[ -]?QA|Financial[ -]?PhraseBank|'
    r'Banking77|\bM4\b|stock[ -]?(?:price|market|return)|financial[ -]?(?:dataset|data|experiment)', re.I)
TARGET = re.compile(r'time.series|forecast|financ|\bstock|\bfraud|\bloan|\bcredit|'
                    r'\binsuran|\bbanking|\bportfolio|counterfactual', re.I)


def screen(paper):
    pid = paper['id']
    result = {'id': pid, 'title': paper['title'], 'paper_url': paper['paper_url']}
    record = DEST / 'screened_fulltexts' / f'{pid}.json'
    if record.exists():
        existing = json.loads(record.read_text())
        if existing.get('status') == 'screened':
            return existing
    path = CACHE / f'{pid}.pdf'
    text_path = CACHE / f'{pid}.txt'
    try:
        if not path.exists():
            urls = [(paper['pdf_url'], 'publisher_version')]
            arxiv = DISCOVERY.get(pid, {}).get('arxiv_id')
            if arxiv:
                urls.append((f'https://arxiv.org/pdf/{arxiv}', 'arxiv_author_version'))
            for url, version in urls:
                response = requests.get(url, timeout=70,
                                        headers={'User-Agent': 'OpenFinMind-LiteratureCollection/1.0'})
                result['http_status'] = response.status_code
                if response.status_code == 200 and response.content.startswith(b'%PDF-'):
                    path.write_bytes(response.content)
                    (CACHE / f'{pid}.source.json').write_text(json.dumps({'url': url, 'version': version}))
                    break
            if not path.exists():
                result['status'] = 'fulltext_unavailable'
                record.write_text(json.dumps(result, indent=2) + '\n')
                return result
        identity = identify(path, paper)
        if not identity['identity_verified']:
            result.update(status='pdf_identity_pending', identity=identity)
            record.write_text(json.dumps(result, indent=2) + '\n')
            return result
        if not text_path.exists():
            subprocess.run(['pdftotext', '-layout', str(path), str(text_path)],
                           check=True, stderr=subprocess.DEVNULL)
        text = text_path.read_text(errors='replace')
        # Exclude the bibliography; every surviving passage still needs review.
        refs = list(re.finditer(r'^\s*References\s*$', text, re.M | re.I))
        body = text[:refs[-1].start()] if refs else text
        passages = []
        for match in BENCHMARK.finditer(body):
            if any(abs(match.start() - p['offset']) < 220 for p in passages):
                continue
            passages.append({'match': match.group(), 'offset': match.start(),
                             'excerpt': re.sub(r'\s+', ' ', body[max(0, match.start()-180):match.end()+350])})
        result.update(status='screened', fulltext_characters=len(text), passages=passages[:18], identity=identity)
        source_file = CACHE / f'{pid}.source.json'
        if source_file.exists():
            result['pdf_source'] = json.loads(source_file.read_text())
    except (requests.RequestException, subprocess.SubprocessError) as exc:
        result.update(status='fulltext_unavailable', error=str(exc)[:250])
    record.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    return result


def main():
    global DISCOVERY
    discovery_path = DEST / 'fulltext_discovery.json'
    if discovery_path.exists():
        DISCOVERY = {p['id']: p for p in json.loads(discovery_path.read_text())}
    CACHE.mkdir(parents=True, exist_ok=True)
    (DEST / 'screened_fulltexts').mkdir(exist_ok=True)
    papers = json.loads((DEST / 'candidates.json').read_text())
    already = json.loads((DEST / 'review_decisions.json').read_text())
    legacy = json.loads((DEST / 'legacy_main_ids.json').read_text())
    chosen = [p for p in papers if p['id'] not in already and
              ((p['year'] < 2020 and p['id'] in legacy) or
               (p['year'] >= 2020 and int(p['issue']) <= BOUNDS[p['year']])) and
              TARGET.search(p['title'] + ' ' + p['abstract'])]
    print('Full-text review candidates:', len(chosen), flush=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        for i, result in enumerate(pool.map(screen, chosen), 1):
            if i % 50 == 0:
                print(f'Screened {i}/{len(chosen)}', flush=True)
    print('Full-text screening complete.', flush=True)


if __name__ == '__main__':
    main()
