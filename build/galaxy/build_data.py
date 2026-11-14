"""characters.txt -> data.json for Galaxy Grid (same shape as the other grids)."""
import json, collections
FILMS = ['1', '2', '3', '4', '5', '6']
GROUPS = ['jedi', 'sith', 'rebel', 'empire', 'republic', 'separatist', 'hunter']
TAGS = {'saber', 'dies', 'pilot', 'droid', 'alien', 'skywalker', 'tatooine', 'limb'}
out = []
for line in open('characters.txt', encoding='utf-8'):
    line = line.strip()
    if not line or line.startswith('#'): continue
    name, films, groups, tags = [x.strip() for x in line.split('|')]
    films, groups, tags = films.split(), groups.split(), tags.split()
    assert films and all(f in FILMS for f in films), (name, films)
    assert all(g in GROUPS for g in groups), (name, groups)
    assert all(t in TAGS for t in tags), (name, tags)
    assert not ('droid' in tags and 'alien' in tags), name
    rows = ['ep' + f for f in films] + groups
    cols = list(tags)
    if any(f in '123' for f in films) and any(f in '456' for f in films): cols.append('both')
    cols += ['in_ep' + f for f in films] + ['in_' + g for g in groups]
    out.append([name, '', '|'.join(rows), ' '.join(cols), 0])
names = [o[0] for o in out]; assert len(names) == len(set(names)), 'duplicate names'
print(len(out), 'characters')
print('per row', {r: sum(1 for o in out if r in o[2].split('|')) for r in ['ep' + f for f in FILMS] + GROUPS})
print(collections.Counter(c for o in out for c in o[3].split() if not c.startswith('in_')))
json.dump({'songs': out, 'artists': []}, open('data.json', 'w'), ensure_ascii=False, separators=(',', ':'))
