"""Write build_got.py (Throne Grid page builder): a copy of make_wiz_builder.py with Throne Grid content swapped in."""
p = open('make_wiz_builder.py').read()
def sub(a, b):
    global p
    assert a in p, a[:90]; p = p.replace(a, b)
sub("build_wiz.py (Wizard Grid page builder)", "build_got.py (Throne Grid page builder)")
sub("'<title>Wizard Grid</title>'", "'<title>Throne Grid</title>'")
sub("'family=IM+Fell+English:ital@0;1&family=DM+Sans'", "'family=Marcellus+SC&family=DM+Sans'")
sub("'like a page of a spellbook'", "'like a war-room map'")
sub("""  --bg: #ecebef;
  --panel: #ffffff;
  --ink: #1b1622;
  --muted: #625a6c;
  --line: #d8d3de;
  --accent: #8c1d2b;
  --accent-2: #8a6416;""", """  --bg: #e6e7ea;
  --panel: #ffffff;
  --ink: #17181c;
  --muted: #5d5f68;
  --line: #d2d4da;
  --accent: #9b1c1c;
  --accent-2: #6d5a2a;""")
sub('"IM Fell English", Georgia, "Times New Roman", serif;', '"Marcellus SC", Georgia, "Times New Roman", serif;')
sub('--bg: #15121a; --panel: #201b27; --ink: #f2ecf6; --muted: #a89eb3; --line: #3a3244;', '--bg: #121316; --panel: #1c1d22; --ink: #ecebe8; --muted: #a3a19c; --line: #34353b;')
sub('--accent: #e0687a; --accent-2: #e2b75a; --accent-ink: #1e0408;', '--accent: #e05a4a; --accent-2: #c9a557; --accent-ink: #1e0604;')
sub('Harry Potter trivia from the seven books</p>', 'The show only. Yes, season 8 counts.</p>')
sub("<h1>Wizard <span>Grid</span></h1>", "<h1>Throne <span>Grid</span></h1>")
sub("Rows and columns can be houses, groups like the Order of the Phoenix or Dumbledore's Army, or traits like Animagus or Quidditch Seeker.",
    "Rows and columns can be great houses, groups like the Night's Watch or the Kingsguard, or a character's fate.")
i = p.index("<b>Medium</b> uses the four houses"); j = p.index("Your guesses are saved on this device.</p>", i)
p = p[:i] + ("Only the HBO series counts (seasons 1 to 8), not the books or the spin-offs. "
             "A house counts by birth, or by marrying in and taking the name, so Catelyn is a Tully and a Stark; Jon Snow counts as Stark and Targaryen; "
             "Joffrey, Tommen and Myrcella count as Baratheon and Lannister. "
             "\"Dies on screen\" includes Jon Snow, who died in season 5 and came back. \"King or queen\" includes rulers and claimants. "
             "<b>Medium</b> uses the bigger houses, the Night's Watch, the Kingsguard and the Small Council; <b>Hard</b> adds Martell, Tully, Bolton and the Free Folk. "
             "The list covers about 110 characters compiled by hand, so a character who fits might be missing. "
             "This is a fan-made game and isn't affiliated with HBO. ") + p[j:]
i = p.index("const TYPE_ROWS = { G:"); j = p.index("const CLASH = [['y1','y2'],['pure','half']", i)
k = p.index("['in_R','in_H']];", j) + len("['in_R','in_H']];")
p = p[:i] + """const TYPE_ROWS = { stark: ['House Stark', 'Winterfell'], lannister: ['House Lannister', 'Casterly Rock'], targaryen: ['House Targaryen', 'Dragonstone'], baratheon: ['House Baratheon', "Storm's End"], greyjoy: ['House Greyjoy', 'Iron Islands'], tyrell: ['House Tyrell', 'Highgarden'], martell: ['House Martell', 'Dorne'], tully: ['House Tully', 'Riverrun'], bolton: ['House Bolton', 'The Dreadfort'], watch: ["Night's Watch", 'Sworn brothers'], kingsguard: ['Kingsguard', 'Or Queensguard'], council: ['Small Council', 'Any time'], freefolk: ['Free Folk', 'Beyond the Wall'] };
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
const CLASH = [['y1','y2'],['early','late'],['early','survives']];""" + p[k:]
sub("'died', 'quidditch', 'seeker', 'prefect', 'animagus', 'pure', 'muggleborn', 'in_order', 'in_da', 'in_de', 'in_staff', 'in_ministry', 'in_weasley', 'in_G', 'in_S'",
    "'dies', 'survives', 'early', 'late', 'king', 'hand', 'bastard', 'in_stark', 'in_lannister', 'in_targaryen', 'in_baratheon', 'in_watch', 'in_kingsguard', 'in_council'")
sub("concat(['G', 'S', 'R', 'H', 'order', 'da', 'weasley', 'staff'])", "concat(['stark', 'lannister', 'targaryen', 'baratheon', 'greyjoy', 'tyrell', 'watch', 'kingsguard', 'council'])")
sub("rows: ['G', 'S', 'order'], cols: ['died', 'pure', 'in_staff']", "rows: ['stark', 'lannister', 'council'], cols: ['dies', 'survives', 'late']")
sub("open('wizards/data.json')", "open('thrones/data.json')")
sub("open('wizard-grid.html', 'w')", "open('throne-grid.html', 'w')")
sub("'wz:", "'tg:")
sub("'Group × fact'", "'House or group × fact'")
sub("open('build_wiz.py', 'w')", "open('build_got.py', 'w')")
open('make_got_builder_out.py', 'w').write(p); print('ok')
