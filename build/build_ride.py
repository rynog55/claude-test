t = open('pop/template.html').read()
def rep(a, b, n=1):
    global t
    assert a in t, a[:70]; t = t.replace(a, b) if n == 0 else t.replace(a, b, n)
rep('<title>Hook Grid</title>', '<title>Ride Grid</title>')
rep('family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=DM+Sans', 'family=Fredoka:wght@500;600;700&family=DM+Sans')
rep('like a chart sheet', 'like a park guide map')
rep("""  --bg: #f3effa;
  --panel: #ffffff;
  --ink: #1d1530;
  --muted: #6a5f82;
  --line: #ddd4ec;
  --accent: #d6246e;
  --accent-2: #2f6fe0;""", """  --bg: #ecf2f4;
  --panel: #ffffff;
  --ink: #132630;
  --muted: #566b75;
  --line: #d3dee3;
  --accent: #d2452f;
  --accent-2: #1f7489;""")
rep('--font-display: "Bricolage Grotesque", "Arial Black", system-ui, sans-serif;', '--font-display: "Fredoka", "Trebuchet MS", system-ui, sans-serif;')
rep("--bg: #130e20; --panel: #1f1833; --ink: #f2edfb; --muted: #a79cc2; --line: #342a4d;", "--bg: #0c1820; --panel: #15242e; --ink: #eef5f8; --muted: #9db2bc; --line: #29404c;", 0)
rep("--accent: #ff4f96; --accent-2: #6aa0ff; --accent-ink: #1a0610;", "--accent: #ff7a5c; --accent-2: #5cc9e0; --accent-ink: #1d0802;", 0)
rep('h1 { font-family: var(--font-display); font-weight: 800; font-size: clamp(30px, 9vw, 40px); line-height: .95; margin: 0; letter-spacing: -.03em;', 'h1 { font-family: var(--font-display); font-weight: 400; font-size: clamp(36px, 11vw, 50px); line-height: .95; margin: 0; letter-spacing: -.01em;')
rep('.left b { display: block; font-family: var(--font-display); font-weight: 800;', '.left b { display: block; font-family: var(--font-display); font-weight: 400;')
rep('.head { align-items: center; text-align: center; padding: 6px 3px; min-height: 66px; gap: 3px; font-family: var(--font-display); font-weight: 700; font-size: 13.5px; letter-spacing: -.01em; }', '.head { align-items: center; text-align: center; padding: 6px 3px; min-height: 66px; gap: 3px; font-family: var(--font-body); font-weight: 700; font-size: 12.5px; letter-spacing: -.005em; }')
rep('font-family: var(--font-display); font-weight: 800; font-size: clamp(12.5px, 3.6vw, 16px); letter-spacing: -.02em; }', 'font-family: var(--font-display); font-weight: 400; font-size: clamp(13px, 3.8vw, 17px); letter-spacing: 0; overflow-wrap: normal; }')
rep('.summary h2 { margin: 0; font-family: var(--font-display); font-weight: 800;', '.summary h2 { margin: 0; font-family: var(--font-display); font-weight: 400;')
rep('.prompt { font-family: var(--font-display); font-weight: 700;', '.prompt { font-family: var(--font-display); font-weight: 400;')
rep('.board { display: grid; grid-template-columns: minmax(0, .85fr) repeat(3, minmax(0, 1fr)); gap: 6px; }', '.board { display: grid; grid-template-columns: minmax(0, 1.1fr) repeat(3, minmax(0, 1fr)); gap: 6px; }')
rep('<h1>Hook <span>Grid</span></h1>', '<h1>Ride <span>Grid</span></h1>')
a = t.index('  <p class="rules">Tap a square'); b = t.index('</div>', a)
t = t[:a] + """  <p class="rules">Disney parks trivia. Tap a square and name an <b>attraction</b> at the <b>park on the left</b> that fits the <b>fact on top</b>. Rides that exist at several parks count as one answer, so Space Mountain works for any park that has a version of it. You get 9 guesses, and each ride can be used once.</p>
  <p class="rules"><b>Medium</b> uses the six US parks plus Disneyland Paris and Tokyo Disneyland, with the most familiar ride types. <b>Hard</b> adds Disney Adventure World, Tokyo DisneySea, Hong Kong and Shanghai, plus crossovers with every park and finer categories like Omnimover and trackless rides. The list covers about 110 rides operating in 2026; shows, walk-throughs and rides closed for long rebuilds are left out. Ride facts were compiled by hand, so a ride that fits might be missing. This is a fan-made game and isn't affiliated with Disney. Your guesses are saved on this device.</p>
""" + t[b:]
s0 = t.index('const TYPE_ROWS = {'); s1 = t.index("const ROWS = ")
t = t[:s0] + """const PARK_NAMES = { MK: ['Magic Kingdom', 'Walt Disney World'], EP: ['EPCOT', 'Walt Disney World'], HS: ['Hollywood Studios', 'Walt Disney World'], AK: ['Animal Kingdom', 'Walt Disney World'], DL: ['Disneyland', 'California'], DCA: ['California Adventure', 'California'], DLP: ['Disneyland Paris', 'Disneyland Park'], DAW: ['Adventure World', 'Paris, formerly Studios'], TDL: ['Tokyo Disneyland', 'Tokyo'], TDS: ['Tokyo DisneySea', 'Tokyo'], HK: ['Hong Kong Disneyland', 'Hong Kong'], SH: ['Shanghai Disneyland', 'Shanghai'] };
const TYPE_ROWS = PARK_NAMES;
const COLS = {
  coaster: ['Roller coaster', 'Any size'],
  dark: ['Dark ride', 'Indoor scenes'],
  sim: ['Simulator', 'Motion theater or flight'],
  boat: ['Boat ride', 'You ride on water'],
  wet: ['You might get wet', 'Splashes or drops'],
  spinner: ['Spinning ride', 'Teacups and friends'],
  aerial: ['Spins up in the air', 'Dumbo-style'],
  drop: ['Big drop', 'Tower or flume plunge'],
  shooter: ['Shoot-and-score', 'Interactive points'],
  launch: ['Launched coaster', 'Zero to fast'],
  indoor: ['Indoor coaster', 'Coaster in the dark'],
  trackless: ['Trackless vehicles', 'Ride system'],
  omni: ['Omnimover', 'Continuous-loading cars'],
  hr: ['Height requirement', 'Any minimum'],
  pixar: ['Pixar', 'Based on a Pixar film'],
  starwars: ['Star Wars', 'Galaxy far, far away'],
  marvel: ['Marvel', 'Superheroes'],
  film: ['Disney animated film', 'Walt Disney Animation'],
  multi: ['At 3+ parks', 'Any version counts'],
  unique: ['Only at one park', 'One of a kind'],
  classic: ['Original opened by 1971', 'Disneyland or Magic Kingdom era'],
  new: ['Opened 2016 or later', 'Original version'],
  at_MK: ['Also at Magic Kingdom', 'Any version'], at_EP: ['Also at EPCOT', 'Any version'], at_HS: ['Also at Hollywood Studios', 'Any version'],
  at_DL: ['Also at Disneyland', 'Any version'], at_DCA: ['Also at California Adventure', 'Any version'],
  at_DLP: ['Also at Disneyland Paris', 'Any version'], at_DAW: ['Also at Adventure World', 'Paris'],
  at_TDL: ['Also at Tokyo Disneyland', 'Any version'], at_TDS: ['Also at Tokyo DisneySea', 'Any version'],
  at_HK: ['Also at Hong Kong', 'Any version'], at_SH: ['Also at Shanghai', 'Any version']
};
const CLASH = [['y1','y2'],['multi','unique'],['classic','new'],['unique','at_MK'],['unique','at_EP'],['unique','at_HS'],['unique','at_DL'],['unique','at_DCA'],['unique','at_DLP'],['unique','at_DAW'],['unique','at_TDL'],['unique','at_TDS'],['unique','at_HK'],['unique','at_SH'],['coaster','launch'],['coaster','indoor']];
""" + t[s1:]
rep("const rowLabel = r => r.startsWith('a:') ? [r.slice(2), 'Lead or featured'] : TYPE_ROWS[r];", "const rowLabel = r => r.startsWith('a:') ? [r.slice(2), ''] : TYPE_ROWS[r];")
rep("return { rows: ['a:Taylor Swift', 'a:Rihanna', 'a:Drake'], cols: ['t10', 'feat', 'late'] };", "return { rows: ['MK', 'DL', 'HS'], cols: ['dark', 'hr', 'multi'] };")
rep("corner.textContent = 'Artist × song fact';", "corner.textContent = 'Band × song fact';")
rep("Type at least 2 letters of a song title or artist.", "Type at least 2 letters of a song or band.")
rep("No song by that name in the list.", "That song isn’t on the playlist.")

rep("const CLASH = [['y1','y2']", """const MEDIUM_COLS = ['coaster', 'dark', 'boat', 'sim', 'wet', 'spinner', 'hr', 'pixar', 'starwars', 'marvel', 'film', 'multi', 'unique', 'classic', 'new', 'at_MK', 'at_DL', 'at_HS', 'at_DCA', 'at_DLP', 'at_TDL'];
const MEDIUM_ROWS = DATA.artists.filter(a => SONGS.filter(s => s.rows.has('a:' + a)).length >= 8).map(a => 'a:' + a).concat(['MK', 'EP', 'HS', 'AK', 'DL', 'DCA', 'DLP', 'TDL']);
let MODE = 'medium';
try { const m = localStorage.getItem('fl:mode'); if (m === 'hard' || m === 'medium') MODE = m; } catch (e) {}
const CLASH = [['y1','y2']""")
rep("  const r = rng(seed);", "  const r = rng(MODE + ':' + seed); const COLPOOL = MODE === 'medium' ? MEDIUM_COLS : Object.keys(COLS); const ROWPOOL = MODE === 'medium' ? MEDIUM_ROWS : ROWS; const MIN = MODE === 'medium' ? 2 : 1;")
rep("const cols = shuffle(Object.keys(COLS), r).slice(0, 3);", "const cols = shuffle(COLPOOL, r).slice(0, 3);")
rep("const rows = shuffle(ROWS, r).slice(0, 3);", "const rows = shuffle(ROWPOOL, r).slice(0, 3);")
rep("if (!n) ok = false;", "if (n < (c.startsWith('at_') ? 1 : MIN)) ok = false;")
rep("    if (rows.filter(x => !x.startsWith('a:')).length > 1) continue;", "    if (cols.some(c => c.startsWith('at_') && rows.includes(c.slice(3)))) continue;")
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
t = t.replace("'fl:", "'rg:")
t = t.replace('Band × song fact', 'Park × ride fact').replace('Type at least 2 letters of a song or band.', 'Type at least 2 letters of a ride name.').replace('That song isn’t on the playlist.', 'That ride isn’t in the list.').replace('Empty squares now show songs that would have worked.', 'Empty squares now show rides that would have worked.')
d = open('rides/data.json').read().replace('</', '<\\/')
open('ride-grid.html', 'w').write(t.replace('__DATA__', d)); print('ok')
