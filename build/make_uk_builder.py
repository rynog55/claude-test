"""Write build_uk.py (Big Blue Grid page builder): a copy of make_wiz_builder.py with Kentucky content swapped in."""
p = open('make_wiz_builder.py').read()
def sub(a, b):
    global p
    assert a in p, a[:90]; p = p.replace(a, b)
sub("build_wiz.py (Wizard Grid page builder)", "build_uk.py (Big Blue Grid page builder)")
sub("'<title>Wizard Grid</title>'", "'<title>Big Blue Grid</title>'")
sub("'family=IM+Fell+English:ital@0;1&family=DM+Sans'", "'family=Oswald:wght@500;600;700&family=DM+Sans'")
sub("'like a page of a spellbook'", "'like a Rupp Arena scoreboard'")
sub("""  --bg: #ecebef;
  --panel: #ffffff;
  --ink: #1b1622;
  --muted: #625a6c;
  --line: #d8d3de;
  --accent: #8c1d2b;
  --accent-2: #8a6416;""", """  --bg: #eef2f8;
  --panel: #ffffff;
  --ink: #0b1a33;
  --muted: #55627a;
  --line: #d3dbe8;
  --accent: #0033a0;
  --accent-2: #0033a0;""")
sub('"IM Fell English", Georgia, "Times New Roman", serif;', '"Oswald", "Arial Narrow", Impact, sans-serif;')
sub('--bg: #15121a; --panel: #201b27; --ink: #f2ecf6; --muted: #a89eb3; --line: #3a3244;', '--bg: #071226; --panel: #0e1d3a; --ink: #f1f5ff; --muted: #9fb0d0; --line: #22355e;')
sub('--accent: #e0687a; --accent-2: #e2b75a; --accent-ink: #1e0408;', '--accent: #5b8cff; --accent-2: #8fb0ff; --accent-ink: #04112a;')
sub('Harry Potter trivia from the seven books</p>', 'Kentucky Wildcats only. Go Cats.</p>')
sub("<h1>Wizard <span>Grid</span></h1>", "<h1>Big Blue <span>Grid</span></h1>")
sub("Rows and columns can be houses, groups like the Order of the Phoenix or Dumbledore's Army, or traits like Animagus or Quidditch Seeker.",
    "Rows are Kentucky head coaches; a player counts for every coach he played for. Columns are titles, NBA draft results, honors and more.")
i = p.index("<b>Medium</b> uses the four houses"); j = p.index("Your guesses are saved on this device.</p>", i)
p = p[:i] + ("Players are everyone on a Kentucky roster from 1930–31 (Adolph Rupp's first season) to 2025–26, from wildcatworld.com's season rosters. "
             "Draft results and NBA All-Star selections come from Wikipedia's NBA draft pages, and honored jerseys, all-time top 10s, Hall of Famers and Olympians "
             "from Wikipedia's Kentucky page. \"One-and-done\" means one season on the roster, then drafted that year. \"Top 10 all-time\" means a top-10 spot in "
             "points, rebounds, assists, steals or blocks. <b>Medium</b> uses Rupp, Hall, Pitino, Tubby Smith and Calipari; <b>Hard</b> adds Sutton, Gillispie "
             "and Pope plus deeper columns. This is a fan-made game and isn't affiliated with the University of Kentucky. ") + p[j:]
i = p.index("const TYPE_ROWS = { G:"); j = p.index("const CLASH = [['y1','y2'],['pure','half']", i)
k = p.index("['in_R','in_H']];", j) + len("['in_R','in_H']];")
p = p[:i] + """const TYPE_ROWS = { rupp: ['Adolph Rupp', '1930–1972'], hall: ['Joe B. Hall', '1972–1985'], sutton: ['Eddie Sutton', '1985–1989'], pitino: ['Rick Pitino', '1989–1997'], smith: ['Tubby Smith', '1997–2007'], gillispie: ['Billy Gillispie', '2007–2009'], calipari: ['John Calipari', '2009–2024'], pope: ['Mark Pope', '2024–'] };
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
const CLASH = [['y1','y2'],['r1','r2'],['top14','r2'],['no1','r2'],['oneanddone','fouryear'],['oneanddone','twocoaches'],['drafted','r1'],['drafted','top14'],['drafted','no1'],['drafted','r2'],['r1','top14'],['r1','no1'],['top14','no1']];""" + p[k:]
sub("'died', 'quidditch', 'seeker', 'prefect', 'animagus', 'pure', 'muggleborn', 'in_order', 'in_da', 'in_de', 'in_staff', 'in_ministry', 'in_weasley', 'in_G', 'in_S'",
    "'champ', 'drafted', 'r1', 'top14', 'allstar', 'oneanddone', 'fouryear', 'kentuckian', 'tall', 'honored', 'top10'")
sub("concat(['G', 'S', 'R', 'H', 'order', 'da', 'weasley', 'staff'])", "concat(['rupp', 'hall', 'pitino', 'smith', 'calipari'])")
sub("rows: ['G', 'S', 'order'], cols: ['died', 'pure', 'in_staff']", "rows: ['rupp', 'pitino', 'calipari'], cols: ['champ', 'kentuckian', 'drafted']")
sub("open('wizards/data.json')", "open('uk/data.json')")
sub("open('wizard-grid.html', 'w')", "open('bigblue-grid.html', 'w')")
sub("'wz:", "'bb:")
sub("'Group × fact'", "'Coach × fact'")
sub("'Type at least 2 letters of a name.'", "'Type at least 2 letters of a player’s name.'")
sub("'That character isn’t in the list.'", "'That player isn’t on a Kentucky roster in this list.'")
sub("'Empty squares now show characters who would have worked.'", "'Empty squares now show players who would have worked.'")
sub('<b>character</b> who fits both', '<b>player</b> who fits both')
sub("each character can be used once", "each player can be used once")
sub("open('build_wiz.py', 'w')", "open('build_uk.py', 'w')")
open('make_uk_builder_out.py', 'w').write(p); print('ok')
