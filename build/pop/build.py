import json, re, collections
exec(open('types.py').read())
TYPES['group'] += ['Fun']; TYPES['uk'] += ['Florence Welch']
songs = json.load(open('songs.json'))
ALIAS = {'Glee cast': 'Glee Cast'}
NUMW = r'\b(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fifteen|twenty|thirty|forty|fifty|hundred|thousand|million|billion|first|second|third|1st|2nd|3rd)\b'
cnt = collections.Counter()
for s in songs:
    s['artists'] = list(dict.fromkeys(ALIAS.get(a, a) for a in s['lead'] + s['feat']))
    for a in s['artists']: cnt[a] += 1
ARTISTS = sorted([a for a, n in cnt.items() if n >= 6 and a != 'Glee Cast'], key=lambda a: -cnt[a])
out = []
for s in songs:
    disp = re.sub(r'\s*\((?:[^)]*remix[^)]*)\)', '', s['title'], flags=re.I).strip()
    base = re.sub(r'\s*\(.*?\)', '', disp).strip()
    rows = ['a:' + a for a in s['artists'] if a in ARTISTS] + [k for k, v in TYPES.items() if set(v) & set(s['artists'])]
    yrs = s['years']; yes = sorted({y for y, p in s['ye']})
    cols = []
    if s['peak'] == 1: cols.append('n1')
    if s['peak']: cols.append('t10')
    if not s['peak'] and yes: cols.append('not10')
    if any(p <= 10 for y, p in s['ye']): cols.append('ye10')
    if len(yes) >= 2: cols.append('twoyears')
    if s['feat']: cols.append('feat')
    if len(re.findall(r"[\w'’!.$&-]+", base)) == 1: cols.append('oneword')
    if re.search(r'\d', base) or re.search(NUMW, base, re.I): cols.append('number')
    cols.append('early' if min(yrs) <= 2014 else 'late')
    if s['grammy']: cols.append('grammy')
    out.append([disp, s['credit'], ' '.join(rows), ' '.join(cols), min(yrs)])
print(len(out), 'songs;', len(ARTISTS), 'artist rows:', ARTISTS)
cc = collections.Counter(c for o in out for c in o[3].split()); print(cc)
rc = collections.Counter(r for o in out for r in o[2].split() if ':' not in r); print(rc)
json.dump({'songs': out, 'artists': ARTISTS}, open('data.json', 'w'), ensure_ascii=False, separators=(',', ':'))
print('one-word sample', [o[0] for o in out if 'oneword' in o[3]][:25]); print('number sample', [o[0] for o in out if 'number' in o[3]][:40])
