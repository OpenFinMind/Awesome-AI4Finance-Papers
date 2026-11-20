"""Reject explicit short-paper evidence independently of a computed long label."""
import re
import html
import unicodedata


def title_key(title):
    return re.sub('[^a-z0-9]', '', unicodedata.normalize('NFKD', title).lower())


def acl2019_program_types(source):
    """Read the official program's separate Main Long/Main Short/SRW sections."""
    result = {}
    kinds = {'1': 'long', '2': 'short', '3': 'demo', '4': 'student_research_workshop'}
    for section in re.finditer(r'<h2 id="papers0([1-4])">(.*?)</h2>(.*?)(?=<h2|\Z)', source, re.S):
        for value in re.findall(r'<p class="paper-item">(.*?)<br\s*/?>', section.group(3), re.S):
            title = html.unescape(re.sub('<[^>]+>', '', value))
            result[title_key(title)] = kinds[section.group(1)]
    return result


def short_paper_reason(paper):
    for field in ('paper_length', 'paper_type', 'submission_type', 'submission_length'):
        value = re.sub(r'[-_\s]+', ' ', str(paper.get(field, '')).strip().lower())
        if value in {'short', 'short paper', 'short papers'}:
            return f'explicit {field}: {value}'
    if re.search(r'\bshort papers?\b', paper.get('booktitle', ''), re.I):
        return 'official short-paper proceedings volume'
    ident = paper.get('id', '')
    if re.search(r'\.acl-short\.', ident):
        return 'ACL short-paper identifier'
    if paper.get('venue') == 'ACL' and re.fullmatch(r'P(?:17|18)-2\d{3}', ident):
        return 'legacy ACL short-paper volume'
    if any(re.search(r'\bbest short paper\b', award, re.I) for award in paper.get('awards', [])):
        return 'official short-paper award'
    evidence = paper.get('paper_length_evidence', {})
    if isinstance(evidence, dict) and evidence.get('evidence_type') == 'official_short_papers_volume':
        return 'official short-paper classification evidence'
    return None


def excluded_publication_reason(paper):
    booktitle = paper.get('booktitle') or ''
    if re.search(r'\bworkshop\b|student research|demonstration|industry track', booktitle, re.I):
        return 'auxiliary proceedings outside Main / Findings: ' + booktitle
    # ACL 2019 combined main long/short papers in P19-1; P19-2 is SRW.
    if paper.get('venue') == 'ACL' and re.fullmatch(r'P19-2\d{3}', paper.get('id', '')):
        return 'ACL 2019 Student Research Workshop volume'
    return None
