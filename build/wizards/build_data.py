"""characters.txt -> data.json for Wizard Grid (same shape as the other grids)."""
import json, collections
GROUPS = ['G', 'S', 'R', 'H', 'order', 'da', 'de', 'weasley', 'staff', 'ministry']
TAGS = {'died', 'quidditch', 'seeker', 'captain', 'prefect', 'animagus', 'ghost', 'triwizard', 'parselmouth', 'pure', 'half', 'muggleborn'}
out = []
for line in open('characters.txt', encoding='utf-8'):
    line = line.strip()
    if not line or line.startswith('#'): continue
    name, groups, tags = [x.strip() for x in line.split('|')]
    groups = groups.split(); tags = tags.split()
    assert all(g in GROUPS for g in groups), (name, groups)
    assert all(t in TAGS for t in tags), (name, tags)
    assert sum(g in 'GSRH' for g in groups) <= 1, (name, 'two houses')
    assert sum(t in ('pure', 'half', 'muggleborn') for t in tags) <= 1, (name, 'two blood statuses')
    cols = tags + ['in_' + g for g in groups]
    out.append([name, '', '|'.join(groups), ' '.join(cols), 0])
names = [o[0] for o in out]; assert len(names) == len(set(names)), 'duplicate names'
print(len(out), 'characters')
print('per row', {g: sum(1 for o in out if g in o[2].split('|')) for g in GROUPS})
print(collections.Counter(c for o in out for c in o[3].split() if not c.startswith('in_')))
json.dump({'songs': out, 'artists': []}, open('data.json', 'w'), ensure_ascii=False, separators=(',', ':'))
