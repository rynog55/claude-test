t = open('pop/template.html').read()
def rep(a, b, n=1):
    global t
    assert a in t, a[:70]; t = t.replace(a, b) if n == 0 else t.replace(a, b, n)
rep('<title>Hook Grid</title>', '<title>Throne Grid</title>')
rep('family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=DM+Sans', 'family=Marcellus+SC&family=DM+Sans')
rep('like a chart sheet', 'like a war-room map')
rep("""  --bg: #f3effa;
  --panel: #ffffff;
  --ink: #1d1530;
  --muted: #6a5f82;
  --line: #ddd4ec;
  --accent: #d6246e;
  --accent-2: #2f6fe0;""", """  --bg: #e6e7ea;
  --panel: #ffffff;
  --ink: #17181c;
  --muted: #5d5f68;
  --line: #d2d4da;
  --accent: #9b1c1c;
  --accent-2: #6d5a2a;""")
rep('--font-display: "Bricolage Grotesque", "Arial Black", system-ui, sans-serif;', '--font-display: "Marcellus SC", Georgia, "Times New Roman", serif;')
rep("--bg: #130e20; --panel: #1f1833; --ink: #f2edfb; --muted: #a79cc2; --line: #342a4d;", "--bg: #121316; --panel: #1c1d22; --ink: #ecebe8; --muted: #a3a19c; --line: #34353b;", 0)
rep("--accent: #ff4f96; --accent-2: #6aa0ff; --accent-ink: #1a0610;", "--accent: #e05a4a; --accent-2: #c9a557; --accent-ink: #1e0604;", 0)
rep('h1 { font-family: var(--font-display); font-weight: 800; font-size: clamp(30px, 9vw, 40px); line-height: .95; margin: 0; letter-spacing: -.03em;', 'h1 { font-family: var(--font-display); font-weight: 400; font-size: clamp(38px, 11.5vw, 54px); line-height: .95; margin: 0; letter-spacing: 0;')
rep('.left b { display: block; font-family: var(--font-display); font-weight: 800;', '.left b { display: block; font-family: var(--font-display); font-weight: 400;')
rep('.head { align-items: center; text-align: center; padding: 6px 3px; min-height: 66px; gap: 3px; font-family: var(--font-display); font-weight: 700; font-size: 13.5px; letter-spacing: -.01em; }', '.head { align-items: center; text-align: center; padding: 6px 3px; min-height: 66px; gap: 3px; font-family: var(--font-body); font-weight: 700; font-size: 12.5px; letter-spacing: -.005em; }')
rep('font-family: var(--font-display); font-weight: 800; font-size: clamp(12.5px, 3.6vw, 16px); letter-spacing: -.02em; }', 'font-family: var(--font-display); font-weight: 400; font-size: clamp(14px, 4.1vw, 19px); letter-spacing: 0; overflow-wrap: normal; }')
rep('.summary h2 { margin: 0; font-family: var(--font-display); font-weight: 800;', '.summary h2 { margin: 0; font-family: var(--font-display); font-weight: 400;')
rep('.prompt { font-family: var(--font-display); font-weight: 700;', '.prompt { font-family: var(--font-display); font-weight: 400;')
rep('.board { display: grid; grid-template-columns: minmax(0, .85fr) repeat(3, minmax(0, 1fr)); gap: 6px; }', '.board { display: grid; grid-template-columns: minmax(0, 1.1fr) repeat(3, minmax(0, 1fr)); gap: 6px; }')
rep('<h1>Hook <span>Grid</span></h1>', '<h1>Throne <span>Grid</span></h1>\n      <p class="tagline" style="margin:6px 0 0;font-style:italic;font-size:13.5px;color:var(--accent-2)">The show only. Yes, season 8 counts.</p>')
a = t.index('  <p class="rules">Tap a square'); b = t.index('</div>', a)
t = t[:a] + """  <p class="rules">Tap a square and name a <b>character</b> who fits both the <b>row on the left</b> and the <b>fact on top</b>. Rows and columns can be great houses, groups like the Night's Watch or the Kingsguard, or a character's fate. You get 9 guesses, and each character can be used once.</p>
  <p class="rules">Only the HBO series counts (seasons 1 to 8), not the books or the spin-offs. A house counts by birth, or by marrying in and taking the name, so Catelyn is a Tully and a Stark; Jon Snow counts as Stark and Targaryen; Joffrey, Tommen and Myrcella count as Baratheon and Lannister. "Dies on screen" includes Jon Snow, who died in season 5 and came back. "King or queen" includes rulers and claimants. <b>Medium</b> uses the bigger houses, the Night's Watch, the Kingsguard and the Small Council; <b>Hard</b> adds Martell, Tully, Bolton and the Free Folk. The list covers about 110 characters compiled by hand, so a character who fits might be missing. This is a fan-made game and isn't affiliated with HBO. Your guesses are saved on this device.</p>
""" + t[b:]
s0 = t.index('const TYPE_ROWS = {'); s1 = t.index("const ROWS = ")
t = t[:s0] + """const TYPE_ROWS = { stark: ['House Stark', 'Winterfell'], lannister: ['House Lannister', 'Casterly Rock'], targaryen: ['House Targaryen', 'Dragonstone'], baratheon: ['House Baratheon', "Storm's End"], greyjoy: ['House Greyjoy', 'Iron Islands'], tyrell: ['House Tyrell', 'Highgarden'], martell: ['House Martell', 'Dorne'], tully: ['House Tully', 'Riverrun'], bolton: ['House Bolton', 'The Dreadfort'], watch: ["Night's Watch", 'Sworn brothers'], kingsguard: ['Kingsguard', 'Or Queensguard'], council: ['Small Council', 'Any time'], freefolk: ['Free Folk', 'Beyond the Wall'] };
const COLS = {
  dies: ['Dies on screen', 'Even if they come back'],
  early: ['Dies in seasons 1–4', 'On screen'],
  late: ['Dies in seasons 5–8', 'On screen'],
  survives: ['Alive at the end', 'After season 8'],
  king: ['King or queen', 'Ruler or claimant'],
  hand: ['Hand of the King', 'Or of the Queen'],
  dragon: ['Rode a dragon', 'Any dragon'],
  resurrected: ['Came back from the dead', 'Any way'],
  aryakill: ['Killed by Arya', 'On screen'],
  bastard: ['Born a bastard', 'Snow, Sand and others'],
  in_stark: ['House Stark', 'Birth or marriage'], in_lannister: ['House Lannister', 'Birth or marriage'], in_targaryen: ['House Targaryen', 'Birth'],
  in_baratheon: ['House Baratheon', 'Birth or marriage'], in_greyjoy: ['House Greyjoy', 'Birth'], in_tyrell: ['House Tyrell', 'Birth'],
  in_martell: ['House Martell', 'Birth'], in_tully: ['House Tully', 'Birth'], in_bolton: ['House Bolton', 'Birth'],
  in_watch: ["Night's Watch", 'Sworn brother'], in_kingsguard: ['Kingsguard', 'Or Queensguard'], in_council: ['Small Council', 'Any time'], in_freefolk: ['Free Folk', 'Beyond the Wall']
};
const CLASH = [['y1','y2'],['early','late'],['early','survives']];
""" + t[s1:]
rep("const rowLabel = r => r.startsWith('a:') ? [r.slice(2), 'Lead or featured'] : TYPE_ROWS[r];", "const rowLabel = r => r.startsWith('a:') ? [r.slice(2), ''] : TYPE_ROWS[r];")
rep("return { rows: ['a:Taylor Swift', 'a:Rihanna', 'a:Drake'], cols: ['t10', 'feat', 'late'] };", "return { rows: ['stark', 'lannister', 'council'], cols: ['dies', 'survives', 'late'] };")
rep("corner.textContent = 'Artist × song fact';", "corner.textContent = 'Band × song fact';")
rep("Type at least 2 letters of a song title or artist.", "Type at least 2 letters of a song or band.")
rep("No song by that name in the list.", "That song isn’t on the playlist.")

rep("const CLASH = [['y1','y2']", """const MEDIUM_COLS = ['dies', 'survives', 'early', 'late', 'king', 'hand', 'bastard', 'in_stark', 'in_lannister', 'in_targaryen', 'in_baratheon', 'in_watch', 'in_kingsguard', 'in_council'];
const MEDIUM_ROWS = DATA.artists.filter(a => SONGS.filter(s => s.rows.has('a:' + a)).length >= 8).map(a => 'a:' + a).concat(['stark', 'lannister', 'targaryen', 'baratheon', 'greyjoy', 'tyrell', 'watch', 'kingsguard', 'council']);
let MODE = 'medium';
try { const m = localStorage.getItem('fl:mode'); if (m === 'hard' || m === 'medium') MODE = m; } catch (e) {}
const CLASH = [['y1','y2']""")
rep("  const r = rng(seed);", "  const r = rng(MODE + ':' + seed); const COLPOOL = MODE === 'medium' ? MEDIUM_COLS : Object.keys(COLS); const ROWPOOL = MODE === 'medium' ? MEDIUM_ROWS : ROWS; const MIN = MODE === 'medium' ? 2 : 1;")
rep("const cols = shuffle(Object.keys(COLS), r).slice(0, 3);", "const cols = shuffle(COLPOOL, r).slice(0, 3);")
rep("const rows = shuffle(ROWS, r).slice(0, 3);", "const rows = shuffle(ROWPOOL, r).slice(0, 3);")
rep("if (!n) ok = false;", "if (n < (c.startsWith('in_') ? 1 : MIN)) ok = false;")
rep("    if (rows.filter(x => !x.startsWith('a:')).length > 1) continue;", "    if (cols.some(c => c.startsWith('in_') && rows.includes(c.slice(3)))) continue;")
rep("""      <p class="sub" id="label">Daily grid</p>
    </div>""", """      <p class="sub" id="label">Daily grid</p>
    </div>""")
rep("""  <div class="board" id="board" aria-label="Puzzle grid"></div>""", """  <div class="modes" role="group" aria-label="Difficulty">
    <button type="button" class="mode" id="mode-medium" data-mode="medium">Medium</button>
    <button type="button" class="mode" id="mode-hard" data-mode="hard">Hard</button>
  </div>

  <div class="board" id="board" aria-label="Puzzle grid"></div>""")
rep(".controls { display: flex;", """.modes { display: flex; gap: 0; align-self: flex-start; border: 1px solid var(--line); border-radius: 999px; padding: 3px; background: var(--panel); }
.mode { font: 600 13px var(--font-body); border: 0; border-radius: 999px; padding: 7px 16px; background: transparent; color: var(--muted); cursor: pointer; }
.mode[aria-pressed="true"] { background: var(--ink); color: var(--bg); }
.mode:focus-visible { outline: 3px solid var(--accent); outline-offset: 2px; }
.controls { display: flex;""")
rep("const last = store.get(", """function setMode(m) {
  MODE = m;
  try { localStorage.setItem('fl:mode', m); } catch (e) {}
  document.querySelectorAll('.mode').forEach(b => b.setAttribute('aria-pressed', String(b.dataset.mode === m)));
}
document.querySelectorAll('.mode').forEach(b => b.addEventListener('click', () => { if (b.dataset.mode !== MODE) { setMode(b.dataset.mode); load(seed); } }));
setMode(MODE);
const last = store.get(""")
rep("""Your guesses are saved on this device.</p>""", """<b>Medium</b> sticks to the bigger bands and well-known facts, and every square has at least 2 right answers. <b>Hard</b> adds every band, more band types, and Spotify's mood, key, energy and popularity ratings. Your guesses are saved on this device.</p>""")

t = t.replace("'hk:", "'fl:")
t = t.replace("'fl:' + seed", "'fl:' + MODE + ':' + seed")
t = t.replace("'fl:", "'tg:")
t = t.replace('Band × song fact', 'House or group × fact').replace('Type at least 2 letters of a song or band.', 'Type at least 2 letters of a name.').replace('That song isn’t on the playlist.', 'That character isn’t in the list.').replace('Empty squares now show songs that would have worked.', 'Empty squares now show characters who would have worked.')
d = open('thrones/data.json').read().replace('</', '<\\/')
open('throne-grid.html', 'w').write(t.replace('__DATA__', d)); print('ok')
