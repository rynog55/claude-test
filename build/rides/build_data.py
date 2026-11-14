"""rides.txt -> data.json for Ride Grid (same shape as the music grids: songs = attractions)."""
import json, collections
PARKS = ['MK', 'EP', 'HS', 'AK', 'DL', 'DCA', 'DLP', 'DAW', 'TDL', 'TDS', 'HK', 'SH']
out = []
for line in open('rides.txt', encoding='utf-8'):
    line = line.strip()
    if not line or line.startswith('#'): continue
    name, parks, tags, year = [x.strip() for x in line.split('|')]
    parks = parks.split(); year = int(year)
    assert all(p in PARKS for p in parks), (name, parks)
    cols = [t for t in tags.split() if t != 'none']
    if len(parks) >= 3: cols.append('multi')
    if len(parks) == 1: cols.append('unique')
    if year <= 1971: cols.append('classic')
    if year >= 2016: cols.append('new')
    cols += ['at_' + p for p in parks]
    import re
    m = re.match(r'^(.*?)\s*\((.*)\)$', name)
    title, alias = (m.group(1), m.group(2)) if m else (name, '')
    out.append([title, alias, '|'.join(parks), ' '.join(cols), year])
names = [o[0] for o in out]; assert len(names) == len(set(names)), 'duplicate names'
print(len(out), 'attractions')
print('per park', {p: sum(1 for o in out if p in o[2].split('|')) for p in PARKS})
print(collections.Counter(c for o in out for c in o[3].split() if not c.startswith('at_')))
json.dump({'songs': out, 'artists': []}, open('data.json', 'w'), ensure_ascii=False, separators=(',', ':'))
