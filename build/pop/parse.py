import json, re, sys, unicodedata, collections
from bs4 import BeautifulSoup
def load(f): return BeautifulSoup(json.load(open('raw/'+f+'.json'))['parse']['text'], 'lxml')
def clean(t): return re.sub(r'\s+',' ', re.sub(r'\[[^\]]*\]|↑|‡|†|\*|\(#\d+\)', '', t)).strip()
def title_of(cell):
    for s in cell.find_all('sup'): s.decompose()
    t = clean(cell.get_text(' ', strip=True))
    t = t.replace('“','"').replace('”','"')
    m = re.findall(r'"\s*([^"]+?)\s*"', t)
    return ' / '.join(m) if m else t.strip('" ')
KNOWN = set()
import glob
for f in glob.glob('raw/ye*.json') + glob.glob('raw/t10_*.json'):
    for a in BeautifulSoup(json.load(open(f))['parse']['text'], 'lxml').select('table.wikitable td a'):
        t = clean(a.get_text(' ', strip=True))
        if t and not t.startswith(('"','“')) and not re.fullmatch(r'[\d\W]+', t): KNOWN.add(t)
KNOWN_SORTED = sorted(KNOWN, key=len, reverse=True)
def split_part(text):
    toks = {}
    for i, n in enumerate(KNOWN_SORTED):
        if len(n) > 2 and n in text and re.search(r'(?<![\w])' + re.escape(n) + r'(?![\w])', text):
            tok = '\x00%d\x00' % i; text = re.sub(r'(?<![\w])' + re.escape(n) + r'(?![\w])', tok, text); toks[tok] = n
    parts = [x.strip() for x in re.split(r',\s*|\s+(?:and|&|x|with|feat\.)\s+', text) if x.strip()]
    out = []
    for x in parts:
        for tok, n in toks.items(): x = x.replace(tok, n)
        if x: out.append(x)
    return out
def artists_of(cell):
    for s in cell.find_all('sup'): s.decompose()
    credit = clean(cell.get_text(' ', strip=True))
    m = re.split(r'\s+featuring\s+', credit, maxsplit=1, flags=re.I)
    fix = lambda xs: [{'P!nk':'Pink','Ke$ha':'Kesha'}.get(x, x) for x in xs]
    lead = fix(split_part(m[0])); feat = fix(split_part(m[1])) if len(m) > 1 else []
    return credit, lead, feat
def key(title, lead):
    t = unicodedata.normalize('NFD', title).encode('ascii','ignore').decode().lower()
    t = re.sub(r'\(.*?\)','',t); t = re.sub(r'[^a-z0-9]','',t)
    a = re.sub(r'[^a-z0-9]','',unicodedata.normalize('NFD', lead[0] if lead else '').encode('ascii','ignore').decode().lower())
    return t+'|'+a
songs = {}
def get(title, credit, lead, feat):
    k = key(title, lead)
    tk = k.split('|')[0]; names = set(lead) | set(feat)
    for k2, s2 in songs.items():
        if k2.split('|')[0] == tk and names & (set(s2['lead']) | set(s2['feat'])): return s2
    if k not in songs: songs[k] = dict(title=title, credit=credit, lead=lead, feat=feat, years=set(), peak=None, ye=[], grammy=[])
    return songs[k]
for y in range(2010, 2020):
    t = load('ye%d' % y).find('table', class_='wikitable')
    for tr in t.find_all('tr')[1:]:
        c = tr.find_all(['td','th'])
        if len(c) < 3: continue
        pos = int(re.sub(r'\D','',c[0].get_text()) or 0)
        title = title_of(c[1]); credit, lead, feat = artists_of(c[2])
        s = get(title, credit, lead, feat); s['years'].add(y); s['ye'].append((y,pos))
    for t in load('t10_%d' % y).find_all('table', class_='wikitable'):
        hdr = [h.get_text(' ',strip=True).lower() for h in t.find('tr').find_all(['th','td'])]
        if not any('single' in h for h in hdr): continue
        last = None
        for tr in t.find_all('tr')[1:]:
            c = tr.find_all(['td','th'])
            idx = next((i for i,x in enumerate(c) if x.get_text(strip=True).startswith(('"','“'))), None)
            if idx is None or len(c) < idx+3: continue
            title = title_of(c[idx])
            if re.fullmatch(r'\s*\d+\s*', c[idx+1].get_text()) and last:
                credit, lead, feat = last; pkc = c[idx+1]
            else:
                credit, lead, feat = artists_of(c[idx+1]); pkc = c[idx+2]; last = (credit, lead, feat)
            pk = re.sub(r'\D','', pkc.get_text())
            s = get(title, credit, lead, feat); s['years'].add(y)
            if pk: s['peak'] = min(int(pk), s['peak'] or 99)
# Grammys: ceremonies 2011-2020 cover songs of 2010-2019
for f, lab in (('roty','Record'),('soty','Song')):
    try: soup = load(f)
    except Exception as e: print('missing', f, file=sys.stderr); continue
    for t in soup.find_all('table', class_='wikitable'):
        year = None
        for tr in t.find_all('tr')[1:]:
            c = tr.find_all(['td','th'])
            if not c: continue
            m = re.match(r'(\d{4})', c[0].get_text(strip=True))
            if m: year = int(m.group(1))
            if not year or not (2011 <= year <= 2020): continue
            idx = next((i for i,x in enumerate(c) if x.get_text(strip=True).startswith(('"','“'))), None)
            if idx is None: continue
            title = title_of(c[idx]); 
            tn = key(title, [])
            win = bool(tr.find('b')) or 'background' in (tr.get('style') or '') or any('background' in (x.get('style') or '') for x in c)
            hit = [s for k,s in songs.items() if k.split('|')[0] == tn.split('|')[0]]
            if not hit: print('grammy no match', year, title, file=sys.stderr)
            for s in hit: s['grammy'].append((year, lab, win))
out = []
for s in songs.values():
    s['years'] = sorted(s['years']); out.append(s)
json.dump(out, open('songs.json','w'), ensure_ascii=False, indent=0)
print(len(out), 'songs', file=sys.stderr)
