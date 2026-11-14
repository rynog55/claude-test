import csv, json, re, collections
rows = list(csv.DictReader(open('in/playlist.csv', encoding='utf-8-sig')))
charts = json.load(open('charts.json'))
TYPES = {
 'seattle': ['Nirvana','Pearl Jam','Alice In Chains','Soundgarden','Temple Of The Dog','Mad Season','Screaming Trees','The Presidents Of The United States Of America','Harvey Danger','Candlebox','Foo Fighters'],
 'female': ['Hole','Garbage','No Doubt','The Cranberries','Alanis Morissette','Fiona Apple','Veruca Salt','The Breeders','Concrete Blonde','Elastica','Letters To Cleo','Luscious Jackson','Mazzy Star','PJ Harvey','Republica','The Sundays','Tracy Bonham'],
 'lostsinger': ['Nirvana','Alice In Chains','Soundgarden','Temple Of The Dog','Stone Temple Pilots','Blind Melon','The Cranberries','Sublime','Mad Season','Screaming Trees','Beastie Boys'],
 'california': ['Red Hot Chili Peppers',"Jane's Addiction",'Green Day','The Offspring','Weezer','No Doubt','Beck','Sublime','Rage Against The Machine','Porno for Pyros','Faith No More','Primus','CAKE','Counting Crows','Third Eye Blind','Hole','Goldfinger','Reel Big Fish','Bad Religion','Social Distortion','blink-182','Eels','Lit','Eve 6','Geggy Tah','Concrete Blonde','Orgy','Mazzy Star','Toad The Wet Sprocket','Dishwalla','Oleander','The Flys','Tonic','Stone Temple Pilots','Rancid'],
 'abroad': ['Radiohead','Blur','The Verve','The Stone Roses','James','Elastica','Placebo','Feeder','PJ Harvey','The Sundays','Republica','White Town','Cornershop','Edwyn Collins','Big Audio Dynamite','Jesus Jones','Silverchair','Our Lady Peace','Alanis Morissette','The Cranberries','U2'],
 'unplugged': ['Nirvana','Alice In Chains','Pearl Jam','Stone Temple Pilots','R.E.M.','Alanis Morissette','Hole','Soul Asylum','The Cranberries'],
 'lolla': ["Jane's Addiction",'Nine Inch Nails','Butthole Surfers','Red Hot Chili Peppers','Pearl Jam','Soundgarden','Rage Against The Machine','Alice In Chains','Primus','Dinosaur Jr.','Porno for Pyros','The Smashing Pumpkins','Beastie Boys','Green Day','The Breeders','The Flaming Lips','Hole','Pavement','Beck','Elastica','Rancid','Screaming Trees'],
}
YEARFIX = {'Plowed':1994,'All I Want':1991,"Superman's Dead":1997,'Molly':1994,'Only Happy When It Rains':1995,'Self Esteem':1994,'Clumsy':1997,'What Do I Have to Do?':1996,'Save Yourself':1998,'High':1997,"Something's Always Wrong":1994,'Starseed':1994,'Soul to Squeeze':1993,'Dyslexic Heart':1992,'Gotta Get Away':1994,'What Would You Say':1994,'Midlife Crisis':1992,'Hunger Strike':1991,'Counting Blue Cars':1995,'Hell':1996,'Closing Time':1998,'Today':1993,'Come Out And Play':1994,'J.A.R.':1995,'Sliver':1990}
def base(t):
    t = re.sub(r'\s+-\s+(.*?(remaster|edit|version|mix|live|1997|single).*)$', '', t, flags=re.I)
    t = re.sub(r'\s*\((?:[^)]*(remaster|version|edit|mix)[^)]*)\)', '', t, flags=re.I)
    return t.strip()
def norm(s): return re.sub(r'[^a-z0-9]', '', re.sub(r'\(.*?\)', '', s.lower().replace('&', 'and').replace('sixteen', '16')))
songs = collections.OrderedDict()
for r in rows:
    artists = [a.strip() for a in r['Artist Name(s)'].split(',')]
    title = base(r['Track Name']); live = bool(re.search(r'\blive\b|unplugged', r['Track Name'] + ' ' + r['Album Name'], re.I))
    k = (norm(title.split(' - ')[0]), artists[0])
    rec = dict(title=title, artists=artists, album=r['Album Name'], live=live, r=r)
    if k in songs:
        if songs[k]['live'] and not live: songs[k] = rec   # prefer the studio version
        continue
    songs[k] = rec
pops = sorted(int(s['r']['Popularity']) for s in songs.values()); n = len(pops)
lo, hi = pops[n // 4], pops[3 * n // 4]
cnt = collections.Counter(s['artists'][0] for s in songs.values())
ARTISTS = sorted([a for a, c in cnt.items() if c >= 4], key=lambda a: -cnt[a])
out = []
for (nk, a0), s in songs.items():
    r = s['r']; t = s['title']; shortt = re.sub(r'\s*\(.*?\)', '', t).strip()
    year = YEARFIX.get(shortt, YEARFIX.get(t, int(r['Release Date'][:4])))
    rws = ['a:' + a for a in s['artists'] if a in ARTISTS] + [k for k, v in TYPES.items() if set(v) & set(s['artists'])]
    if cnt[a0] == 1: rws.append('onesong')
    cols = []
    match = lambda key: any(p[0] == nk and any(a.lower() in p[1].lower() for a in s['artists']) for p in charts[key])
    if match('alt'): cols.append('altno1')
    if match('rock'): cols.append('rockno1')
    if s['live']: cols.append('live')
    if float(r['Acousticness']) >= 0.5: cols.append('acoustic')
    if r['Mode'] == '0': cols.append('minor')
    v = float(r['Valence'])
    if v <= 0.3: cols.append('dark')
    if v >= 0.6: cols.append('upbeat')
    if float(r['Energy']) >= 0.9: cols.append('blast')
    ms = int(r['Duration (ms)'])
    if ms >= 300000: cols.append('long')
    if ms < 180000: cols.append('short')
    p = int(r['Popularity'])
    if p <= lo: cols.append('deep')
    if p >= hi: cols.append('smash')
    if r['Explicit'] == 'true': cols.append('explicit')
    cols.append('y1' if year <= 1993 else 'y2' if year <= 1995 else 'y3')
    if norm(shortt) == norm(re.sub(r'\s*\(.*?\)', '', s['album'])): cols.append('titletrack')
    if norm(s['album']) == norm(a0): cols.append('selftitled')
    if len(shortt.split()) == 1: cols.append('oneword')
    if r['Record Label'].startswith(('Geffen', 'DGC')): cols.append('geffen')
    out.append([t, ', '.join(s['artists']), '|'.join(rws), ' '.join(cols), year])
print(len(out), 'songs;', len(ARTISTS), 'band rows:', ARTISTS)
print('popularity cutoffs', lo, hi)
print(collections.Counter(c for o in out for c in o[3].split()))
print(collections.Counter(x for o in out for x in o[2].split() if ':' not in x))
print('alt no1s:', [o[0] for o in out if 'altno1' in o[3]])
print('title tracks:', [o[0] for o in out if 'titletrack' in o[3]])
miss = {a for v in TYPES.values() for a in v} - {a for o in out for a in o[1].split(', ')}; print('type names not in playlist:', miss)
json.dump({'songs': out, 'artists': ARTISTS}, open('data.json', 'w'), ensure_ascii=False, separators=(',', ':'))
