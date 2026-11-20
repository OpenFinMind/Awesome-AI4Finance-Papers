#!/usr/bin/env python3
"""Retrieve accessible author PDFs and prepare evidence for KDD human review."""
import concurrent.futures
import hashlib
import json
import re
import subprocess
import threading
from pathlib import Path
from urllib.parse import urlsplit

import requests

from collect_kdd import AUDIT, FINANCE, clean, save

CACHE = Path('/tmp/ai4finance_kdd_review')
BENCHMARKS = re.compile(
    r'\b(?:NASDAQ|NYSE|SSE50|CSI300|SP500|S&P\s*500|Dow Jones|Yahoo Finance|'
    r'Exchange(?:[-_ ]Rate)?|German[-_ ]Credit|Credit[-_ ]Card|Credit[-_ ]Approval|'
    r'Bank[-_ ]Marketing|Lending[-_ ]Club|UCI[-_ ]Adult|Adult dataset|DGraph(?:Fin)?|'
    r'T[-_ ]Finance|AMLSim|PaySim|Elliptic|Ethereum|Bitcoin|FiQA|FinQA|TAT[-_ ]QA|'
    r'financial transactions?|financial markets?|stock prices?|stock markets?|'
    r'stock returns?|credit scoring|loan default|money laundering|portfolio management)\b', re.I)
LOCK = threading.Lock()
SEMAPHORES = {}
INSPECTION_VERSION = 2


def host_lock(url):
    host = urlsplit(url).netloc
    with LOCK:
        return SEMAPHORES.setdefault(host, threading.BoundedSemaphore(2))


def snippets(text, pattern, limit=14):
    found = []
    seen = set()
    for match in pattern.finditer(text):
        name = match.group().lower()
        if name in seen:
            continue
        seen.add(name)
        found.append({'match': match.group(), 'excerpt': clean(text[max(0, match.start()-160):match.end()+400])})
        if len(found) >= limit:
            break
    return found


def inspect(p):
    output = CACHE / (p['id'] + '.json')
    fingerprint = hashlib.sha256(json.dumps(p.get('pdf_locations', [])).encode()).hexdigest()
    prior = {}
    if output.exists():
        prior = json.loads(output.read_text())
        if prior.get('inspection_version') == INSPECTION_VERSION and (
                prior['status'] == 'inspected' or prior.get('locator_fingerprint') == fingerprint):
            return prior
    result = {**prior, 'id': p['id'], 'status': 'unavailable', 'attempts': prior.get('attempts', []),
              'inspection_version': INSPECTION_VERSION, 'locator_fingerprint': fingerprint}
    pdf = CACHE / (p['id'] + '.pdf')
    text_path = CACHE / (p['id'] + '.txt')
    locations = list(dict.fromkeys(p.get('pdf_locations', [])))
    locations.sort(key=lambda u: ('arxiv.org' not in u, 'doi.org' in u or 'dl.acm.org' in u))
    for url in locations:
        if pdf.exists():
            break
        if 'doi.org/' in url or 'dl.acm.org/' in url:
            continue  # These locator links do not grant access to a PDF.
        if url.startswith('http://arxiv.org'):
            url = url.replace('http://', 'https://', 1)
        try:
            with host_lock(url):
                response = requests.get(url, timeout=(12, 30))
            result['attempts'].append({'url': url, 'status': response.status_code})
            if response.status_code != 200 or not response.content.startswith(b'%PDF-'):
                continue
            if len(response.content) > 50_000_000:
                continue
            pdf.write_bytes(response.content)
            result['source_url'] = response.url
            result['pdf_version'] = 'arxiv' if 'arxiv.org' in url else 'author_repository'
        except requests.RequestException as exc:
            result['attempts'].append({'url': url, 'error': str(exc)[:150]})
    if pdf.exists():
        try:
            subprocess.run(['pdftotext', '-layout', str(pdf), str(text_path)], check=True,
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=45)
            text = text_path.read_text(errors='replace')
            title_words = set(re.findall(r'[a-z]{3,}', p['title'].lower()))
            front = set(re.findall(r'[a-z]{3,}', '\f'.join(text.split('\f')[:2]).lower()))
            overlap = len(title_words & front) / max(1, len(title_words))
            info = subprocess.check_output(['pdfinfo', str(pdf)], stderr=subprocess.DEVNULL).decode(errors='replace')
            pages = re.search(r'^Pages:\s*(\d+)', info, re.M)
            # Two-column extraction can place the References heading beside a
            # final content line. Keep citation-list hits out of finance evidence.
            boundary = re.search(r'\bREFERENCES\b|\n\s*(?:\d+\.?\s+)?(?:References|Bibliography)\b', text[2000:])
            body = text[:2000 + boundary.start()] if boundary else text
            result.update(status='inspected' if overlap >= .65 else 'pdf_identity_unverified',
                          title_token_overlap=round(overlap, 4), pages=int(pages.group(1)) if pages else None,
                          bytes=pdf.stat().st_size, sha256=hashlib.sha256(pdf.read_bytes()).hexdigest(),
                          body_financial_hits=snippets(body, FINANCE), benchmark_hits=snippets(body, BENCHMARKS),
                          cache_filename=pdf.name)
        except (OSError, subprocess.SubprocessError) as exc:
            result.update(status='extraction_failed', error=str(exc)[:200])
    save(output, result)
    return result


def main():
    CACHE.mkdir(parents=True, exist_ok=True)
    candidates = json.loads((AUDIT / 'candidate_queue.json').read_text())
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as pool:
        for i, result in enumerate(pool.map(inspect, candidates), 1):
            results.append(result)
            if i % 40 == 0:
                save(AUDIT / 'fulltext_results.json', results)
                print(i, '/', len(candidates), 'processed;', sum(r['status']=='inspected' for r in results), 'PDFs inspected', flush=True)
    save(AUDIT / 'fulltext_results.json', results)
    print('Complete:', len(results), 'candidates;', sum(r['status']=='inspected' for r in results), 'PDFs inspected', flush=True)


if __name__ == '__main__':
    main()
