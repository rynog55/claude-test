import json, re, unicodedata, collections
html = open('hardwood-grid.html').read()
raw = html.split('const RAW = `')[1].split('`;')[0].strip().split('\n') + open('extra.txt').read().strip().split('\n')
ALIAS = {'Connecticut':'UConn','Louisiana State':'LSU','Mississippi St.':'Mississippi State','Miami (Florida)':'Miami','Miami (FL)':'Miami',
 'North Carolina State':'NC State','Southern California':'USC','Brigham Young':'BYU','Texas Christian':'TCU','Southern Methodist':'SMU',
 'Virginia Commonwealth':'VCU','Central Florida':'UCF','St. Joseph\'s':"Saint Joseph's",'Pittsburgh':'Pittsburgh','UNC':'North Carolina'}
KEEP_PAREN = re.compile(r'\((FL|Florida|OH|Ohio|MD|Chicago|CA)\)')
def canon(s):
    s = s.replace(' ',' ')
    keep = KEEP_PAREN.search(s)
    if keep and keep.group(1) in ('OH','Ohio'): base='Miami (OH)'
    else:
        base = re.sub(r'\s*\([^)]*\)', '', s).strip()
    return ALIAS.get(base, base)
def norm(n): return re.sub(r'[^a-z]','',unicodedata.normalize('NFD',n).encode('ascii','ignore').decode().lower()).strip()
P = collections.OrderedDict()
def add(name, school, tags, year=None):
    k = (norm(name), school)
    if k not in P: P[k] = {'n':name,'s':school,'t':set(),'y':year}
    P[k]['t'] |= set(tags)
    if year and not P[k]['y']: P[k]['y'] = year
for l in raw:
    if not l.strip(): continue
    n,s,t = l.split('|'); add(n, s, t.split())
d = json.load(open('draft.json'))
for x in d:
    if not x['school'] or 'forfeit' in x['name'].lower(): continue
    s = canon(x['school']); tags=[]
    pk = int(x['pick']) if x['pick'].isdigit() else 99
    if x['round']=='1' and pk<=14: tags.append('lot')
    if x['round']=='2': tags.append('r2')
    if pk==1: tags.append('top1')
    if set(x['marks'])&set('*+^'): tags.append('as')
    if '~' in x['marks']: tags.append('roy')
    add(x['name'], s, tags, x['year'])
pl = list(P.values())
CATS=['champ','mop','poy','top1','mvp','as','roy','lot','r2']
by = collections.defaultdict(lambda: collections.Counter())
for p in pl:
    for t in p['t']: by[p['s']][t]+=1
pool = sorted([s for s,c in by.items() if sum(1 for k in CATS if c[k]>=2)>=4 and sum(c.values())>=8])
print(len(pl),'players;',len(pool),'pool schools'); print(pool)
for s in pool: print(s, dict(by[s]))
out = [[p['n'],p['s'],' '.join(sorted(p['t'])),p['y'] or 0] for p in pl]
json.dump({'players':out,'pool':pool}, open('data.json','w'), ensure_ascii=False, separators=(',',':'))
# name collisions across schools (possible mis-merges or real duplicates)
c=collections.Counter(norm(p['n']) for p in pl); print('dupe names:',[ (p['n'],p['s'],p['y']) for p in pl if c[norm(p['n'])]>1])
