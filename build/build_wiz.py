t = open('pop/template.html').read()
def rep(a, b, n=1):
    global t
    assert a in t, a[:70]; t = t.replace(a, b) if n == 0 else t.replace(a, b, n)
rep('<title>Hook Grid</title>', '<title>Wizard Grid</title>')
rep('family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=DM+Sans', 'family=IM+Fell+English:ital@0;1&family=DM+Sans')
rep('like a chart sheet', 'like a page of a spellbook')
rep("""  --bg: #f3effa;
  --panel: #ffffff;
  --ink: #1d1530;
  --muted: #6a5f82;
  --line: #ddd4ec;
  --accent: #d6246e;
  --accent-2: #2f6fe0;""", """  --bg: #ecebef;
  --panel: #ffffff;
  --ink: #1b1622;
  --muted: #625a6c;
  --line: #d8d3de;
  --accent: #8c1d2b;
  --accent-2: #8a6416;""")
rep('--font-display: "Bricolage Grotesque", "Arial Black", system-ui, sans-serif;', '--font-display: "IM Fell English", Georgia, "Times New Roman", serif;')
rep("--bg: #130e20; --panel: #1f1833; --ink: #f2edfb; --muted: #a79cc2; --line: #342a4d;", "--bg: #15121a; --panel: #201b27; --ink: #f2ecf6; --muted: #a89eb3; --line: #3a3244;", 0)
rep("--accent: #ff4f96; --accent-2: #6aa0ff; --accent-ink: #1a0610;", "--accent: #e0687a; --accent-2: #e2b75a; --accent-ink: #1e0408;", 0)
rep('h1 { font-family: var(--font-display); font-weight: 800; font-size: clamp(30px, 9vw, 40px); line-height: .95; margin: 0; letter-spacing: -.03em;', 'h1 { font-family: var(--font-display); font-weight: 400; font-size: clamp(38px, 11.5vw, 54px); line-height: .95; margin: 0; letter-spacing: 0;')
rep('.left b { display: block; font-family: var(--font-display); font-weight: 800;', '.left b { display: block; font-family: var(--font-display); font-weight: 400;')
rep('.head { align-items: center; text-align: center; padding: 6px 3px; min-height: 66px; gap: 3px; font-family: var(--font-display); font-weight: 700; font-size: 13.5px; letter-spacing: -.01em; }', '.head { align-items: center; text-align: center; padding: 6px 3px; min-height: 66px; gap: 3px; font-family: var(--font-body); font-weight: 700; font-size: 12.5px; letter-spacing: -.005em; }')
rep('font-family: var(--font-display); font-weight: 800; font-size: clamp(12.5px, 3.6vw, 16px); letter-spacing: -.02em; }', 'font-family: var(--font-display); font-weight: 400; font-size: clamp(14px, 4.1vw, 19px); letter-spacing: 0; overflow-wrap: normal; }')
rep('.summary h2 { margin: 0; font-family: var(--font-display); font-weight: 800;', '.summary h2 { margin: 0; font-family: var(--font-display); font-weight: 400;')
rep('.prompt { font-family: var(--font-display); font-weight: 700;', '.prompt { font-family: var(--font-display); font-weight: 400;')
rep('.board { display: grid; grid-template-columns: minmax(0, .85fr) repeat(3, minmax(0, 1fr)); gap: 6px; }', '.board { display: grid; grid-template-columns: minmax(0, 1.1fr) repeat(3, minmax(0, 1fr)); gap: 6px; }')
rep('<h1>Hook <span>Grid</span></h1>', '<h1>Wizard <span>Grid</span></h1>\n      <p class="tagline" style="margin:6px 0 0;font-style:italic;font-size:13.5px;color:var(--accent-2)">Harry Potter trivia from the seven books</p>')
a = t.index('  <p class="rules">Tap a square'); b = t.index('</div>', a)
t = t[:a] + """  <p class="rules">Tap a square and name a <b>character</b> who fits both the <b>row on the left</b> and the <b>fact on top</b>. Rows and columns can be houses, groups like the Order of the Phoenix or Dumbledore's Army, or traits like Animagus or Quidditch Seeker. You get 9 guesses, and each character can be used once.</p>
  <p class="rules"><b>Medium</b> uses the four houses, the Order, Dumbledore's Army, the Weasleys and Hogwarts staff. <b>Hard</b> adds Death Eaters and the Ministry, plus more traits. Facts come from the seven books, not the films or later stories, and a fact only counts when the books state it, so a character whose house or blood status is never given doesn't count for those squares. "Dies in the books" means during the story, so James and Lily Potter don't count. The list covers about 130 characters compiled by hand, so a character who fits might be missing. This is a fan-made game and isn't affiliated with J.K. Rowling or Warner Bros. Your guesses are saved on this device.</p>
""" + t[b:]
s0 = t.index('const TYPE_ROWS = {'); s1 = t.index("const ROWS = ")
t = t[:s0] + """const TYPE_ROWS = { G: ['Gryffindor', 'House'], S: ['Slytherin', 'House'], R: ['Ravenclaw', 'House'], H: ['Hufflepuff', 'House'], order: ['Order of the Phoenix', 'Members'], da: ["Dumbledore's Army", 'Members'], de: ['Death Eaters', 'Followers of Voldemort'], weasley: ['Weasley family', 'By birth or marriage'], staff: ['Hogwarts staff', 'Teachers and more'], ministry: ['Ministry of Magic', 'Employees'] };
const COLS = {
  died: ['Dies in the books', 'During the story'],
  quidditch: ['Played Quidditch', 'School or pro'],
  seeker: ['Played Seeker', 'Chased the Snitch'],
  captain: ['Quidditch captain', 'School team'],
  prefect: ['Prefect', 'Or Head Boy or Girl'],
  animagus: ['Animagus', 'Registered or not'],
  ghost: ['Ghost', 'Haunts Hogwarts'],
  triwizard: ['Triwizard champion', '1994 tournament'],
  parselmouth: ['Parselmouth', 'Speaks to snakes'],
  pure: ['Pure-blood', 'As the books state'],
  half: ['Half-blood', 'As the books state'],
  muggleborn: ['Muggle-born', 'As the books state'],
  in_G: ['Gryffindor', 'House'], in_S: ['Slytherin', 'House'], in_R: ['Ravenclaw', 'House'], in_H: ['Hufflepuff', 'House'],
  in_order: ['Order of the Phoenix', 'Member'], in_da: ["Dumbledore's Army", 'Member'], in_de: ['Death Eater', 'Follower of Voldemort'],
  in_weasley: ['Weasley', 'By birth or marriage'], in_staff: ['Hogwarts staff', 'Any time in the books'], in_ministry: ['Ministry of Magic', 'Worked there']
};
const CLASH = [['y1','y2'],['pure','half'],['pure','muggleborn'],['half','muggleborn'],['in_G','in_S'],['in_G','in_R'],['in_G','in_H'],['in_S','in_R'],['in_S','in_H'],['in_R','in_H']];
""" + t[s1:]
rep("const rowLabel = r => r.startsWith('a:') ? [r.slice(2), 'Lead or featured'] : TYPE_ROWS[r];", "const rowLabel = r => r.startsWith('a:') ? [r.slice(2), ''] : TYPE_ROWS[r];")
rep("return { rows: ['a:Taylor Swift', 'a:Rihanna', 'a:Drake'], cols: ['t10', 'feat', 'late'] };", "return { rows: ['G', 'S', 'order'], cols: ['died', 'pure', 'in_staff'] };")
rep("corner.textContent = 'Artist × song fact';", "corner.textContent = 'Band × song fact';")
rep("Type at least 2 letters of a song title or artist.", "Type at least 2 letters of a song or band.")
rep("No song by that name in the list.", "That song isn’t on the playlist.")

rep("const CLASH = [['y1','y2']", """const MEDIUM_COLS = ['died', 'quidditch', 'seeker', 'prefect', 'animagus', 'pure', 'muggleborn', 'in_order', 'in_da', 'in_de', 'in_staff', 'in_ministry', 'in_weasley', 'in_G', 'in_S'];
const MEDIUM_ROWS = DATA.artists.filter(a => SONGS.filter(s => s.rows.has('a:' + a)).length >= 8).map(a => 'a:' + a).concat(['G', 'S', 'R', 'H', 'order', 'da', 'weasley', 'staff']);
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
t = t.replace("'fl:", "'wz:")
t = t.replace('Band × song fact', 'Group × fact').replace('Type at least 2 letters of a song or band.', 'Type at least 2 letters of a name.').replace('That song isn’t on the playlist.', 'That character isn’t in the list.').replace('Empty squares now show songs that would have worked.', 'Empty squares now show characters who would have worked.')
d = open('wizards/data.json').read().replace('</', '<\\/')
open('wizard-grid.html', 'w').write(t.replace('__DATA__', d)); print('ok')
