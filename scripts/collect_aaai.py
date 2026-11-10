#!/usr/bin/env python3
"""Cache publisher-deposited AAAI metadata and prepare a finance review queue.

The queue is not an admission list. Track membership and financial relevance
must be reviewed before records are added to the collection.
"""
import concurrent.futures
import gzip
import hashlib
import html
import json
import re
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'checks/aaai_expansion'
RAW = ROOT / 'sources/aaai'
FINANCE = re.compile(
    r'financ\w*|\bstocks?\b|\btrading\b|\bportfolio\b|\binvest\w*|\basset pric\w*|'
    r'\binsuran\w*|\bbank(?:ing|s)?\b|\bcredit\b|\bloans?\b|\blending\b|\bfraud\w*|'
    r'\bmoney launder\w*|\banti.money\b|\bearnings?\b|\baccounting\b|\bESG\b|'
    r'\bFinQA\b|\bTAT.QA\b|\bFiQA\b|\bFinBERT\b|\bFinGPT\b|\bFinLLM\b|'
    r'\bXBRL\b|\bbitcoin\b|\bethereum\b|\bcryptocurr\w*|\bcrypto.asset\w*|'
    r'\bexchange rates?\b|\boption pric\w*|\bderivatives? pric\w*|\bhedging\b|'
    r'\bmacro.?economic\w*|\beconomic forecast\w*|\bcreditcard\b|\bcredit.card\b|'
    r'\bGerman.Credit\b|\bLending.Club\b|\bUCI.Adult\b|\bincome predict\w*|'
    r'\btime.series\b|\bmultivariate forecast\w*|\blong.term forecast\w*', re.I)


def clean(value):
    return re.sub(r'\s+', ' ', html.unescape(re.sub('<[^>]+>', ' ', value or ''))).strip()


def fetch_year(year):
    result = []
    manifest = []
    offset = 0
    while True:
        params = {'filter': f'from-pub-date:{year}-01-01,until-pub-date:{year}-12-31',
                  'rows': 1000, 'offset': offset}
        url = requests.Request('GET', 'https://api.crossref.org/journals/2374-3468/works',
                               params=params).prepare().url
        path = RAW / f'crossref_{year}_{offset:05d}.json.gz'
        meta = path.with_name(path.name + '.meta.json')
        if path.exists() and meta.exists():
            data = json.loads(gzip.decompress(path.read_bytes()))
            info = json.loads(meta.read_text())
        else:
            for attempt in range(4):
                try:
                    response = requests.get(url, timeout=100,
                                            headers={'User-Agent': 'OpenFinMind-LiteratureCollection/1.0'})
                    response.raise_for_status()
                    data = response.json()
                    break
                except (requests.RequestException, ValueError):
                    if attempt == 3:
                        raise
                    time.sleep(2 * (attempt + 1))
            content = json.dumps(data, ensure_ascii=False).encode()
            path.write_bytes(gzip.compress(content))
            info = {'url': url, 'retrieved_at_utc': datetime.now(timezone.utc).isoformat(),
                    'sha256_uncompressed': hashlib.sha256(content).hexdigest(),
                    'records': len(data['message']['items']),
                    'total_results': data['message']['total-results']}
            meta.write_text(json.dumps(info, indent=2) + '\n')
        manifest.append({'file': str(path.relative_to(ROOT)), **info})
        result.extend(data['message']['items'])
        print(f'AAAI metadata {year}: {len(result)}/{data["message"]["total-results"]}', flush=True)
        offset += len(data['message']['items'])
        if offset >= data['message']['total-results'] or not data['message']['items']:
            return result, manifest


def main():
    RAW.mkdir(parents=True, exist_ok=True)
    DEST.mkdir(parents=True, exist_ok=True)
    records = {}
    manifest = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        for items, sources in pool.map(fetch_year, range(2017, 2027)):
            manifest.extend(sources)
            for item in items:
                records[item['DOI'].lower()] = item
    candidates = []
    for doi, item in sorted(records.items()):
        title = clean(' '.join(item.get('title', [])))
        abstract = clean(item.get('abstract', ''))
        if not FINANCE.search(title + ' ' + abstract):
            continue
        volume = item.get('volume', '')
        if not volume.isdigit() or not 31 <= int(volume) <= 40:
            continue
        url = item.get('resource', {}).get('primary', {}).get('URL', '')
        article_id = url.rstrip('/').split('/')[-1]
        if not article_id.isdigit():
            continue
        pdf = next((x['URL'] for x in item.get('link', [])
                    if x.get('content-type') == 'application/pdf'), '')
        candidates.append({
            'id': f'aaai-{int(volume)+1986}-{article_id}', 'doi': doi,
            'venue': 'AAAI', 'year': int(volume)+1986, 'title': title,
            'authors': [' '.join(filter(None, [a.get('given'), a.get('family')]))
                        for a in item.get('author', [])],
            'abstract': abstract, 'paper_url': url, 'pdf_url': pdf,
            'volume': volume, 'issue': item.get('issue', ''), 'proceedings_pages': item.get('page', ''),
            'title_matches': sorted(set(m.group().lower() for m in FINANCE.finditer(title))),
            'abstract_matches': sorted(set(m.group().lower() for m in FINANCE.finditer(abstract))),
            'metadata_sources': [f'https://api.crossref.org/works/{doi}'],
        })
    (DEST / 'candidates.json').write_text(json.dumps(candidates, ensure_ascii=False, indent=2) + '\n')
    (DEST / 'source_manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print(json.dumps({'publisher_records': len(records), 'review_candidates': len(candidates)}, indent=2))


if __name__ == '__main__':
    main()
