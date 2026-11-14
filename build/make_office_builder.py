"""Write build_office.py (Scranton Grid page builder): a copy of make_wiz_builder.py with Scranton Grid content swapped in."""
p = open('make_wiz_builder.py').read()
def sub(a, b):
    global p
    assert a in p, a[:90]; p = p.replace(a, b)
sub("build_wiz.py (Wizard Grid page builder)", "build_office.py (Scranton Grid page builder)")
sub("'<title>Wizard Grid</title>'", "'<title>Scranton Grid</title>'")
sub("'family=IM+Fell+English:ital@0;1&family=DM+Sans'", "'family=Courier+Prime:ital,wght@0,400;0,700;1,400&family=DM+Sans'")
sub("'like a page of a spellbook'", "'like a sheet of office paper under a typewritten title card'")
sub("""  --bg: #ecebef;
  --panel: #ffffff;
  --ink: #1b1622;
  --muted: #625a6c;
  --line: #d8d3de;
  --accent: #8c1d2b;
  --accent-2: #8a6416;""", """  --bg: #ededed;
  --panel: #ffffff;
  --ink: #111111;
  --muted: #5c5c5c;
  --line: #d0d0d0;
  --accent: #111111;
  --accent-2: #1f4e9c;""")
sub('"IM Fell English", Georgia, "Times New Roman", serif;', '"Courier Prime", "Courier New", Courier, monospace;')
sub('--bg: #15121a; --panel: #201b27; --ink: #f2ecf6; --muted: #a89eb3; --line: #3a3244;', '--bg: #101010; --panel: #1b1b1b; --ink: #f4f4f4; --muted: #a6a6a6; --line: #333333;')
sub('--accent: #e0687a; --accent-2: #e2b75a; --accent-ink: #1e0408;', '--accent: #f4f4f4; --accent-2: #7fa6e8; --accent-ink: #111111;')
sub('Harry Potter trivia from the seven books</p>', 'That’s what she said.</p>')
sub("<h1>Wizard <span>Grid</span></h1>", "<h1>Scranton <span>Grid</span></h1>")
sub("Rows and columns can be houses, groups like the Order of the Phoenix or Dumbledore's Army, or traits like Animagus or Quidditch Seeker.",
    "Rows and columns can be departments like Sales or the warehouse, or life events like getting married or dating a coworker.")
i = p.index("<b>Medium</b> uses the four houses"); j = p.index("Your guesses are saved on this device.</p>", i)
p = p[:i] + ("Covers the US show, seasons 1 to 9. \"Ran the Scranton branch\" counts anyone who ran it, even briefly, so Creed counts. "
             "Front desk and annex covers reception, HR, customer service, quality assurance and supplier relations. "
             "\"Married\" and \"has kids\" mean by the finale. The office is small, so some squares have a single answer. "
             "<b>Medium</b> uses Sales, Accounting, the warehouse, the bosses and the front desk; <b>Hard</b> adds corporate and the Stamford branch. "
             "The list covers about 40 characters compiled by hand, so a character who fits might be missing. "
             "This is a fan-made game and isn't affiliated with NBC or the show. ") + p[j:]
i = p.index("const TYPE_ROWS = { G:"); j = p.index("const CLASH = [['y1','y2'],['pure','half']", i)
k = p.index("['in_R','in_H']];", j) + len("['in_R','in_H']];")
p = p[:i] + """const TYPE_ROWS = { sales: ['Sales', 'Scranton or elsewhere'], accounting: ['Accounting', 'The numbers people'], warehouse: ['Warehouse', 'Downstairs'], boss: ['Ran the Scranton branch', 'Even briefly'], frontdesk: ['Front desk & annex', 'Reception, HR and more'], corporate: ['Corporate', 'Dunder Mifflin or Sabre'], stamford: ['Stamford branch', 'Before the merger'] };
const COLS = {
  married: ['Married by the finale', 'On screen or off'],
  parent: ['Has kids by the finale', 'Any number'],
  dated: ['Dated a coworker', 'On screen'],
  musician: ['Plays music', 'On the show'],
  pilot: ['In the pilot episode', 'Season 1, episode 1'],
  wedding: ['Wedding shown on screen', 'Their own'],
  left: ['Left Dunder Mifflin', 'Quit, fired, retired or moved on'],
  in_sales: ['Sales', 'Any time'], in_accounting: ['Accounting', 'Any time'], in_warehouse: ['Warehouse', 'Any time'],
  in_boss: ['Ran the Scranton branch', 'Even briefly'], in_frontdesk: ['Front desk & annex', 'Any time'],
  in_corporate: ['Corporate', 'Dunder Mifflin or Sabre'], in_stamford: ['Stamford branch', 'Any time']
};
const CLASH = [['y1','y2']];""" + p[k:]
sub("'died', 'quidditch', 'seeker', 'prefect', 'animagus', 'pure', 'muggleborn', 'in_order', 'in_da', 'in_de', 'in_staff', 'in_ministry', 'in_weasley', 'in_G', 'in_S'",
    "'married', 'parent', 'dated', 'pilot', 'wedding', 'left', 'in_sales', 'in_boss', 'in_frontdesk', 'in_warehouse', 'in_corporate', 'in_accounting'")
sub("concat(['G', 'S', 'R', 'H', 'order', 'da', 'weasley', 'staff'])", "concat(['sales', 'accounting', 'warehouse', 'boss', 'frontdesk'])")
sub("rows: ['G', 'S', 'order'], cols: ['died', 'pure', 'in_staff']", "rows: ['sales', 'boss', 'frontdesk'], cols: ['married', 'parent', 'dated']")
sub("open('wizards/data.json')", "open('office/data.json')")
sub("open('wizard-grid.html', 'w')", "open('scranton-grid.html', 'w')")
sub("'wz:", "'sc:")
sub("'Group × fact'", "'Department × fact'")
sub("open('build_wiz.py', 'w')", "open('build_office.py', 'w')")
open('make_office_builder_out.py', 'w').write(p); print('ok')
