"""characters.txt -> data.json for Throne Grid (same shape as the other grids)."""
import json, collections
GROUPS = ['stark', 'lannister', 'targaryen', 'baratheon', 'greyjoy', 'tyrell', 'martell', 'tully', 'bolton', 'watch', 'kingsguard', 'council', 'freefolk']
TAGS = {'king', 'hand', 'dragon', 'resurrected', 'aryakill', 'bastard'}
out = []
for line in open('characters.txt', encoding='utf-8'):
    line = line.strip()
    if not line or line.startswith('#'): continue
    name, groups, tags, death = [x.strip() for x in line.split('|')]
    groups, tags = groups.split(), tags.split()
    assert all(g in GROUPS for g in groups), (name, groups)
    assert all(t in TAGS for t in tags), (name, tags)
    assert death in ('0', '-') or death in '12345678', (name, death)
    cols = list(tags)
    if death == '0': cols.append('survives')
    if death in list('12345678'):
        cols.append('dies'); cols.append('early' if int(death) <= 4 else 'late')
    if death == '0' and 'resurrected' in tags:   # Jon Snow died in season 5 and came back
        cols += ['dies', 'late']
    cols += ['in_' + g for g in groups]
    out.append([name, '', '|'.join(groups), ' '.join(cols), 0])
names = [o[0] for o in out]; assert len(names) == len(set(names)), 'duplicate names'
print(len(out), 'characters')
print('per row', {g: sum(1 for o in out if g in o[2].split('|')) for g in GROUPS})
print(collections.Counter(c for o in out for c in o[3].split() if not c.startswith('in_')))
json.dump({'songs': out, 'artists': []}, open('data.json', 'w'), ensure_ascii=False, separators=(',', ':'))
