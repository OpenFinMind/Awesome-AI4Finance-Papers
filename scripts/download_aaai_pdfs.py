#!/usr/bin/env python3
"""Download reviewed AAAI papers, checking PDF identity before publication."""
import concurrent.futures
import hashlib
import json
import re
import subprocess
import unicodedata
from datetime import datetime, timezone
from difflib import SequenceMatcher
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'checks/aaai_expansion'
CACHE = Path('/tmp/ai4finance_aaai_pdf_review')


def norm(text):
    return re.sub('[^a-z0-9]', '', unicodedata.normalize('NFKD', text).lower())


def identify(path, paper):
    text = subprocess.check_output(['pdftotext', '-f', '1', '-l', '2', str(path), '-'],
                                   stderr=subprocess.DEVNULL).decode(errors='replace')
    compact = norm(text[:16000])
    title = norm(paper['title'])
    exact = title in compact
    words = re.findall(r'[a-z0-9]+', unicodedata.normalize('NFKD', text[:7000]).lower())
    expected = re.findall(r'[a-z0-9]+', unicodedata.normalize('NFKD', paper['title']).lower())
    score = 1.0 if exact else max((SequenceMatcher(None, ' '.join(expected),
                ' '.join(words[i:i+len(expected)])).ratio() for i in range(min(len(words), 400))), default=0)
    authors = [name for name in paper['authors'] if norm(name) in compact]
    passed = score >= 0.86 and bool(authors)
    return {'title_exact': exact, 'title_similarity': round(score, 4),
            'matched_authors': authors, 'identity_verified': passed}


def download(paper):
    pid = paper['id']
    previous = DEST / 'pdf_records' / f'{pid}.json'
    if previous.exists():
        result = json.loads(previous.read_text())
        if result['status'] == 'downloaded' and (ROOT / result['local_path']).exists():
            return result
    urls = [(paper['pdf_url'], 'publisher_version')]
    if paper.get('publisher_cdn_url'):
        urls.insert(0, (paper['publisher_cdn_url'], 'publisher_version'))
    if paper.get('arxiv_id'):
        urls.append((f"https://arxiv.org/pdf/{paper['arxiv_id']}", 'arxiv_author_version'))
    failures = []
    result = {'id': pid, 'status': 'access_blocked', 'local_path': '', 'attempts': failures}
    for url, version in urls:
        if not url:
            continue
        try:
            path = CACHE / f'{pid}.pdf'
            source_path = CACHE / f'{pid}.source.json'
            cached_source = json.loads(source_path.read_text()) if source_path.exists() else None
            if path.exists() and ((cached_source and cached_source['url'] == url) or
                                  (not cached_source and url == paper['pdf_url'])):
                payload, final_url, status = path.read_bytes(), url, 200
            else:
                response = requests.get(url, timeout=70,
                                        headers={'User-Agent': 'OpenFinMind-LiteratureCollection/1.0'})
                payload, final_url, status = response.content, response.url, response.status_code
            if status != 200 or not payload.startswith(b'%PDF-'):
                failures.append({'url': url, 'http_status': status,
                                 'error': 'No valid PDF response'})
                continue
            path.write_bytes(payload)
            identity = identify(path, paper)
            if not identity['identity_verified']:
                failures.append({'url': url, 'error': 'PDF identity requires review', **identity})
                continue
            info = subprocess.check_output(['pdfinfo', str(path)], stderr=subprocess.DEVNULL).decode()
            pages = int(re.search(r'^Pages:\s*(\d+)', info, re.M).group(1))
            title = re.sub('[^A-Za-z0-9]+', '_', paper['title']).strip('_')[:130]
            relative = f"pdfs/AAAI/{paper['year']}/{pid}__{title}.pdf"
            target = ROOT / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(payload)
            result.update(status='downloaded', local_path=relative, pages=pages,
                          bytes=len(payload), sha256=hashlib.sha256(payload).hexdigest(),
                          pdf_version=version, requested_url=url, final_url=final_url,
                          downloaded_at_utc=datetime.now(timezone.utc).isoformat(), identity=identity)
            break
        except (requests.RequestException, subprocess.SubprocessError, AttributeError, ValueError) as exc:
            failures.append({'url': url, 'error': str(exc)[:300]})
    previous.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(pid, result['status'], result.get('pdf_version', ''), flush=True)
    return result


def main():
    CACHE.mkdir(parents=True, exist_ok=True)
    (DEST / 'pdf_records').mkdir(parents=True, exist_ok=True)
    papers = json.loads((DEST / 'pdf_candidates.json').read_text())
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        results = list(pool.map(download, papers))
    (DEST / 'pdf_results.json').write_text(json.dumps(results, ensure_ascii=False, indent=2) + '\n')
    print('Verified local PDFs:', sum(r['status'] == 'downloaded' for r in results), '/', len(results))


if __name__ == '__main__':
    main()
