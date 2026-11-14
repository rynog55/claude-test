import json, re
from bs4 import BeautifulSoup
def norm(s): return re.sub(r'[^a-z0-9]', '', re.sub(r'\(.*?\)', '', s.lower().replace('&', 'and')))
out = {}
for f, key in (('alt90','alt'),('alt80','alt'),('rock90','rock'),('rock80','rock')):
    s = BeautifulSoup(json.load(open('raw/%s.json' % f))['parse']['text'], 'lxml')
    pairs = set()
    for t in s.find_all('table', class_='wikitable'):
        for sup in t.find_all('sup'): sup.decompose()
        for tr in t.find_all('tr'):
            c = tr.find_all(['td','th'])
            for i, x in enumerate(c[:-1]):
                tx = x.get_text(' ', strip=True).replace('“','"').replace('”','"')
                m = re.fullmatch(r'"\s*(.+?)\s*"\s*(\(.*\))?', tx)
                if m: pairs.add((norm(m.group(1)), c[i+1].get_text(' ', strip=True))); break
    out[key] = out.get(key, []) + sorted(pairs)
    print(f, len(pairs))
json.dump(out, open('charts.json', 'w'))
