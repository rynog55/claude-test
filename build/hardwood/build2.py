import json, re, unicodedata, collections
exec(open('build.py').read().split('P = collections.OrderedDict()')[0])  # reuse raw, ALIAS, canon, norm
_canon = canon
def canon(s):
    c = _canon(s)
    c = re.sub(r' St\.$', ' State', c)
    return ALIAS.get(c, c)
COLLEGE = {'champ','mop','poy'}
people = []
byname = collections.defaultdict(list)
d = json.load(open('draft.json'))
for x in d:
    if not x['school'] or 'forfeit' in x['name'].lower(): continue
    tags=set(); pk = int(x['pick']) if x['pick'].isdigit() else 99
    if x['round']=='1' and pk<=14: tags.add('lot')
    if x['round']=='2': tags.add('r2')
    if pk==1: tags.add('top1')
    if set(x['marks'])&set('*+^'): tags.add('as')
    if '~' in x['marks']: tags.add('roy')
    p={'n':x['name'],'s':[canon(x['school'])],'t':tags,'y':x['year']}
    people.append(p); byname[norm(x['name'])].append(p)
merged=[]
for l in raw:
    if not l.strip(): continue
    n,s,t = l.split('|'); s=canon(s); t=t.split()
    cands = byname[norm(n)]
    if len(cands)>1: cands=[c for c in cands if s in c['s']] or cands[:0]
    if cands: p=cands[0]
    else:
        p={'n':n,'s':[],'t':set(),'y':0}; people.append(p); byname[norm(n)].append(p)
    if s not in p['s']:
        p['s'].append(s)
        if p['y']: merged.append((n,p['s']))
    for tag in t: p['t'].add(tag+'@'+s if tag in COLLEGE else tag)
print('transfer merges:', merged)
CATS=['champ','mop','poy','top1','mvp','as','roy','lot','r2']
def has(p,s,c): return s in p['s'] and (c in p['t'] or c+'@'+s in p['t'])
schools = collections.Counter(s for p in people for s in p['s'])
pool=[]
for s in schools:
    cnt={c:sum(1 for p in people if has(p,s,c)) for c in CATS}
    if sum(1 for c in CATS if cnt[c]>=2)>=4 and sum(cnt.values())>=10: pool.append(s)
pool.sort(); print(len(people),'people;',len(pool),'pool:',pool)
out=[[p['n'],'|'.join(p['s']),' '.join(sorted(p['t'])),p['y'] or 0] for p in people]
json.dump({'players':out,'pool':pool}, open('data.json','w'), ensure_ascii=False, separators=(',',':'))
import os; print(os.path.getsize('data.json'),'bytes')
