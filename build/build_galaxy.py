t = open('pop/template.html').read()
def rep(a, b, n=1):
    global t
    assert a in t, a[:70]; t = t.replace(a, b) if n == 0 else t.replace(a, b, n)
rep('<title>Hook Grid</title>', '<title>Galaxy Grid</title>')
rep('family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=DM+Sans', 'family=Exo+2:ital,wght@0,600;0,800;1,500&family=DM+Sans')
rep('like a chart sheet', 'like a starship display')
rep("""  --bg: #f3effa;
  --panel: #ffffff;
  --ink: #1d1530;
  --muted: #6a5f82;
  --line: #ddd4ec;
  --accent: #d6246e;
  --accent-2: #2f6fe0;""", """  color-scheme: dark;
  --bg: #07080d;
  --panel: #10131c;
  --ink: #eef0f6;
  --muted: #9aa1b4;
  --line: #262b3a;
  --accent: #ffe81f;
  --accent-2: #5aa9ff;""")
rep('--font-display: "Bricolage Grotesque", "Arial Black", system-ui, sans-serif;', '--font-display: "Exo 2", "Trebuchet MS", system-ui, sans-serif;')
rep("--bg: #130e20; --panel: #1f1833; --ink: #f2edfb; --muted: #a79cc2; --line: #342a4d;", "--bg: #07080d; --panel: #10131c; --ink: #eef0f6; --muted: #9aa1b4; --line: #262b3a;", 0)
rep("--accent: #ff4f96; --accent-2: #6aa0ff; --accent-ink: #1a0610;", "--accent: #ffe81f; --accent-2: #5aa9ff; --accent-ink: #141200;", 0)
rep('h1 { font-family: var(--font-display); font-weight: 800; font-size: clamp(30px, 9vw, 40px); line-height: .95; margin: 0; letter-spacing: -.03em;', 'h1 { font-family: var(--font-display); font-weight: 400; font-size: clamp(38px, 11.5vw, 54px); line-height: .95; margin: 0; letter-spacing: 0;')
rep('.left b { display: block; font-family: var(--font-display); font-weight: 800;', '.left b { display: block; font-family: var(--font-display); font-weight: 400;')
rep('.head { align-items: center; text-align: center; padding: 6px 3px; min-height: 66px; gap: 3px; font-family: var(--font-display); font-weight: 700; font-size: 13.5px; letter-spacing: -.01em; }', '.head { align-items: center; text-align: center; padding: 6px 3px; min-height: 66px; gap: 3px; font-family: var(--font-body); font-weight: 700; font-size: 12.5px; letter-spacing: -.005em; }')
rep('font-family: var(--font-display); font-weight: 800; font-size: clamp(12.5px, 3.6vw, 16px); letter-spacing: -.02em; }', 'font-family: var(--font-display); font-weight: 400; font-size: clamp(14px, 4.1vw, 19px); letter-spacing: 0; overflow-wrap: normal; }')
rep('.summary h2 { margin: 0; font-family: var(--font-display); font-weight: 800;', '.summary h2 { margin: 0; font-family: var(--font-display); font-weight: 400;')
rep('.prompt { font-family: var(--font-display); font-weight: 700;', '.prompt { font-family: var(--font-display); font-weight: 400;')
rep('.board { display: grid; grid-template-columns: minmax(0, .85fr) repeat(3, minmax(0, 1fr)); gap: 6px; }', '.board { display: grid; grid-template-columns: minmax(0, 1.1fr) repeat(3, minmax(0, 1fr)); gap: 6px; }')
rep('<h1>Hook <span>Grid</span></h1>', '<h1>Galaxy <span>Grid</span></h1>\n      <p class="tagline" style="margin:6px 0 0;font-style:italic;font-size:13.5px;color:var(--accent-2)">Episodes I–VI. Nothing after.</p>')
a = t.index('  <p class="rules">Tap a square'); b = t.index('</div>', a)
t = t[:a] + """  <p class="rules">Tap a square and name a <b>character</b> who fits both the <b>row on the left</b> and the <b>fact on top</b>. Rows and columns can be films, groups like the Jedi or the Rebel Alliance, or traits like wielding a lightsaber. You get 9 guesses, and each character can be used once.</p>
  <p class="rules">Only Episodes I to VI count, in their current versions with the Special Edition changes (so Jabba appears in A New Hope). Anakin and Darth Vader are one answer, and so are Palpatine and Darth Sidious. "Dies on screen" means within these six films. <b>Medium</b> uses the six films plus Jedi, Rebels and the Empire; <b>Hard</b> adds the Sith, the Republic, the Separatists and bounty hunters. The list covers about 90 characters compiled by hand, so a character who fits might be missing. This is a fan-made game and isn't affiliated with Lucasfilm or Disney. Your guesses are saved on this device.</p>
""" + t[b:]
s0 = t.index('const TYPE_ROWS = {'); s1 = t.index("const ROWS = ")
t = t[:s0] + """const TYPE_ROWS = { ep1: ['Episode I', 'The Phantom Menace'], ep2: ['Episode II', 'Attack of the Clones'], ep3: ['Episode III', 'Revenge of the Sith'], ep4: ['Episode IV', 'A New Hope'], ep5: ['Episode V', 'The Empire Strikes Back'], ep6: ['Episode VI', 'Return of the Jedi'], jedi: ['Jedi', 'Order members'], sith: ['Sith', 'Dark side lords'], rebel: ['Rebel Alliance', 'Members'], empire: ['Galactic Empire', 'Officers and rulers'], republic: ['Galactic Republic', 'Officials and troops'], separatist: ['Separatists', 'The Confederacy'], hunter: ['Bounty hunters', 'For hire'] };
const COLS = {
  saber: ['Wields a lightsaber', 'On screen'],
  dies: ['Dies on screen', 'Episodes I–VI'],
  pilot: ['Flies a ship', 'On screen'],
  droid: ['Droid', 'Machine'],
  alien: ['Non-human', 'Not a droid'],
  skywalker: ['Skywalker family', 'Blood or marriage'],
  tatooine: ['Lived on Tatooine', 'Desert planet'],
  limb: ['Loses a limb', 'Hand, arm or more'],
  both: ['In both trilogies', 'Prequels and originals'],
  in_ep1: ['Also in Episode I', 'The Phantom Menace'], in_ep2: ['Also in Episode II', 'Attack of the Clones'], in_ep3: ['Also in Episode III', 'Revenge of the Sith'],
  in_ep4: ['Also in Episode IV', 'A New Hope'], in_ep5: ['Also in Episode V', 'The Empire Strikes Back'], in_ep6: ['Also in Episode VI', 'Return of the Jedi'],
  in_jedi: ['Jedi', 'Order member'], in_sith: ['Sith', 'Dark side lord'], in_rebel: ['Rebel Alliance', 'Member'], in_empire: ['Galactic Empire', 'Serves the Emperor'],
  in_republic: ['Galactic Republic', 'Official or trooper'], in_separatist: ['Separatist', 'The Confederacy'], in_hunter: ['Bounty hunter', 'For hire']
};
const CLASH = [['y1','y2'],['droid','alien'],['droid','saber'],['droid','skywalker']];
""" + t[s1:]
rep("const rowLabel = r => r.startsWith('a:') ? [r.slice(2), 'Lead or featured'] : TYPE_ROWS[r];", "const rowLabel = r => r.startsWith('a:') ? [r.slice(2), ''] : TYPE_ROWS[r];")
rep("return { rows: ['a:Taylor Swift', 'a:Rihanna', 'a:Drake'], cols: ['t10', 'feat', 'late'] };", "return { rows: ['ep4', 'ep5', 'jedi'], cols: ['saber', 'dies', 'in_ep6'] };")
rep("corner.textContent = 'Artist × song fact';", "corner.textContent = 'Band × song fact';")
rep("Type at least 2 letters of a song title or artist.", "Type at least 2 letters of a song or band.")
rep("No song by that name in the list.", "That song isn’t on the playlist.")

rep("const CLASH = [['y1','y2']", """const MEDIUM_COLS = ['saber', 'dies', 'pilot', 'droid', 'alien', 'both', 'in_ep1', 'in_ep2', 'in_ep3', 'in_ep4', 'in_ep5', 'in_ep6', 'in_jedi', 'in_rebel', 'in_empire'];
const MEDIUM_ROWS = DATA.artists.filter(a => SONGS.filter(s => s.rows.has('a:' + a)).length >= 8).map(a => 'a:' + a).concat(['ep1', 'ep2', 'ep3', 'ep4', 'ep5', 'ep6', 'jedi', 'rebel', 'empire']);
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
t = t.replace("'fl:", "'gx:")
t = t.replace('Band × song fact', 'Film or group × fact').replace('Type at least 2 letters of a song or band.', 'Type at least 2 letters of a name.').replace('That song isn’t on the playlist.', 'That character isn’t in the list.').replace('Empty squares now show songs that would have worked.', 'Empty squares now show characters who would have worked.')
d = open('galaxy/data.json').read().replace('</', '<\\/')
open('galaxy-grid.html', 'w').write(t.replace('__DATA__', d)); print('ok')
