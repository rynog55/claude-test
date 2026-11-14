import json, re, sys, glob
from bs4 import BeautifulSoup
out = []
for f in sorted(glob.glob('h*.json')):
    y = int(f[1:5])
    try: html = json.load(open(f))['parse']['text']
    except Exception: print('FAIL', y, file=sys.stderr); continue
    soup = BeautifulSoup(html, 'lxml')
    best = None
    for t in soup.find_all('table', class_='wikitable'):
        if not t.find('tr'): continue
        hdr = [th.get_text(' ', strip=True).lower() for th in t.find('tr').find_all(['th','td'])]
        if any('player' in h for h in hdr) and any(('school' in h or 'college' in h) for h in hdr):
            best = (t, hdr); break
    if not best: print('NOTABLE', y, file=sys.stderr); continue
    t, hdr = best
    pi = next(i for i,h in enumerate(hdr) if 'player' in h)
    si = next(i for i,h in enumerate(hdr) if 'school' in h or 'college' in h)
    ri = next((i for i,h in enumerate(hdr) if h.startswith('round') or h=='rnd.'), None)
    ki = next((i for i,h in enumerate(hdr) if h.startswith('pick')), None)
    n = 0
    for tr in t.find_all('tr')[1:]:
        cells = tr.find_all(['td','th'])
        if len(cells) != len(hdr): continue
        pc = cells[pi]; a = pc.find('a')
        name = (a.get_text(strip=True) if a else pc.get_text(' ', strip=True))
        raw = re.sub(r'\[.*?\]', '', pc.get_text('', strip=True))
        marks = ''.join(ch for ch in raw if ch in '*+^#~')
        name = re.sub(r'[\*\^\+#~†‡§]+$', '', re.sub(r'\[.*?\]', '', name)).strip()
        sc = cells[si]; sa = sc.find('a'); stitle = sa.get('title','') if sa else ''
        for sm in sc.find_all(['small','sup']): sm.decompose()
        school = re.sub(r'\[.*?\]', '', sc.get_text(' ', strip=True))
        school = re.sub(r'\s*\((Fr|So|Jr|Sr|Gr|RS|R-|Redshirt|Fresh|Soph|Jun|Sen|Grad|[0-9])[^)]*\)', '', school, flags=re.I)
        school = re.sub(r'\s+', ' ', school).strip()

        pick = cells[ki].get_text(strip=True) if ki is not None else ''
        rnd = cells[ri].get_text(strip=True) if ri is not None else ''
        out.append(dict(year=y, round=rnd, pick=pick, name=name, school=school, stitle=stitle, marks=marks)); n += 1
    print(y, n, file=sys.stderr)
json.dump(out, open('../draft.json','w'), indent=0)
