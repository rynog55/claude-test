import csv, json, re, collections, glob
from bs4 import BeautifulSoup
rows = list(csv.DictReader(open('in/playlist.csv', encoding='utf-8-sig')))
def norm(s): return re.sub(r'[^a-z0-9]', '', re.sub(r'\(.*?\)', '', s.lower().replace('&', 'and')))
def chart(files, artist_before=False):
    pairs = set()
    for f in files:
        s = BeautifulSoup(json.load(open(f))['parse']['text'], 'lxml')
        for t in s.find_all('table', class_='wikitable'):
            if artist_before and 'weeks at number one' not in t.find('tr').get_text(' ', strip=True).lower(): continue
            for sup in t.find_all('sup'): sup.decompose()
            for tr in t.find_all('tr'):
                c = tr.find_all(['td', 'th'])
                for i, x in enumerate(c[:-1] if not artist_before else c):
                    tx = x.get_text(' ', strip=True).replace('“', '"').replace('”', '"')
                    m = re.match(r'"\s*(.+?)\s*"', tx)
                    if m:
                        nxt = c[i - 1 if artist_before and i > 0 else i + 1].get_text(' ', strip=True)
                        if re.fullmatch(r'\d+', nxt) and i + 2 < len(c): nxt = c[i + 2].get_text(' ', strip=True)
                        pairs.add((norm(m.group(1)), nxt.lower())); break
    return pairs
US10 = chart(sorted(glob.glob('raw/t10_*.json'))); UK1 = chart(['raw/uk1.json', 'raw/uk1_70s.json'], artist_before=True)
print('chart entries', len(US10), len(UK1))
ALIAS = {'Elvis Costello & The Attractions': 'Elvis Costello', 'Adam & The Ants': 'Adam Ant', 'M / Robin Scott': 'M', 'Eurythmics': 'Eurythmics'}
TYPES = {
 'uk': ['The Smiths','The Cure','Joe Jackson','Duran Duran','Thompson Twins','Squeeze','The Police','The Psychedelic Furs','Depeche Mode','The Fixx','The Clash','David Bowie','Siouxsie and the Banshees','Simple Minds','XTC','Fine Young Cannibals','Pretenders','Echo & the Bunnymen','New Order','A Flock Of Seagulls','The Human League','Naked Eyes','Roxy Music','YAZ','Orchestral Manoeuvres In The Dark','Eurythmics','Culture Club','Billy Idol','Elvis Costello','Tears For Fears','Morrissey','Public Image Ltd.','Modern English','Pet Shop Boys','General Public','Love and Rockets','Howard Jones','Talk Talk','Wang Chung','Haircut 100','Bronski Beat','Adam Ant','Bow Wow Wow','The Cult','The Alarm','Bryan Ferry','Joy Division','The The','ABC','B-Movie','Big Audio Dynamite','Big Country','Cutting Crew','Dave Edmunds','Dead Or Alive','Dexys Midnight Runners','Erasure','Gary Numan','Heaven 17','Kim Wilde','M','Madness','Paul Young','Peter Murphy','Rockpile','Soft Cell','Spandau Ballet','The Dream Academy','The English Beat','The Jam','The Outfield','The Vapors','Ultravox','When In Rome','World Party'],
 'us': ['The Cars','Talking Heads','R.E.M.','Violent Femmes',"The B-52's",'Missing Persons','DEVO','The Smithereens','Oingo Boingo',"The Go-Go's",'The Romantics','The Replacements','Berlin',"'Til Tuesday",'Animotion','Concrete Blonde','Josie Cotton','Marshall Crenshaw','Matthew Sweet','Pixies','The Bangles','The Call','The Dead Milkmen','The Flirts','The Jim Carroll Band','The Motels','The Plimsouls','The Waitresses','They Might Be Giants','Tom Tom Club','Tommy Tutone','Translator','Wall Of Voodoo'],
 'world': ['INXS','The Church','a-ha','Alphaville','Falco','Men Without Hats','Corey Hart','Crowded House','Real Life','U2'],
 'female': ['Siouxsie and the Banshees','Pretenders',"The B-52's",'Missing Persons','Berlin',"The Go-Go's",'Bow Wow Wow','Eurythmics','YAZ',"'Til Tuesday",'Animotion','Concrete Blonde','Josie Cotton','Kim Wilde','The Bangles','The Flirts','The Motels','The Waitresses','Tom Tom Club'],
 'duo': ['Tears For Fears','Eurythmics','YAZ','Pet Shop Boys','Soft Cell','Naked Eyes','Erasure'],
 'solo': ['Joe Jackson','David Bowie','Billy Idol','Elvis Costello','Morrissey','Howard Jones','Adam Ant','Falco','Bryan Ferry','Corey Hart','Dave Edmunds','Gary Numan','Kim Wilde','Josie Cotton','Marshall Crenshaw','Matthew Sweet','Paul Young','Peter Murphy'],
 'liveaid': ['The Cars','Duran Duran','Thompson Twins','Pretenders','Simple Minds','INXS','David Bowie','Elvis Costello','Howard Jones','Adam Ant','Bryan Ferry','The Power Station','Ultravox','Spandau Ballet','U2','Paul Young'],
 'died': ['INXS','Joy Division','The Cars','David Bowie','Talk Talk','The Clash','Falco','The Smithereens','The Power Station','Dead Or Alive','The Jim Carroll Band','Big Country','The Waitresses','The Outfield'],
}
YEARFIX = {'Love Will Tear Us Apart':1980,'Blue Monday':1983,'In Between Days':1985,'Close to Me':1985,"Why Can't I Be You?":1987,'Antmusic':1980,'Hold Me Now':1983,'What Is Love?':1983,'Need You Tonight':1987,'If You Leave':1986,'Saved By Zero':1983,'Red Skies':1982,'Obsession':1984,'Goody Two Shoes':1982,'Stand Or Fall':1982,'True':1983,'Doctor! Doctor!':1984,'Kids In America':1981,'Desperate But Not Serious':1982,'Lay Your Hands On Me':1985,'True Faith':1987,'Strangelove':1987,'Brand New Lover':1986,'Someday, Someway':1982,'Rock Me Amadeus':1985,'Sixty Eight Guns':1984,'Mirror In the Bathroom':1980,'The Walls Came Down':1983,'Rock Lobster':1979,'Johnny, Are You Queer?':1981,'Pop Muzik':1979,'Brass in Pocket':1979}
def base(t):
    t = re.sub(r'\s+-\s+.*$', '', t)
    t = re.sub(r'\s*\((?:[^)]*(remaster|version|edit|mix|short)[^)]*)\)', '', t, flags=re.I)
    return t.strip()
songs = collections.OrderedDict()
for r in rows:
    credits = [a.strip() for a in re.split(r'[;,]', r['Artist Name(s)']) if a.strip()]
    a0 = ALIAS.get(credits[0], credits[0])
    title = base(r['Track Name']); k = (norm(title), a0)
    if k not in songs: songs[k] = dict(title=title, a0=a0, credit=a0, r=r)
pops = sorted(int(s['r']['Popularity']) for s in songs.values()); n = len(pops); lo, hi = pops[n // 4], pops[3 * n // 4]
cnt = collections.Counter(s['a0'] for s in songs.values())
ARTISTS = sorted([a for a, c in cnt.items() if c >= 3], key=lambda a: (-cnt[a], a))
out = []; unk = set()
for (nk, a0), s in songs.items():
    r = s['r']; t = s['title']
    year = YEARFIX.get(t, int(r['Release Date'][:4]))
    rws = (['a:' + a0] if a0 in ARTISTS else []) + [k for k, v in TYPES.items() if a0 in v]
    if not any(a0 in TYPES[k] for k in ('uk', 'us', 'world')): unk.add(a0)
    if cnt[a0] == 1: rws.append('onesong')
    cols = []; al = a0.lower().replace('the ', '')
    hit = lambda P: any(p[0] == nk and (al in p[1] or p[1].replace('the ', '') in al) for p in P)
    if hit(US10): cols.append('us10')
    if hit(UK1): cols.append('uk1')
    g = r['Genres']
    if 'synthpop' in g: cols.append('synth')
    if re.search(r'post-punk|gothic|darkwave|deathrock|cold wave', g): cols.append('dark_genre')
    if r['Mode'] == '0': cols.append('minor')
    v = float(r['Valence'])
    if v <= 0.35: cols.append('dark')
    if v >= 0.75: cols.append('upbeat')
    if float(r['Danceability']) >= 0.75: cols.append('dance')
    ms = int(r['Duration (ms)'])
    if ms >= 300000: cols.append('long')
    if ms < 200000: cols.append('short')
    p = int(r['Popularity'])
    if p <= lo: cols.append('deep')
    if p >= hi: cols.append('smash')
    cols.append('y1' if year <= 1981 else 'y2' if year <= 1984 else 'y3')
    if len(re.sub(r'\(.*?\)', '', t).split()) == 1: cols.append('oneword')
    out.append([t, a0, '|'.join(rws), ' '.join(cols), year])
print(len(out), 'songs;', len(ARTISTS), 'band rows (3+ songs):', ARTISTS)
print('no country tag:', unk)
print(collections.Counter(c for o in out for c in o[3].split()))
print(collections.Counter(x for o in out for x in o[2].split('|') if ':' not in x))
print('US top 10:', [o[0] for o in out if 'us10' in o[3]])
print('UK No.1:', [o[0] for o in out if 'uk1' in o[3]])
json.dump({'songs': out, 'artists': ARTISTS}, open('data.json', 'w'), ensure_ascii=False, separators=(',', ':'))
