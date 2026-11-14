import json, re
exec(open('tags.py').read())
songs = json.load(open('songs.json')); singles = json.load(open('singles.json'))
lc = lambda t: t.lower().replace('...', '…').strip()
def inl(t, L): return lc(t) in {lc(x) for x in L}
ALB = {'debut':'Taylor Swift','fearless':'Fearless','speaknow':'Speak Now','red':'Red','1989':'1989','reputation':'reputation','lover':'Lover','folklore':'folklore','evermore':'evermore','midnights':'Midnights','ttpd':'TTPD','showgirl':'Showgirl'}
out = []; miss = set()
for s in songs:
    t = s['title']
    if t == "Taylor Swift's 1st Phone Call with Tim McGraw" or '10 Minute' in t: continue
    rows = [s['album']] + (['vault'] if inl(t, VAULT) else [])
    cols = []
    for k, L in LYRIC.items():
        if inl(t, L): cols.append(k)
    pk = singles.get(lc(t).replace('…','...')) if lc(t).replace('…','...') in singles else singles.get("' " + lc(t) + " '", 'x')
    if pk != 'x' and (lc(t).replace('…','...') in singles or ("' " + lc(t) + " '") in singles):
        cols.append('single')
        if pk and pk == 1: cols.append('n1')
        if pk and pk <= 10: cols.append('t10')
    if inl(t, OPENER): cols.append('opener')
    if inl(t, CLOSER): cols.append('closer')
    if inl(t, TRACK5): cols.append('track5')
    if s['feat']: cols.append('feat')
    if len(re.findall(r"[\w'’!?.&…-]+", re.sub(r'\(.*?\)', '', t))) == 1: cols.append('oneword')
    w = s['writers']
    if s['album'] == 'red' and not w:
        if inl(t, RED_SOLO): cols.append('solo')
        if inl(t, RED_MARTIN): cols.append('martin')
    elif s['album'] == 'speaknow':
        if not inl(t, SPEAKNOW_NOT_SOLO): cols.append('solo')
    elif s['album'] == 'showgirl':
        if inl(t, SHOWGIRL_STD): cols.append('martin')
    else:
        if 'Antonoff' in w: cols.append('antonoff')
        if 'Dessner' in w: cols.append('dessner')
        if re.search(r'\bMartin\b', w): cols.append('martin')
        if re.sub(r'Taylor Swift|Swift', '', w).strip() == '' and w: cols.append('solo')
    disp = t
    if s['album'] in ('folklore', 'evermore'): disp = t.lower()
    disp = STYLE.get(t.lower(), disp)
    out.append([disp, ' '.join(rows), ' '.join(cols)])
allt = {lc(o[0]).strip('"') for o in out}
for L in list(LYRIC.values()) + [OPENER, CLOSER, TRACK5, VAULT]:
    for x in L:
        if lc(x) not in allt: miss.add(x)
print('unmatched hand tags:', miss)
import collections
print(len(out), collections.Counter(c for o in out for c in o[2].split()))
print('singles not matched:', [k for k in singles if k not in {lc(o[0]).strip('"').replace('…','...') for o in out}])
json.dump(out, open('data.json', 'w'), ensure_ascii=False, separators=(',', ':'))
