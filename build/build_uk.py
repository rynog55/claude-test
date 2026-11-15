t = open('pop/template.html').read()
def rep(a, b, n=1):
    global t
    assert a in t, a[:70]; t = t.replace(a, b) if n == 0 else t.replace(a, b, n)
rep('<title>Hook Grid</title>', '<title>Big Blue Grid</title>')
rep('family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=DM+Sans', 'family=Oswald:wght@500;600;700&family=DM+Sans')
rep('like a chart sheet', 'like a Rupp Arena scoreboard')
rep("""  --bg: #f3effa;
  --panel: #ffffff;
  --ink: #1d1530;
  --muted: #6a5f82;
  --line: #ddd4ec;
  --accent: #d6246e;
  --accent-2: #2f6fe0;""", """  --bg: #eef2f8;
  --panel: #ffffff;
  --ink: #0b1a33;
  --muted: #55627a;
  --line: #d3dbe8;
  --accent: #0033a0;
  --accent-2: #0033a0;""")
rep('--font-display: "Bricolage Grotesque", "Arial Black", system-ui, sans-serif;', '--font-display: "Oswald", "Arial Narrow", Impact, sans-serif;')
rep("--bg: #130e20; --panel: #1f1833; --ink: #f2edfb; --muted: #a79cc2; --line: #342a4d;", "--bg: #071226; --panel: #0e1d3a; --ink: #f1f5ff; --muted: #9fb0d0; --line: #22355e;", 0)
rep("--accent: #ff4f96; --accent-2: #6aa0ff; --accent-ink: #1a0610;", "--accent: #5b8cff; --accent-2: #8fb0ff; --accent-ink: #04112a;", 0)
rep('h1 { font-family: var(--font-display); font-weight: 800; font-size: clamp(30px, 9vw, 40px); line-height: .95; margin: 0; letter-spacing: -.03em;', 'h1 { font-family: var(--font-display); font-weight: 400; font-size: clamp(38px, 11.5vw, 54px); line-height: .95; margin: 0; letter-spacing: 0;')
rep('.left b { display: block; font-family: var(--font-display); font-weight: 800;', '.left b { display: block; font-family: var(--font-display); font-weight: 400;')
rep('.head { align-items: center; text-align: center; padding: 6px 3px; min-height: 66px; gap: 3px; font-family: var(--font-display); font-weight: 700; font-size: 13.5px; letter-spacing: -.01em; }', '.head { align-items: center; text-align: center; padding: 6px 3px; min-height: 66px; gap: 3px; font-family: var(--font-body); font-weight: 700; font-size: 12.5px; letter-spacing: -.005em; }')
rep('font-family: var(--font-display); font-weight: 800; font-size: clamp(12.5px, 3.6vw, 16px); letter-spacing: -.02em; }', 'font-family: var(--font-display); font-weight: 400; font-size: clamp(14px, 4.1vw, 19px); letter-spacing: 0; overflow-wrap: normal; }')
rep('.summary h2 { margin: 0; font-family: var(--font-display); font-weight: 800;', '.summary h2 { margin: 0; font-family: var(--font-display); font-weight: 400;')
rep('.prompt { font-family: var(--font-display); font-weight: 700;', '.prompt { font-family: var(--font-display); font-weight: 400;')
rep('.board { display: grid; grid-template-columns: minmax(0, .85fr) repeat(3, minmax(0, 1fr)); gap: 6px; }', '.board { display: grid; grid-template-columns: minmax(0, 1.1fr) repeat(3, minmax(0, 1fr)); gap: 6px; }')
rep('<h1>Hook <span>Grid</span></h1>', '<h1>Big Blue <span>Grid</span></h1>\n      <p class="tagline" style="margin:6px 0 0;font-style:italic;font-size:13.5px;color:var(--accent-2)">Kentucky Wildcats only. Go Cats.</p>')
a = t.index('  <p class="rules">Tap a square'); b = t.index('</div>', a)
t = t[:a] + """  <p class="rules">Tap a square and name a <b>player</b> who fits both the <b>row on the left</b> and the <b>fact on top</b>. Rows are Kentucky head coaches; a player counts for every coach he played for. Columns are titles, NBA draft results, honors and more. You get 9 guesses, and each player can be used once.</p>
  <p class="rules">Players are everyone on a Kentucky roster from 1930–31 (Adolph Rupp's first season) to 2025–26, from wildcatworld.com's season rosters. Draft results and NBA All-Star selections come from Wikipedia's NBA draft pages, and honored jerseys, all-time top 10s, Hall of Famers and Olympians from Wikipedia's Kentucky page. "One-and-done" means one season on the roster, then drafted that year. "Top 10 all-time" means a top-10 spot in points, rebounds, assists, steals or blocks. <b>Easy</b> uses Rupp, Hall, Pitino, Tubby Smith and Calipari; <b>Hard</b> adds Sutton, Gillispie and Pope plus deeper columns. This is a fan-made game and isn't affiliated with the University of Kentucky. Your guesses are saved on this device.</p>
""" + t[b:]
s0 = t.index('const TYPE_ROWS = {'); s1 = t.index("const ROWS = ")
t = t[:s0] + """const TYPE_ROWS = { rupp: ['Adolph Rupp', '1930–1972'], hall: ['Joe B. Hall', '1972–1985'], sutton: ['Eddie Sutton', '1985–1989'], pitino: ['Rick Pitino', '1989–1997'], smith: ['Tubby Smith', '1997–2007'], gillispie: ['Billy Gillispie', '2007–2009'], calipari: ['John Calipari', '2009–2024'], pope: ['Mark Pope', '2024–'] };
const COLS = {
  champ: ['National champion', 'On a title team'],
  mop: ['Final Four MOP', 'Most Outstanding Player'],
  drafted: ['Drafted into the NBA', 'Any round'],
  r1: ['First-round pick', 'NBA draft'],
  top14: ['Top-14 pick', 'NBA draft'],
  no1: ['No. 1 overall pick', 'NBA draft'],
  r2: ['Second-round pick', 'NBA draft'],
  allstar: ['NBA All-Star', 'At least once'],
  oneanddone: ['One-and-done', 'One season, then drafted'],
  fouryear: ['Four-year Wildcat', 'Four or more seasons'],
  kentuckian: ['From Kentucky', 'Hometown in the state'],
  tall: ['6′10″ or taller', 'Listed height'],
  honored: ['Jersey honored', 'In Rupp Arena'],
  top10: ['Top 10 all-time', 'Points, boards, assists, steals or blocks'],
  hof: ['Hall of Famer', 'Naismith Hall'],
  olympian: ['Olympian', 'Played in the Games'],
  twocoaches: ['Played for 2 coaches', 'At Kentucky'],
  in_rupp: ['Also played for Rupp', 'Two-coach careers'], in_hall: ['Also played for Hall', 'Two-coach careers'], in_sutton: ['Also played for Sutton', 'Two-coach careers'],
  in_pitino: ['Also played for Pitino', 'Two-coach careers'], in_smith: ['Also played for Tubby', 'Two-coach careers'], in_gillispie: ['Also played for Gillispie', 'Two-coach careers'],
  in_calipari: ['Also played for Calipari', 'Two-coach careers'], in_pope: ['Also played for Pope', 'Two-coach careers']
};
const CLASH = [['y1','y2'],['r1','r2'],['top14','r2'],['no1','r2'],['oneanddone','fouryear'],['oneanddone','twocoaches'],['drafted','r1'],['drafted','top14'],['drafted','no1'],['drafted','r2'],['r1','top14'],['r1','no1'],['top14','no1']];
""" + t[s1:]
rep("const rowLabel = r => r.startsWith('a:') ? [r.slice(2), 'Lead or featured'] : TYPE_ROWS[r];", "const rowLabel = r => r.startsWith('a:') ? [r.slice(2), ''] : TYPE_ROWS[r];")
rep("return { rows: ['a:Taylor Swift', 'a:Rihanna', 'a:Drake'], cols: ['t10', 'feat', 'late'] };", "return { rows: ['rupp', 'pitino', 'calipari'], cols: ['champ', 'kentuckian', 'drafted'] };")
rep("corner.textContent = 'Artist × song fact';", "corner.textContent = 'Band × song fact';")
rep("Type at least 2 letters of a song title or artist.", "Type at least 2 letters of a song or band.")
rep("No song by that name in the list.", "That song isn’t on the playlist.")

rep("const CLASH = [['y1','y2']", """const MEDIUM_COLS = ['champ', 'drafted', 'r1', 'top14', 'allstar', 'oneanddone', 'fouryear', 'kentuckian', 'tall', 'honored', 'top10'];
const MEDIUM_ROWS = DATA.artists.filter(a => SONGS.filter(s => s.rows.has('a:' + a)).length >= 8).map(a => 'a:' + a).concat(['rupp', 'hall', 'pitino', 'smith', 'calipari']);
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
    <button type="button" class="mode" id="mode-medium" data-mode="medium">Easy</button>
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
rep("""Your guesses are saved on this device.</p>""", """<b>Easy</b> sticks to the bigger bands and well-known facts, and every square has at least 2 right answers. <b>Hard</b> adds every band, more band types, and Spotify's mood, key, energy and popularity ratings. Your guesses are saved on this device.</p>""")

t = t.replace("'hk:", "'fl:")
t = t.replace("'fl:' + seed", "'fl:' + MODE + ':' + seed")
t = t.replace("'fl:", "'bb:")
t = t.replace('Band × song fact', 'Coach × fact').replace('Type at least 2 letters of a song or band.', 'Type at least 2 letters of a player’s name.').replace('That song isn’t on the playlist.', 'That player isn’t on a Kentucky roster in this list.').replace('Empty squares now show songs that would have worked.', 'Empty squares now show players who would have worked.')
d = open('uk/data.json').read().replace('</', '<\\/')
open('bigblue-grid.html', 'w').write(t.replace('__DATA__', d)); print('ok')
