"""Read a track without mixing its Core and Application publication artifacts."""
import csv,json,io,gzip
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
TRACKS=('main','findings')
SCOPES=('core','application')
def partitions():
    return [(track,scope,ROOT/track/scope) for track in TRACKS for scope in SCOPES]
def catalog(track):
    result={}
    for scope in SCOPES:
        with (ROOT/track/scope/'finance_catalog.csv').open(encoding='utf-8-sig',newline='') as f:
            for row in csv.DictReader(f):
                assert row['id'] not in result
                row=dict(row)
                if row['local_path']:row['local_path']=scope+'/'+row['local_path']
                result[row['id']]=row
    return result
def records(track):
    result={}
    for scope in SCOPES:
        for row in map(json.loads,(ROOT/track/scope/'finance_catalog.jsonl').read_text().splitlines()):
            row=json.loads(json.dumps(row))
            if row.get('download',{}).get('local_path'):row['download']['local_path']=scope+'/'+row['download']['local_path']
            result[row['id']]=row
    return result
def assignments(track):
    result={}
    for scope in SCOPES:result.update(json.loads((ROOT/track/scope/'checks/finance_taxonomy/assignments.json').read_text()))
    return result
def legacy(track,kind):
    baseline=json.loads(gzip.decompress((ROOT/'checks/taxonomy_v3/baseline.json.gz').read_bytes()))
    if kind=='csv':return {r['id']:r for r in csv.DictReader(io.StringIO(baseline[track+'/finance_catalog.csv']))}
    if kind=='jsonl':return {r['id']:r for r in map(json.loads,baseline[track+'/finance_catalog.jsonl'].splitlines())}
    if kind=='assignment':return json.loads(baseline[track+'/checks/finance_taxonomy/assignments.json'])
    raise ValueError(kind)
