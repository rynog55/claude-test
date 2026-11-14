"""Derive build_ride.py (Ride Grid page builder) from the Flannel Grid builder by targeted replacements."""
p = open('build_lith.py').read()
def sub(a, b):
    global p
    assert a in p, a[:90]; p = p.replace(a, b)
sub("'<title>Flannel Grid</title>'", "'<title>Ride Grid</title>'")
sub("'family=Special+Elite&family=DM+Sans'", "'family=Fredoka:wght@500;600;700&family=DM+Sans'")
sub("'like a photocopied zine page'", "'like a park guide map'")
sub('''  --bg: #e7e6e2;
  --panel: #f8f7f4;
  --ink: #1a1916;
  --muted: #625e56;
  --line: #d0cdc5;
  --accent: #b02a20;
  --accent-2: #2d6a4c;''', '''  --bg: #ecf2f4;
  --panel: #ffffff;
  --ink: #132630;
  --muted: #566b75;
  --line: #d3dee3;
  --accent: #d2452f;
  --accent-2: #1f7489;''')
sub("""'--font-display: "Special Elite", "Courier New", monospace;'""", """'--font-display: "Fredoka", "Trebuchet MS", system-ui, sans-serif;'""")
sub('"--bg: #131310; --panel: #1e1d19; --ink: #efece4; --muted: #a39e92; --line: #363329;"', '"--bg: #0c1820; --panel: #15242e; --ink: #eef5f8; --muted: #9db2bc; --line: #29404c;"')
sub('"--accent: #e8604f; --accent-2: #6fc39a; --accent-ink: #1c0805;"', '"--accent: #ff7a5c; --accent-2: #5cc9e0; --accent-ink: #1d0802;"')
sub("font-size: clamp(30px, 9vw, 42px); line-height: 1; margin: 0; letter-spacing: -.01em;", "font-size: clamp(36px, 11vw, 50px); line-height: .95; margin: 0; letter-spacing: -.01em;")
sub("font-size: clamp(11px, 3.2vw, 15px); letter-spacing: -.035em; overflow-wrap: normal; }'", "font-size: clamp(13px, 3.8vw, 17px); letter-spacing: 0; overflow-wrap: normal; }'")
sub("'<h1>Flannel <span>Grid</span></h1>'", "'<h1>Ride <span>Grid</span></h1>'")
sub("""rep('<p class="sub" id="label">Daily grid</p>""", """rep('<p class="sub" id="label">Daily grid</p>""") if False else None
a = p.index('t = t[:a] + """  <p class="rules">'); b = p.index('""" + t[b:]', a)
p = p[:a] + '''t = t[:a] + """  <p class="rules">Disney parks trivia. Tap a square and name an <b>attraction</b> at the <b>park on the left</b> that fits the <b>fact on top</b>. Rides that exist at several parks count as one answer, so Space Mountain works for any park that has a version of it. You get 9 guesses, and each ride can be used once.</p>
  <p class="rules"><b>Medium</b> uses the six US parks plus Disneyland Paris and Tokyo Disneyland, with the most familiar ride types. <b>Hard</b> adds Disney Adventure World, Tokyo DisneySea, Hong Kong and Shanghai, plus crossovers with every park and finer categories like Omnimover and trackless rides. The list covers about 110 rides operating in 2026; shows, walk-throughs and rides closed for long rebuilds are left out. Ride facts were compiled by hand, so a ride that fits might be missing. This is a fan-made game and isn't affiliated with Disney. Your guesses are saved on this device.</p>
''' + p[b:]
a = p.index('const TYPE_ROWS = {\n  seattle'); b = p.index("const CLASH = [['y1','y2']", a); e = p.index('\n', b)
p = p[:a] + """const PARK_NAMES = { MK: ['Magic Kingdom', 'Walt Disney World'], EP: ['EPCOT', 'Walt Disney World'], HS: ['Hollywood Studios', 'Walt Disney World'], AK: ['Animal Kingdom', 'Walt Disney World'], DL: ['Disneyland', 'California'], DCA: ['California Adventure', 'California'], DLP: ['Disneyland Paris', 'Disneyland Park'], DAW: ['Adventure World', 'Paris, formerly Studios'], TDL: ['Tokyo Disneyland', 'Tokyo'], TDS: ['Tokyo DisneySea', 'Tokyo'], HK: ['Hong Kong Disneyland', 'Hong Kong'], SH: ['Shanghai Disneyland', 'Shanghai'] };
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
const CLASH = [['y1','y2'],['multi','unique'],['classic','new'],['unique','at_MK'],['unique','at_EP'],['unique','at_HS'],['unique','at_DL'],['unique','at_DCA'],['unique','at_DLP'],['unique','at_DAW'],['unique','at_TDL'],['unique','at_TDS'],['unique','at_HK'],['unique','at_SH'],['coaster','launch'],['coaster','indoor']];""" + p[e:]
sub("const MEDIUM_COLS = ['altno1', 'smash', 'long', 'short', 'y1', 'y2', 'y3', 'oneword'];",
    "const MEDIUM_COLS = ['coaster', 'dark', 'boat', 'sim', 'wet', 'spinner', 'hr', 'pixar', 'starwars', 'marvel', 'film', 'multi', 'unique', 'classic', 'new', 'at_MK', 'at_DL', 'at_HS', 'at_DCA', 'at_DLP', 'at_TDL'];")
sub(".length >= 8).map(a => 'a:' + a).concat(['seattle', 'female', 'california', 'abroad', 'lostsinger']);",
    ".length >= 8).map(a => 'a:' + a).concat(['MK', 'EP', 'HS', 'AK', 'DL', 'DCA', 'DLP', 'TDL']);")
sub("\"    if (rows.filter(x => !x.startsWith('a:')).length > (MODE === 'medium' ? 2 : 1)) continue;\"",
    "\"    if (cols.some(c => c.startsWith('at_') && rows.includes(c.slice(3)))) continue;\"")
sub("\"return { rows: ['a:Nirvana', 'a:Pearl Jam', 'seattle'], cols: ['altno1', 'minor', 'y1'] };\"",
    "\"return { rows: ['MK', 'DL', 'HS'], cols: ['dark', 'hr', 'multi'] };\"")
sub("rep(\"cols: ['altno1', 'minor', 'y1'] };\", \"cols: ['altno1', 'long', 'y1'] };\")\n", "")
sub('"if (!n) ok = false;", "if (n < MIN) ok = false;"', '"if (!n) ok = false;", "if (n < (c.startsWith(\'at_\') ? 1 : MIN)) ok = false;"')
sub("open('lith/data.json')", "open('rides/data.json')")
sub("open('flannel-grid.html', 'w')", "open('ride-grid.html', 'w')")
sub("d = open(", "t = t.replace(\"'fl:\", \"'rg:\")\nt = t.replace('Band × song fact', 'Park × ride fact').replace('Type at least 2 letters of a song or band.', 'Type at least 2 letters of a ride name.').replace('That song isn’t on the playlist.', 'That ride isn’t in the list.').replace('Empty squares now show songs that would have worked.', 'Empty squares now show rides that would have worked.')\nd = open(")
open('build_ride.py', 'w').write(p); print('ok')
