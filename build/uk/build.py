"""Kentucky Grid data: wildcatworld.com season rosters + Wikipedia NBA draft pages + the Wikipedia Kentucky page -> data.json."""
import json, re, glob, collections, unicodedata
from bs4 import BeautifulSoup

def norm(n):
    n = unicodedata.normalize('NFD', n).encode('ascii', 'ignore').decode().lower()
    n = re.sub(r'\b(jr|sr|ii|iii|iv)\b\.?', '', n)
    n = re.sub(r'"[^"]*"|\([^)]*\)', '', n)
    n = re.sub(r'[^a-z]', '', n)
    return ALIAS.get(n, n)
HOF_ALLSTARS = {'danissel', 'cliffhagan'}
EXTRA_DRAFTED = {'cliffhagan'}   # 1953, 3rd round (Boston); missing from the parsed 1953 table   # marked only as Hall of Famers on the draft pages, but were NBA All-Stars
ALIAS = {'roblock': 'robertlock', 'kennyrollins': 'kenrollins', 'williamevans': 'billyevans', 'wahwahjones': 'wallacejones', 'wallacewahwahjones': 'wallacejones'}

COACHES = [('rupp', 1931, 1972), ('hall', 1973, 1985), ('sutton', 1986, 1989), ('pitino', 1990, 1997),
           ('smith', 1998, 2007), ('gillispie', 2008, 2009), ('calipari', 2010, 2024), ('pope', 2025, 2026)]
CHAMPS = {1948, 1949, 1951, 1958, 1978, 1996, 1998, 2012}
MOP = {'alexgroza', 'jackgivens', 'tonydelk', 'jeffsheppard', 'anthonydavis'}
coach_of = lambda y: next(c for c, a, b in COACHES if a <= y <= b)

# 1) Rosters: seasons, hometown, height
players = {}
for r in json.load(open('rosters.json')):
    k = norm(r['name'])
    if not k: continue
    p = players.setdefault(k, dict(name=r['name'], seasons=set(), home='', ht=''))
    p['seasons'].add(r['season'])
    if r['home']: p['home'] = r['home']
    if r['ht']: p['ht'] = r['ht']
    if len(r['name']) > len(p['name']) and '"' not in r['name']: p['name'] = r['name']

# 2) NBA draft (Kentucky picks only), 1950-2025
picks = {}
def add_pick(name, year, rnd, pick, marks):
    k = norm(name)
    if k in picks and picks[k]['year'] <= year: return   # keep the first time drafted
    picks[k] = dict(name=name, year=year, rnd=rnd, pick=pick, marks=marks)
for o in json.load(open('draft_2000s.json')):
    add_pick(o['name'], o['year'], o['round'], o['pick'], o['marks'])
for f in sorted(glob.glob('raw/d19*.json')):
    y = int(re.search(r'd(\d{4})', f).group(1))
    try: s = BeautifulSoup(json.load(open(f))['parse']['text'], 'lxml')
    except Exception: continue
    for t in s.find_all('table', class_='wikitable'):
        tr0 = t.find('tr')
        if not tr0: continue
        hdr = [c.get_text(' ', strip=True).lower() for c in tr0.find_all(['th', 'td'])]
        if not (any('player' in h for h in hdr) and any(('school' in h or 'college' in h) for h in hdr)): continue
        pi = next(i for i, h in enumerate(hdr) if 'player' in h); si = next(i for i, h in enumerate(hdr) if 'school' in h or 'college' in h)
        ri = next((i for i, h in enumerate(hdr) if h.startswith('round') or h.startswith('rnd')), None)
        ki = next((i for i, h in enumerate(hdr) if h.startswith('pick')), None)
        for tr in t.find_all('tr')[1:]:
            c = tr.find_all(['td', 'th'])
            if len(c) != len(hdr): continue
            if not re.match(r'Kentucky\b(?!\s+(State|Wesleyan|Christian))', c[si].get_text(' ', strip=True)): continue
            raw = re.sub(r'\[[^\]]*\]', '', c[pi].get_text('', strip=True)); a = c[pi].find('a')
            name = re.sub(r'[\*\^\+#~†‡§]+$', '', (a.get_text(strip=True) if a else raw)).strip()
            add_pick(name, y, c[ri].get_text(strip=True) if ri is not None else '', c[ki].get_text(strip=True) if ki is not None else '',
                     ''.join(ch for ch in raw if ch in '*+^~'))
        break

# 3) Kentucky page: honored jerseys, all-time top 10s, Hall of Fame, Olympians
s = BeautifulSoup(json.load(open('raw/main.json'))['parse']['text'], 'lxml')
honored, top10, hof, olympian = set(), set(), set(), set()
for t in s.find_all('table', class_='wikitable'):
    h = [c.get_text(' ', strip=True) for c in t.find('tr').find_all(['th', 'td'])]
    body = [[c.get_text(' ', strip=True) for c in tr.find_all(['td', 'th'])] for tr in t.find_all('tr')[1:]]
    if h[:2] == ['Name', 'Number']: honored |= {norm(r[0]) for r in body if r}
    elif h[0] == 'Name' and len(h) > 2 and h[2] in ('Points', 'Rebounds', 'Assists', 'Steals', 'Blocks'): top10 |= {norm(r[0]) for r in body if r}
    elif h[:2] == ['Year Inducted', 'Name']: hof |= {norm(r[1]) for r in body if len(r) > 2 and 'coach' not in r[2].lower()}
    elif h[:2] == ['Year', 'Player/Coach']: olympian |= {norm(r[1]) for r in body if len(r) > 1}

# 4) Combine into answers
out = []; unmatched_picks = []
for k, p in players.items():
    seasons = sorted(p['seasons']); coaches = sorted({coach_of(y) for y in seasons}, key=[c for c, _, _ in COACHES].index)
    cols = []
    if CHAMPS & set(seasons): cols.append('champ')
    if k in MOP: cols.append('mop')
    d = picks.get(k)
    if d:
        cols.append('drafted'); pk = int(d['pick']) if d['pick'].isdigit() else 99
        if d['rnd'] == '1' or pk <= 14 and d['year'] >= 1985: cols.append('r1')
        if d['rnd'] == '1' and pk <= 14: cols.append('top14')
        if pk == 1: cols.append('no1')
        if d['rnd'] == '2': cols.append('r2')
        if set(d['marks']) & set('*+'): cols.append('allstar')
        if len(seasons) == 1 and d['year'] == seasons[0]: cols.append('oneanddone')
    if k in HOF_ALLSTARS and 'allstar' not in cols: cols.append('allstar')
    if k in EXTRA_DRAFTED and 'drafted' not in cols: cols.append('drafted')
    if len(seasons) >= 4: cols.append('fouryear')
    if re.search(r',\s*(KY|Ky\.?|Kentucky)\b', p['home']): cols.append('kentuckian')
    m = re.match(r"(\d)'\s*(\d+)", p['ht'].replace('’', "'"))
    if m and int(m.group(1)) * 12 + int(m.group(2)) >= 82: cols.append('tall')
    if k in honored: cols.append('honored')
    if k in top10: cols.append('top10')
    if k in hof: cols.append('hof')
    if k in olympian: cols.append('olympian')
    if len(coaches) >= 2: cols.append('twocoaches')
    cols += ['in_' + c for c in coaches]
    yrs = f"{seasons[0]-1}–{str(seasons[-1])[2:]}" if len(seasons) > 1 else f"{seasons[0]-1}–{str(seasons[0])[2:]}"
    out.append([p['name'], '', '|'.join(coaches), ' '.join(cols), yrs])
unmatched_picks = sorted(v['name'] + ' ' + str(v['year']) for k, v in picks.items() if k not in players)
dup = collections.Counter(o[0] for o in out); out = [o if dup[o[0]] == 1 else [o[0] + ' (' + o[4] + ')'] + o[1:] for o in out]
print(len(out), 'players;', len(picks), 'Kentucky draft picks;', 'picks not matched to a roster:', unmatched_picks)
print('honored', len(honored), 'top10', len(top10), 'hof', len(hof), 'olympian', len(olympian))
print('per coach', collections.Counter(c for o in out for c in o[2].split('|')))
print(collections.Counter(c for o in out for c in o[3].split() if not c.startswith('in_')))
miss = lambda S: [x for x in S if x not in players]
print('not on a roster -> honored:', miss(honored), 'top10:', miss(top10), 'hof:', miss(hof), 'olympian:', miss(olympian))
json.dump({'songs': out, 'artists': []}, open('data.json', 'w'), ensure_ascii=False, separators=(',', ':'))
