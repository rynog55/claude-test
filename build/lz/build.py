import json, re, collections
songs = json.load(open('songs.json')); ex = json.load(open('extra.json'))
O2 = ['Good Times Bad Times','Ramble On','Black Dog','In My Time of Dying','For Your Life','Trampled Under Foot',"Nobody's Fault but Mine",'No Quarter',"Since I've Been Loving You",'Dazed and Confused','Stairway to Heaven','The Song Remains the Same','Misty Mountain Hop','Kashmir','Whole Lotta Love','Rock and Roll']
HAND = {
 'myth': ['Ramble On','The Battle of Evermore','Immigrant Song','No Quarter','Achilles Last Stand','Misty Mountain Hop'],
 'water': ['The Rain Song','The Ocean','Fool in the Rain','When the Levee Breaks','Down by the Seaside','Thank You'],
 'place': ['Going to California','Kashmir','When the Levee Breaks','Black Country Woman','The Song Remains the Same'],
 'season': ['Stairway to Heaven','Tangerine','Dancing Days','The Rain Song'],
 'unsung': ['Black Dog','The Crunge',"D'yer Mak'er",'Four Sticks','Misty Mountain Hop','Achilles Last Stand','Carouselambra','Royal Orleans','Out on the Tiles','Bron-Y-Aur Stomp','The Wanton Song','Boogie with Stu',"Walter's Walk",'South Bound Saurez','Hats Off to (Roy) Harper','Immigrant Song'],
 'instrumental': ['Black Mountain Side','Moby Dick','Bron-Yr-Aur',"Bonzo's Montreux"],
}
MEMBERS = {'page','plant','jones','bonham','jimmy','robert','john','paul','and','arr','.','traditional_x'}
out = []
lastside = collections.defaultdict(int)
for s in songs: lastside[s['album']] = max(lastside[s['album']], s['side'])
for s in songs:
    t, w = s['title'], s['writers']; cols = []
    toks = set(re.findall(r'[a-z]+', w.lower()))
    for k, L in HAND.items():
        if t in L: cols.append(k)
    if t in ex['singles']: cols.append('single')
    if t in ex['tsrts'] and s['album'] != 'coda': cols.append('tsrts')
    if t in O2 and s['album'] != 'coda': cols.append('o2')
    if s['sidepos'] == 1: cols.append('sideopen')
    if s['side'] == lastside[s['album']] and s['sidepos'] == s['sidelen']: cols.append('closer')
    if s['secs'] >= 420: cols.append('long')
    if s['secs'] < 180: cols.append('short')
    if 'jones' in toks: cols.append('jones')
    if 'bonham' in toks: cols.append('bonham')
    if {'page','plant','jones','bonham'} <= toks: cols.append('all4')
    if toks <= {'page','plant','jimmy','robert'} and {'page','plant'} <= toks: cols.append('pageplant')
    if toks - MEMBERS - {'inspired','by'} : cols.append('outside')
    if len(re.sub(r'\(.*?\)', '', t).split()) == 1: cols.append('oneword')
    out.append([t, s['album'], ' '.join(cols)])
print(collections.Counter(c for o in out for c in o[2].split()))
print('outside:', [o[0] for o in out if 'outside' in o[2]])
miss = [x for L in list(HAND.values()) + [O2] for x in L if x not in {o[0] for o in out}]; print('unmatched:', miss)
json.dump(out, open('data.json', 'w'), ensure_ascii=False, separators=(',', ':'))
