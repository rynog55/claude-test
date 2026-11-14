"""characters.txt -> data.json for Scranton Grid (same shape as the other grids)."""
import json, collections
GROUPS = ['sales', 'accounting', 'warehouse', 'boss', 'frontdesk', 'corporate', 'stamford']
TAGS = {'married', 'parent', 'dated', 'musician', 'pilot', 'wedding', 'left'}
out = []
for line in open('characters.txt', encoding='utf-8'):
    line = line.strip()
    if not line or line.startswith('#'): continue
    name, groups, tags = [x.strip() for x in line.split('|')]
    groups, tags = groups.split(), tags.split()
    assert all(g in GROUPS for g in groups), (name, groups)
    assert all(t in TAGS for t in tags), (name, tags)
    cols = tags + ['in_' + g for g in groups]
    out.append([name, '', '|'.join(groups), ' '.join(cols), 0])
names = [o[0] for o in out]; assert len(names) == len(set(names)), 'duplicate names'
print(len(out), 'characters')
print('per row', {g: sum(1 for o in out if g in o[2].split('|')) for g in GROUPS})
print(collections.Counter(c for o in out for c in o[3].split() if not c.startswith('in_')))
json.dump({'songs': out, 'artists': []}, open('data.json', 'w'), ensure_ascii=False, separators=(',', ':'))
