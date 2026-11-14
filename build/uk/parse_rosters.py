import glob, re, json, collections
from bs4 import BeautifulSoup
rows = []; nohdr = []
for f in sorted(glob.glob('ww/s*.html')):
    y = int(re.search(r's(\d{4})', f).group(1))
    s = BeautifulSoup(open(f, 'rb').read(), 'lxml'); got = 0
    for t in s.find_all('table'):
        tr0 = t.find('tr')
        if not tr0: continue
        hdr = [c.get_text(' ', strip=True).lower() for c in tr0.find_all(['th', 'td'])]
        if not any(h.startswith('player') or h == 'name' for h in hdr): continue
        pi = next(i for i, h in enumerate(hdr) if h.startswith('player') or h == 'name')
        ci = next((i for i, h in enumerate(hdr) if h.startswith('class') or h in ('yr', 'yr.', 'year')), None)
        hi = next((i for i, h in enumerate(hdr) if h.startswith('hometown')), None)
        ti = next((i for i, h in enumerate(hdr) if h in ('ht', 'ht.', 'height')), None)
        for tr in t.find_all('tr')[1:]:
            c = tr.find_all(['td', 'th'])
            if len(c) <= pi: continue
            name = re.sub(r'\s+', ' ', c[pi].get_text(' ', strip=True)).strip()
            if not name or name.lower() in ('player', 'name'): continue
            g = lambda i: c[i].get_text(' ', strip=True) if i is not None and i < len(c) else ''
            rows.append(dict(season=y, name=name, cls=g(ci), home=g(hi), ht=g(ti))); got += 1
        if got: break
    if not got: nohdr.append(y)
json.dump(rows, open('rosters.json', 'w'), indent=0)
print(len(rows), 'roster rows;', len({r['name'] for r in rows}), 'distinct names; seasons without a table:', nohdr)
print(collections.Counter(r['cls'] for r in rows).most_common(12))
print([r for r in rows if r['season'] in (1951, 1978, 1996)][:6])
