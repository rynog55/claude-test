import json, re
from bs4 import BeautifulSoup
ALB = ['i','ii','iii','iv','hoth','pg','presence','itod']
DEFAULT = {'ii':'Page Plant','iv':'Page Plant','hoth':'Page Plant','pg':'Page Plant','itod':'Jones Page Plant'}
songs = []
for al in ALB:
    s = BeautifulSoup(json.load(open('raw/%s.json' % al))['parse']['text'], 'lxml')
    side = 0
    for t in s.find_all('table', class_='tracklist'):
        cap = t.find('caption').get_text(' ', strip=True) if t.find('caption') else ''
        if not re.match(r'Side', cap): continue
        side += 1
        for sup in t.find_all('sup'): sup.decompose()
        hdr = [c.get_text(' ', strip=True).lower() for c in t.find('tr').find_all(['th','td'])]
        wi = next((i for i,h in enumerate(hdr) if 'writer' in h), None)
        li = next((i for i,h in enumerate(hdr) if 'length' in h), None)
        rows = [tr for tr in t.find_all('tr')[1:] if tr.find_all(['th','td']) and re.match(r'\d+\.', tr.find_all(['th','td'])[0].get_text(strip=True))]
        for n, tr in enumerate(rows):
            c = tr.find_all(['th','td'])
            raw = c[1].get_text(' ', strip=True).replace('“','"').replace('”','"')
            m = re.search(r'"\s*(.+?)\s*"', raw); title = re.sub(r'\s*\[.*?\]', '', m.group(1) if m else raw).strip()
            w = c[wi].get_text(' ', strip=True) if wi is not None else ''
            if not w: w = DEFAULT.get(al, '?')
            ln = c[li].get_text(strip=True) if li is not None else ''
            mm, ss = (ln.split(':') + ['0'])[:2]
            songs.append(dict(album=al, title=title, writers=w, secs=int(mm)*60+int(re.sub(r'\D','',ss) or 0), side=side, sidepos=n+1, sidelen=len(rows)))
coda = [("We're Gonna Groove","Ben E. King James Bethea",'2:40'),("Poor Tom","Page Plant",'3:02'),("I Can't Quit You Baby","Willie Dixon",'4:18'),("Walter's Walk","Page Plant",'4:31'),("Ozone Baby","Page Plant",'3:36'),("Darlene","Bonham Jones Page Plant",'5:06'),("Bonzo's Montreux","Bonham",'4:22'),("Wearing and Tearing","Page Plant",'5:30')]
for i,(t,w,l) in enumerate(coda):
    m,s_ = l.split(':'); songs.append(dict(album='coda', title=t, writers=w, secs=int(m)*60+int(s_), side=1 if i<4 else 2, sidepos=i%4+1, sidelen=4))
json.dump(songs, open('songs.json','w'), indent=0)
for s in songs: print(s['album'], s['side'], s['sidepos'], s['title'], '|', s['writers'], '|', s['secs'])
