t = open('pop/template.html').read()
def rep(a, b):
    global t
    assert a in t, a[:60]; t = t.replace(a, b)
rep('<title>Hook Grid</title>', '<title>Swiftie Grid</title>')
rep('family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=DM+Sans', 'family=Instrument+Serif:ital@0;1&family=DM+Sans')
rep('/* Layout: one centered column like a chart sheet', '/* Layout: one centered column like a liner-notes sheet')
rep("""  --bg: #f3effa;
  --panel: #ffffff;
  --ink: #1d1530;
  --muted: #6a5f82;
  --line: #ddd4ec;
  --accent: #d6246e;
  --accent-2: #2f6fe0;""", """  --bg: #eef0f8;
  --panel: #ffffff;
  --ink: #181b33;
  --muted: #5e6488;
  --line: #d6daec;
  --accent: #7b4fd6;
  --accent-2: #b0428a;""")
rep('--font-display: "Bricolage Grotesque", "Arial Black", system-ui, sans-serif;', '--font-display: "Instrument Serif", Georgia, "Times New Roman", serif;')
t = t.replace("--bg: #130e20; --panel: #1f1833; --ink: #f2edfb; --muted: #a79cc2; --line: #342a4d;", "--bg: #0e1024; --panel: #191c38; --ink: #eef0ff; --muted: #9ea3c8; --line: #2c3058;")
t = t.replace("--accent: #ff4f96; --accent-2: #6aa0ff; --accent-ink: #1a0610;", "--accent: #b49bff; --accent-2: #f08fc6; --accent-ink: #160b33;")
assert '#ff4f96' not in t
rep('h1 { font-family: var(--font-display); font-weight: 800; font-size: clamp(30px, 9vw, 40px); line-height: .95; margin: 0; letter-spacing: -.03em;', 'h1 { font-family: var(--font-display); font-weight: 400; font-size: clamp(36px, 11vw, 50px); line-height: .9; margin: 0; letter-spacing: -.01em;')
rep('h1 span { color: var(--accent); }', 'h1 span { color: var(--accent); font-style: italic; }')
rep('.left b { display: block; font-family: var(--font-display); font-weight: 800; font-size: 32px;', '.left b { display: block; font-family: var(--font-display); font-weight: 400; font-size: 40px;')
rep('font-family: var(--font-display); font-weight: 700; font-size: 13.5px; letter-spacing: -.01em; }', 'font-family: var(--font-body); font-weight: 700; font-size: 12.5px; letter-spacing: -.005em; }')
rep('font-family: var(--font-display); font-weight: 800; font-size: clamp(12.5px, 3.6vw, 16px); letter-spacing: -.02em; }', 'font-family: var(--font-display); font-weight: 400; font-size: clamp(17px, 5vw, 22px); letter-spacing: 0; }')
rep('.summary h2 { margin: 0; font-family: var(--font-display); font-weight: 800; font-size: 24px; letter-spacing: -.02em; }', '.summary h2 { margin: 0; font-family: var(--font-display); font-weight: 400; font-size: 30px; }')
rep('.prompt { font-family: var(--font-display); font-weight: 700; font-size: 16px;', '.prompt { font-family: var(--font-display); font-weight: 400; font-size: 21px;')
rep('<h1>Hook <span>Grid</span></h1>', '<h1>Swiftie <span>Grid</span></h1>')
a = t.index('  <p class="rules">Tap a square'); b = t.index('</div>', a)
t = t[:a] + """  <p class="rules">Tap a square and name a <b>Taylor Swift song</b> from the <b>album on the left</b> that fits the <b>fact on top</b>. Every grid has at least one lyric square. You get 9 guesses, and each song can be used once.</p>
  <p class="rules">The song list covers all 12 studio albums, including deluxe tracks, From the Vault songs and the Showgirl Encore edition, from Wikipedia. Re-recorded songs count under their original album. Track numbers, writers, singles and chart peaks come from Wikipedia. The lyric squares were tagged by hand, so a song that fits might be missing, and Encore-edition songs have no lyric tags. Your guesses are saved on this device.</p>
""" + t[b:]
rep('placeholder="Search songs or artists…"', 'placeholder="Search song titles…"')
s0 = t.index('const DATA = __DATA__;'); s1 = t.index('function rng(')
t = t[:s0] + open('ts/head.js').read() + t[s1:]
rep("""    const rows = shuffle(ROWS, r).slice(0, 3);
    if (rows.filter(x => !x.startsWith('a:')).length > 1) continue;""", """    if (!cols.some(c => LYRIC.has(c))) continue;
    const rows = shuffle(ROWS, r).slice(0, 3);""")
rep("return { rows: ['a:Taylor Swift', 'a:Rihanna', 'a:Drake'], cols: ['t10', 'feat', 'late'] };", "return { rows: ['red', '1989', 'folklore'], cols: ['color', 'single', 'oneword'] };")
rep("    if (ok && thin <= 2) return { rows, cols };", "    if (ok && thin <= 3) return { rows, cols };")
rep("corner.textContent = 'Artist × song fact';", "corner.textContent = 'Album × song fact';")
rep("""    const rh = document.createElement('div'); rh.className = 'rowhead' + (row.startsWith('a:') ? '' : ' type'); rh.append(lab);
    if (!row.startsWith('a:')) { const sm = document.createElement('small'); sm.textContent = sub; rh.appendChild(sm); }""",
"""    const rh = document.createElement('div'); rh.className = 'rowhead' + (row === 'vault' ? ' type' : ''); rh.append(row === 'ttpd' ? 'TTPD' : row === 'showgirl' ? 'Showgirl' : lab);
    const sm = document.createElement('small'); sm.textContent = sub; rh.appendChild(sm);""")
rep("btn.querySelector('.name').textContent = s.title; btn.querySelector('.by').textContent = s.credit;", "btn.querySelector('.name').textContent = s.title; btn.querySelector('.by').textContent = s.album;")
rep("btn.setAttribute('aria-label', lab + ', ' + COLS[c][0] + ': ' + s.title + ' by ' + s.credit);", "btn.setAttribute('aria-label', lab + ', ' + COLS[c][0] + ': ' + s.title);")
rep("const IDX = SONGS.map(s => ({ t: norm(s.title), a: norm(s.credit) }));", "const IDX = SONGS.map(s => ({ t: norm(s.title), a: norm(s.album) }));")
rep("Type at least 2 letters of a song title or artist.", "Type at least 2 letters of a song title.")
rep("if (a.split(' ').some(w => w.startsWith(q)) || a.startsWith(q)) return 3; return 9; };", "return 9; };")
rep("const sm = document.createElement('small'); sm.textContent = s.credit + (used.has(s.i) ? ' · already used' : '');", "const sm = document.createElement('small'); sm.textContent = s.album + (used.has(s.i) ? ' · already used' : '');")
rep("No song by that name in the list.", "No Taylor Swift song by that name in the list.")
t = t.replace("'hk:", "'sg:")
assert 's.credit' not in t and "'hk:" not in t
d = open('ts/data.json').read().replace('</', '<\\/')
open('swiftie-grid.html', 'w').write(t.replace('__DATA__', d))
print('ok')
