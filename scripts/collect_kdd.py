#!/usr/bin/env python3
"""Cache official Research Track inventories and retrieve review metadata.

Candidate retrieval never admits a paper. Reviewed decisions are stored separately.
"""
import argparse
import concurrent.futures
import gzip
import hashlib
import html
import json
import re
import time
import unicodedata
from datetime import datetime, timezone
from pathlib import Path

import requests
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / 'checks/track_screening/kdd'
SOURCES = ROOT / 'main/sources/kdd'
URLS = {
    2017: 'https://www.kdd.org/kdd2017/accepted-papers',
    2018: 'https://www.kdd.org/kdd2018/accepted-papers',
    2019: 'https://www.kdd.org/kdd2019/proceedings',
    2020: 'https://www.kdd.org/kdd2020/proceedings/',
    2021: 'https://www.kdd.org/kdd2021/accepted-papers/toc.html',
    2022: 'https://www.kdd.org/kdd2022/toc.html',
    2023: 'https://kdd.org/kdd2023/wp-content/uploads/2023/08/toc.html',
    2024: 'https://kdd.org/kdd2024/research-track-papers/',
    2025: 'https://kdd.org/kdd2025/research-track-papers-2/',
    2026: 'https://kdd2026.kdd.org/papers/',
}
POLICIES = {
    2017: 'https://www.kdd.org/kdd2017/announcements/view/kdd-2017-call-for-research-papers',
    2018: 'https://www.kdd.org/kdd2018/calls/view/kdd-2018-call-for-research-papers',
    2019: 'https://www.kdd.org/kdd2019/calls/view/kdd-2019-call-for-research-papers',
    2020: 'https://www.kdd.org/kdd2020/calls/view/kdd-2020-call-for-research-papers',
    2021: 'https://www.kdd.org/calls/view/call-for-research-track-papers-kdd-2021',
    2022: 'https://www.kdd.org/kdd2022/cfpResearch.html',
    2023: 'https://kdd.org/kdd2023/call-for-research-track-papers/',
    2024: 'https://kdd.org/kdd2024/research-track-call-for-papers/',
    2025: 'https://kdd.org/kdd2025/research-track-call-for-papers/',
    2026: 'https://kdd2026.kdd.org/research-track-call-for-papers/',
}
FINANCE = re.compile(
    r'financ\w*|\bstocks?\b|\btrading\b|\bportfolio\b|\binvest(?:ments?|ing|ors?|ed)?\b|\basset pric\w*|'
    r'\binsuran\w*|\bbank(?:ing|s)?\b|\bcredit\b|\bloans?\b|\blending\b|\bfraud\w*|'
    r'\bmoney launder\w*|\banti.money\b|\bearnings?\b|\baccounting\b|\bESG\b|'
    r'bitcoin|ethereum|cryptocurr\w*|crypto.asset\w*|\bexchange rates?\b|\bhedging\b|'
    r'\boption pric\w*|\bderivatives? pric\w*|\bmacro.?economic\w*|\beconomic forecast\w*|'
    r'\bGerman.Credit\b|\bLending.Club\b|\bUCI.Adult\b|\bincome predict\w*|\bFiQA\b|'
    r'\bFinQA\b|\bTAT.QA\b|\bcreditcard\b|\bcredit.card\b|\bfinancial statements?\b', re.I)
METHODS = re.compile(r'time.series|forecast\w*|fairness|fair learn\w*|counterfactual|recourse|'
                     r'tabular|anomaly detect\w*|graph anomal\w*|outlier detect\w*|causal discover\w*', re.I)


def clean(text):
    text = re.sub(r'\s+', ' ', html.unescape(str(text or ''))).strip()
    try:
        return text.encode('latin1').decode('utf8')
    except (UnicodeEncodeError, UnicodeDecodeError):
        return text


def key(title):
    return re.sub('[^a-z0-9]', '', unicodedata.normalize('NFKD', clean(title)).encode('ascii', 'ignore').decode().lower())


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def cached(url, name, params=None):
    path = SOURCES / (name + '.gz')
    if path.exists():
        return gzip.decompress(path.read_bytes())
    for attempt in range(6):
        response = requests.get(url, params=params, timeout=75,
                                headers={'User-Agent': 'OpenFinMind-PaperCollection/1.0'})
        if response.status_code in (429, 502, 503, 504) and attempt < 5:
            wait = max(10 * (attempt + 1), float(response.headers.get('Retry-After', '0')))
            print('Waiting for metadata service:', response.status_code, wait, flush=True)
            time.sleep(wait)
            continue
        response.raise_for_status()
        break
    data = response.content
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(gzip.compress(data, mtime=0))
    save(path.with_suffix(path.suffix + '.meta.json'), {
        'url': response.url, 'retrieved_at_utc': datetime.now(timezone.utc).isoformat(),
        'uncompressed_sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data)})
    return data


def record(year, title, authors='', abstract='', doi='', paper_url='', **extra):
    title = clean(title)
    if isinstance(authors, str):
        authors = [re.sub(r'\s*\([^)]*\)', '', a).strip(' ;*') for a in authors.split(';')]
    return dict(id=f'kdd-{year}-' + hashlib.sha256(key(title).encode()).hexdigest()[:12],
                title=title, authors=[clean(a) for a in authors if a], year=year, venue='KDD',
                track='main', publication_track='Research Track', abstract=clean(abstract),
                abstract_source=URLS[year] if abstract else '', doi=doi.lower().rstrip('.'),
                paper_url=('https://doi.org/' + doi if doi else paper_url),
                track_evidence_url=URLS[year], **extra)


def parse(year, data):
    soup = BeautifulSoup(data, 'html.parser')
    papers = []
    if year == 2026:
        text = data.decode('utf8')
        for match in re.finditer(r'const\s+(cycle[12]Papers)\s*=\s*', text):
            items, _ = json.JSONDecoder().raw_decode(text[match.end():])
            for item in items:
                if item['track'] == 'rtp':
                    papers.append(record(year, item['title'], item['authors'],
                                         doi=item['url'].split('doi.org/')[-1], cycle=match.group(1)))
    elif year in (2024, 2025):
        for row in soup.select('.page-content table tr'):
            bold = row.find('strong')
            if not bold:
                continue
            title = bold.get_text(' ', strip=True)
            if len(title) < 12:
                continue
            following = row.find_next_sibling('tr')
            doi = re.search(r'10\.1145/[\d.]+', row.get_text())
            papers.append(record(year, title, following.get_text(' ', strip=True) if following else '',
                                 doi=doi.group().rstrip('.') if doi else ''))
    elif 2019 <= year <= 2023:
        section = ''
        for heading in soup.find_all(['h2', 'h3']):
            if heading.name == 'h2':
                section = heading.get_text(' ', strip=True)
                continue
            if 'Research Track' not in section:
                continue
            pieces = []
            for node in heading.next_siblings:
                if getattr(node, 'name', None) in ('h2', 'h3'):
                    break
                pieces.append(str(node))
            fragment = BeautifulSoup(''.join(pieces), 'html.parser')
            abstract = fragment.find(class_='DLabstract')
            link = heading.find('a', href=True)
            doi = re.search(r'10\.1145/[\d.]+', link['href']) if link else None
            papers.append(record(year, heading.get_text(' ', strip=True),
                                 [a.get_text(' ', strip=True) for a in fragment.select('.DLauthors li')],
                                 abstract.get_text(' ', strip=True) if abstract else '',
                                 doi.group().rstrip('.') if doi else '', link['href'] if link else '',
                                 official_section=section))
    else:
        for heading in soup.find_all(['h3', 'h4']):
            if not heading.get_text(' ', strip=True).lower().startswith('research track papers'):
                continue
            for node in heading.next_siblings:
                if getattr(node, 'name', None) in ('h2', 'h3', 'h4'):
                    break
                if not getattr(node, 'find_all', None):
                    continue
                for a in node.find_all('a', href=True):
                    if '/papers/view/' not in a['href'] and '/accepted-papers/view/' not in a['href']:
                        continue
                    container = a.find_parent('td') if year == 2017 else a.find_parent(class_='media-body')
                    author = container.find('small') if year == 2017 else container.find_all('span')[-1]
                    papers.append(record(year, a.get_text(' ', strip=True),
                                         re.sub(r'^Author\(s\):\s*', '', author.get_text(' ', strip=True)),
                                         paper_url=a['href']))
    unique = {p['id']: p for p in papers}
    assert unique, year
    return list(unique.values())


def prepare():
    def fetch(year):
        return year, parse(year, cached(URLS[year], f'official_{year}.html'))
    records = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
        for year, papers in pool.map(fetch, URLS):
            records.extend(papers)
            print(year, len(papers), 'Research Track papers', flush=True)
    save(AUDIT / 'records.json', records)


def enrich():
    records = json.loads((AUDIT / 'records.json').read_text())
    # Publisher metadata resolves DOI identities; track membership comes only from
    # the conference sources above, never from a whole-proceedings search result.
    def crossref(year):
        ordinal = {2017: '23rd', 2018: '24th', 2019: '25th', 2024: '30th'}[year]
        params = {'filter': f'prefix:10.1145,from-pub-date:{year}-01-01,until-pub-date:{year}-12-31',
                  'query.container-title': f'Proceedings of the {ordinal} ACM SIGKDD Conference on Knowledge Discovery and Data Mining', 'rows': 1000}
        data = json.loads(cached('https://api.crossref.org/works', f'crossref_{year}.json', params))
        parent = {2017: '3097983', 2018: '3219819', 2019: '3292500', 2024: '3637528'}[year]
        result = {}
        for x in data['message']['items']:
            if not x.get('title') or not x['DOI'].startswith('10.1145/' + parent + '.'):
                continue
            result[key(x['title'][0])] = x
            for subtitle in x.get('subtitle', []):
                result[key(x['title'][0] + ': ' + subtitle)] = x
        return year, result
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as pool:
        maps = dict(pool.map(crossref, (2017, 2018, 2019, 2024)))
    for p in records:
        item = maps.get(p['year'], {}).get(key(p['title']))
        if item:
            p.update(doi=item['DOI'].lower(), paper_url='https://doi.org/' + item['DOI'].lower(),
                     authors=[' '.join(filter(None, [a.get('given'), a.get('family')])) for a in item.get('author', [])],
                     proceedings_pages=item.get('page', ''))
    metadata = {}
    for path in SOURCES.glob('openalex_*.json.gz'):
        items = json.loads(gzip.decompress(path.read_bytes())).get('results', [])
        metadata.update({x['doi'].split('doi.org/')[-1].lower(): x for x in items if x.get('doi')})
    targets = [p for p in records if p['doi'] and p['doi'] not in metadata and (not p['abstract'] or
               FINANCE.search(p['title'] + ' ' + p['abstract']) or
               METHODS.search(p['title'] + ' ' + p['abstract']))]
    batches = [targets[i:i + 45] for i in range(0, len(targets), 45)]
    def openalex(batch):
        dois = '|'.join(p['doi'] for p in batch)
        name = 'openalex_' + hashlib.sha256(dois.encode()).hexdigest()[:16] + '.json'
        data = json.loads(cached('https://api.openalex.org/works', name,
            {'filter': 'doi:' + dois, 'per-page': 50,
             'select': 'id,doi,title,abstract_inverted_index,locations'}))
        return data.get('results', [])
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        for result in pool.map(openalex, batches):
            metadata.update({x['doi'].split('doi.org/')[-1].lower(): x for x in result if x.get('doi')})
    for p in records:
        item = metadata.get(p['doi'])
        p['pdf_locations'] = []
        if item and (key(item['title']) == key(p['title']) or
                     (len(key(item['title'])) >= 30 and key(p['title']).startswith(key(item['title'])))):
            inverted = item.get('abstract_inverted_index') or {}
            if inverted and not p['abstract']:
                words = {pos: word for word, positions in inverted.items() for pos in positions}
                p['abstract'] = clean(' '.join(words[i] for i in sorted(words)))
                p['abstract_source'] = item['id']
            p['pdf_locations'] = [x['pdf_url'] for x in item.get('locations', []) if x.get('pdf_url')]
            p['metadata_locator'] = item['id']
        text = p['title'] + ' ' + p['abstract']
        p['financial_matches'] = sorted(set(m.group().lower() for m in FINANCE.finditer(text)))
        p['method_matches'] = sorted(set(m.group().lower() for m in METHODS.finditer(text)))
        p['fulltext_candidate'] = bool(p['financial_matches'] or p['method_matches'] or not p['abstract'])
    save(AUDIT / 'records.json', records)
    save(AUDIT / 'candidate_queue.json', [p for p in records if p['fulltext_candidate']])
    print(json.dumps({'records': len(records), 'abstracts': sum(bool(p['abstract']) for p in records),
                      'candidates': sum(p['fulltext_candidate'] for p in records),
                      'doi_resolved': sum(bool(p['doi']) for p in records)}, indent=2))


def supplement(cached_only=False):
    """Use public bibliographic locators; retrieve the original PDFs separately."""
    records = json.loads((AUDIT / 'records.json').read_text())
    results = {r['id']: r for r in json.loads((AUDIT / 'fulltext_results.json').read_text())}
    metadata = {}
    for path in SOURCES.glob('semanticscholar_*.json.gz'):
        for item in json.loads(gzip.decompress(path.read_bytes())):
            if item and (item.get('externalIds') or {}).get('DOI'):
                metadata[item['externalIds']['DOI'].lower()] = item
    targets = [p for p in records if p['fulltext_candidate'] and p['doi'] and p['doi'] not in metadata
               and results.get(p['id'], {}).get('status') != 'inspected']
    for offset in range(0, 0 if cached_only else len(targets), 40):
        ids = ['DOI:' + p['doi'] for p in targets[offset:offset + 40]]
        digest = hashlib.sha256(json.dumps(ids).encode()).hexdigest()[:16]
        response = requests.post('https://api.semanticscholar.org/graph/v1/paper/batch',
            params={'fields': 'title,abstract,openAccessPdf,externalIds'}, json={'ids': ids}, timeout=60)
        if response.status_code == 429:
            time.sleep(max(60, float(response.headers.get('Retry-After', '60'))))
            response = requests.post('https://api.semanticscholar.org/graph/v1/paper/batch',
                params={'fields': 'title,abstract,openAccessPdf,externalIds'}, json={'ids': ids}, timeout=60)
        if response.status_code == 429:
            print('Locator service remains rate limited; retaining cached results.', flush=True)
            break
        response.raise_for_status()
        path = SOURCES / f'semanticscholar_{digest}.json.gz'
        path.write_bytes(gzip.compress(response.content, mtime=0))
        save(path.with_suffix(path.suffix + '.meta.json'), {'url': response.url, 'method': 'POST',
             'ids': ids, 'uncompressed_sha256': hashlib.sha256(response.content).hexdigest()})
        for item in response.json():
            if item and (item.get('externalIds') or {}).get('DOI'):
                metadata[item['externalIds']['DOI'].lower()] = item
        print('Supplementary locators:', offset + len(ids), '/', len(targets), flush=True)
        time.sleep(1)
    for p in records:
        item = metadata.get(p['doi'])
        if not item:
            continue
        if not p['abstract'] and item.get('abstract'):
            p['abstract'] = clean(item['abstract'])
            p['abstract_source'] = 'https://api.semanticscholar.org/graph/v1/paper/' + item['paperId']
        extra = [(item.get('openAccessPdf') or {}).get('url')]
        arxiv = (item.get('externalIds') or {}).get('ArXiv')
        if arxiv:
            extra.append('https://arxiv.org/pdf/' + arxiv)
        for url in extra:
            if url and url not in p['pdf_locations']:
                p['pdf_locations'].append(url)
        p['financial_matches'] = sorted(set(m.group().lower() for m in FINANCE.finditer(p['title'] + ' ' + p['abstract'])))
    save(AUDIT / 'records.json', records)
    save(AUDIT / 'candidate_queue.json', [p for p in records if p['fulltext_candidate']])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('stage', choices=['prepare', 'enrich', 'supplement'])
    parser.add_argument('--cached-only', action='store_true')
    args = parser.parse_args()
    if args.stage == 'supplement':
        supplement(args.cached_only)
    else:
        {'prepare': prepare, 'enrich': enrich}[args.stage]()
