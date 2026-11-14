t = open('pop/template.html').read()
def rep(a, b, n=1):
    global t
    assert a in t, a[:70]; t = t.replace(a, b) if n == 0 else t.replace(a, b, n)
rep('<title>Hook Grid</title>', '<title>Flannel Grid</title>')
rep('family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=DM+Sans', 'family=Special+Elite&family=DM+Sans')
rep('like a chart sheet', 'like a photocopied zine page')
rep("""  --bg: #f3effa;
  --panel: #ffffff;
  --ink: #1d1530;
  --muted: #6a5f82;
  --line: #ddd4ec;
  --accent: #d6246e;
  --accent-2: #2f6fe0;""", """  --bg: #e7e6e2;
  --panel: #f8f7f4;
  --ink: #1a1916;
  --muted: #625e56;
  --line: #d0cdc5;
  --accent: #b02a20;
  --accent-2: #2d6a4c;""")
rep('--font-display: "Bricolage Grotesque", "Arial Black", system-ui, sans-serif;', '--font-display: "Special Elite", "Courier New", monospace;')
rep("--bg: #130e20; --panel: #1f1833; --ink: #f2edfb; --muted: #a79cc2; --line: #342a4d;", "--bg: #131310; --panel: #1e1d19; --ink: #efece4; --muted: #a39e92; --line: #363329;", 0)
rep("--accent: #ff4f96; --accent-2: #6aa0ff; --accent-ink: #1a0610;", "--accent: #e8604f; --accent-2: #6fc39a; --accent-ink: #1c0805;", 0)
rep('h1 { font-family: var(--font-display); font-weight: 800; font-size: clamp(30px, 9vw, 40px); line-height: .95; margin: 0; letter-spacing: -.03em;', 'h1 { font-family: var(--font-display); font-weight: 400; font-size: clamp(30px, 9vw, 42px); line-height: 1; margin: 0; letter-spacing: -.01em;')
rep('.left b { display: block; font-family: var(--font-display); font-weight: 800;', '.left b { display: block; font-family: var(--font-display); font-weight: 400;')
rep('.head { align-items: center; text-align: center; padding: 6px 3px; min-height: 66px; gap: 3px; font-family: var(--font-display); font-weight: 700; font-size: 13.5px; letter-spacing: -.01em; }', '.head { align-items: center; text-align: center; padding: 6px 3px; min-height: 66px; gap: 3px; font-family: var(--font-body); font-weight: 700; font-size: 12.5px; letter-spacing: -.005em; }')
rep('font-family: var(--font-display); font-weight: 800; font-size: clamp(12.5px, 3.6vw, 16px); letter-spacing: -.02em; }', 'font-family: var(--font-display); font-weight: 400; font-size: clamp(11px, 3.2vw, 15px); letter-spacing: -.035em; overflow-wrap: normal; }')
rep('.summary h2 { margin: 0; font-family: var(--font-display); font-weight: 800;', '.summary h2 { margin: 0; font-family: var(--font-display); font-weight: 400;')
rep('.prompt { font-family: var(--font-display); font-weight: 700;', '.prompt { font-family: var(--font-display); font-weight: 400;')
rep('.board { display: grid; grid-template-columns: minmax(0, .85fr) repeat(3, minmax(0, 1fr)); gap: 6px; }', '.board { display: grid; grid-template-columns: minmax(0, 1.1fr) repeat(3, minmax(0, 1fr)); gap: 6px; }')
rep('<h1>Hook <span>Grid</span></h1>', '<h1>Flannel <span>Grid</span></h1>')
a = t.index('  <p class="rules">Tap a square'); b = t.index('</div>', a)
t = t[:a] + """  <p class="rules">Tap a square and name a song from <b>your '90s alt-radio playlist</b> that fits the <b>band on the left</b> and the <b>fact on top</b>. You get 9 guesses, and each song can be used once.</p>
  <p class="rules">The answer list is the 327 songs on your Spotify playlist of tracks heard on SiriusXM's '90s alternative channel. This game isn't affiliated with SiriusXM. Length, popularity, label, explicit flag and the mood, energy, key and acoustic ratings come from Spotify's data. Popularity was measured when you exported the playlist: "Deep cut" is the least-played quarter and "Spotify smash" the most-played quarter. Modern Rock and Mainstream Rock No. 1s come from Wikipedia. Years use the song's original release, and band facts were tagged by hand. Your guesses are saved on this device.</p>
""" + t[b:]
s0 = t.index('const TYPE_ROWS = {'); s1 = t.index("const ROWS = ")
t = t[:s0] + """const TYPE_ROWS = {
  seattle: ['Seattle-area band', 'Washington State'],
  female: ['Female lead singer', 'Band or solo'],
  lostsinger: ['Lead singer has died', 'Or a lead vocalist'],
  california: ['From California', 'Formed or based there'],
  abroad: ['From outside the US', 'UK, Ireland, Canada, Australia'],
  unplugged: ['Did MTV Unplugged', 'In the 1990s'],
  lolla: ['Played Lollapalooza', '1991 to 1997 tours'],
  onesong: ['Only one song here', 'Just one on the playlist']
};
const COLS = {
  altno1: ['Modern Rock No. 1', 'Billboard alternative chart'],
  rockno1: ['Mainstream Rock No. 1', 'Billboard rock chart'],
  live: ['Live recording', 'The version on the playlist'],
  acoustic: ['Mostly acoustic', 'Spotify acoustic rating'],
  minor: ['In a minor key', 'Spotify key analysis'],
  dark: ['Dark mood', 'Spotify mood rating'],
  upbeat: ['Upbeat mood', 'Spotify mood rating'],
  blast: ['Full blast', 'Top energy rating'],
  long: ['5 minutes or longer', 'Track length'],
  short: ['Under 3 minutes', 'Track length'],
  deep: ['Deep cut', 'Least-played quarter on Spotify'],
  smash: ['Spotify smash', 'Most-played quarter'],
  explicit: ['Explicit', 'Spotify explicit tag'],
  y1: ['Released by 1993', 'Original release'],
  y2: ['Released 1994–95', 'Original release'],
  y3: ['Released 1996 or later', 'Original release'],
  selftitled: ['From a self-titled album', 'Album shares the band name'],
  oneword: ['One-word title', 'Ignoring parentheses'],
  geffen: ['On Geffen or DGC', 'Record label']
};
const CLASH = [['y1','y2'],['y1','y3'],['y2','y3'],['dark','upbeat'],['long','short'],['deep','smash']];
""" + t[s1:]
rep("const rowLabel = r => r.startsWith('a:') ? [r.slice(2), 'Lead or featured'] : TYPE_ROWS[r];", "const rowLabel = r => r.startsWith('a:') ? [r.slice(2), ''] : TYPE_ROWS[r];")
rep("return { rows: ['a:Taylor Swift', 'a:Rihanna', 'a:Drake'], cols: ['t10', 'feat', 'late'] };", "return { rows: ['a:Nirvana', 'a:Pearl Jam', 'seattle'], cols: ['altno1', 'minor', 'y1'] };")
rep("corner.textContent = 'Artist × song fact';", "corner.textContent = 'Band × song fact';")
rep("Type at least 2 letters of a song title or artist.", "Type at least 2 letters of a song or band.")
rep("No song by that name in the list.", "That song isn’t on the playlist.")

rep("const CLASH = [['y1','y2']", """const MEDIUM_COLS = ['altno1', 'smash', 'long', 'short', 'y1', 'y2', 'y3', 'oneword'];
const MEDIUM_ROWS = DATA.artists.filter(a => SONGS.filter(s => s.rows.has('a:' + a)).length >= 8).map(a => 'a:' + a).concat(['seattle', 'female', 'california', 'abroad', 'lostsinger']);
let MODE = 'medium';
try { const m = localStorage.getItem('fl:mode'); if (m === 'hard' || m === 'medium') MODE = m; } catch (e) {}
const CLASH = [['y1','y2']""")
rep("  const r = rng(seed);", "  const r = rng(MODE + ':' + seed); const COLPOOL = MODE === 'medium' ? MEDIUM_COLS : Object.keys(COLS); const ROWPOOL = MODE === 'medium' ? MEDIUM_ROWS : ROWS; const MIN = MODE === 'medium' ? 2 : 1;")
rep("const cols = shuffle(Object.keys(COLS), r).slice(0, 3);", "const cols = shuffle(COLPOOL, r).slice(0, 3);")
rep("const rows = shuffle(ROWS, r).slice(0, 3);", "const rows = shuffle(ROWPOOL, r).slice(0, 3);")
rep("if (!n) ok = false;", "if (n < MIN) ok = false;")
rep("    if (rows.filter(x => !x.startsWith('a:')).length > 1) continue;", "    if (rows.filter(x => !x.startsWith('a:')).length > (MODE === 'medium' ? 2 : 1)) continue;")
rep("cols: ['altno1', 'minor', 'y1'] };", "cols: ['altno1', 'long', 'y1'] };")
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
d = open('lith/data.json').read().replace('</', '<\\/')
open('flannel-grid.html', 'w').write(t.replace('__DATA__', d)); print('ok')
