import json, re, collections
from bs4 import BeautifulSoup
ALBUMS = ['debut','fearless','speaknow','red','1989','reputation','lover','folklore','evermore','midnights','ttpd','showgirl']
def base(t):
    t = t.replace('“','"').replace('”','"')
    m = re.search(r'"\s*(.+?)\s*"', t); t = m.group(1) if m else t
    t = re.sub(r'\s*\((Taylor.s Version|From the Vault)[^)]*\)', '', t).strip()
    return t.strip("' ").replace("' ", "'") if t.startswith("'") else t
songs = collections.OrderedDict()
for al in ALBUMS:
    s = BeautifulSoup(json.load(open('raw/%s.json' % al))['parse']['text'], 'lxml')
    for t in s.find_all('table', class_='tracklist'):
        cap = (t.find('caption').get_text(' ', strip=True) if t.find('caption') else '')
        for sup in t.find_all('sup'): sup.decompose()
        hdr = [c.get_text(' ', strip=True).lower() for c in t.find('tr').find_all(['th','td'])]
        wi = next((i for i,h in enumerate(hdr) if 'writer' in h), None)
        for tr in t.find_all('tr')[1:]:
            c = tr.find_all(['th','td'])
            if len(c) < 3 or not re.match(r'\d+\.', c[0].get_text(strip=True)): continue
            raw = c[1].get_text(' ', strip=True)
            paren = ' '.join(re.findall(r'\(([^)]*)\)', re.sub(r'"[^"]*"', '', raw.replace('“','"').replace('”','"'))))
            paren = re.sub(r"Taylor.s Version|From the Vault|featuring[^)]*", '', paren, flags=re.I)
            if re.search(r'\b(remix|acoustic|live|demo|piano|mix|edit|version|voice memo|instrumental|strings|radio|alternate|first draft|original|long pond|session|songwriter)\b', paren, re.I): continue
            b = base(raw); k = (al, b.lower())
            if k not in songs: songs[k] = dict(album=al, title=b, vault='Vault' in raw, feat=re.findall(r'featuring\s+([^)"]+)', raw), writers=c[wi].get_text(' ', strip=True) if wi is not None else '', ed=cap, no=int(c[0].get_text(strip=True).rstrip('.')))
out = list(songs.values())
# dedupe a title appearing on two albums (keep first)
seen=set(); res=[]
for s in out:
    if s['title'].lower() in seen: continue
    seen.add(s['title'].lower()); res.append(s)
json.dump(res, open('songs.json','w'), ensure_ascii=False, indent=0)
for al in ALBUMS:
    print(al, [ (s['no'], s['title'] + (' [V]' if s['vault'] else ''), s['feat']) for s in res if s['album']==al])
print(len(res))
