p = open('build_lith.py').read()
def sub(a, b):
    global p
    assert a in p, a[:80]; p = p.replace(a, b)
sub("'<title>Flannel Grid</title>'", "'<title>First Wave Grid</title>'")
sub("'family=Special+Elite&family=DM+Sans'", "'family=Bebas+Neue&family=DM+Sans'")
sub("'like a photocopied zine page'", "'like a neon club flyer'")
sub('''  --bg: #e7e6e2;
  --panel: #f8f7f4;
  --ink: #1a1916;
  --muted: #625e56;
  --line: #d0cdc5;
  --accent: #b02a20;
  --accent-2: #2d6a4c;''', '''  --bg: #f0eef6;
  --panel: #ffffff;
  --ink: #1a1630;
  --muted: #625c80;
  --line: #d9d4ea;
  --accent: #c8136a;
  --accent-2: #087f90;''')
sub("""'--font-display: "Special Elite", "Courier New", monospace;'""", """'--font-display: "Bebas Neue", "Arial Narrow", Impact, sans-serif;'""")
sub('"--bg: #131310; --panel: #1e1d19; --ink: #efece4; --muted: #a39e92; --line: #363329;"', '"--bg: #110d22; --panel: #1b1633; --ink: #f3efff; --muted: #a59fc4; --line: #2f2a4f;"')
sub('"--accent: #e8604f; --accent-2: #6fc39a; --accent-ink: #1c0805;"', '"--accent: #ff4fa3; --accent-2: #33d6e6; --accent-ink: #1e0414;"')
sub("font-size: clamp(30px, 9vw, 42px); line-height: 1; margin: 0; letter-spacing: -.01em;", "font-size: clamp(34px, 10vw, 52px); line-height: .9; margin: 0; letter-spacing: .02em;")
sub("font-size: clamp(11px, 3.2vw, 15px); letter-spacing: -.035em; overflow-wrap: normal; }'", "font-size: clamp(15px, 4.4vw, 20px); letter-spacing: .02em; overflow-wrap: normal; }'")
sub("'<h1>Flannel <span>Grid</span></h1>'", "'<h1>First Wave <span>Grid</span></h1>'")
a = p.index('t = t[:a] + """  <p class="rules">'); b = p.index('""" + t[b:]', a)
p = p[:a] + '''t = t[:a] + """  <p class="rules">Tap a square and name a song from <b>your new wave playlist</b> that fits the <b>band on the left</b> and the <b>fact on top</b>. You get 9 guesses, and each song can be used once.</p>
  <p class="rules">The answer list is the songs on your Spotify playlist of classic new wave, synth-pop and post-punk heard on satellite radio. This game isn't affiliated with SiriusXM. Length, popularity, danceability, mood, key and genre come from Spotify's data. Popularity was measured when you exported the playlist: "Deep cut" is the least-played quarter and "Spotify smash" the most-played quarter. US top 10 and UK No. 1 hits come from Wikipedia's chart pages. Years use the song's original release, and band facts were tagged by hand. Your guesses are saved on this device.</p>
''' + p[b:]
a = p.index('const TYPE_ROWS = {\n  seattle'); b = p.index("const CLASH = [['y1','y2']", a); e = p.index('\n', b)
p = p[:a] + """const TYPE_ROWS = {
  uk: ['British act', 'England, Scotland, Wales'],
  us: ['American act', 'Formed in the US'],
  world: ['Not UK or US', 'Ireland, Australia, Europe, Canada'],
  female: ['Female lead singer', 'Or a female co-lead'],
  duo: ['A duo', 'Two-person act'],
  solo: ['Solo artist', 'Not a band'],
  liveaid: ['Played Live Aid', 'July 13, 1985'],
  died: ['Lead singer has died', 'Frontman or frontwoman'],
  onesong: ['Only one song here', 'Just one on the playlist']
};
const COLS = {
  us10: ['US top 10 hit', 'Billboard Hot 100'],
  uk1: ['UK No. 1', 'UK singles chart'],
  synth: ['Synth-pop act', 'Spotify genre tag'],
  dark_genre: ['Post-punk or goth act', 'Spotify genre tag'],
  minor: ['In a minor key', 'Spotify key analysis'],
  dark: ['Dark mood', 'Spotify mood rating'],
  upbeat: ['Upbeat mood', 'Spotify mood rating'],
  dance: ['Dance-floor ready', 'Top danceability'],
  long: ['5 minutes or longer', 'Track length'],
  short: ['Under 3:20', 'Track length'],
  deep: ['Deep cut', 'Least-played quarter on Spotify'],
  smash: ['Spotify smash', 'Most-played quarter'],
  y1: ['Released by 1981', 'Original release'],
  y2: ['Released 1982–84', 'Original release'],
  y3: ['Released 1985 or later', 'Original release'],
  oneword: ['One-word title', 'Ignoring parentheses']
};
const CLASH = [['y1','y2'],['y1','y3'],['y2','y3'],['dark','upbeat'],['long','short'],['deep','smash'],['us10','deep']];""" + p[e:]
sub("const MEDIUM_COLS = ['altno1', 'smash', 'long', 'short', 'y1', 'y2', 'y3', 'oneword'];", "const MEDIUM_COLS = ['us10', 'smash', 'synth', 'long', 'y1', 'y2', 'y3', 'oneword'];")
sub(".length >= 8).map(a => 'a:' + a).concat(['seattle', 'female', 'california', 'abroad', 'lostsinger']);", ".length >= 5).map(a => 'a:' + a).concat(['uk', 'us', 'world', 'female', 'solo', 'duo', 'liveaid']);")
sub("(MODE === 'medium' ? 2 : 1)) continue;", "(MODE === 'medium' ? 3 : 1)) continue;")
sub("\"return { rows: ['a:Nirvana', 'a:Pearl Jam', 'seattle'], cols: ['altno1', 'minor', 'y1'] };\"", "\"return { rows: ['uk', 'us', 'female'], cols: ['us10', 'smash', 'y2'] };\"")
sub("rep(\"cols: ['altno1', 'minor', 'y1'] };\", \"cols: ['altno1', 'long', 'y1'] };\")\n", "")
sub("open('lith/data.json')", "open('wave/data.json')")
sub("open('flannel-grid.html', 'w')", "open('wave-grid.html', 'w')")
sub("d = open(", "t = t.replace(\"'fl:\", \"'nw:\")\nd = open(")
open('build_wave.py', 'w').write(p); print('ok')
