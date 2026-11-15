"""Derive build_wiz.py (Wizard Grid page builder) from the Flannel Grid builder by targeted replacements."""
p = open('build_lith.py').read()
def sub(a, b):
    global p
    assert a in p, a[:90]; p = p.replace(a, b)
sub("'<title>Flannel Grid</title>'", "'<title>Wizard Grid</title>'")
sub("'family=Special+Elite&family=DM+Sans'", "'family=IM+Fell+English:ital@0;1&family=DM+Sans'")
sub("'like a photocopied zine page'", "'like a page of a spellbook'")
sub('''  --bg: #e7e6e2;
  --panel: #f8f7f4;
  --ink: #1a1916;
  --muted: #625e56;
  --line: #d0cdc5;
  --accent: #b02a20;
  --accent-2: #2d6a4c;''', '''  --bg: #ecebef;
  --panel: #ffffff;
  --ink: #1b1622;
  --muted: #625a6c;
  --line: #d8d3de;
  --accent: #8c1d2b;
  --accent-2: #8a6416;''')
sub("""'--font-display: "Special Elite", "Courier New", monospace;'""", """'--font-display: "IM Fell English", Georgia, "Times New Roman", serif;'""")
sub('"--bg: #131310; --panel: #1e1d19; --ink: #efece4; --muted: #a39e92; --line: #363329;"', '"--bg: #15121a; --panel: #201b27; --ink: #f2ecf6; --muted: #a89eb3; --line: #3a3244;"')
sub('"--accent: #e8604f; --accent-2: #6fc39a; --accent-ink: #1c0805;"', '"--accent: #e0687a; --accent-2: #e2b75a; --accent-ink: #1e0408;"')
sub("font-size: clamp(30px, 9vw, 42px); line-height: 1; margin: 0; letter-spacing: -.01em;", "font-size: clamp(38px, 11.5vw, 54px); line-height: .95; margin: 0; letter-spacing: 0;")
sub("font-size: clamp(11px, 3.2vw, 15px); letter-spacing: -.035em; overflow-wrap: normal; }'", "font-size: clamp(14px, 4.1vw, 19px); letter-spacing: 0; overflow-wrap: normal; }'")
sub("'<h1>Flannel <span>Grid</span></h1>'", "'<h1>Wizard <span>Grid</span></h1>\\n      <p class=\"tagline\" style=\"margin:6px 0 0;font-style:italic;font-size:13.5px;color:var(--accent-2)\">Harry Potter trivia from the seven books</p>'")
a = p.index('t = t[:a] + """  <p class="rules">'); b = p.index('""" + t[b:]', a)
p = p[:a] + '''t = t[:a] + """  <p class="rules">Tap a square and name a <b>character</b> who fits both the <b>row on the left</b> and the <b>fact on top</b>. Rows and columns can be houses, groups like the Order of the Phoenix or Dumbledore's Army, or traits like Animagus or Quidditch Seeker. You get 9 guesses, and each character can be used once.</p>
  <p class="rules"><b>Easy</b> uses the four houses, the Order, Dumbledore's Army, the Weasleys and Hogwarts staff. <b>Hard</b> adds Death Eaters and the Ministry, plus more traits. Facts come from the seven books, not the films or later stories, and a fact only counts when the books state it, so a character whose house or blood status is never given doesn't count for those squares. "Dies in the books" means during the story, so James and Lily Potter don't count. The list covers about 130 characters compiled by hand, so a character who fits might be missing. This is a fan-made game and isn't affiliated with J.K. Rowling or Warner Bros. Your guesses are saved on this device.</p>
''' + p[b:]
a = p.index('const TYPE_ROWS = {\n  seattle'); b = p.index("const CLASH = [['y1','y2']", a); e = p.index('\n', b)
p = p[:a] + """const TYPE_ROWS = { G: ['Gryffindor', 'House'], S: ['Slytherin', 'House'], R: ['Ravenclaw', 'House'], H: ['Hufflepuff', 'House'], order: ['Order of the Phoenix', 'Members'], da: ["Dumbledore's Army", 'Members'], de: ['Death Eaters', 'Followers of Voldemort'], weasley: ['Weasley family', 'By birth or marriage'], staff: ['Hogwarts staff', 'Teachers and more'], ministry: ['Ministry of Magic', 'Employees'] };
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
const CLASH = [['y1','y2'],['pure','half'],['pure','muggleborn'],['half','muggleborn'],['in_G','in_S'],['in_G','in_R'],['in_G','in_H'],['in_S','in_R'],['in_S','in_H'],['in_R','in_H']];""" + p[e:]
sub("const MEDIUM_COLS = ['altno1', 'smash', 'long', 'short', 'y1', 'y2', 'y3', 'oneword'];",
    "const MEDIUM_COLS = ['died', 'quidditch', 'seeker', 'prefect', 'animagus', 'pure', 'muggleborn', 'in_order', 'in_da', 'in_de', 'in_staff', 'in_ministry', 'in_weasley', 'in_G', 'in_S'];")
sub(".length >= 8).map(a => 'a:' + a).concat(['seattle', 'female', 'california', 'abroad', 'lostsinger']);",
    ".length >= 8).map(a => 'a:' + a).concat(['G', 'S', 'R', 'H', 'order', 'da', 'weasley', 'staff']);")
sub("\"    if (rows.filter(x => !x.startsWith('a:')).length > (MODE === 'medium' ? 2 : 1)) continue;\"",
    "\"    if (cols.some(c => c.startsWith('in_') && rows.includes(c.slice(3)))) continue;\"")
sub("\"return { rows: ['a:Nirvana', 'a:Pearl Jam', 'seattle'], cols: ['altno1', 'minor', 'y1'] };\"",
    "\"return { rows: ['G', 'S', 'order'], cols: ['died', 'pure', 'in_staff'] };\"")
sub("rep(\"cols: ['altno1', 'minor', 'y1'] };\", \"cols: ['altno1', 'long', 'y1'] };\")\n", "")
sub('"if (!n) ok = false;", "if (n < MIN) ok = false;"', '"if (!n) ok = false;", "if (n < (c.startsWith(\'in_\') ? 1 : MIN)) ok = false;"')
sub("open('lith/data.json')", "open('wizards/data.json')")
sub("open('flannel-grid.html', 'w')", "open('wizard-grid.html', 'w')")
sub("d = open(", "t = t.replace(\"'fl:\", \"'wz:\")\nt = t.replace('Band × song fact', 'Group × fact').replace('Type at least 2 letters of a song or band.', 'Type at least 2 letters of a name.').replace('That song isn’t on the playlist.', 'That character isn’t in the list.').replace('Empty squares now show songs that would have worked.', 'Empty squares now show characters who would have worked.')\nd = open(")
open('build_wiz.py', 'w').write(p); print('ok')
