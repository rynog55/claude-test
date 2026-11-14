"""Throne Grid's houses are small, so allow single-answer squares in both modes (with a cap on how many per grid)."""
t = open('throne-grid.html').read()
for a, b in [("const MIN = MODE === 'medium' ? 2 : 1;", "const MIN = 1;"),
             ("if (ok && solvable(rows, cols) && thin <= 2) return", "if (ok && solvable(rows, cols) && thin <= (MODE === 'medium' ? 3 : 5)) return")]:
    assert a in t, a; t = t.replace(a, b)
open('throne-grid.html', 'w').write(t); print('tweaked')
