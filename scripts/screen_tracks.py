#!/usr/bin/env python3
"""Screen every ACL/EMNLP Findings record independently of awards/presentation.

Raw official XML and one disposition per record are retained. Network retrieval
and PDF inspection are resumable; admission decisions are a separate input.
"""
import concurrent.futures
import csv
import gzip
import hashlib
import json
import re
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[1]
CACHE = Path('/tmp/ai4finance_findings_review')
INSPECTION_VERSION = 2
FIN = re.compile(r'financ(?:e|ial)|\bstocks?\b|\btrading\b|\bportfolio\b|\basset pric|\bderivative pric|\bcredit\b|\bloan\b|\bbank(?:ing|s)?\b|\binsurance\b|\bfraud\b|\bmoney\b|\binvest(?:ment|ing|or)|\bearnings\b|\baccounting\b|\btax(?:ation)?\b|\bESG\b|\beconomic(?:s)?\b|\bmacroeconom|\binflat|\bGDP\b|\bcrypto|\bblockchain|\bAML\b|\bhedging\b|\binvoice|\breceipt|\bbanknote|\bFinQA\b|\bConvFinQA\b|\bTAT-QA\b|\bMultiHiertt\b|\bFiQA\b|\bFinTabNet\b|\bFinBERT\b|\bFinancialPhraseBank\b|\bFinanceBench\b|\bFinTextQA\b|\bXBRL\b|\bEDGAR\b|\bFOMC\b|\bBanking77\b|\bFinCausal\b|\bFinNum\b', re.I)
FOCUSED_FINANCE = re.compile(r'financ(?:e|ial)|\b(?:finqa|convfinqa|tat-qa|multiHiertt|fiqa|fintabnet|banking77|banking 77|financialphrasebank|fincausal|finnum|finbench|sroie|cord dataset)\b|credit[- ](?:risk|scor|default|card)|stock[- ](?:market|pric|movement|predict)|\bloan\b|\binsurance\b|\binvoice|\breceipt|\bESG\b|\bscam|\bfraud|\bcrypto|\bearnings\b|\bFOMC\b', re.I)


def body_length_evidence(text):
    """Require substantive page-six content before explicit back matter.

    Uses reading-order extraction, not a PDF's total page count. A failure is
    unverified, never an automatic short-paper label.
    """
    pages = text.split('\f')
    boundary = re.compile(r'(?im)^\s*(?:\d+[. ]+)?(?:References|Bibliography|Limitations|Ethical Considerations|Ethics Statement|Acknowledg(?:e)?ments|Broader Impact|Appendix|Appendices)\s*$')
    first = next(((i,m.start()) for i,p in enumerate(pages) if (m:=boundary.search(p))), None)
    candidates = []
    if first and first[0] >= 5:
        for index in range(5, min(first[0]+1, len(pages))):
            content = pages[index][:first[1]] if index == first[0] else pages[index]
            candidates.append((index,content))
    index,sixth = max(candidates, key=lambda x:len(re.findall(r'\b[A-Za-z]{3,}\b',x[1])), default=(5,''))
    prose = re.findall(r'\b[A-Za-z]{3,}\b', sixth)
    evidence = dict(first_backmatter_page=first[0]+1 if first else None,
                    inspected_content_page=index+1,
                    sixth_content_page_words=len(prose),
                    sixth_content_page_excerpt=re.sub(r'\s+',' ',sixth)[:2400])
    return bool(first and len(prose)>=160), evidence



def apply_length_override(result):
    """Use reviewed content boundaries only for the exact inspected publisher PDF."""
    path = ROOT/'checks/track_screening/length_overrides.json'
    if not path.exists():
        return result
    review = json.loads(path.read_text()).get(result.get('id'))
    if not review:
        return result
    assert result.get('sha256') == review['pdf_sha256'], 'Reviewed PDF identity changed'
    result['content_exceeds_short_limit'] = True
    result['length_inspection'] = review['inspection']
    result['manual_length_review'] = review
    return result


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def prepare(source):
    target = ROOT / 'findings/sources'
    target.mkdir(parents=True, exist_ok=True)
    records = []
    manifest = []
    for year in range(2020, 2027):
        name = f'findings-{year}-anthology'
        for suffix in ('.gz', '.meta.json'):
            shutil.copy2(source / 'sources/raw' / (name + suffix), target / (name + suffix))
        data = gzip.decompress((target / (name + '.gz')).read_bytes())
        url = json.loads((target / (name + '.meta.json')).read_text())['url']
        manifest.append(dict(file=f'findings/sources/{name}.gz', url=url,
                             uncompressed_sha256=hashlib.sha256(data).hexdigest()))
        root = ET.fromstring(data)
        for volume in root.findall('volume'):
            venue = volume.get('id')
            if venue not in ('acl', 'emnlp'):
                continue
            for node in volume.findall('paper'):
                text = lambda tag: ' '.join(''.join(e.itertext()) for e in node.findall(tag)).strip()
                ident = f'{year}.findings-{venue}.{node.get("id")}'
                page = f'https://aclanthology.org/{ident}/'
                record = dict(id=ident, venue=venue.upper(), year=year, track='findings',
                              title=text('title'), abstract=text('abstract'),
                              authors=[' '.join(''.join(a.find(t).itertext()) for t in ('first','last')
                                                if a.find(t) is not None) for a in node.findall('author')],
                              paper_url=page, pdf_url=page[:-1]+'.pdf', doi=text('doi'),
                              pages=text('pages'), booktitle=''.join(volume.find('meta/booktitle').itertext()),
                              metadata_sources=[url], abstract_source=page,
                              awards=[], award_evidence=[], oral=False, oral_evidence=[],
                              presentation_original=[], code_urls=[])
                record['metadata_hits'] = sorted(set(m.group().lower() for m in FIN.finditer(record['title']+' '+record['abstract'])))
                # Every record without an abstract is queued for PDF screening.
                record['fulltext_candidate'] = bool(record['metadata_hits'] or not record['abstract'])
                records.append(record)
    save(ROOT/'checks/track_screening/findings_records.json', records)
    save(ROOT/'checks/track_screening/findings_sources.json', manifest)
    print(json.dumps(dict(records=len(records), candidates=sum(r['fulltext_candidate'] for r in records),
                          missing_abstracts=sum(not r['abstract'] for r in records),
                          venue_year=dict(Counter(f"{r['venue']}/{r['year']}" for r in records))), indent=2))


def inspect(record):
    CACHE.mkdir(exist_ok=True)
    out = CACHE/(record['id']+'.json')
    if out.exists():
        cached=json.loads(out.read_text())
        if cached.get('inspection_version')==INSPECTION_VERSION:
            return apply_length_override(cached)
    pdf = CACHE/(record['id']+'.pdf')
    result = dict(id=record['id'], source_url=record['pdf_url'], status='unavailable',inspection_version=INSPECTION_VERSION)
    try:
        if not pdf.exists():
            response = requests.get(record['pdf_url'], timeout=70,
                                    headers={'User-Agent':'OpenFinMind-LiteratureCollection/1.0'})
            response.raise_for_status()
            assert response.content.startswith(b'%PDF-'), 'Not a PDF'
            pdf.write_bytes(response.content)
        text = subprocess.check_output(['pdftotext','-layout',str(pdf),'-'], timeout=45,stderr=subprocess.DEVNULL).decode(errors='replace')
        (CACHE/(record['id']+'.txt')).write_text(text)
        # Financial evidence must precede References, not be a reference-only hit.
        match = re.search(r'(?m)^\s*(?:\d+[. ]+)?References\s*$', text)
        body = text[:match.start()] if match else text
        hits = []
        for found in FIN.finditer(body):
            snippet = re.sub(r'\s+', ' ', body[max(0,found.start()-180):found.end()+400]).strip()
            if snippet not in hits:
                hits.append(snippet)
        result.update(status='inspected', bytes=pdf.stat().st_size,
                      sha256=hashlib.sha256(pdf.read_bytes()).hexdigest(),
                      pages=len([p for p in text.split('\f') if p.strip()]),
                      fulltext_hits=hits, references_boundary_found=bool(match))
        # Conservative content-length evidence, distinct from total PDF pages:
        # substantive prose on page 6 before excluded back matter exceeds the
        # maximum 5 content pages for a final ACL short paper.
        reading = subprocess.check_output(['pdftotext',str(pdf),'-'], timeout=45,stderr=subprocess.DEVNULL).decode(errors='replace')
        result['content_exceeds_short_limit'], result['length_inspection'] = body_length_evidence(reading)
        first=reading.split('\f')[0]
        normalize=lambda s:re.sub('[^a-z0-9]','',s.lower())
        title_words=set(re.findall(r'[a-z]{3,}',record['title'].lower()))
        result['title_in_first_page']=normalize(record['title']) in normalize(first)
        result['title_token_overlap']=len(title_words & set(re.findall(r'[a-z]{3,}',first.lower())))/max(1,len(title_words))
        reference=re.search(r'(?im)^\s*References\s*$',reading)
        review_body=reading[:reference.start()] if reference else reading
        result['references_boundary_found']=bool(reference)
        result['focused_finance_hits']=[re.sub(r'\s+',' ',review_body[max(0,m.start()-130):m.end()+230])
                                        for m in FOCUSED_FINANCE.finditer(review_body)]
        abstract=re.search(r'(?is)\bAbstract\b(.*?)(?:\n\s*1\s*\n|\n\s*1\s+Introduction|\n\s*Introduction)',first)
        if abstract:
            result['recovered_abstract']=re.sub(r'\s+',' ',abstract.group(1)).strip()
    except Exception as exc:
        result['error'] = str(exc)[:400]
    result = apply_length_override(result)
    save(out, result)
    return result


def download():
    records=json.loads((ROOT/'checks/track_screening/findings_records.json').read_text())
    selected=[r for r in records if r['fulltext_candidate']]
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        for n,result in enumerate(pool.map(inspect,selected),1):
            if n%40==0:
                print(f'Inspected {n}/{len(selected)}',flush=True)
    results=[json.loads((CACHE/(r['id']+'.json')).read_text()) for r in selected]
    save(ROOT/'checks/track_screening/findings_fulltext_results.json',results)
    by_id={r['id']:r for r in results}
    for record in records:
        recovered=by_id.get(record['id'],{}).get('recovered_abstract')
        if not record['abstract'] and recovered:
            record.update(abstract=recovered,abstract_source=record['pdf_url'])
    save(ROOT/'checks/track_screening/findings_records.json',records)
    print(dict(Counter(r['status'] for r in results)), flush=True)


if __name__=='__main__':
    if sys.argv[1]=='prepare':
        prepare(Path(sys.argv[2]))
    elif sys.argv[1]=='download':
        download()
