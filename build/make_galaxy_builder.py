"""Write build_galaxy.py (Galaxy Grid page builder): a copy of make_wiz_builder.py with Galaxy Grid content swapped in."""
p = open('make_wiz_builder.py').read()
def sub(a, b):
    global p
    assert a in p, a[:90]; p = p.replace(a, b)
sub("build_wiz.py (Wizard Grid page builder)", "build_galaxy.py (Galaxy Grid page builder)")
sub("'<title>Wizard Grid</title>'", "'<title>Galaxy Grid</title>'")
sub("'family=IM+Fell+English:ital@0;1&family=DM+Sans'", "'family=Exo+2:ital,wght@0,600;0,800;1,500&family=DM+Sans'")
sub("'like a page of a spellbook'", "'like a starship display'")
sub("""  --bg: #ecebef;
  --panel: #ffffff;
  --ink: #1b1622;
  --muted: #625a6c;
  --line: #d8d3de;
  --accent: #8c1d2b;
  --accent-2: #8a6416;""", """  color-scheme: dark;
  --bg: #07080d;
  --panel: #10131c;
  --ink: #eef0f6;
  --muted: #9aa1b4;
  --line: #262b3a;
  --accent: #ffe81f;
  --accent-2: #5aa9ff;""")
sub('"IM Fell English", Georgia, "Times New Roman", serif;', '"Exo 2", "Trebuchet MS", system-ui, sans-serif;')
sub('--bg: #15121a; --panel: #201b27; --ink: #f2ecf6; --muted: #a89eb3; --line: #3a3244;', '--bg: #07080d; --panel: #10131c; --ink: #eef0f6; --muted: #9aa1b4; --line: #262b3a;')
sub('--accent: #e0687a; --accent-2: #e2b75a; --accent-ink: #1e0408;', '--accent: #ffe81f; --accent-2: #5aa9ff; --accent-ink: #141200;')
sub('Harry Potter trivia from the seven books</p>', 'Episodes I–VI. Nothing after.</p>')
sub("<h1>Wizard <span>Grid</span></h1>", "<h1>Galaxy <span>Grid</span></h1>")
# rules prose (plain text inside the builder)
sub("Rows and columns can be houses, groups like the Order of the Phoenix or Dumbledore's Army, or traits like Animagus or Quidditch Seeker.",
    "Rows and columns can be films, groups like the Jedi or the Rebel Alliance, or traits like wielding a lightsaber.")
i = p.index("<b>Easy</b> uses the four houses"); j = p.index("Your guesses are saved on this device.</p>", i)
p = p[:i] + ("Only Episodes I to VI count, in their current versions with the Special Edition changes (so Jabba appears in A New Hope). "
             "Anakin and Darth Vader are one answer, and so are Palpatine and Darth Sidious. \"Dies on screen\" means within these six films. "
             "<b>Easy</b> uses the six films plus Jedi, Rebels and the Empire; <b>Hard</b> adds the Sith, the Republic, the Separatists and bounty hunters. "
             "The list covers about 90 characters compiled by hand, so a character who fits might be missing. "
             "This is a fan-made game and isn't affiliated with Lucasfilm or Disney. ") + p[j:]
# categories (plain JS text inside the builder)
i = p.index("const TYPE_ROWS = { G:"); j = p.index("const CLASH = [['y1','y2'],['pure','half']", i); k = p.index("['in_R','in_H']];", j) + len("['in_R','in_H']];")
p = p[:i] + """const TYPE_ROWS = { ep1: ['Episode I', 'The Phantom Menace'], ep2: ['Episode II', 'Attack of the Clones'], ep3: ['Episode III', 'Revenge of the Sith'], ep4: ['Episode IV', 'A New Hope'], ep5: ['Episode V', 'The Empire Strikes Back'], ep6: ['Episode VI', 'Return of the Jedi'], jedi: ['Jedi', 'Order members'], sith: ['Sith', 'Dark side lords'], rebel: ['Rebel Alliance', 'Members'], empire: ['Galactic Empire', 'Officers and rulers'], republic: ['Galactic Republic', 'Officials and troops'], separatist: ['Separatists', 'The Confederacy'], hunter: ['Bounty hunters', 'For hire'] };
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
const CLASH = [['y1','y2'],['droid','alien'],['droid','saber'],['droid','skywalker']];""" + p[k:]
sub("'died', 'quidditch', 'seeker', 'prefect', 'animagus', 'pure', 'muggleborn', 'in_order', 'in_da', 'in_de', 'in_staff', 'in_ministry', 'in_weasley', 'in_G', 'in_S'",
    "'saber', 'dies', 'pilot', 'droid', 'alien', 'both', 'in_ep1', 'in_ep2', 'in_ep3', 'in_ep4', 'in_ep5', 'in_ep6', 'in_jedi', 'in_rebel', 'in_empire'")
sub("concat(['G', 'S', 'R', 'H', 'order', 'da', 'weasley', 'staff'])", "concat(['ep1', 'ep2', 'ep3', 'ep4', 'ep5', 'ep6', 'jedi', 'rebel', 'empire'])")
sub("rows: ['G', 'S', 'order'], cols: ['died', 'pure', 'in_staff']", "rows: ['ep4', 'ep5', 'jedi'], cols: ['saber', 'dies', 'in_ep6']")
sub("open('wizards/data.json')", "open('galaxy/data.json')")
sub("open('wizard-grid.html', 'w')", "open('galaxy-grid.html', 'w')")
sub("'wz:", "'gx:")
sub("'Group × fact'", "'Film or group × fact'")
sub("open('build_wiz.py', 'w')", "open('build_galaxy.py', 'w')")
open('make_galaxy_builder_out.py', 'w').write(p); print('ok')
